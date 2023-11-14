from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'Hello'

@app.route('/get/drinks')
def all_drinks():
    drinks = Drink.query.all()

    output = []
    for  drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return {"drinks": output}

@app.route('/get/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    
    return {"name": drink.name, "description": drink.description}

@app.route('/post/drinks', methods=['POST'])
def add_drink():
    drink =Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/delete/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get_or_404(id)

    if drink is None:
        return {"error": "Drink Not Found"}
    else:
        db.session.delete(drink)
        db.session.commit()
    return {"message": "Successfully Deleted"}