first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)


#Book notes:
#To insert a variable’s value into a string, place the letter f immediately before the opening quotation mark in full_name. Put braces around
#the name or names of any variable you want to use inside the string. Python will replace each variable with its value when the string is displayed.
#
#These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable in braces with its value

print(f"Hello, {full_name.title()}!")

#You can also use f-strings to compose a message, and then assign the entire message to a variable

message = f"Hello, {full_name.title()}!"
print(message)

#NOTE:
#F-strings were first introduced in Python 3.6. If you’re using Python 3.5 or earlier, you’ll need to use the format() method rather than this f syntax.
#To use format(), list the variables you want to use in the string inside the parentheses following format. Each variable is referred to by a set of braces;
#the braces will be filled by the values listed in parentheses in the order provided:
#
#full_name = "{} {}".format(first_name, last_name)
