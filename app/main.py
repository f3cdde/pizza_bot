from flask import Flask, request, url_for
from app.config import Config
from app.services.order_service import OrderService
from app.services.menu_service import MenuService
from app.utils.whatsapp_utils import WhatsAppUtils

app = Flask(__name__)
order_service = OrderService()
menu_service = MenuService()
whatsapp_utils = WhatsAppUtils()

@app.route('/')
def index():
    return 'Pizza Bot está funcionando!'

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From', '')

    if 'menu' in incoming_msg:
        menu_items = "\n".join([f"{item}: ${price}" for item, price in menu_service.get_menu().items()])
        message = f"Olá,\n\nAqui está nosso menu:\n\n{menu_items}\n\nObrigado por escolher nossa pizzaria!"
        whatsapp_utils.send_message(from_number, message)
    elif 'pedido' in incoming_msg:
        # Exemplo de pedido: "pedido margherita 2 rua abc, 123"
        parts = incoming_msg.split()
        pizza_type = parts[1]
        quantity = int(parts[2])
        address = " ".join(parts[3:])
        order = order_service.create_order("Cliente", from_number, pizza_type, quantity, address)
        message = f"Olá Cliente,\n\nSeu pedido de {quantity} pizza(s) {pizza_type} foi recebido com sucesso!\nEndereço de entrega: {address}\n\nObrigado por escolher nossa pizzaria!"
        whatsapp_utils.send_message(from_number, message)
    elif 'catalogo' in incoming_msg:
        catalog_url = url_for('static', filename='catalogo.pdf', _external=True)
        message = "Aqui está o catálogo da nossa pizzaria."
        whatsapp_utils.send_message(from_number, message)
        whatsapp_utils.send_media(from_number, catalog_url)
    else:
        message = "Desculpe, não entendi sua mensagem. Por favor, envie 'menu' para ver o menu, 'pedido' para fazer um pedido ou 'catalogo' para receber o catálogo."
        whatsapp_utils.send_message(from_number, message)

    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
