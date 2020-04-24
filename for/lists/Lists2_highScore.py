#High scores program
#Looking at nested sequences
#scores = []
scores = [(55,"Tim")]
choice = None
while choice != 0:
    print(
      """
High Scores vers2.0
0 - Quit
1 - List Scores
2 - Add a score

 """
)
#note you will have an infinite loop at this stage
#make sure choice is indented 4 spaces
    choice = input("Choice (choose 0,1 or 2: ")
    print()

#exit
    if choice == "0":
        print("Good-bye") #keep the following line at the end

        input("\n\Press enter key to exit")#comment out later
        break
# display high-score table
# between final input(press any key to exit) and if statement
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)


#add a score
    elif choice == "2":
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?:"))
        entry = (score, name)
        scores.append(entry)        #add entry to the scores array
        scores.sort(reverse = True) # higest score is first
        scores = scores[:6]         # keel the top 6 scores

# number outside range chosen
    else:
        print("Sorry, invalid choice")

# After the user enters 0 to exit, the program waits for the user to hit enter. (Otherwise it would keep on going through the loop.) Note-input is not indented, and not inside the while loop.
#input("\n\nPress enter key to exit")