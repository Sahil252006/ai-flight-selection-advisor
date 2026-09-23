from ai.parser import parse_travel_query
from utils.flight_filter import filter_flights


# =========================================
# USER REQUEST
# =========================================

query = """
I want to travel from Mumbai to Delhi.
My budget is around 7000 rupees.
I don't want the journey to be longer than 3 hours.
I want a direct evening flight.
"""


# =========================================
# AI PARSING
# =========================================

preferences = parse_travel_query(query)


print("\n===== AI EXTRACTED PREFERENCES =====")

print("Source:", preferences.source)
print("Destination:", preferences.destination)
print("Budget:", preferences.budget)
print("Maximum Duration:", preferences.max_duration)
print("Maximum Stops:", preferences.max_stops)
print("Preferred Time:", preferences.preferred_time)


# =========================================
# FILTER FLIGHTS
# =========================================

filtered_flights = filter_flights(
    preferences
)


print("\n===== MATCHING FLIGHTS =====")

if filtered_flights.empty:

    print("No matching flights found.")

else:

    print(
        filtered_flights[
            [
                "flight_id",
                "airline",
                "source",
                "destination",
                "price",
                "duration_hours",
                "stops",
                "departure_time",
                "time_period"
            ]
        ].to_string(index=False)
    )