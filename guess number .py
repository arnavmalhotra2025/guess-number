import random
import time
number = random.randint(1, 100)

def intro():
    print("May I ask you for your name?")
    
    global name 
    name = input()
    print(name +",we are going to play a game I am thinking of a number beetween 1 and 100")
    if(number%2==0):
        x = 'even'
    else:
        x = 'odd'
    print("\nThis is an {} number".format(x))
    time.sleep(.5)    
    print("go ahed. guess")
    
    
def pick():
    guessesTaken = 0
    
    while guessesTaken < 6:
        time.sleep(.25)
        enter = input("guess:")
        
        try:
            
            guess = int(enter)
            
            if guess <= 100 and guess >= 1:
                guessesTaken = guessesTaken+1
                
                if guessesTaken<6:
                    if guess < number:
                        print("the guess of the number that you have entered is too low")
                    if guess > number:
                        print("the guess of the number you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("try again")
                    if guess== number:
                        break
            if guess>100 or guess<1:
                print("silly goose! that number isn't in the range!")
                time.sleep(.25)
                print("please enter a number between 1 and 100")
                
        except:
            print ("i don't think that whatever you have entered is an number")
    
    if guess == number:
        guessesTaken= str(guessesTaken)
        print('good job, {} you guessed my number in {} guesses'.format(name, guessesTaken))
        
    if guess != number:
        print('nope. the number i was thinking of was'+str(number))
        
playing = "yes"
while playing == "yes" or playing == "y" or playing == "Yes":
    intro()
    pick()
    print("do you want to play again")
    playing = input() 
           