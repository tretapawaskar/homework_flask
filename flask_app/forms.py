from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    age = StringField('Age:')
    breed = StringField('Breed:')
    colour = StringField('Colour:')
    characteristics = StringField('Characteristics:')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner')
    email = StringField('Email')
    pup_id = IntegerField("Id of Puppy")
    submit = SubmitField("Add Owner")

