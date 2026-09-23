import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl


def create_fuzzy_variables():

    # =========================================
    # PRICE INPUT
    # =========================================

    price = ctrl.Antecedent(
        np.arange(0, 15001, 100),
        "price"
    )

    price["cheap"] = fuzz.trapmf(
        price.universe,
        [0, 0, 4000, 6500]
    )

    price["moderate"] = fuzz.trimf(
        price.universe,
        [4500, 7500, 10000]
    )

    price["expensive"] = fuzz.trapmf(
        price.universe,
        [8000, 11000, 15000, 15000]
    )

    # =========================================
    # FLIGHT DURATION INPUT
    # =========================================

    duration = ctrl.Antecedent(
        np.arange(0, 8.1, 0.1),
        "duration"
    )

    duration["short"] = fuzz.trapmf(
        duration.universe,
        [0, 0, 1.8, 2.5]
    )

    duration["medium"] = fuzz.trimf(
        duration.universe,
        [2, 3.5, 5]
    )

    duration["long"] = fuzz.trapmf(
        duration.universe,
        [4.5, 5.5, 8, 8]
    )

    # =========================================
    # NUMBER OF STOPS INPUT
    # =========================================

    stops = ctrl.Antecedent(
        np.arange(0, 4, 1),
        "stops"
    )

    stops["direct"] = fuzz.trimf(
        stops.universe,
        [0, 0, 1]
    )

    stops["few"] = fuzz.trimf(
        stops.universe,
        [0, 1, 2]
    )

    stops["many"] = fuzz.trapmf(
        stops.universe,
        [1, 2, 3, 3]
    )

    # =========================================
    # DEPARTURE TIME INPUT
    # =========================================

    departure_time = ctrl.Antecedent(
        np.arange(0, 24.1, 0.1),
        "departure_time"
    )

    # Early morning: approximately 00:00–07:00
    departure_time["early_morning"] = fuzz.trapmf(
        departure_time.universe,
        [0, 0, 5, 7]
    )

    # Morning: approximately 06:00–12:00
    departure_time["morning"] = fuzz.trimf(
        departure_time.universe,
        [6, 9, 12]
    )

    # Afternoon: approximately 11:00–17:00
    departure_time["afternoon"] = fuzz.trimf(
        departure_time.universe,
        [11, 14, 17]
    )

    # Evening: approximately 16:00–21:00
    departure_time["evening"] = fuzz.trimf(
        departure_time.universe,
        [16, 19, 22]
    )

    # Night: approximately 21:00–24:00
    departure_time["night"] = fuzz.trapmf(
        departure_time.universe,
        [21, 23, 24, 24]
    )

    # =========================================
    # USER TIME PREFERENCE MATCH
    # =========================================

    time_match = ctrl.Antecedent(
        np.arange(0, 1.01, 0.01),
        "time_match"
    )

    time_match["poor"] = fuzz.trapmf(
        time_match.universe,
        [0, 0, 0.25, 0.45]
    )

    time_match["moderate"] = fuzz.trimf(
        time_match.universe,
        [0.3, 0.55, 0.8]
    )

    time_match["excellent"] = fuzz.trapmf(
        time_match.universe,
        [0.65, 0.8, 1, 1]
    )

    # =========================================
    # SUITABILITY OUTPUT
    # =========================================

    suitability = ctrl.Consequent(
        np.arange(0, 101, 1),
        "suitability"
    )

    suitability["low"] = fuzz.trapmf(
        suitability.universe,
        [0, 0, 30, 50]
    )

    suitability["medium"] = fuzz.trimf(
        suitability.universe,
        [30, 55, 75]
    )

    suitability["high"] = fuzz.trapmf(
        suitability.universe,
        [65, 80, 100, 100]
    )

    # =========================================
    # RETURN FUZZY VARIABLES
    # =========================================

    return (
        price,
        duration,
        stops,
        departure_time,
        time_match,
        suitability
    )