 
from flask import Flask, request, render_template
from weather import weather

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = weather(city)
    return render_template(
        "weather.html",
        title=weather_data['name'],
        temp=f"{weather_data['main']['temp']:.1f}",
        description=f"{weather_data['weather'][0]['description']}",
        wind=f"{weather_data['main']['feels_like']}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
