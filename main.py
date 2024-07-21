from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
import json
import os
from pomodoro_timer.pomodoro_timer_class import PomodoroTimer
from morse_converter import Morse
from achievement_collector import steam_api


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)
morse = Morse()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/pomodoro-timer')
def pomodoro_timer():
    PomodoroTimer().run()
    return url_for('index')


@app.route('/morse-converter', methods=['GET', 'POST'])
def morse_converter():
    placeholder = "Type some text into the box and convert it to Morse Code."
    if request.method == 'POST':
        try:
            to_convert = request.form['to_convert']
            converted_string = morse.convert_string(to_convert)
            return render_template('morse_converter.html', converted_string=converted_string, to_convert=to_convert)
        except IndexError:
            flash("Input invalid.")
            return redirect(url_for('morse_converter'))
    return render_template('morse_converter.html', placeholder=placeholder)


@app.route('/achievement-collector')
def achievement_collector():
    with open('achievement_collector/game_data.json', 'r') as json_file:
        game_data = json.load(json_file)
        game_list = [game for game in game_data.values()]
        new_game_list = []
        achievement_dict = {}
        for game in game_list:
            new_game_list.append(game)
            if game['achievements'] is None:
                pass
            else:
                achievements = [achievement for achievement in game['achievements'].values()]
                achievement_dict[game['gameName']] = achievements[:3]
    return render_template('achievement_collector.html', game_data=game_list,
                           achievements=achievement_dict)


if __name__ == "__main__":
    app.run(debug=True)
