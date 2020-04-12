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

#3-4. Guest List:

relatives = ["dad", "MOM", " marina", "LUISA "]

message9 = f"\n{relatives[0].title()}, let us go for some dinner together."
message10 = f" Once this is over, I will take you out for dinner, {relatives[1].lower()}."
message11 = f"It's been a while since the last time we have met, let me update you over a dinner together aunt {relatives[2].title().lstrip()}. "
message12 = f" {relatives[3].title().rstrip()}, we have so much to talk about, let's eat something together so you can laugh at my stories. "

print(message9)
print(message10.lstrip())
print(message11.rstrip())
print(message12.strip())

#3-5. Changing Guest List

print(f"\nAunt {relatives[2].title().lstrip()} cannot make it, so we will need to change the guest list.\nPrinting new set of invitations (some have not changed).\n***NEW INVITATIONS***")

relatives[2] = " josefina "
new_message11 = f" Aunt {relatives[2].strip().title()}, I was not able to say goodbye before you left, let us have a last dinner together."

print(message9)
print(message10.lstrip())
print(new_message11.lstrip())
print(message12.strip())

#3-6. More Guests:

announcement_message = """

Dear family, we have got lucky today! I have been informed by the resturant that there will be a bigger table available for us.
Therefore, I will invite 3 more guests! Be on the lookout for new invitations coming over.

Printing the new guest list:
"""

print(announcement_message)

relatives.insert(0, "Carolina")
relatives.insert(2, "Gabriel")
relatives.append("Daniel")

for name in relatives:
    print("\t"+ name.title().strip())

new_message9 = f"\n{relatives[1].title()}, let us go for some dinner together."
new_message10 = f" Once this is over, I will take you out for dinner, {relatives[3].lower()}."
new_message13 = "We have SO much to giggle about! Let's eat something together, "+relatives[0] 
new_message12 = f" {relatives[5].title().rstrip()}, we have so much to talk about, let's eat something together so you can laugh at my stories. "
new_message14 = relatives[2]+", we will meet again! We are not complete without your jokes, see you soon."
new_message15 = "Let us celebrate being together again! Thanks for always being there to give me your honest opinion, "+relatives[6]
new_message11 = f" Aunt {relatives[4].strip().title()}, I was not able to say goodbye before you left, let us have a last dinner together."

print("\nSending new set of invitations\n***DISPLAYING PREVIEW***")

print(new_message9)
print(new_message10.lstrip())
print(new_message13)
print(new_message12.strip())
print(new_message14)
print(new_message15)
print(new_message11.lstrip())

#3-7. Shrinking Guest List


