name = "ada lovelace"

#Changing case to title
print(name.title())

#Changing case to uppercase
print(name.upper())

#Changing to case to lowercase
print(name.lower())

#Book notes:
#In this example, the variable name refers to the lowercase string "ada lovelace". The method title() appears after the variable in the print() call.
#A method is an action that Python can perform on a piece of data. The dot (.) after name in name.title() tells Python to make the title() method act
#on the variable name. Every method is followed by a set of parentheses, because methods often need additional information to do their work. That
#information is provided inside the parentheses. The title() function doesn’t need any additional information, so its parentheses are empty.
#
#The title() method changes each word to title case, where each word begins with a capital letter. This is useful because you’ll often want to think
#of a name as a piece of information. For example, you might want your program to recognize the input values Ada, ADA, and ada as the same name, and
#display all of them as Ada.
