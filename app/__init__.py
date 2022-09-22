import os
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), users=users)

# @app.route('/profile')
# def profile():
#     return render_template('profile.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/user/<id>/')
def user(id):
    try:
        user = users[int(id)]
        return render_template('user.html', **user)
    except Exception as e:
        return f"User not found! {id}"

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

    
    

users = [
    {'pic': '/static/img/logo.jpg',
    'name': "serenity",
    'intro': "hi, my name is user fsdfjgsdjkfnglsdfkgs",
    'edu': {
        "Bachelors in A": 2028,
        "Masters in B": 2033, 
        "PhD in C": 2045
    },
    # 'hobbies': ["x","y","z"],
    'work': {
        "company A": 2018,
        "company B": 2023,
        "company C": 2024
    }
    },
    {'pic': '/static/img/logo.jpg',
    'name': "jo",
    'intro': "hi, my name is ufsdfsdfsd",
    'edu': {
        "Bachelors in A": 2018,
        "Masters in B": 2023, 
        "PhD in C": 2040
    },
    # 'hobbies': ["x","y","z"],
    'work': {
        "company A": 2018,
        "company B": 2023,
        "company C": 2024
    }
    },
    {'pic': '/static/img/logo.jpg',
    'name': "jane",
    'intro': "hi, my name is user 1",
    'edu': {
        "Bachelors in A": 2018,
        "Masters in B": 2023, 
        "PhD in C": 2040
    },
    # 'hobbies': ["x","y","z"],
    'work': {
        "company A": 2018,
        "company B": 2023,
        "company C": 2024
    }
    }
    
    
    
]