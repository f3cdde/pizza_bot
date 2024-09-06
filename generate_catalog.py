import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_catalog():
    # Certifique-se de que o diretório 'app/static' exista
    os.makedirs('app/static', exist_ok=True)

    c = canvas.Canvas("app/static/catalogo.pdf", pagesize=letter)
    width, height = letter

    # Título
    c.setFont("Helvetica-Bold", 24)
    c.drawString(200, height - 50, "Catálogo da Pizzaria")

    # Subtítulo
    c.setFont("Helvetica", 18)
    c.drawString(50, height - 100, "Nossas Pizzas")

    # Lista de Pizzas
    pizzas = [
        {"name": "Margherita", "price": 10.0, "description": "Molho de tomate, mussarela e manjericão."},
        {"name": "Pepperoni", "price": 12.0, "description": "Molho de tomate, mussarela e pepperoni."},
        {"name": "Hawaiian", "price": 11.0, "description": "Molho de tomate, mussarela, presunto e abacaxi."},
        {"name": "Veggie", "price": 9.0, "description": "Molho de tomate, mussarela e vegetais variados."},
    ]

    y = height - 150
    for pizza in pizzas:
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, f"{pizza['name']} - ${pizza['price']}")
        y -= 20
        c.setFont("Helvetica", 12)
        c.drawString(50, y, pizza['description'])
        y -= 40

    # Informações de Contato
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "Informações de Contato")
    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(50, y, "Endereço: Rua da Pizzaria, 123")
    y -= 20
    c.drawString(50, y, "Telefone: (11) 1234-5678")
    y -= 20
    c.drawString(50, y, "WhatsApp: (11) 9876-5432")

    c.save()

if __name__ == "__main__":
    generate_catalog()
