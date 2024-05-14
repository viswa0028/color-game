from termcolor import colored
import random
i = 0
k = True
def add_highscore(score):
    try:
        with open("highscore.txt", "r") as f:
            highscore = int(f.read())
    except (FileNotFoundError, ValueError):
        highscore = 0

    if score > highscore:
        with open("highscore.txt", "w") as f:
            f.write(str(score))
        print(f"New high score: {score}")
    else:
        print(f"High score: {highscore}")
while k == True:
    colors = ["blue", "green", "grey", "red", "magenta", "yellow", "cyan", "white"]
    random_color = random.choice(colors)
    random_word = random.choice(colors)
    print(colored(random_word, random_color))
    a = str(input("what is the color:-" + " "))
    if random_color == a:
        i = i+1
        k = True
    else:
        print("game over")
        print(f"your score is {i}".format(i))
        k = False
add_highscore(i)
