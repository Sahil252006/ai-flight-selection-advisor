import skfuzzy.control as ctrl

from fuzzy.membership import create_fuzzy_variables
from fuzzy.rules import create_rules


# =========================================
# CREATE FUZZY VARIABLES
# =========================================

(
    price,
    duration,
    stops,
    departure_time,
    time_match,
    suitability
) = create_fuzzy_variables()


# =========================================
# CREATE FUZZY RULES
# =========================================

rules = create_rules(
    price,
    duration,
    stops,
    departure_time,
    time_match,
    suitability
)


# =========================================
# CREATE FUZZY CONTROL SYSTEM
# =========================================

control_system = ctrl.ControlSystem(
    rules
)


# =========================================
# CALCULATE FLIGHT SUITABILITY
# =========================================

def calculate_suitability(
    flight_price,
    flight_duration,
    flight_stops,
    departure_hour,
    time_match_score=1.0
):

    # Create a fresh simulation
    simulation = ctrl.ControlSystemSimulation(
        control_system
    )

    # -----------------------------------------
    # INPUT 1: PRICE
    # -----------------------------------------

    simulation.input["price"] = flight_price

    # -----------------------------------------
    # INPUT 2: FLIGHT DURATION
    # -----------------------------------------

    simulation.input["duration"] = flight_duration

    # -----------------------------------------
    # INPUT 3: NUMBER OF STOPS
    # -----------------------------------------

    simulation.input["stops"] = flight_stops

    # -----------------------------------------
    # INPUT 4: ACTUAL DEPARTURE TIME
    # -----------------------------------------

    simulation.input["departure_time"] = departure_hour

    # -----------------------------------------
    # INPUT 5: USER TIME PREFERENCE MATCH
    # -----------------------------------------

    simulation.input["time_match"] = time_match_score

    # -----------------------------------------
    # RUN FUZZY INFERENCE
    # -----------------------------------------

    simulation.compute()

    # -----------------------------------------
    # DEFUZZIFICATION
    # -----------------------------------------

    score = simulation.output["suitability"]

    return round(
        float(score),
        2
    )