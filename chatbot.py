import json

try:
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except:
    data = {"intents": []}

def get_response(user_input):
    user_input = user_input.lower()

    for item in data["intents"]:
        for pattern in item["patterns"]:
            if pattern in user_input:
                return item["response"]

    return "Sorry, I didn't understand. Try asking about admission, fees, placement, hostel."