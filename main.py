import random

print("Welcome to Mad libs")
print("Choose your story")
print("1 - Hospital")
print("2 - Camping")
print("3 - Magic castle")

choice = input("Type 1, 2, or 3: ")
story = ""
words = []
inputs = []

if choice not in ("1", "2", "3"):
    print("Wrong choice!\n")
    quit()

if choice == "1":
    inputs += [
        "Enter a number: ",
        "Enter a measure of time: ",
        "Enter a mode of transportation: ",
        "Enter an adjective: ",
        "Enter another adjective: ",
        "Enter a noun: ",
        "Enter a color: ",
        "Enter a part of the body: ",
        "Enter a verb: ",
        "Enter a number: ",
        "Enter a noun: ",
        "Enter another noun: ",
        "Enter a part of the body: ",
        "Enter a verb: ",
        "Enter a noun: ",
        "Enter an adjective: ",
        "Enter a silly word: ",
        "Enter a noun: "
    ]
    for i in inputs:
        words.append(input(i))

    story += (
        f"It was about {words[0]} {words[1]} ago when I arrived at the hospital in a {words[2]} The hospital is a/an\n"
        f"{words[3]} place, there are a lot of {words[4]} {words[5]} here. There are nurses here who have\n"
        f"{words[6]} {words[7]}. If someone wants to come into my room I told them that they have to {words[8]} first.\n"
        f"I've decorated my room with {words[9]} {words[10]}. Today I talked to a doctor and they were wearing a\n"
        f"{words[11]} on their {words[12]}. I heard that all doctors {words[13]} {words[14]} every day for breakfast.\n"
        f"The most {words[15]} thing about being in the hospital is the {words[16]} {words[17]}!\n"
    )

elif choice == "2":
    inputs += [
        "Enter a proper noun(person's name): ",
        "Enter a noun: ",
        "Enter an adjective(feeling): ",
        "Entera a verb: ",
        "Enter an adjective(feeling): ",
        "Enter an animal: ",
        "Enter a verb: ",
        "Enter a color: ",
        "Enter a verb(ending in ing): ",
        "Enter an adverb(ending in ly): ",
        "Enter a number: ",
        "Enter a measure of time: ",
        "Enter a color: ",
        "Enter an animal: ",
        "Enter a number: ",
        "Enter a silly word: ",
        "Enter a noun: ",
    ]

    for i in inputs:
        words.append(input(i))

    story += (
        f"This weekend I am going camping with {words[0]}. I packed my lantern, sleeping bag,\n"
        f"and {words[1]}. I am so {words[2]} to {words[3]} in a tent. I am {words[4]} we might see a(n)\n"
        f"{words[5]}, I hear they're kind of a dangerous. While we're camping, we are going to hike, fish,\n"
        f"and {words[6]}. I have heard that the {words[7]} lake is great for {words[8]}. Then we will {words[9]}\n"
        f"hike through the forest for {words[10]} {words[11]}. If I see a {words[12]} {words[13]} while hiking, I\n"
        f"I am going to bring it home as a pet! At night we will tell {words[14]} {words[15]} stories and roast\n"
        f"{words[16]} around the campfire!\n"
    )

else:
    inputs += [
        "Enter a proper noun(person's name): ",
        "Enter an adjective: ",
        "Enter a color: ",
        "Enter an animal: ",
        "Enter a place: ",
        "Enter an adjective: ",
        "Enter a magical creature(plural): ",
        "Enter an adjective: ",
        "Enter a magical creature(plural): ",
        "Enter a room in a house: ",
        "Enter a noun: ",
        "Enter another noun: ",
        "Enter a noun(plural): ",
        "Enter an adjective: ",
        "Enter a noun(plural): ",
        "Enter a number: ",
        "Enter a measure of time: ",
        "Enter a verb(ending in ing): ",
        "Enter an adjective: ",
        "Enter a noun: ",
    ]

    for i in inputs:
        words.append(input(i))

    story += (
        f"Dear {words[0]}, I am writing to you from a {words[1]} castle in an enchanted forest.\n"
        f"I found myself here one day after going for a ride on a {words[2]} {words[3]} in {words[4]}.\n"
        f"There are {words[5]} {words[6]} and {words[7]} {words[8]} here! In the {words[9]} there is a pool full\n"
        f"of {words[10]}. I fall asleep each night on a {words[11]} of {words[12]} and dream of {words[13]}\n"
        f"{words[14]}. It feels as though I have lived here for {words[15]} {words[16]}. I hope one day\n"
        f"you can visit, although the only way to get here now is {words[17]} on a {words[18]} {words[19]}!!"
    )

print("/// Your Mad libs story ///")
print(story)