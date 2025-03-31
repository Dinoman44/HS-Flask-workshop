# The TODOS are to keep track of what needs to be implemented.
# Implementation will be taught during the workshop. DO NOT change anything beforehand. [IMPORTANT]
import random
import time

from flask import Flask, redirect, render_template, request
from werkzeug.exceptions import default_exceptions

from forms import EditPlanetForm
from util import init_data, write_back, SOME_EXTERNAL_URL


##########################
# Initialise application #
##########################
app = Flask(__name__) # initialise the application
app.config["SECRET_KEY"] = "todo" # TODO 6: Set a secret key


#######################
# Initialise app data #
#######################
PLANET_DATA_MD = dict() # dictionary to hold planet data, in the form of {planet_name: markdown_string}
PLANET_DATA_HTML = dict() # dictionary to hold planet data, in the form of {planet_name: html_string}
DWARF_PLANETS_MD = [] # list of dwarf planet markdown entries
DWARF_PLANETS_HTML = [] # list of dwarf planet html entries
RANDOM_FACTS = [] # list of random solar system facts
# load the data into the above structures
init_data(PLANET_DATA_MD, PLANET_DATA_HTML, DWARF_PLANETS_MD, DWARF_PLANETS_HTML, RANDOM_FACTS)


#############
# Home page #
#############
@app.route("/")
def hello():
    return "hello" # TODO 1: show the home page


##################
# Leave the site #
##################
@app.route("/leave")
def leave():
    time.sleep(3)
    return "leaving the site..." # TODO 2: redirect to an external website


###################
# Get random fact #
###################
@app.route("/random-fact")
def get_random_fact():
    return "get random fact" # TODO 3: return a random fact from RANDOM_FACTS


#######################
# See list of planets #
#######################
@app.route("/planets")
def planets():
    return "planets" # TODO 4: show the list of planets


#############################
# See list of dwarf planets #
#############################
@app.route("/dwarf-planets")
def dwarf_planets():
    return "dwarf planets" # TODO 5: show the list of dwarf planets


#######################
# Edit a planet entry #
#######################
@app.route("/edit/planet/")
def edit_planet_entry():
    return "edit planet entry" # TODO 7: allow the user to edit a planet entry


##########################
# Error handler function #
##########################
def planetary_error_handler(e):
    return render_template("error.html", name=e.name, code=e.code)

# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(planetary_error_handler)

if __name__ == "__main__":
    app.run()