from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    is_open = db.Column(db.Boolean, default=False)
    order_items = db.relationship("OrderItem", backref="orderItem")

    def __repr__(self):
        return f"Order {self.id}, user_id{self.user_id},is_open{self.is_open},order_items{self.order_items}"

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "id_open": self.is_open,
            "order_items": [x.serialize() for x in self.order_items],
        }


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    book_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return f"OrderItem {self.id}, order_id {self.order_id}, book_id{self.book_id},quantity{self.quantity}"

    def serialize(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "book_id": self.book_id,
            "quantity": self.quantity,
        }
