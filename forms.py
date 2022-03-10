from flask_wtf import FlaskForm
from wtforms import StringField,  IntegerField,TextAreaField ,BooleanField
from wtforms.validators import Optional, URL,NumberRange,AnyOf,InputRequired



class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired(message="Name cannot be blank")])
    species = StringField('Species',validators= [InputRequired(message="Please add the valid species"),
                AnyOf(values=['cat','dog','porcupine' ], message='Species should be cat, dog, or porcupine') ] )  
    photo_url =  StringField("Photo URL",validators=[InputRequired(message="Please the  valid url for image"),Optional(),URL() ])
    age =IntegerField("Age",validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")  
    available = BooleanField('available')


class EditPetForm(FlaskForm):
    """Form for editing a pet."""
    photo_url =  StringField("Photo URL",validators=[Optional(),URL() ])
    age =IntegerField("Age",validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")  
    available = BooleanField('available')