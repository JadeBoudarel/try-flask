from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/coucou')
def coucou():
    mon_user={'username':'Richard'}
    mes_posts=[ {
            'author': {'username': 'TonTon'},
            'body': 'Bonjour'
        }]
    return render_template('coucou.html' , title='coucou' , user=mon_user ,posts=mes_posts)

@app.route('/velo_data')
def velo_data():

    return render_template('data_velo.html', title='data_velo')