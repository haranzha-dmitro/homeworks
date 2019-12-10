import uuid


class Product:
    def __init__(self, name, description='', img_name=None, price=0):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.img_name = img_name
        self.price = price


class Supermarket:
    def __init__(self, name, location='', img_name=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.img_name = img_name
        self.location = location
