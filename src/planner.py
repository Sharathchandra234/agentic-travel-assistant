class TravelPlanner:
    def create_itinerary(self, destination, budget, days):

        places = {
            "Goa": [
                "Baga Beach & Calangute Beach",
                "Fort Aguada & Old Goa Churches",
                "Dudhsagar Falls & Panjim Market",
                "Anjuna Beach & Vagator Beach",
                "Sunset Cruise on Mandovi River",
            ]
        }

        activities = places.get(
            destination,
            [f"Explore {destination}"]
        )

        itinerary = []

        for day in range(days):
            itinerary.append(
                {
                    "day": day + 1,
                    "activity": activities[
                        day % len(activities)
                    ]
                }
            )

        return itinerary