print("welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! lets play")
score = 0

answer= input("what colour do law students wear? ")
if answer.lower() == "black and white":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer= input("what is the result of 2+3? ")
if answer.lower() == "5":
    print("correct!")
    score +=1
else:
    print("incorrect!")

answer= input("what is == in python? ")
if answer.lower() == "equal to":
    print("correct!")
    score +=1
else:
    print("incorrect!")


answer= input("what is the name of the planet you're on? ")
if answer.lower() == "earth":
    print("correct!")
    score+=1
else:
    print("incorrect!")


answer= input("what is the name of cos 101 teacher? ")
if answer.lower() == "mr barka":
    print("correct!")
    score+=1
else:
    print("incorrect!")


answer= input("How many colours are there on the Nigerian flag? ")
if answer.lower() == "two":
    print("correct!")
    score+=1
else:
    print("incorrect!")


answer= input("Would you like a macbook? ")
if answer.lower() == "yes":
    print("correct!")
    score +=1
else:
    print("incorrect!")


answer= input("What does SRC stand for? ")
if answer.lower() == "student representative council":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    
    

    
answer= input("Are you enjoying your stay at Bingham? ")
if answer.lower() == "no":
    print("correct!")
    score +=1
else:
    print("incorrect!")


answer= input("what resturant has the best food? ")
if answer.lower() == "munch box":
    print("correct!")
    score +=1
else:
    print("incorrect!")



print("you got " + str(score) + " questions correct")
print("you got " + str((score/10) * 100) + "%")
    
    
    

