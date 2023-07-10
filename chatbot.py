import json
import nltk
from nltk.chat.util import Chat, reflections
from weather import get_weather

def load_pairs_from_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return [(pair["pattern"], pair["responses"]) for pair in data]

def chatbot():
    print("Hi, I'm the chatbot. How can I assist you today?")
    pairs = load_pairs_from_file("pairs.json")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Bye! Take care.")
            break
        elif "weather" in user_input.lower():
            location = "Marble Falls, TX"  # Set the location for weather query
            weather_info = get_weather(location)
            if weather_info:
                temperature = weather_info['Temperature']['Metric']['Value']
                weather_text = weather_info['WeatherText']
                response = f"The current temperature in {location} is {temperature}°C. The weather condition is {weather_text}."
            else:
                response = "Sorry, I couldn't retrieve the weather information."
            print(response)
        else:
            response = chat.respond(user_input)
            print(response)

if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()
