# First 3 print functions print plain lines of text into the terminal. 
print("Good evening")
print("I am your personal assistant.")
print("What may I call you?")

# The name string calls for an input function. The argument is whatever the user decides to type in for their name.
name = input()

# This print function calls upon the word "Welcome" then whatever the person decided to type in for the name argument,
# and then a period to end the sentence.
print("Welcome" , name + ".")

dogName= input("""Who's a good boy?

""")

print("You are," , dogName + "!")