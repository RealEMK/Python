playerName = input("Please enter your name.\n\n")

print("Welcome," , playerName + ".")

answer = input("Would you like to save your game? (Yes/No\n\n")
if answer == "Yes":
    print("Game saved.")
elif answer == "No":
    print("Cancelled.")

else:
    print(answer)