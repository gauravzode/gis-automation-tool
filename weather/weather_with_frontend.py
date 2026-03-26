from flask import Flask, jsonify, request
import requests
import config

app = Flask(__name__)
API_KEY = config.API_KEY

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City is required"}), 400

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    r = requests.get(base_url, params=params)

    if r.status_code == 200:
        data = r.json()
        result = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
