import json

indian_states_and_capitals = {
    "Kerala": "Thiruvananthapuram",
    "Tamil Nadu": "Chennai",
    "Maharashtra": "Mumbai",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Goa": "Panaji",
    "Uttar Pradesh": "Lucknow"
}
# Write the dictionary to a JSON file
with open('indian_states.json', 'w') as file:
    json.dump(indian_states_and_capitals, file, indent=4)
