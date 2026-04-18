# Transcriptor: Ferramenta de Conversão de Áudio

O Transcriptor é uma ferramenta de transcrição feita em Python, desenvolvida para transcrever arquivos de áudio `.mp3` em texto. Criada visando uma transcrição eficiente e precisa, com uma interface web utilizando Gradio para ser fácil de usar. Atualmente, o Transcriptor reconhece apenas o idioma Português Brasil (PT-BR).

## Funcionalidades

- **Transcrição de Áudio**: Transcreva arquivos de áudio `.mp3` em texto utilizando o modelo Faster-Whisper.
- **Interface Web**: Interface web interativa construída com Gradio para facilitar o envio de arquivos e o download das transcrições.
- **Transcrições com Marcação de Tempo**: As transcrições são fornecidas com timestamps, permitindo referência fácil a partes específicas do arquivo de áudio.
- **Flexibilidade de Modelos**: A ferramenta foi projetada para funcionar com diferentes modelos, oferecendo flexibilidade nas tarefas de transcrição.
- **Fácil de Usar**: Desenvolvida para ser intuitiva, com uma interface web simples para envio de arquivos e download das transcrições.

## Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| **Python** | Linguagem de programação principal do projeto |
| **Faster-Whisper** | Modelo de machine learning utilizado para as tarefas de transcrição |
| **Gradio** | Framework utilizado para construir a interface web |
| **MoviePy** | Biblioteca utilizada para manipulação de arquivos de vídeo |
| **FFmpeg-Python** | Biblioteca utilizada para processamento multimídia |
| **OS** | Para interações com o sistema operacional |
| **Tempfile** | Para criação de diretórios temporários |
| **Webbrowser** | Para abrir a interface web no navegador |

## Instalação

Para instalar as dependências do projeto, siga os passos abaixo:

1. **Clone o Repositório**
```bash
   git clone https://github.com/seu-usuario/TranscriptorV2.git
   cd TranscriptorV2
```

2. **Crie um Ambiente Virtual**
```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
   source venv/bin/activate  # Linux/Mac
```

3. **Instale as Dependências**
```bash
   pip install -r requirements.txt
```

## 💻 Uso

Para utilizar a ferramenta TranscriptorV2, siga os passos abaixo:

1. **Execute o Script**
```bash
   python transcritorv2.py
```

2. **Envie o Arquivo de Áudio** — envie um arquivo `.mp3` pela interface web.
3. **Selecione o Modelo** — selecione o modelo de transcrição desejado.
4. **Baixe a Transcrição** — faça o download do arquivo de texto transcrito.

## 📸 Capturas de Tela

<img width="1499" height="852" alt="image" src="https://github.com/user-attachments/assets/709a518c-6522-4ea8-ace7-cea2e943de0f" />
