import requests

def get_weather(city="Hamburg"):
    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)
    data = response.json()

    current = data["current_condition"][0]

    temperature = int(current["temp_C"])

    # ➕ NEU: Temperatur-Logik
    if temperature > 30:
        weather_warning = "🔥 Sehr heiß → Lüfter hochdrehen!"
    elif temperature > 20:
        weather_warning = "🌤️ Warm"
    else:
        weather_warning = "❄️ Kühl"

    weather_data = {
        "temperature": temperature,
        "weather": current["weatherDesc"][0]["value"],
        "warning": weather_warning   # ➕ NEU
    }
    
    return weather_data
    
if __name__ == "__main__":
    print(get_weather())