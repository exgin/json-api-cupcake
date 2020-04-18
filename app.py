"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
from secrets import APP_CONFIG_SECRET_KEY

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = APP_CONFIG_SECRET_KEY

connect_db(app)


@app.route('/')
def home():
    """Home page"""

    return ":0"

# JSON API Routes


@app.route('/api/cupcakes')
def all_cupcakes():
    """Get data about all cupcakes"""
    cupcakes = Cupcake.query.all()
