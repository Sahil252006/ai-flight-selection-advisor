from fuzzy.inference import calculate_suitability


# =========================================
# TEST FLIGHT
# =========================================

# 18.5 = 18:30 / 6:30 PM
score = calculate_suitability(
    flight_price=5800,
    flight_duration=2.3,
    flight_stops=0,
    departure_hour=14
)


print(
    "Flight Suitability Score:",
    score
)