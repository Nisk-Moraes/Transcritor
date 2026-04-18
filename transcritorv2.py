"""
Transcritor de Áudio com Faster-Whisper
Ferramenta para transcrição automática de arquivos .mp3
usando o modelo Faster-Whisper (CTranslate2), com interface web via Gradio.
Idioma fixo: Português Brasileiro (pt).
"""

import os
import tempfile
import webbrowser
import gradio as gr
from faster_whisper import WhisperModel
from moviepy import VideoFileClip


def formatar_tempo(segundos: float) -> str:
    """Converte segundos em formato HH:MM:SS."""
    h = int(segundos // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def transcrever(arquivo, modelo_nome: str):
    """
    Função principal de transcrição.
    Recebe o caminho do arquivo e o tamanho do modelo Whisper.
    Retorna: texto completo, segmentos com timestamps, caminho do .txt para download.
    """
    if arquivo is None:
        raise gr.Error("Nenhum arquivo selecionado. Por favor, envie um arquivo .mp3")

    # Verificar extensão do arquivo
    nome_base = os.path.basename(arquivo)
    _, extensao = os.path.splitext(nome_base)
    extensao = extensao.lower()

    if extensao not in (".mp3"):
        raise gr.Error("Formato de arquivo não suportado. Por favor, envie um arquivo .mp3")

    caminho_audio = arquivo

    dir_temp = tempfile.mkdtemp()

    # Carregar o modelo Faster-Whisper
    gr.Info(f"Carregando modelo Faster-Whisper '{modelo_nome}'... isso pode levar um momento na primeira vez.")
    try:
        # Usar "cpu" como dispositivo padrão; trocar para "cuda" se houver GPU disponível
        modelo = WhisperModel(modelo_nome, device="cpu", compute_type="int8")
    except Exception as e:
        raise gr.Error(f"Erro ao carregar o modelo: {str(e)}")

    # Transcrever o áudio com idioma fixo em português
    gr.Info("Transcrevendo... isso pode levar alguns minutos dependendo do tamanho do arquivo.")
    try:
        segmentos_iter, info = modelo.transcribe(caminho_audio, language="pt", beam_size=5)
        # Consumir o iterador de segmentos para obter texto e timestamps
        segmentos = list(segmentos_iter)
    except Exception as e:
        raise gr.Error(f"Erro durante a transcrição: {str(e)}")

    # Texto completo da transcrição
    texto_completo = " ".join(seg.text.strip() for seg in segmentos).strip()

    # Segmentos com marcações de tempo
    linhas_timestamps = []
    for seg in segmentos:
        inicio = formatar_tempo(seg.start)
        fim = formatar_tempo(seg.end)
        texto_seg = seg.text.strip()
        linhas_timestamps.append(f"[{inicio} → {fim}] {texto_seg}")
    texto_timestamps = "\n".join(linhas_timestamps)

    # Salvar arquivo .txt com o mesmo nome base do arquivo original
    nome_sem_ext = os.path.splitext(nome_base)[0]
    caminho_txt = os.path.join(dir_temp, f"{nome_sem_ext}.txt")
    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write(texto_completo)

    gr.Info("Transcrição concluída com sucesso!")
    return texto_completo, texto_timestamps, caminho_txt


# --- Interface Gradio ---

with gr.Blocks(
    title="Transcritor de Áudio"
) as app:
    gr.Markdown(
        """
        # 🎙️ Transcritor de Áudio
        Transcreva arquivos de áudio (.mp3) para texto usando o modelo **Faster-Whisper**.
        Até **4x mais rápido** que o Whisper original, com a mesma qualidade.
        O idioma de transcrição é **Português Brasileiro**.
        """
    )

    with gr.Row():
        with gr.Column(scale=2):
            entrada_arquivo = gr.File(
                label="Selecione um arquivo de áudio (.mp3)",
                file_types=[".mp3"],
                type="filepath",
            )
        with gr.Column(scale=1):
            seletor_modelo = gr.Dropdown(
                choices=["tiny", "base", "small", "medium", "large-v3"],
                value="base",
                label="Tamanho do modelo Whisper",
                info="Modelos maiores são mais precisos, porém mais lentos. 'tiny' é o mais rápido; 'large-v3' é o mais preciso.",
            )

    botao_transcrever = gr.Button("🎤 Transcrever", variant="primary", size="lg")

    with gr.Column():
        saida_texto = gr.Textbox(
            label="Transcrição completa",
            lines=12,
            # show_copy_button=True,
            interactive=False,
        )
        saida_download = gr.File(label="Baixar transcrição em .txt")

    with gr.Accordion("📋 Transcrição com marcações de tempo", open=False):
        saida_timestamps = gr.Textbox(
            label="Segmentos com tempo",
            lines=15,
            # show_copy_button=True,
            interactive=False,
        )

    botao_transcrever.click(
        fn=transcrever,
        inputs=[entrada_arquivo, seletor_modelo],
        outputs=[saida_texto, saida_timestamps, saida_download],
    )

    gr.Markdown(
        """
        ---
        <center>Desenvolvido por Nicolas Moraes</center>
        """,
    )

# Iniciar a aplicação
if __name__ == "__main__":

    webbrowser.open("http://localhost:7860")
    app.launch(theme=gr.themes.Soft(primary_hue=gr.themes.colors.blue,secondary_hue=gr.themes.colors.slate))
    # app.launch(server_name="0.0.0.0", server_port=7860)
