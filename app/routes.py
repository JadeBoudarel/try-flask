from flask import render_template, jsonify
from app import app
import pandas as pd


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
    mon_user = {'username': 'Richard'}
    mes_posts = [{
        'author': {'username': 'TonTon'},
        'body': 'Bonjour'
    }]
    return render_template('coucou.html', title='coucou', user=mon_user, posts=mes_posts)


@app.route('/velo_data')
def velo_data():
    csv_df = pd.read_csv("./parcours.csv", sep=';', index_col='date', parse_dates=True, dayfirst=True)
    my_newindex = pd.date_range('2022-11-27', end='2023-03-25', freq='D')
    csv_df_reindexed = csv_df.reindex(my_newindex, fill_value=0)

    velo_datas = []

    _index: pd.Timestamp
    for _index, row in csv_df_reindexed.iterrows():
        _date = _index.strftime("%Y-%m-%d")
        my_line = {'x': _date, 'y': row['km']}
        velo_datas.append(my_line)

    return jsonify(velo_datas), 201


@app.route('/velo_plot')
def velo_plot():
    return render_template(template_name_or_list='velo_plot.html', title='velo_plot')
