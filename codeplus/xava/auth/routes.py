from flask import Blueprint, request, url_for, redirect, render_template, flash, session
from ..extensions import db,bcrypt

from xava.products.models import Addproduct, Brand, Category
from .form import RegistrationForm, LoginForm


auth = Blueprint("auth", __name__)


@auth.route('/register', methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.home'))
    return render_template('auth/register.html', form=form, title="Register Page")



@auth.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'amuianga@gmail.com' and form.password.data == 'Pr3t@B0a':
            flash(f'The account  {form.email.data} was logged in !', 'success')
            return redirect(url_for('main.home'))
        
        else:
            flash(f'Login unsuccessful, Please check Username and password!', 'danger')
    return render_template('auth/login.html', form=form, title="Login Page")

