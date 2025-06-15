# server/models/restaurant_pizza.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"), nullable=False)

    __table_args__ = (
        CheckConstraint("price >= 1 AND price <= 30", name="price_between_1_and_30"),
    )

    # relationships
    restaurant = db.relationship("Restaurant", back_populates="pizzas")
    pizza      = db.relationship("Pizza",      back_populates="restaurants")

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "restaurant_id": self.restaurant_id,
            "pizza_id": self.pizza_id,
        }
