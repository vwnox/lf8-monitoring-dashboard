from api import get_weather
from system import get_system_data

def combine_data():
    weather = get_weather()
    system = get_system_data()

    return {
        "weather": weather,
        "system": system
    }

if __name__ == "__main__":
    print(combine_data())