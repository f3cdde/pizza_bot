from app.models import Menu

class MenuService:
    def __init__(self):
        self.menu = Menu()

    def get_menu(self):
        return self.menu.items
