import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal

from langchain_google_genai import ChatGoogleGenerativeAI


# =========================================
# LOAD ENVIRONMENT VARIABLES
# =========================================

load_dotenv()


# =========================================
# USER PREFERENCE SCHEMA
# =========================================

class TravelPreferences(BaseModel):

    source: Optional[str] = Field(
        default=None,
        description="Departure city mentioned by the user."
    )

    destination: Optional[str] = Field(
        default=None,
        description="Destination city mentioned by the user."
    )

    budget: Optional[float] = Field(
        default=None,
        description="Maximum budget for the flight in Indian Rupees."
    )

    max_duration: Optional[float] = Field(
        default=None,
        description="Maximum acceptable flight duration in hours."
    )

    max_stops: Optional[int] = Field(
        default=None,
        description="Maximum number of stops the user accepts."
    )

    preferred_time: Optional[
        Literal[
            "early_morning",
            "morning",
            "afternoon",
            "evening",
            "night"
        ]
    ] = Field(
        default=None,
        description="Preferred departure period."
    )


# =========================================
# CREATE GEMINI MODEL
# =========================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    max_retries=3
)


# =========================================
# STRUCTURED OUTPUT MODEL
# =========================================

structured_llm = llm.with_structured_output(
    TravelPreferences
)


# =========================================
# PARSE USER QUERY
# =========================================

def parse_travel_query(user_query: str) -> TravelPreferences:

    prompt = f"""
You are a travel preference extraction assistant.

Read the user's natural-language flight request and extract
only the travel preferences that are explicitly stated or
strongly implied.

Important rules:

1. Extract the departure city.
2. Extract the destination city.
3. Extract the maximum budget in INR.
4. Extract the maximum acceptable flight duration in hours.
5. Convert "direct", "non-stop", or "without stops" to max_stops = 0.
6. If the user says "one stop", use max_stops = 1.
7. Convert time preferences into one of:
   early_morning, morning, afternoon, evening, night.
8. If a value is not mentioned, return null.
9. Do not invent missing preferences.

User request:

{user_query}
"""

    result = structured_llm.invoke(prompt)

    return result