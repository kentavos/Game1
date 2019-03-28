# Choose your own adventure game

print("You're mindlessly surfing twitter when your phone vibrates with a new msg indicator. Somehow the sender is blocked. 'Wake up, Neo...'")
print("That's a new trick you think as you chuckle at the reference. 'Who is this?' you type back. 'A friend in need of a favor'")
print("No one comes to mind with enough skill to completely anonimize their phone number. 'Who dis? What's the favor?'' 'You have mail...")
print("Your laptop dings with the sound of a new email. Again the address is anonymous. There is a file attached. The message says run me")
answer1 = input ("Reply with 1 to run the program.  Reply with 2 to delete it. ")

answer1 = int(answer1)

if answer1 == 1:
    print ("Your curiousity gets the better of you and you run the program. Your cooling fan comes on as the program decompresses. It's huge.")

elif answer1 == 2:
    print ("You're scared and hit delete. You reply to the text again and get no response. You go back to mindlessly surfing social networks. THE END")

else:
    print ("Bad input")
    quit()
