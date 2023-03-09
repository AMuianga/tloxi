from wtforms import (
    Form,
    IntegerField,
    StringField,
    TextAreaField,
    validators,
    DecimalField
)


class Addproducts(Form):
    name = StringField("Nome", [validators.DataRequired()])
    price = DecimalField("Price", [validators.DataRequired()])
    discount = IntegerField("Discount", default=0)
    stock = IntegerField("Stock", [validators.DataRequired()])
    description = TextAreaField("Description", [validators.DataRequired()])
    colors = StringField("Colors", [validators.DataRequired()])
