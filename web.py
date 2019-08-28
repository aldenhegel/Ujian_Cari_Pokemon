from flask import Flask, send_from_directory, render_template, url_for, jsonify, abort, redirect, request
import requests
import json




app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hasil', methods = ['POST'])
def hasil():
    data = request.form
    data = dict(data)
    url = 'https://pokeapi.co/api/v2/pokemon/' + data['pokemon']
    data1 = requests.get(url)
    if str(data1) == '<Response [404]>':
        return render_template('no.html')
    else:
        data1 = data1.json()
        return render_template('hasil.html', data = data1)



if __name__ == '__main__':
    app.run(debug = True)