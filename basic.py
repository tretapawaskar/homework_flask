import os
from forms import  AddForm , DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET_KEY'

basedir = os.path.abspath(os.path.dirname(__file__))
##app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Silver@123@localhost/adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    age = db.Column(db.Text)
    breed = db.Column(db.Text)
    colour = db.Column(db.Text)
    characteristics = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name,age,breed,colour,characteristics):
        self.name = name
        self.age = age
        self.breed = breed
        self.colour = colour
        self.characteristics = characteristics

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner assigned yet."

class Owner(db.Model):

    __tablename__ = 'owners'
    id = db.Column(db.Integer,primary_key= True,autoincrement=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,email,puppy_id):
        self.name = name
        self.email = email
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.name}"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        breed = form.breed.data
        colour = form.colour.data
        characteristics = form.characteristics.data
        new_pup = Puppy(name,age,breed,colour,characteristics)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html',form=form)
@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        pup_id = form.pup_id.data
        new_owner = Owner(name,email,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html',form=form)

@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
