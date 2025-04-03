from models import db, Cart

class CartService:
    @staticmethod
    def add_to_cart(user_id, product_id):
        cart_item = Cart(user_id=user_id, product_id=product_id)
        db.session.add(cart_item)
        db.session.commit()
        return {"message": "Product added to cart"}

    @staticmethod
    def remove_from_cart(user_id, product_id):
        Cart.query.filter_by(user_id=user_id, product_id=product_id).delete()
        db.session.commit()
        return {"message": "Product removed from cart"}
