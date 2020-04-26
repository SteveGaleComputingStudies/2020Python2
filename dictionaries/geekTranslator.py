
#Geek translator
# Using dictionaries.
geek = {"404":" page not found",
"401": "unauthorised",
"400": "bad request",
"403": "forbidden.",
"418":"im a teapot"}


choice = None
while choice != 0:
    print(
'''
Geek translator
0 – Quit
1 – Look up a geek term
2 – Add a geek term
3 – Redefine a geek term
4 – Delete a geek term
'''
)
    choice = input("Choice: ")
    print()
#exit
    if choice == "0":
        print("Good-bye")
        break                                                       #exit program
#get a definition
    elif choice == "1":                                             #select / display term
        term = input("What term do you want me to translate?")
        if term in geek:                                            #does the term exist?
            definition = geek[term]                                 #get the definition
            print("\n",term,"means", definition)
        else:                                                       #term doesnt exist
            print("\nSorry, I don’t know",term)
#add a key-value pair
    elif choice == "2":                                             # insert term
        term = input("What term do you want to add?")
        if term not in geek:                                        # only add if it doesnt exist
            definition = input("\nWhat’s the definition?")
            geek[term] = definition                                 # add the key value pair
            print("\n", term,"has been added")
        else:                                                       # term exists 
            print("\nThat term already exists, try redefining it")
#re-define an existing term
    elif choice == "3":                                             #update term
        term = input("What term do you want to redefine?")
        if term in geek:                                            # does the term exist?
            definition = input("what’s the new definition? ")
            geek[term]= definition                                  # update the value
            print("Term has been redefined")
        else:
            print("\nThat term doesn’t exist, try adding it")
#delete a pair
    elif choice =="4":                                              #delete term
        term = input("what term do you want to delete?")
        if term in geek:                                            # does the term exist?
            del geek[term]                                          #delete the term
            print("\nOkay delete", term)
        else:
            print("\nCant do that", term, "doesn’t exist in the dictionary")
# SG added choice = 5 to list all terms
    elif choice == "5":                                             #select / display all terms
        for term in geek:                                           
            print("\n",term,"means", geek[term])
# some unknown choice
    else:
        print("\nSorry, but",choice, "isn’t a valid choice")
        input("\nPress the 0 key to exit")