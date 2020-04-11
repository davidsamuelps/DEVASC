first_name = "Joe"
last_name = "Smith"
full_name = f"{first_name} {last_name}"

#First message with first name only:
message = f"Hello {first_name}, would you like to learn Python today?"
print(message)

#Second message with full name in a variable:
message2 = f"Hello {full_name}, would you like to learn Python today?"
print(message2)

#Third message with first name and last name as separate variables:
message3 = f"Hello Mr. {first_name} {last_name}, would you like to learn Python today?"
print(message3)

#Fourth message stripping space in the right:
full_name2 = "Joe Smith "
message4 = f"Hello Mr. {full_name2.rstrip()}, would you like to learn Python today?"
print(message4)

#Fifth message stripping space in the left:
full_name3 = " Joe Smith"
message5 = f"Hello Mr. {full_name3.lstrip()}, would you like to learn Python today?"
print(message5)

#Sixt message stripping spaces from both sides:
full_name4 = " Joe Smith "
message6 = f"Hello Mr. {full_name4.strip()}, would you like to learn Python today?"
print(message6)

#Sevent message with names in separate variables and stripping spaces from them and the message
first_name2 = " Joe"
last_name2 = "Smith "
message7 = f" Hello Mr. {first_name.lstrip()} {last_name.rstrip()}, would you like to learn Python today? "
print(message6.strip())

#Eigth message with first name in lowercase and first name in uppercase
message8 = f" Hello Mr. {first_name.lower()} {last_name.upper()}, would you like to learn Python today? "
print(message8.strip())

#Ninth message with title case
first_name3 = "joe "
last_name3 = " smith"
first_name4 = first_name3.rstrip()
last_name4 = last_name3.lstrip()
message9 = f" Hello Mr. {first_name4.title()} {last_name4.title()}, would you like to learn Python today? "
print(message9.strip())

#Tenth message with quotation marks:
author = "Maria Sharapova"
quote = '"I have had lots of luck in my career but there has also been a lot of hard work."'
message10 = f"\nInspiring quote:\n\t{quote}\n\t{author}"
print(message10)
