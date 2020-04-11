#3-1. Names

names = ['peter', 'ivan', 'DAVID', ' Daniel ']
print(names[0].title())
print(names[1].upper())
print(names[2].lower())
print(names[3].strip())

#3-2 Greetings

message1 = f"\nYO, {names[0].title()}, welcome to my code output!"
message2 = f"YO, {names[1].title()}, welcome to my code output!"
message3 = f"YO, {names[2].title()}, welcome to my code output!"
message4 = f"YO, {names[3].title().strip()}, welcome to my code output!"

print(message1)
print(message2)
print(message3)
print(message4)

#3-3 Your Own List

transportation_methods = ['car', 'train', 'plane', 'bus']
message5 = f"\nI don't need a {transportation_methods[0]}, just yet"
message6 = f"I like traveling in a {transportation_methods[1]} because they always bring free coffee"
message7 = f"Traveling by {transportation_methods[2]} is my favorite thing to do"
message8 = f"The {transportation_methods[3]} routes here are efficient"

print(message5)
print(message6)
print(message7)
print(message8)


