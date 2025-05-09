# DO NOT EDIT THIS FILE
# This file contains utility functions for reading and writing data to/from markdown files.
# It is used by the main application and should not be modified.
import markdown

def convert_markdown_to_html_dict(data: dict) -> dict:
    """
    Converts a dictionary of Markdown strings into a dictionary of HTML strings.
    Args:
        data (dict): A dictionary where keys are strings and values are Markdown-formatted strings.
    Returns:
        dict: A dictionary where keys are the same as the input, and values are the corresponding HTML strings
            converted from the Markdown input.
    """
    return {key: markdown.markdown(value) for key, value in data.items()}


def convert_markdown_to_html_list(datalist: list) -> list:
    """
    Converts a list of Markdown strings into a list of HTML strings.
    Args:
        datalist (list): A list of strings written in Markdown format.
    Returns:
        list: A list of strings converted to HTML format using the markdown library.
    """
    return [markdown.markdown(data) for data in datalist]


def init_data(pmd: dict, phtml: dict, dpmd: list, dphtml: list, r: list) -> None:
    """
    Initializes and populates data structures with content from markdown files.
    This function clears the provided dictionaries and lists, then reads data 
    from specific markdown files to populate them. It also converts markdown 
    content to HTML format where applicable.
    Args:
        pmd (dict): A dictionary to store planet data in markdown format.
        phtml (dict): A dictionary to store planet data in HTML format.
        dpmd (list): A list to store dwarf planet data in markdown format.
        dphtml (list): A list to store dwarf planet data in HTML format.
        r (list): A list to store random facts from a markdown file.
    File Dependencies:
        - "data/random-facts.md": Contains random facts, one per line.
        - "data/planets-data.md": Contains planet data separated by "\n--------\n".
        - "data/dwarf-data.md": Contains dwarf planet data separated by "\n------\n".
    Notes:
        - The `convert_markdown_to_html_dict` function is used to convert the 
          planet markdown data to HTML format and populate `phtml`.
        - The `convert_markdown_to_html_list` function is used to convert the 
          dwarf planet markdown data to HTML format and populate `dphtml`.
    """

    # Clear existing data
    r.clear()
    pmd.clear()
    phtml.clear()
    dpmd.clear()
    dphtml.clear()

    # Read and process data from markdown files

    # Read random facts
    with open("data/random-facts.md", "r") as file:
        r.extend(file.readlines())
    
    # Read planet data
    with open("data/planets-data.md", "r") as file:
        n = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
        entries = file.read().split("\n--------\n")
        pmd.update(dict(zip(n, entries)))
        phtml.update(convert_markdown_to_html_dict(pmd))
    
    # Read dwarf planet data
    with open("data/dwarf-data.md", "r") as file:
        dpmd.extend(file.read().split("\n------\n"))
        dphtml.extend(convert_markdown_to_html_list(dpmd))


def write_back(planet: str, planet_data_md: dict, planet_data_html: dict, newentry: str) -> bool:
    """
    Updates the markdown and HTML representations of a planet's data and writes the updated markdown data to a file.
    Args:
        planet (str): The name of the planet to update.
        planet_data_md (dict): A dictionary containing the markdown data for all planets.
        planet_data_html (dict): A dictionary containing the HTML data for all planets.
        newentry (str): The new markdown entry for the specified planet.
    Returns:
        bool: `True` if the operation was successful, `False` if a KeyError occurred.
    """

    try:
        # Update the planet data
        planet_data_md[planet] = newentry
        planet_data_html[planet] = markdown.markdown(newentry)
        with open("data/planets-data.md", "w") as file:
            file.write("\n--------\n".join(planet_data_md.values()))
        return True
    except KeyError:
        return False
    
SOME_EXTERNAL_URL = "https://hckr.cc/hackerschool-week-10-externalURL-demo"