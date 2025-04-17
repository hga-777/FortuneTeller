
import random

print("🔮 Welcome to Hritik Anand's Fortune Teller (21JE0410) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ")

fortunes = {
    "happy": [
        "Great things await you, Hritik! Keep smiling.",
        "Happiness brings success — enjoy every moment!"
    ],
    "sad": [
        "Even rainy days lead to rainbows.",
        "Your tears water the seeds of greatness."
    ],
    "neutral": [
        "Peace brings power. Stay centered.",
        "The balance you hold is your superpower."
    ],
    "stressed": [
        "Breathe, Hritik. You've got this!",
        "Stress is temporary. Strength is forever."
    ]
}

selected_fortune = random.choice(fortunes.get(mood.lower(), ["Mood unclear, but surprises are coming your way!"]))
print(f"✨ Your fortune: {selected_fortune} ✨")
