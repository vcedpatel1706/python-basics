weather = input("how is the weather")
weather=weather.lower()
if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Read a book"
elif weather == "snowy":
    activity = "Build a snowman"

print(activity)