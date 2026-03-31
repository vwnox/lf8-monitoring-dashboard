from flask import Flask
from api import get_weather
from system import get_system_data

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
    app.run(debug=True)
    