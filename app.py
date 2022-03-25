from flask import Flask, render_template
import os, requests

app = Flask(__name__) 
api_key = "e49985ff7c17a901d9d3a3d15fe21ba2"

@app.route('/<city>', methods=['GET'])
def city_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    data = requests.get(url).json()
 
    return render_template('home.html', data=data)

if __name__=="__main__":
    app.run(port=5000, debug=True)