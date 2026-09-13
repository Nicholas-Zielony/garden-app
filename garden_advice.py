
# FUNCTIONS
def get_advice(prompt, garden_dict):
    """
    Get user input to select a season or plant based on args given.
    Returns advice to be used later.\n

    args:\n
    prompt (string):
        added onto input string for question context.\n
    garden_dict (dict[string]):
        keys and responses for the season or plant.\n

    return:\n
        string: The advice given for later use.

    """
    # Allow user input for season and plant type and check for errors
    user_input = input(f"Please enter a {prompt}: ").strip().lower()
    if garden_dict.get(user_input) is not None:
        return garden_dict.get(user_input)
    else:
        # Give no specific advice (bad user input)
        return garden_dict['ERROR']


def main():
    """
    Main code section.
    Gives advice for gardeners based on season and plant type inputted.
    """

    # Dictionaries
    garden_season = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n",
        "ERROR": "No advice for this season.\n"
    }
    garden_plant = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "ERROR": "No advice for this type of plant."
    }

    # Variable to hold gardening advice
    advice = ""

    # Determine advice based on season and plant type
    advice += get_advice("season (summer or winter)", garden_season)
    advice += get_advice("plant (flower or vegetable)", garden_plant)

    # Print the generated advice
    print(advice)

    # TODO: Examples of possible features to add:
    # - Recommend plants based on the entered season.


# MAIN LAUNCHER
if __name__ == "__main__":
    main()
