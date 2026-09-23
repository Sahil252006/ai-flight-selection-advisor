import streamlit as st
import pandas as pd

from ai.parser import parse_travel_query
from utils.flight_filter import (
    filter_flights,
    calculate_time_match
)
from fuzzy.inference import calculate_suitability


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Flight Selection Advisor",
    page_icon="✈️",
    layout="wide"
)


# =========================================================
# HEADER
# =========================================================

st.title("✈️ AI Flight Selection & Travel Suitability Advisor")

st.write(
    "Find suitable flights using "
    "**AI + LangChain + Fuzzy Logic**."
)

st.divider()


# =========================================================
# USER INPUT
# =========================================================

st.subheader("🧳 Tell us about your travel")

query = st.text_area(
    "Describe your flight requirements in your own words:",
    placeholder=(
        "Example: I want to travel from Mumbai to Delhi "
        "under ₹7000. I want a direct evening flight "
        "and the journey should be less than 3 hours."
    ),
    height=130
)


# =========================================================
# SEARCH BUTTON
# =========================================================

search_button = st.button(
    "🔍 Find Suitable Flights",
    type="primary"
)


# =========================================================
# PROCESS REQUEST
# =========================================================

if search_button:

    if not query.strip():

        st.warning(
            "Please enter your travel requirements."
        )

    else:

        try:

            # -------------------------------------------------
            # STEP 1: AI PREFERENCE EXTRACTION
            # -------------------------------------------------

            with st.spinner(
                "🤖 Understanding your travel requirements..."
            ):

                preferences = parse_travel_query(
                    query
                )


            # -------------------------------------------------
            # DISPLAY AI UNDERSTANDING
            # -------------------------------------------------

            st.subheader(
                "🧠 AI Understood Your Requirements"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Departure",
                    preferences.source
                    if preferences.source
                    else "Not specified"
                )

                st.metric(
                    "Destination",
                    preferences.destination
                    if preferences.destination
                    else "Not specified"
                )


            with col2:

                budget = (
                    f"₹{preferences.budget:,.0f}"
                    if preferences.budget is not None
                    else "Not specified"
                )

                duration = (
                    f"{preferences.max_duration} hrs"
                    if preferences.max_duration is not None
                    else "Not specified"
                )

                st.metric(
                    "Maximum Budget",
                    budget
                )

                st.metric(
                    "Maximum Duration",
                    duration
                )


            with col3:

                stops = (
                    str(preferences.max_stops)
                    if preferences.max_stops is not None
                    else "Not specified"
                )

                time = (
                    preferences.preferred_time
                    .replace("_", " ")
                    .title()
                    if preferences.preferred_time
                    else "Not specified"
                )

                st.metric(
                    "Maximum Stops",
                    stops
                )

                st.metric(
                    "Preferred Time",
                    time
                )


            st.divider()


            # -------------------------------------------------
            # STEP 2: FILTER FLIGHTS
            # -------------------------------------------------

            with st.spinner(
                "✈️ Searching available flights..."
            ):

                flights = filter_flights(
                    preferences
                )


            if flights.empty:

                st.error(
                    "No flights match your specified requirements."
                )

            else:

                # -------------------------------------------------
                # STEP 3: FUZZY LOGIC
                # -------------------------------------------------

                with st.spinner(
                    "🧠 Calculating flight suitability..."
                ):

                    results = []

                    for _, flight in flights.iterrows():

                        # -----------------------------------------
                        # CALCULATE TIME PREFERENCE MATCH
                        # -----------------------------------------

                        time_match_score = calculate_time_match(
                            flight["time_period"],
                            preferences.preferred_time
                        )


                        # -----------------------------------------
                        # CALCULATE FUZZY SUITABILITY
                        # -----------------------------------------

                        score = calculate_suitability(
                            flight_price=flight["price"],
                            flight_duration=flight["duration_hours"],
                            flight_stops=flight["stops"],
                            departure_hour=flight["departure_hour"],
                            time_match_score=time_match_score
                        )


                        # -----------------------------------------
                        # STORE RESULT
                        # -----------------------------------------

                        results.append({
                            "flight_id":
                                flight["flight_id"],

                            "airline":
                                flight["airline"],

                            "price":
                                flight["price"],

                            "duration":
                                flight["duration_hours"],

                            "stops":
                                flight["stops"],

                            "departure":
                                flight["departure_time"],

                            "time_period":
                                flight["time_period"],

                            "score":
                                score
                        })


                    # -------------------------------------------------
                    # SORT HIGHEST SCORE FIRST
                    # -------------------------------------------------

                    results = sorted(
                        results,
                        key=lambda x: x["score"],
                        reverse=True
                    )


                # -------------------------------------------------
                # STEP 4: DISPLAY RESULTS
                # -------------------------------------------------

                st.subheader(
                    "✈️ Recommended Flights"
                )

                st.caption(
                    f"{len(results)} matching flight(s) found"
                )


                for index, flight in enumerate(
                    results,
                    start=1
                ):

                    with st.container(
                        border=True
                    ):

                        col1, col2, col3 = st.columns(
                            [2, 3, 2]
                        )


                        # -----------------------------------------
                        # FLIGHT INFORMATION
                        # -----------------------------------------

                        with col1:

                            st.markdown(
                                f"### {index}. "
                                f"{flight['flight_id']}"
                            )

                            st.write(
                                flight["airline"]
                            )


                        # -----------------------------------------
                        # FLIGHT DETAILS
                        # -----------------------------------------

                        with col2:

                            st.write(
                                f"🛫 **Departure:** "
                                f"{flight['departure']}"
                            )

                            st.write(
                                f"💰 **Price:** "
                                f"₹{flight['price']:,.0f}"
                            )

                            st.write(
                                f"⏱️ **Duration:** "
                                f"{flight['duration']} hours"
                            )


                            stops_text = (
                                "Non-stop"
                                if flight["stops"] == 0
                                else f"{flight['stops']} stop(s)"
                            )


                            st.write(
                                f"🔄 **Stops:** "
                                f"{stops_text}"
                            )


                        # -----------------------------------------
                        # SUITABILITY SCORE
                        # -----------------------------------------

                        with col3:

                            st.metric(
                                "Suitability",
                                f"{flight['score']}/100"
                            )

                            st.progress(
                                min(
                                    flight["score"] / 100,
                                    1.0
                                )
                            )


        except Exception as e:

            st.error(
                "Something went wrong while processing "
                "your request."
            )

            st.exception(e)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI Flight Selection & Travel Suitability Advisor "
    "• Powered by LangChain, Gemini & Fuzzy Logic"
)