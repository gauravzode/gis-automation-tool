from flask import Flask, render_template, request
import requests
import config

app = Flask(__name__)
API_KEY = config.API_KEY

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        if not city:
            error = "City is required"
        else:
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            r = requests.get(url, params=params)

            if r.status_code == 200:
                data = r.json()
                weather = {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "desc": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"]
                }
            else:
                error = "City not found"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)


