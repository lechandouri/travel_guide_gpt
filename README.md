# Travel Planner Using GPT-4

This script allows users to input trip information, including the names of cities they plan to visit and the number of days they will spend in each city. The script then generates a travel plan and multiple recommendations using OpenAI's GPT-4 language model.

## Prerequisites

- Python 3.6 or above
- OpenAI Python library
- `dotenv` Python library

## Setup

1. Clone the repository or download the script file to your local machine.
2. Install the required Python libraries
3. Obtain an API key for GPT-4 from OpenAI and store it in the `.env` file in the project directory. The `.env` file should have the following content: `GPT_4_API_KEY=YOUR_API_KEY`

## Usage

1. Run the script using the following command: `python trip_recommendation.py`
2. Follow the prompts to enter the city names and the number of days you plan to spend in each city.
3. Once you enter "done" to finish entering the trip information, the script will generate trip recommendations based on the provided information.
4. The generated recommendations will include activities, sightseeing landmarks, shopping districts, local food recommendations, tips for each city, things to be cautious about, and a fun fact about each city.
5. The trip recommendations will be displayed as a JSON object.

## Limitations

- This script relies on OpenAI's GPT-4 language model for generating trip recommendations. The quality and accuracy of the recommendations may vary based on the model's capabilities and the information provided.
- The script assumes that you have obtained a valid API key for GPT-4 from OpenAI and stored it in the `.env` file.
