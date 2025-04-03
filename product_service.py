from models import db, Product

class ProductService:
    @staticmethod
    def add_product(name, price):
        product = Product(name=name, price=price)
        db.session.add(product)
        db.session.commit()
        return {"message": "Product added successfully"}

    @staticmethod
    def get_products():
        return [{"id": p.id, "name": p.name, "price": p.price} for p in Product.query.all()]
