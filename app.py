from distutils.log import debug
from flask import Flask, request, render_template, redirect, jsonify, flash, session
from flask_debugtoolbar   import DebugToolbarExtension
from models import db, connectdb, Pet
from forms import AddPetForm,EditPetForm


app = Flask(__name__)

# config DB url (connect to db)

app.config['SQLALCHEMY_DATABASE_URI']  =  'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False



app.config['SECRET_KEY'] = "test@123!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] =False
app.config['SQLALCHEMY_ECHO'] =True
debug = DebugToolbarExtension(app)
connectdb(app)


@app.route('/')
def display_pets():
    """We will get the list of the pets"""
    pets = Pet.query.all()
    return render_template('list.html',pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """The function will help us to add a pet in the database at the same time, 
    if the data entered is not correct, then it will redirect to the add pet form """
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        url = form.photo_url.data
        age=form.age.data
        notes =form.notes.data
        available = form.available.data
        Pet.add_new_pet(name,species,url,age,notes,available)
        print(name, species)
        flash(f"Pet {name} with species {species} is added  ")
        return redirect("/")

    else:
        return render_template("pet_add_form.html", form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """This is a function that help us to edit the Pet's information and submit 
    them to the database"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet) 

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("pet_edit.html", form=form,pet=pet)


@app.route('/available')
def available_pets():
    """We will get the list of the pets available for adoption"""
    pets = Pet.query.filter_by(available =True)
    return render_template('list.html',pets=pets)


@app.route('/adopted')
def adopted_pets():
    """We will get the list of the pets already adopted"""
    pets = Pet.query.filter_by(available=False)
    return render_template('list.html',pets=pets)