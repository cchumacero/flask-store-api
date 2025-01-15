class Product():
    def __init__(self, id, title=None, price=None, description=None, category=None, images=None):
        self.id = id
        self.title = title
        self.price = price
        self.description = description
        self.category = category
        self.images = images

    def to_JSON(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'category': self.category,
            'images': self.images
        }
