from flask import Blueprint, request, url_for, redirect, render_template, flash


main = Blueprint("main", __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('main/home.html', title='Home Page')


@main.route('/')
@main.route('/about')
def about():
    return render_template('main/about.html', title='About Page')