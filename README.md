# PlanetPedia - Project Structure

### `/data/`
Contains the data for our application
* `dwarf-data.md` contains data on the dwarf planets
* `planets-data.md` contains data on the planets of the solar system
* `random-facts.md` contains a list of random solar system facts

### `/templates/`
Contains the HTML files that will be rendered for the frontend.
* `layout.html` contains a shared layout for each page. Do not edit this.
* `index.html` is the homepage. No need to edit this.
* `planet-list.html` is the page that will display the list of planets [TODO]
* `dplanet-list.html` is the page that will display the list of dwarf planets [TODO]
* `random-fact.html` will display a random fact [TODO]
* `edit-planet.html` will allow the user to edit the entry for a planet [TODO]
* `error.html` will just display any errors. No need to edit this.

### `/static/styles`
Contains the (singular) CSS file needed for our application's styling: `styles.css`

This can be extended to add more styles, either to `styles.css` or in a different stylesheet file.

_General note:_

`/static/` is meant to contain all static files; generally it contains 3 main subfolders `styles` (for CSS stylesheets), `scripts` (for JavaScript code) and `media` (for images, videos, etc.). We do not have any JS scripts or any media for now, but feel free to add your own.

### `forms.py`
This will eventually contain the forms we need for our application. **We will work on this during the workshop.**

### `util.py`
Some useful functions that handle reading/writing data, conversion to different formats, etc. **Do not edit this.**

### `app.py`
Our Flask application will be written here. **We will work on this during the workshop.**

_TODO:_ If you have time, read through `app.py` to get an idea of what will happen during the workshop.

# PlanetPedia - The project
Like Wikipedia, but less extensive. Users can read about the planets in the solar system and edit entries that appear to be erroneous.

## Routes, Handlers, HTML files

A **route** is a URL pattern.

A **handler** is a function that handles requests made to a particular route.

The table below matches each route in the application to its handler as well as the relevant HTML file (if any).

| Route                        | Handler                          | HTML File (if any)         | Description                                 |
|------------------------------|----------------------------------|----------------------------|---------------------------------------------|
| `/`                          | `hello`                          | `index.html`               | Homepage of the application.                |
| `/leave`                     | `leave`                          | None (redirects elsewhere) | Leave the application.                      |
| `/random-fact`               | `get_random_fact`                | `random-fact.html`         | Get a random solar system fact.             |
| `/planets`                   | `planets`                        | `planet-list.html`         | Get the list of planets.                    |
| `/dwarf-planets`             | `dwarf_planets`                  | `dplanet-list.html`        | Get the list of dwarf planets.              |
| `/edit/planet/<planet_name>` | `edit_planet_entry(planet_name)` | `edit-planet.html`         | Allow user to edit an entry about a planet. |

## Setup and Installation

**Note: We will do this during the workshop as well. No need to do this in advance.**

1. Ensure you have Python 3.10+ installed on your system, along with `pip`.
2. Clone/fork/download the source code from this repository.
3. `cd` into the folder with these files such that `app.py` appears in the working directory.
4. Create a Python virtual environment:

On Linux/MacOS:
```bash
python3 -m venv .venv
```
On Windows:
```powershell
py -m venv .venv
```

5. Activate the virtual environment:

On Linux/MacOS:
```bash
source .venv/bin/activate
```
On Windows:
```powershell
.venv\Scripts\activate
```

6. Install the necessary modules:
```bash
pip install flask flask-wtf wtforms
```

Or, from the `requirements.txt`:
```bash
pip install -r requirements.txt
```

7. Turn on debug mode for Flask:

On Linux/MacOS:
```bash
export FLASK_DEBUG=1
```
On Windows:
```powershell
set FLASK_DEBUG=1
```

8. Run the command `flask run`, and then open up a browser and go to the URL `http://localhost:5000/`. The application should be set up if ALL previous instructions have been followed.