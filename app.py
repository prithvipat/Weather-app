 
from flask import Flask, request, render_template
from weather import weather
from datetime import datetime

day = datetime.today().weekday()
weekdates = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekday = weekdates[day]
arr = [weekdates[day + 1], weekdates[day + 2], weekdates[day + 3], weekdates[day + 4]]

current_day = datetime.now()
month = current_day.strftime("%B")
day_num = current_day.day

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = weather(city)

    if weather_data == 'Error':
        return render_template(
            "error.html",
        )
    
    else:
        return render_template(
            "weather.html",
            day=f"{weekday} {month} {day_num}",
            title=weather_data['name'],
            temp=f"{weather_data['main']['temp']:.1f}",
            description=f"{weather_data['weather'][0]['description']}",
            feels_like=f"{weather_data['main']['feels_like']}",
            img= "sun.png"
            )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=8000)
