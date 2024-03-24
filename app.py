from flask import Flask, request, render_template
from weather import weather, forecast, images, forecast_img
from datetime import datetime

# Getting the Date
day = datetime.today().weekday()
weekdates = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekday = weekdates[day]
arr = [weekdates[day + 1], weekdates[day + 2], weekdates[day + 3], weekdates[day + 4]] # My variable names suck :()
current_day = datetime.now()
month = current_day.strftime("%B")
day_num = current_day.day

app = Flask(__name__)

# Homepage
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Weather page for said city
@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = weather(city)  # Data from today

    if weather_data == 'Error': # If there is an error with the city name it goes to a seperate page
        return render_template(
            "error.html",
        )

    else:
        forecast_data = forecast(city) # Data from upcoming days
        img=images(city) # Images
        descript = f"{weather_data['weather'][0]['description']}"
        descript.capitalize()

        dayOneImg = forecast_img(city, 8)
        dayTwoImg = forecast_img(city, 16)

        return render_template(
            "weather.html",
            # Current Day
            day=f"{weekday} {month} {day_num}",
            title=weather_data['name'],
            temp=f"{weather_data['main']['temp']:.1f}",
            description=descript,
            feels_like=f"{weather_data['main']['feels_like']}",
            img=img,

            # Next Day
            dayOne=f"{arr[0]}",
            tempDay1 = f"{forecast_data['list'][6]['main']['temp']}",
            imgDay1 = f"{dayOneImg}",

            # Day After
            dayTwo=f"{arr[1]}",
            tempDay2 = f"{forecast_data['list'][14]['main']['temp']}",
            imgDay2 = f"{dayTwoImg}"
        )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
