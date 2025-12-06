
# score = input("Enter a number:")

# def game(s):
#     f = open("Hi-score.txt", "a")
#     str = f" high score is {s}"

#     if s in f:
#         f.write(f" High score is again {s}")
#     elif s > f:
#         f.write(str)
 


#     f.write(str)
    
    
    

#     f.close()
# game(score)



# solution:
import random
def game():
    print("Welcome to the game!")
    score =random.randint(1, 100)
    with open("Hi-score.txt", "r") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score is: {score}")

 
    if(score > hiscore):
            with open("Hi-score.txt", "w") as f:
                f.write(str(score))


    return score

game()