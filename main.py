import requests
import datetime

print("Welcome to Haashir's Adhaan Timing API!")

city = input("\nType your city: ")
country = input("Type your country: ")

# School of Though Dictionary
sot = {1: "University of Islamic Sciences, Karachi", 2: "Islamic Society of North America", 3: "Muslim World League",
       4: "Umm Al-Qura University, Makkah", 5: "Egyptian General Authority of Survey",
       6: "Institute of Geophysics, University of Tehran",
       7: "Gulf Region", 8: "Kuwait", 9: "Qatar", 10: "Union Organization islamic de France"}

print("\nSchools of thought: \n")
# Iterates over entire dictionary and prints key value pairs
for num, school in sot.items():
    print(f"{num} - {school}")

method = int(input("\nType your school of thought: "))

# Request
adhaan_data = requests.get(
    f" http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}/:date")
data = adhaan_data.json()

# Its working
if adhaan_data.status_code == 200:

    timings = data['data']['timings']

    # converts 24 hour timings into 12 hour
    for prayer, time_24h in timings.items():
        time_12h = datetime.datetime.strptime(time_24h, "%H:%M").strftime("%I:%M %p")
        timings[prayer] = time_12h

    print(f"\nThe prayer timings for {city}, \nusing the {sot[method]} is:\n")

    for prayer, time_12h in timings.items():
        if prayer == "Fajr" or prayer == "Dhuhr" or prayer == "Asr" or prayer == "Maghrib" or prayer == "Isha":
            print(f"{prayer}: {time_12h}")

    sun = input("\nWould you like to know the sunset and sunrise times? (y/n): ")
    print()
    if sun == 'y':
        for prayer, time_12h in timings.items():
            if prayer == "Sunrise" or prayer == "Sunset":
                print(f"{prayer}: {time_12h}")
        print("\nAlright Goodbye!, changes work!")
    else:
        print("\nAlright Goodbye!")

# Error
elif adhaan_data.status_code == 404:
    print("Error, that place is not found")
# Too many requests
elif adhaan_data.status_code == 529:
    print("Bad request")
# Prolly code error
else:
    print("IDK!")
