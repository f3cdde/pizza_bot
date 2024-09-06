# Pizza Bot

Este é um bot para atendimento automático de pizzaria via WhatsApp. O bot permite que os clientes vejam o menu, façam pedidos de pizza e recebam o catálogo da pizzaria em PDF.

## Estrutura do Projeto

pizza_bot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── order_service.py
│   │   ├── menu_service.py
│   ├── templates/
│   │   ├── order_template.txt
│   │   ├── menu_template.txt
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── whatsapp_utils.py
│   ├── static/
│   │   └── catalogo.pdf
├── generate_catalog.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .gitignore
└── README.md


## Dependências

- Flask
- twilio
- python-dotenv
- reportlab

## Configuração do Ambiente

1. Clone o repositório:
   git clone https://github.com/seu-usuario/pizza_bot.git

2. Navegue até o diretório do projeto:
   cd pizza_bot

3. Crie um arquivo .env com as seguintes variáveis de ambiente:
   TWILIO_ACCOUNT_SID=seu_twilio_account_sid
   TWILIO_AUTH_TOKEN=seu_twilio_auth_token
   TWILIO_PHONE_NUMBER=seu_twilio_phone_number
   PIZZERIA_PHONE_NUMBER=seu_pizzeria_phone_number

4. Construa e inicie os serviços Docker:
   docker-compose up --build

5. Acesse a aplicação no navegador em http://localhost:5000.

## Gerar o Catálogo

1. Instale a biblioteca reportlab:
   pip install reportlab

2. Execute o script para gerar o catálogo:
   python generate_catalog.py


### Passos para Garantir que o Projeto está Funcional

1. **Clone o repositório**: Certifique-se de que você pode clonar o repositório do GitHub.

2. **Navegue até o diretório do projeto**: Certifique-se de que você está no diretório onde o arquivo `generate_catalog.py` está localizado.

3. **Crie os arquivos necessários**: Certifique-se de que todos os arquivos mencionados acima estão presentes e configurados corretamente.

4. **Gere o catálogo**: Execute o script `generate_catalog.py` para gerar o arquivo `catalogo.pdf`.

5. **Construa e inicie os serviços Docker**: Construa e inicie os serviços Docker com o comando:
   docker-compose up --build

6. Aguarde até que todos os serviços estejam prontos: Certifique-se de que todos os serviços estejam prontos antes de tentar acessar a aplicação no navegador.

7. Acesse a aplicação no navegador: Acesse a aplicação no navegador em http://localhost:5000.

------

## Passos para Configurar o Twilio com WhatsApp
1. Crie uma Conta no Twilio:
   Se você ainda não tem uma conta no Twilio, crie uma em twilio.com.
2. Configure um Sandbox do WhatsApp no Twilio:
   No painel do Twilio, vá para a seção Messaging e selecione Try it out > Send a WhatsApp message.
   Siga as instruções para configurar o sandbox do WhatsApp. Você precisará enviar uma mensagem de verificação para um número de telefone fornecido pelo Twilio para ativar o sandbox.
3. Obtenha as Credenciais do Twilio:
   No painel do Twilio, vá para a seção Account e copie o Account SID e o Auth Token. Esses valores serão usados no arquivo .env.
4. Atualize o Arquivo .env:
   Certifique-se de que o arquivo .env contém as seguintes variáveis de ambiente com os valores corretos:
   TWILIO_ACCOUNT_SID=seu_twilio_account_sid
   TWILIO_AUTH_TOKEN=seu_twilio_auth_token
   TWILIO_PHONE_NUMBER=seu_twilio_phone_number
   PIZZERIA_PHONE_NUMBER=seu_pizzeria_phone_number
5. Atualize o Código do Servidor Flask:
   Certifique-se de que o código do servidor Flask está configurado para lidar com mensagens do WhatsApp. O código já deve estar configurado corretamente com as funções send_message e send_media no arquivo whatsapp_utils.py.
6. Configure o Webhook no Twilio:
   No painel do Twilio, vá para a seção Messaging e selecione WhatsApp Sandbox.
   Na seção Sandbox Configuration, configure o Webhook URL para apontar para o endpoint /webhook do seu servidor Flask. Por exemplo, se você estiver executando o servidor localmente, use http://localhost:5000/webhook.
7. Teste o Bot:
   Envie uma mensagem para o número do sandbox do WhatsApp que você configurou no Twilio.
   O bot deve responder de acordo com as mensagens definidas no código do servidor Flask.
