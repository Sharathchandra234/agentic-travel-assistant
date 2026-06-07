
import os
import requests

from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

OPENWEATHER_API_KEY = os.getenv(
    "OPENWEATHER_API_KEY"
)


@tool
def weather_tool(city: str):
    """Get weather information for a city."""

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",
        }

        response = requests.get(
            url,
            params=params,
            timeout=10,
        )

        data = response.json()
        print("OPENWEATHER RESPONSE:", data)

        if response.status_code != 200:
            return {
                "error": data.get(
                    "message",
                    "Weather service unavailable"
                )
            }

        return {
            "temperature": f"{data['main']['temp']}°C",
            "condition": data['weather'][0]['main'],
            "humidity": f"{data['main']['humidity']}%"
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@tool
def hotel_tool(city: str):
    """Get hotel recommendations for a city."""

    return [
        {"name": "Grand Hotel", "price": 4000},
        {"name": "Sea View Resort", "price": 5500},
        {"name": "Budget Inn", "price": 2500},
    ]


@tool
def budget_tool(
    destination: str,
    budget: int,
):
    """Generate a travel budget allocation."""

    return {
        "accommodation": int(budget * 0.4),
        "food": int(budget * 0.3),
        "transportation": int(budget * 0.15),
        "activities": int(budget * 0.15),
    }

