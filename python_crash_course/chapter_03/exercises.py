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

#Exercise 3-9
print("\n\nPrinting the number of guests for the dinner\n")
print(len(relatives))


#3-5. Changing Guest List

print(f"\nAunt {relatives[2].title().lstrip()} cannot make it, so we will need to change the guest list.\nPrinting new set of invitations (some have not changed).\n***NEW INVITATIONS***")

relatives[2] = " josefina "
new_message11 = f" Aunt {relatives[2].strip().title()}, I was not able to say goodbye before you left, let us have a last dinner together."

print(message9)
print(message10.lstrip())
print(new_message11.lstrip())
print(message12.strip())

#Exercise 3-9
print("\n\nPrinting the number of guests for the dinner\n")
print(len(relatives))

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

#Exercise 3-9
print("\n\nPrinting the number of guests for the dinner\n")
print(len(relatives))

#3-7. Shrinking Guest List

announcement_message2 = """

***With much regret we have been informed about the table arrangement not happening. We will be only able to invite two people***

Printing current guest list:
"""
print(announcement_message2.upper())

for name in relatives:
    print("\t"+name.title().strip())

print("""
Removing extra guests from the list
""")

list_max_position = 6
counter = 0

for counter in range (0,5):
  removed_relative = relatives.pop()
  print("With utmost regret I must cancel your invitation to our dinner, "+removed_relative.title().strip())

for names in relatives:
    print("You are still invited to the dinner, "+names.title().strip())

print("Displaying remaining guests:")

for name in relatives:
    print("\t"+name.title().strip())

print("Removing remaining guests")

relatives.remove("Carolina")
relatives.remove("dad")

print("\nDisplaying remaining guests - list should be empty")
print(relatives)

#Exercise 3-9
print("\n\nPrinting the number of guests for the dinner\n")
print(len(relatives))

#3-8. Seeing the World (list indexes are in lowercase - uppercase can be more complex)

destinations = ["mexico", "chile", "sweden", "belgium", "denmark"]
print("\n\nPrinting current list without modifications\n")
print(destinations)

print("\nAltering the order of the list using sorted function\n")
sorted_list = sorted(destinations)
print(sorted_list)

#Syntax for sorted function can be tricky:
#- You cannot simply print it. Instead, create a variable, tag the result of the function applied to the list with the variable, and print the variable
#- THIS cannot be done **print(destinations.sort())** - prints "none" - same applies for the reverse method (see below how the change is performed and the original list printed)
#- Reverse order also requires a different syntax (see next use of the function)

print("\nPrinting list to confirm it has not been affected\n")
print(destinations)

print("\nAltering the order of the list using sorted function with reverse argument\n")
#Watch out for this syntax - not described in the book
sorted_list2 = sorted(destinations, reverse=True)
print(sorted_list2)

print("\nPrinting list to confirm it has not been affected\n")
print(destinations)

print("\nAltering the order of the list using reverse method\n")
destinations.reverse()
print(destinations)

print("\nApplying reverse method again to show restore the original order\n")
destinations.reverse()
print(destinations)

print("\nAltering the order of the list using sort method\n")
destinations.sort()
print(destinations)

print("\nAltering the order of the list using sort method with reverse argument\n")
destinations.sort()
print(destinations)

#3-9. Dinner Guests (handled in exercises 3-4 through 3-7)

#3-10. Every Function

print("\n\nCreating empty list")
cities = []
print(cities)

print("Adding one city with insert method")
cities.insert(0, "prague")
print(cities)

print("Adding another city at the end with append method")
cities.append("turku")
print(cities)

print("Adding more cities with append method")
cities.append("madrid")
cities.append("paris")
cities.append("barcelona")
cities.append("brno")
cities.append("helsinki")

print(cities)
print("Counting current list lenght")
print(f"The number of elements in the list is {len(cities)}")

print("Removing the last element of the list with pop method")
cities.pop()
print(cities)

print("Removing Barcelona with remove method")
cities.remove("barcelona")
print(cities)
print(f"The number of remaining elements in the list is {len(cities)}")

print("\nDisplaying elements in alternate order without modifying the original list")
cities_scrambled = sorted(cities)
print(cities_scrambled)
print("\nPrinting original list")
print(cities)

print("\nNow printing in reverse order without affecting the list")
cities_scrambled2 = sorted(cities, reverse=True)
print(cities_scrambled2)
print("\nPrinting original list")
print(cities)

print("\nRearranging the list using sort method - this changes the list permanently")
cities.sort()
print(cities)

print("Rearranging the list usign sort method with reverse argument - the list has changed permanently again")
cities.sort(reverse=True)
print(cities)

#3-11. Intentional Error - I have done this endless amount of times (actually a lot of them, it was a loop)
