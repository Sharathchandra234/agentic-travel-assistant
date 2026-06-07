
from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import GOOGLE_API_KEY, GEMINI_MODEL
import re
import logging

from src.memory import TravelMemory
from src.tools import weather_tool, hotel_tool, budget_tool

logger = logging.getLogger(__name__)


class TravelAgent:
    def __init__(self):
        self.memory = TravelMemory()

        self.llm = ChatGoogleGenerativeAI(
            model=GEMINI_MODEL,
            google_api_key=GOOGLE_API_KEY,
            temperature=0.3,
        )

    def extract_details(self, query: str):
        numbers = re.findall(r"\d+", query)

        days = 3
        budget = 20000

        if len(numbers) >= 1:
            days = int(numbers[0])

        if len(numbers) >= 2:
            budget = int(numbers[1])

        destination = "Unknown"

        words = query.lower().split()

        if "to" in words:
            index = words.index("to")

            if index + 1 < len(words):
                destination = words[index + 1].capitalize()

        return destination, budget, days

    def generate_itinerary(
        self,
        destination,
        budget,
        days,
    ):
        prompt = f"""
Create a detailed {days}-day travel itinerary for {destination}.

Budget: ₹{budget}

For each day provide:

Day Number
Morning Activities
Afternoon Activities
Evening Activities
Food Recommendations
Estimated Daily Cost

Make the itinerary realistic and budget friendly.
"""

        response = self.llm.invoke(prompt)

        return response.content

    def plan_trip(self, query: str):
        destination, budget, days = self.extract_details(query)

        weather = weather_tool.invoke(
            {"city": destination}
        )

        hotels = hotel_tool.invoke(
            {"city": destination}
        )

        budget_plan = budget_tool.invoke(
            {
                "destination": destination,
                "budget": budget,
            }
        )

        itinerary = self.generate_itinerary(
            destination,
            budget,
            days,
        )

        self.memory.save_preference(
            "preferred_destination",
            destination,
        )

        self.memory.save_conversation(query)

        prompt = f"""
Give travel advice for:

Destination: {destination}
Budget: ₹{budget}
Days: {days}

Include:
- Top attractions
- Packing tips
- Budget tips
- Safety tips

Keep it under 100 words.
"""

        response = self.llm.invoke(prompt)

        travel_advice = response.content

        return {
            "destination": destination,
            "budget": budget,
            "days": days,
            "weather": weather,
            "hotels": hotels,
            "budget_plan": budget_plan,
            "itinerary": itinerary,
            "travel_advice": travel_advice,
        }

    def get_memory_summary(self):
        return self.memory.get_recent_conversations()

