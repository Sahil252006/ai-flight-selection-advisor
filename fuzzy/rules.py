import skfuzzy.control as ctrl


def create_rules(
    price,
    duration,
    stops,
    departure_time,
    time_match,
    suitability
):

    rules = [

        # =========================================
        # TIME PREFERENCE RULES
        # =========================================

        ctrl.Rule(
            time_match["excellent"]
            & price["cheap"]
            & duration["short"]
            & stops["direct"],
            suitability["high"]
        ),

        ctrl.Rule(
            time_match["excellent"]
            & price["moderate"]
            & duration["short"]
            & stops["direct"],
            suitability["high"]
        ),

        ctrl.Rule(
            time_match["excellent"]
            & duration["short"]
            & stops["direct"],
            suitability["high"]
        ),

        ctrl.Rule(
            time_match["excellent"]
            & price["cheap"]
            & duration["medium"]
            & stops["direct"],
            suitability["high"]
        ),

        ctrl.Rule(
            time_match["moderate"]
            & price["cheap"]
            & duration["short"]
            & stops["direct"],
            suitability["medium"]
        ),

        ctrl.Rule(
            time_match["moderate"]
            & price["moderate"]
            & duration["short"]
            & stops["direct"],
            suitability["medium"]
        ),

        ctrl.Rule(
            time_match["poor"]
            & duration["long"],
            suitability["low"]
        ),

        ctrl.Rule(
            time_match["poor"]
            & stops["many"],
            suitability["low"]
        ),

        # =========================================
        # HIGH SUITABILITY RULES
        # =========================================

        ctrl.Rule(
            price["cheap"]
            & duration["short"]
            & stops["direct"]
            & departure_time["morning"],
            suitability["high"]
        ),

        ctrl.Rule(
            price["cheap"]
            & duration["short"]
            & stops["direct"]
            & departure_time["evening"],
            suitability["high"]
        ),

        ctrl.Rule(
            price["moderate"]
            & duration["short"]
            & stops["direct"]
            & departure_time["morning"],
            suitability["high"]
        ),

        ctrl.Rule(
            price["moderate"]
            & duration["short"]
            & stops["direct"]
            & departure_time["evening"],
            suitability["high"]
        ),

        ctrl.Rule(
            price["cheap"]
            & duration["medium"]
            & stops["direct"]
            & departure_time["morning"],
            suitability["high"]
        ),

        ctrl.Rule(
            price["cheap"]
            & duration["medium"]
            & stops["direct"]
            & departure_time["evening"],
            suitability["high"]
        ),

        # =========================================
        # MEDIUM SUITABILITY RULES
        # =========================================

        ctrl.Rule(
            price["expensive"]
            & duration["short"]
            & stops["direct"]
            & departure_time["morning"],
            suitability["medium"]
        ),

        ctrl.Rule(
            price["expensive"]
            & duration["short"]
            & stops["direct"]
            & departure_time["evening"],
            suitability["medium"]
        ),

        ctrl.Rule(
            price["moderate"]
            & duration["medium"]
            & stops["direct"]
            & departure_time["afternoon"],
            suitability["medium"]
        ),

        ctrl.Rule(
            price["moderate"]
            & duration["long"]
            & stops["few"]
            & departure_time["afternoon"],
            suitability["medium"]
        ),

        ctrl.Rule(
            price["expensive"]
            & duration["medium"]
            & stops["few"]
            & departure_time["morning"],
            suitability["medium"]
        ),

        # =========================================
        # LOW SUITABILITY RULES
        # =========================================

        ctrl.Rule(
            price["cheap"]
            & duration["long"]
            & stops["many"]
            & departure_time["night"],
            suitability["low"]
        ),

        ctrl.Rule(
            price["expensive"]
            & duration["long"]
            & stops["many"]
            & departure_time["night"],
            suitability["low"]
        ),

        ctrl.Rule(
            duration["long"]
            & stops["many"]
            & departure_time["night"],
            suitability["low"]
        ),

        ctrl.Rule(
            price["expensive"]
            & duration["long"]
            & stops["few"]
            & departure_time["night"],
            suitability["low"]
        ),

        # =========================================
        # ADDITIONAL TIME-BASED RULES
        # =========================================

        ctrl.Rule(
            departure_time["night"]
            & duration["long"],
            suitability["low"]
        ),

        ctrl.Rule(
            departure_time["early_morning"]
            & stops["many"],
            suitability["medium"]
        ),

        ctrl.Rule(
            departure_time["evening"]
            & stops["direct"]
            & duration["short"],
            suitability["high"]
        ),

        ctrl.Rule(
            departure_time["morning"]
            & stops["direct"]
            & duration["short"],
            suitability["high"]
        ),

        # =========================================
        # ADDITIONAL TIME-PREFERENCE RULES
        # =========================================

        ctrl.Rule(
            time_match["excellent"]
            & departure_time["evening"]
            & duration["short"],
            suitability["high"]
        ),

        ctrl.Rule(
            time_match["excellent"]
            & departure_time["morning"]
            & duration["short"],
            suitability["high"]
        ),

        ctrl.Rule(
            time_match["excellent"]
            & departure_time["afternoon"]
            & duration["short"],
            suitability["high"]
        ),

        ctrl.Rule(
            time_match["moderate"]
            & departure_time["afternoon"]
            & duration["short"],
            suitability["medium"]
        ),

        ctrl.Rule(
            time_match["moderate"]
            & departure_time["morning"]
            & duration["medium"],
            suitability["medium"]
        ),

        ctrl.Rule(
            time_match["poor"]
            & departure_time["night"]
            & duration["long"],
            suitability["low"]
        )
    ]

    return rules