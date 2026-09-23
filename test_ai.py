from ai.parser import parse_travel_query


query = """
I want to travel from Mumbai to Delhi.
My budget is around 7000 rupees.
I don't want the journey to be longer than 3 hours.
I want a direct evening flight.
"""


preferences = parse_travel_query(query)


print("\n===== EXTRACTED TRAVEL PREFERENCES =====")

print("Source:", preferences.source)
print("Destination:", preferences.destination)
print("Budget:", preferences.budget)
print("Maximum Duration:", preferences.max_duration)
print("Maximum Stops:", preferences.max_stops)
print("Preferred Time:", preferences.preferred_time)