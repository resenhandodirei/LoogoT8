# LoogoT8 - README

## Descrição do Projeto

**LoogoT8** é uma automação desenvolvida para ajudar instituições de ensino a captar alunos que quase concluíram o processo de matrícula, mas desistiram na última etapa. O projeto tem como objetivo identificar as barreiras que impedem esses alunos de finalizarem a matrícula, oferecer suporte imediato e personalizar o processo para aumentar a taxa de conversão de matrículas.

O LoogoT8 assume a forma de um robô com identidade visual futurista inspirada no conceito de infinito e astronomia. Ele interage diretamente com alunos do ensino médio, oferecendo ajuda e respondendo dúvidas durante o processo de inscrição.

## Funcionalidades Principais

- **Captação de Leads**: Identificação de alunos que não concluíram a matrícula e envio de alertas personalizados.
- **Interação Inteligente**: Respostas automáticas e personalizadas para dúvidas comuns dos alunos durante o processo de matrícula.
- **Relatórios e Análises**: Geração de relatórios detalhados sobre os motivos de desistência e análise de padrões de comportamento dos alunos.
- **Integração com Sistemas de Gestão de Matrículas**: Facilita o fluxo de informações para melhorar a taxa de conversão.
- **Notificações Personalizadas**: Envio automático de e-mails e mensagens para ajudar na conclusão da matrícula.

## Tecnologias Utilizadas

- **Python**: Backend responsável pelo funcionamento da automação.
- **Flask**: Framework web para criar a API e gerenciar as interações.
- **SQLite**: Banco de dados leve para armazenar as informações dos alunos e relatórios.
- **HTML/CSS/JavaScript**: Para criar uma interface web simples para gerenciar os dados.
- **Bootstrap**: Framework CSS para facilitar a criação de interfaces responsivas.
- **Jinja2**: Utilizado para renderizar as páginas dinâmicas no Flask.

## Requisitos Técnicos

- Python 3.x
- Flask 2.x
- SQLite
- Navegador Web (Google Chrome, Firefox, etc.)
- Editor de código (VSCode, Sublime Text, etc.)

## Como Instalar e Executar

### Backend (Flask)

1. Clone o repositório:
   ```bash
   git clone https://github.com/seurepositorio/LoogoT8.git
   ```
2. Entre no diretório do projeto:
   ```bash
   cd LoogoT8
   ```
3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute o servidor Flask:
   ```bash
   flask run
   ```

### Frontend (Interface Web)

1. Após iniciar o servidor Flask, acesse o sistema abrindo o navegador e visitando:
   ```
   http://127.0.0.1:5000
   ```

## Equipe de Desenvolvimento

- **Larissa Martins Correa** - Desenvolvedora Fullstack
- **Marcelo Silva** - Coordenador de Matrículas (Stakeholder)
- **Renata Gomes** - Assistente de Matrículas (Stakeholder)
- **Lucas Almeida** - Potencial Aluno (Persona)

## Estrutura de Diretórios

```
LoogoT8/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── templates/
│   └── static/
├── database/
│   └── loogot8.db
├── assets/
│   ├── logo.png
│   └── prototipacao-da-logo.png
└── README.md
```

## Contribuição

Sinta-se à vontade para abrir issues e pull requests! Toda contribuição para melhorar o projeto e atender melhor às necessidades dos alunos e instituições é bem-vinda.

## Licença

Este projeto está sob a licença MIT - consulte o arquivo LICENSE para mais detalhes.

