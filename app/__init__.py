import os, json 
from peewee import *
from flask import Flask, render_template, request, url_for, jsonify
from dotenv import load_dotenv
from playhouse.shortcuts import model_to_dict
import datetime

load_dotenv()
app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


# MySQL database
mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

# PeeWee auto create timeline table
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
        
mydb.connect()
mydb.create_tables([TimelinePost])




json_url = os.path.join(SITE_ROOT, "data", "places.json")
places = json.load(open(json_url))


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

@app.route('/timeline')
def timeline():
    posts = [
        model_to_dict(p)
        for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
    ]
    return render_template('timeline.html', title="Timeline", posts=posts)




# Timeline API
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
    

@app.route('/api/timeline_post/', methods=['DELETE'])
def delete_time_line_post():
    obj = TimelinePost.get(TimelinePost.name=="test")
    obj.delete_instance()
    return print(f"Deleted test record")

users = [
    {'pic': '/static/img/jane_avatar.png',
    'name': "Jane Chong",

    'intro': ["CS masters student @ UPenn (Graduating Dec 2023)", 
    "Current Site Reliability Engineering Fellow @ MLH", 
    "Seeking 2023 Spring/Summer SWE/SRE internships",
    "Ex-management consultant @ Deloitte, Full ride scholar @ UQ", 
    "First gen student/immigrant, has US work authorization" 
    ],

    'project': {
        "https://devpost.com/software/greenfridge": "Green Fridge - Fridge camera and mobile app that tracks food items and expiry", 
    "https://devpost.com/software/virtual-campus-1ra9fq?ref_content=user-portfolio&ref_feature=in_progress": "Virtual Campus - Real time multiplayer web app for my online master program"
    },

    'edu': {
        "Languages": "Python, Java, C, SQL, HTML/CSS, JavaScript, Swift",
        "Tools": "Flask, Jinja, React, Express, Google Cloud Platform, Linux, Git", 
        "Certifications": "Professional Scrum Master I, CodePath iOS University",
        "Courses": "Data Structures, Algorithms, Databases, Computer Systems, Software Development, Discrete Math (TA)"
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