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
    'name': "serenity",
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
    },
    {'pic': '/static/img/jo_avatar.png',
    'name': "jo",
    'intro': "Internet buff. Incurable gamer. Subtly charming troublemaker. Web specialist. Evil problem solver. Friendly thinker.",
    'edu': {
        "Bachelors in A": 2018,
        "Masters in B": 2023, 
        "PhD in C": 2040
    },
    'work': {
        "company A": 2018,
        "company B": 2023,
        "company C": 2024
    },
    "hobby_0":{
        "hobby":"Embroidery",
        "image":"/static/img/hobbies/hobby_embroidery.jpg",
        "blurb":"Embroidery is the art of applying thread or yarn to a cloth or other substance using a needle. "
    },
    "hobby_1":{
        "hobby":"Stone Collecting",
        "image":"/static/img/hobbies/hobby_stone_collecting.jpg",
        "blurb":"Amateur geology is the study and hobby of collecting rocks and minerals or fossils from the natural environment. "
    },
    "hobby_2":{
        "hobby":"Beer Tasting",
        "image":"/static/img/hobbies/hobby_beer_tasting.jpg",
        "blurb":"Tasting beers is a great opportunity to learn about the history of beer as well as its many components, like malt and yeast."
    },
    "place_0":{
        "place":"Daming",
        "blurb":"Daming County is a county under the jurisdiction of Handan City in far southern Hebei Province, China. It was formerly one of the capitals of the Northern Song.",
        "link":"https://en.wikipedia.org/wiki/Daming_County"
    },
    "place_1":{
        "place":"Port Willunga",
        "blurb":"Before the British colonisation of South Australia, the Port Willunga area, along with most of the Adelaide plains area and down the western side of the Fleurieu Peninsula, was inhabited by the Kaurna people.",
        "link":"https://en.wikipedia.org/wiki/Port_Willunga,_South_Australia"
    },
    "place_2":{
        "place":"Pirching am Traubenberg",
        "blurb":"Pirching am Traubenberg is a municipality in the district of Südoststeiermark in the Austrian state of Styria. ",
        "link":"https://www.steiermark.com/en/Holiday-regions/Cities-towns/Pirching-am-Traubenberg_c_841655"
    },
    "place_3":{
        "place":"Ḩisyah",
        "blurb":"Hisyah is a town in central Syria, administratively part of the Homs Governorate, located about 35 kilometers south of Homs.",
        "link":"https://en.wikipedia.org/wiki/Hisyah"
    },
    "place_4":{
        "place":"Novotroyits’ke",
        "blurb":"Until 18 July, 2020, Novotroitske was the administrative center of Novotroitske Raion. The raion was abolished in July 2020 as part of the administrative reform of Ukraine, which reduced the number of raions of Kherson Oblast to five.",
        "link":"https://en.wikipedia.org/wiki/Novotroitske,_Kherson_Oblast"
    },
    "place_5":{
        "place":"Howrah",
        "blurb":"The history of the city of Howrah dates back over 500 years, but the district is situated in an area historically occupied by the ancient Bengali kingdom of Bhurshut.",
        "link":"https://en.wikipedia.org/wiki/Howrah"
    },
    "map":{
        "location":"Vlore County",
        "address":"https://www.google.com/maps/embed?pb=!4v1663954980520!6m8!1m7!1ssCtmt5vB9xQGIK5oTkz5Wg!2m2!1d40.14050738524855!2d19.64203503900379!3f272.09!4f5!5f0.8160813932612223"
    }
    },
    {'pic': '/static/img/jane_avatar.png',
    'name': "jane",
    'intro': "Hardcore internet fanatic. Travel maven. Extreme zombie expert. Coffee evangelist. Musicaholic. Devoted creator. Gamer. Organizer.",
    'edu': {
        "Bachelors in A": 2018,
        "Masters in B": 2023, 
        "PhD in C": 2040
    },
    'work': {
        "company A": 2018,
        "company B": 2023,
        "company C": 2024
    },
    "hobby_0":{
        "hobby":"Travel",
        "image":"/static/img/hobbies/hobby_travel.jpg",
        "blurb":"Travel is the act of moving from one place to another, usually across long distances. "
    },
    "hobby_1":{
        "hobby":"Ballet Dancing",
        "image":"/static/img/hobbies/hobby_ballet.jpg",
        "blurb":"A sort of performance dance, ballet has its origins in the Italian Renaissance and subsequently evolved into a concert dance in France and Russia around the fourteenth century."
    },
    "hobby_2":{
        "hobby":"Dowsing",
        "image":"/static/img/hobbies/hobby_dowsing.jpg",
        "blurb":"In order to identify underground water, buried metals or ores, precious stones, oil, so-called radioactive elements, cemetery sites, and harmful 'earth vibrations.' "
    },
    "place_0":{
        "place":"Dorlisheim",
        "blurb":"Dorlisheim is a commune in the Bas-Rhin department in Grand Est in north-eastern France.",
        "link":"https://en.wikipedia.org/wiki/Dorlisheim"
    },
    "place_1":{
        "place":"Bardi",
        "blurb":"According to a legend, the town's name derives from 'Bardus', or 'Barrio', the last elephant of Hannibal's army, who supposedly died here during the march to Rome.",
        "link":"https://en.wikipedia.org/wiki/Bardi,_Emilia-Romagna"
    },
    "place_2":{
        "place":"Yanzihe",
        "blurb":"Yanzihe is a locality in Hubei. Yanzihe is situated northwest of Dongwan, and east of Shikanshang.",
        "link":"https://ceb.wikipedia.org/wiki/Yanzihe"
    },
    "place_3":{
        "place":"Kuvshinovo",
        "blurb":"The main industry branch in Kuvshinovo is paper production.",
        "link":"https://en.wikipedia.org/wiki/Kuvshinovo,_Kuvshinovsky_District,_Tver_Oblast"
    },
    "place_4":{
        "place":"Sembalunbumbung",
        "blurb":"Sembalunbumbung is a village in Indonesia and has an elevation of 1,191 metres. Sembalunbumbung is situated southeast of Sembalunlawang, and north of Pusuk.",
        "link":"https://mapcarta.com/15601426"
    },
    "place_5":{
        "place":"Bang Rakam",
        "blurb":"The district was established on 10 December 1905, then named Chum Saeng District. Khun Phadet Prachadun was the first district head officer.",
        "link":"https://en.wikipedia.org/wiki/Bang_Rakam_district"
    },
    "map":{
        "location":"Si Kaeo",
        "address":"https://www.google.com/maps/embed?pb=!4v1663955065652!6m8!1m7!1sQ_ur_9Tm3-NgZx21UrA-tg!2m2!1d16.20508301633371!2d104.3767273992051!3f282.90249597244343!4f2.9684585023826173!5f0.4000000000000002"
    }
    }
    
    
    
]