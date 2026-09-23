import pandas as pd


# =========================================
# LOAD FLIGHT DATA
# =========================================

def load_flights():

    flights = pd.read_csv(
        "data/flights.csv"
    )

    return flights


# =========================================
# CONVERT TIME TO DECIMAL HOUR
# =========================================

def convert_time_to_hour(time_string):

    hour, minute = map(
        int,
        time_string.split(":")
    )

    return hour + (minute / 60)


# =========================================
# GET TIME PERIOD
# =========================================

def get_time_period(hour):

    if 0 <= hour < 7:
        return "early_morning"

    elif 7 <= hour < 12:
        return "morning"

    elif 12 <= hour < 17:
        return "afternoon"

    elif 17 <= hour < 21:
        return "evening"

    else:
        return "night"


# =========================================
# FILTER FLIGHTS
# =========================================

def filter_flights(preferences):

    flights = load_flights()

    # -----------------------------------------
    # SOURCE
    # -----------------------------------------

    if preferences.source:

        flights = flights[
            flights["source"].str.lower()
            == preferences.source.lower()
        ]


    # -----------------------------------------
    # DESTINATION
    # -----------------------------------------

    if preferences.destination:

        flights = flights[
            flights["destination"].str.lower()
            == preferences.destination.lower()
        ]


    # -----------------------------------------
    # MAXIMUM BUDGET
    # -----------------------------------------

    if preferences.budget is not None:

        flights = flights[
            flights["price"]
            <= preferences.budget
        ]


    # -----------------------------------------
    # MAXIMUM DURATION
    # -----------------------------------------

    if preferences.max_duration is not None:

        flights = flights[
            flights["duration_hours"]
            <= preferences.max_duration
        ]


    # -----------------------------------------
    # MAXIMUM STOPS
    # -----------------------------------------

    if preferences.max_stops is not None:

        flights = flights[
            flights["stops"]
            <= preferences.max_stops
        ]


    # -----------------------------------------
    # DEPARTURE HOUR
    # -----------------------------------------

    if not flights.empty:

        flights = flights.copy()

        flights["departure_hour"] = (
            flights["departure_time"]
            .apply(convert_time_to_hour)
        )

        flights["time_period"] = (
            flights["departure_hour"]
            .apply(get_time_period)
        )


    return flights

# =========================================
# CALCULATE TIME PREFERENCE MATCH
# =========================================

def calculate_time_match(
    flight_period,
    preferred_period
):

    if preferred_period is None:
        return 1.0

    if flight_period == preferred_period:
        return 1.0

    adjacent_periods = {
        "early_morning": ["morning"],
        "morning": ["early_morning", "afternoon"],
        "afternoon": ["morning", "evening"],
        "evening": ["afternoon", "night"],
        "night": ["evening"]
    }

    if flight_period in adjacent_periods.get(
        preferred_period,
        []
    ):
        return 0.55

    return 0.15