from flask import Flask, render_template
from main import get_animal_by_index

app = Flask(__name__)



@app.route('/<int:itemid>')
def main_str(itemid):
    animal_info = get_animal_by_index(itemid)
    return render_template("index.html", animal_info=animal_info)

app.run()