import os, json 
from peewee import *
from flask import Flask, render_template, request, url_for, jsonify
from dotenv import load_dotenv
from playhouse.shortcuts import model_to_dict
#GoogleMaps(app, key="8JZ7i18MjFuM35dJHq70n3Hx4")





load_dotenv()
app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)
print(mydb)
#Timeline Post 
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

# Places JSON
json_url = os.path.join(SITE_ROOT, "data", "places.json")
places = json.load(open(json_url))

# Hobbies JSON
json_url = os.path.join(SITE_ROOT, "data", "hobbies.json")
hobbies = json.load(open(json_url))
"""
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="MLH Fellow", url=os.getenv("URL"), users=users)
"""
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


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
    {'pic': '/static/img/Serena.jpg',
    'name': "Serenity",
    'intro': " Hi, my name is Serenity and I am glad that you have come to read my portfolio. I am a self taught programmer with mainly experience using python and Java. I transitioned from a career in accounting because at the time I felt like it really wasn't the fit for me. Currently I am just riding the waves of life and would love to see where it takes me",
    'edu':{
        "2019": "Bachelors in Accountning",
        "2023": "Masters in Computer Science"
    },
    'work': {
        "Cohn Reznick": "If you have ever recieved rent relief in that good old state of conneticuit. That was good old me behind teh scenes calling the shots... And maybe 500 other peolpe. But my main goal was to audit fraudulent cases that were being mishandled or improperly filed or on a larger scale, landlords who wanted to evect tenants after recieving money.",
        "All Temps": "Worked for HR.. and hired people who were in desperate need of a job ",
        "Red Cross":  "Conducted research on under serviced communities 2 times a year and after certain disasters to see how things can improve and Participated in activities that assisted others in their time of need such as installing fire alarms, or providing rescue during Hurricanes."
    },

    "hobby_0":{
        "hobby":"Ice Skating",
        "image":"/static/img/lemon.jpg",
        "blurb":"If you've never made yourself feel like Elsa you're missing out. A pair of skates and a warm pretzel in the winter is an amazing feeling "
    },
    "hobby_1":{
        "hobby":"Going Out",
        "image":"/static/img/travel.gif",
        "blurb":"Theres no way that I could stay cooped up in the house all day... for the most part. SO I do dare to go out into the night and explore the town every now and again. Even if I may miss the last bus."
    },
    "hobby_2":{
        "hobby":"Swimming",
        "image":"/static/img/swim.png",
        "blurb":"Although not an Olymian I am an absolute lover of swimming. When I can, I go to my local gym at leat twice a week and exercise or hang with my personal trainer."
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

