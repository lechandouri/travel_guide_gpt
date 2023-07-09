import os
import openai
import json
from dotenv import load_dotenv
load_dotenv()

def setup_openai_params():
    openai.api_key = os.getenv("GPT_4_API_KEY")
    
def get_completion(prompt):
    setup_openai_params()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.0
        )
    except Exception as e:
        return f"Sorry, got an error: {e}"
    return response.choices[0].message["content"]

if __name__ == "__main__":

    trip_information = []
    while True:
        city = input("Enter the name of a city you'll visit (or 'done' to finish): ")
        if city == "done":
            break
        days = input("Enter the number of days in {}: ".format(city))
        trip = {"city": city, "days": days}
        trip_information.append(trip)

    context = f"""
    Your task is to suggest a trip itinerary for each city and its associated number of days.\
    Breakdown the suggested itinerary by day.\
    The itinerary should include the following:\
        Activities of all sorts (cultural, entertainment, etc), and their associated price when they are not free. If they are free, mention that.\
        Sightseeing and landmarks recommendations (monuments, parks, etc).\
        Shopping districts, and any nice walking areas (markets, fashion districts, etc).\
        Local food recommendations (pastries, dishes, snacks, etc).\
        Tips for each city about things that should be booked in advance, but also any useful information prior to travelling.\
        Things to be cautious about, when necessary.\
        One fun fact about the city.\
    Output the suggestions for the trip as a JSON object.\
    """
    messages = [
        {'role':'system', 'content': context},
        {'role':'user', 'content':f"Trip information: ```{trip_information}```"}]

    response = get_completion(messages)
    print(response)
    
    with open('travel_plan.json', 'w') as file:
        json.dump(trip_information, file)
