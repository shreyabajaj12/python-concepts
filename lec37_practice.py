def game():
    return 1

score = game()
with open("highscore.txt") as f:
    highScore = (f.read())

    if highScore=='':
        with open("highscore.txt","w")as f:
            f.write(str(score))

    elif int(highScore)<score :
        with open("highscore.txt","w") as f:
            f.write(str(score))
