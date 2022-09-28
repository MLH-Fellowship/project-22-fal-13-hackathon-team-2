import os, json 
from flask import Flask, render_template, request, url_for, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# Places JSON
json_url = os.path.join(SITE_ROOT, "data", "places.json")
places = json.load(open(json_url))

# Hobbies JSON
json_url = os.path.join(SITE_ROOT, "data", "hobbies.json")
hobbies = json.load(open(json_url))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="MLH Fellow", url=os.getenv("URL"), users=users)

@app.route('/places')
def get_places():
    global places   
    return json.dumps(places)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), users=users)

@app.route('/user/<id>/')
def user(id):
    try:
        user = users[int(id)]
        return render_template('user.html', **user, **places)
    except Exception as e:
        return f"User not found! {id}"


users = [
    {'pic': '/static/img/serena_avatar.png',
    'name': "Serenity",
    'intro': "Tv fan. General social media scholar. Music fanatic. Food advocate. Zombie practitioner. Passionate travel specialist.",
    'edu': {
        "Bachelors in A": 2028,
        "Masters in B": 2033, 
        "PhD in C": 2045
    },
    'work': {
        "company A": 2018,
        "company B": 2023,
        "company C": 2024
    },
    "hobby_0":{
        "hobby":"Physics",
        "image":"/static/img/hobbies/hobby_physics.jpg",
        "blurb":"Physicists look at how and why things move and behave in space and time, along with the concepts of energy and force that go along with it. "
    },
    "hobby_1":{
        "hobby":"Insect Collecting",
        "image":"/static/img/hobbies/hobby_insect_collecting.jpg",
        "blurb":"The term 'insect collecting' refers to the practice of acquiring insects and other arthropods for scientific research or personal enjoyment. "
    },
    "hobby_2":{
        "hobby":"Fingerprint Collecting",
        "image":"/static/img/hobbies/hobby_fingerprint_collecting.jpg",
        "blurb":"When the skin of your finger rubs together, it leaves an imprint known as a fingerprint. "
    },
    "place_0":{
        "place":"Dusun Desa Sukadana",
        "blurb":"Dusun Desa Sukadana is a locality in Western Java.  Sukadana used to be a capital city of a Malay kingdom called Tanjungpura.",
        "link":"https://en.wikipedia.org/wiki/Sukadana"
    },
    "place_1":{
        "place":"Creches-sur-Saone",
        "blurb":"Crêches-sur-Saône is a commune in the Saône-et-Loire department in the region of Bourgogne-Franche-Comté in eastern France.",
        "link":"https://creches-sur-saone.com/"
    },
    "place_2":{
        "place":"Pirching am Traubenberg",
        "blurb":"Pirching am Traubenberg is a municipality in the district of Südoststeiermark in the Austrian state of Styria. ",
        "link":"https://www.steiermark.com/en/Holiday-regions/Cities-towns/Pirching-am-Traubenberg_c_841655"
    },
    "place_3":{
        "place":"Dade City",
        "blurb":"Dade City is popular with tourists for its antique stores, restaurants, and historic architecture, including the Pasco County Courthouse, Hugh Embry Library, and Edwinola.",
        "link":"https://en.wikipedia.org/wiki/Dade_City,_Florida"
    },
    "place_4":{
        "place":"Grimbsy",
        "blurb":"Grimsby lies in the national character areas of the Humber and the Lincolnshire coast and Marshes; it is predominantly low in topography.",
        "link":"https://en.wikipedia.org/wiki/Grimsby"
    },
    "place_5":{
        "place":"Porto Novo",
        "blurb":"Porto-Novo was once a tributary of the Yoruba kingdom of Oyo, which had offered it protection from the neighbouring Fon, who were expanding their influence and power in the region.",
        "link":"https://en.wikipedia.org/wiki/Porto-Novo"
    },
    "map":{
        "location":"Thaba-Tseka",
        "address":"https://www.google.com/maps/embed?pb=!4v1663954870490!6m8!1m7!1srxPf3cxrHGZzWogKDLrXoQ!2m2!1d-29.53141695448499!2d28.23740622745882!3f2.09!4f-13.799999999999997!5f0.8160813932612223"
    }
    }
]