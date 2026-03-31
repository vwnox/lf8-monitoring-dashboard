import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        
from app.api import get_weather

def test_get_weather():
    data = get_weather()
    
    assert "temperature" in data
    assert "weather" in data
    