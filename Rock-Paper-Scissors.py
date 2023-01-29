print("Rock-Paper-Scissors Game\n")

while True:
    print("Enter choice \n1 for Rock \n2 for Paper \n3 for Scissors \n")
    
    choice = int(input("Your turn: "))
 
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))
         
    if choice == 1:
        choice_name = 'rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissors'
        
    print("Your choice is: " + choice_name)
    print("Now its computer's turn.......")
 
    comp_choice = random.randint(1,3)
     
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
    
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'
        
    print("Computer choice is: " + comp_choice_name)
 
    print(choice_name + " V/s " + comp_choice_name)
 
    result = None
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        result = "paper"
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        result = "rock"
    else:
        result = "scissors"
 
    if result == choice_name:
        print("<== User Wins ==>")
    else:
        print("<== Computer Wins ==>")
        
    print("Do you want to play again? (Y/N)")
    ans = input()
 
    if ans == 'n' or ans == 'N':
        break

print("\nThanks for playing")
