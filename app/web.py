from flask import Flask
from app.api import get_weather
from app.system import get_system_data
import os

app = Flask(__name__)

@app.route("/")
def home():
    weather = get_weather()
    system = get_system_data()

    return f"""
    <h1>Monitoring Dashboard</h1>

    <h2>Wetter</h2>
    <p>Temperatur: {weather['temperature']} °C</p>
    <p>Zustand: {weather['weather']}</p>

    <h2>System</h2>
    <p>CPU: {system['cpu_usage']} %</p>
    <p>RAM: {system['memory_usage']} %</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)