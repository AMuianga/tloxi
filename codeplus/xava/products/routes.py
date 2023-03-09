from flask import Blueprint, redirect, request,render_template, session,flash,url_for
from ..extensions import db
from .models import Brand, Category, Addproduct
from .form import Addproducts


products = Blueprint("products", __name__)


@products.route('/')
def index():
    return render_template('index.html')

