happy_words = ["happy", "joy", "cheerful", "glad", "awesome", "good", "excited", "delighted"]
sad_words = ["sad", "unhappy", "depressed", "crying", "upset", "lonely", "bad", "gloomy"]

text = input("Enter a sentence: ").lower()

happy_count = 0
sad_count = 0

for word in happy_words:
    if word in text:
        happy_count += 2

for word in sad_words:
    if word in text:
        sad_count += 2

if happy_count > sad_count:
    print("Prediction: Happy")
elif sad_count > happy_count:
    print("Prediction: Sad")
else:
    print("Prediction: Neutral")
