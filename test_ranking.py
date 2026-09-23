from ai.parser import parse_travel_query
from utils.flight_filter import filter_flights
from fuzzy.inference import calculate_suitability


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
# AI PREFERENCE EXTRACTION
# =========================================

preferences = parse_travel_query(query)


# =========================================
# FILTER FLIGHTS
# =========================================

flights = filter_flights(preferences)


# =========================================
# APPLY FUZZY LOGIC
# =========================================

results = []


for _, flight in flights.iterrows():

    score = calculate_suitability(
        flight_price=flight["price"],
        flight_duration=flight["duration_hours"],
        flight_stops=flight["stops"],
        departure_hour=flight["departure_hour"]
    )

    results.append({
        "flight_id": flight["flight_id"],
        "airline": flight["airline"],
        "price": flight["price"],
        "duration_hours": flight["duration_hours"],
        "stops": flight["stops"],
        "departure_time": flight["departure_time"],
        "suitability": score
    })


# =========================================
# SORT BY FUZZY SCORE
# =========================================

results = sorted(
    results,
    key=lambda x: x["suitability"],
    reverse=True
)


# =========================================
# DISPLAY RESULTS
# =========================================

print("\n===== AI PREFERENCES =====")

print("Source:", preferences.source)
print("Destination:", preferences.destination)
print("Budget:", preferences.budget)
print("Maximum Duration:", preferences.max_duration)
print("Maximum Stops:", preferences.max_stops)
print("Preferred Time:", preferences.preferred_time)


print("\n===== FLIGHT RECOMMENDATIONS =====")


if not results:

    print("No suitable flights found.")

else:

    for i, flight in enumerate(results, start=1):

        print(
            f"\n{i}. {flight['flight_id']} - "
            f"{flight['airline']}"
        )

        print(
            f"   Price: ₹{flight['price']}"
        )

        print(
            f"   Duration: {flight['duration_hours']} hours"
        )

        print(
            f"   Stops: {flight['stops']}"
        )

        print(
            f"   Departure: {flight['departure_time']}"
        )

        print(
            f"   Suitability Score: "
            f"{flight['suitability']}/100"
        )