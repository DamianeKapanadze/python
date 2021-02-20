max = 1000
min = 0
print("Whenever you want to quit, press 'q' !")
print("Think of a natural number between ", max, " and ", min)
guesses =0
while True:
    guesses += 1
    ans = int((max+min)/2)
    print("Is your number ", ans, " ?")
    s = input()
    if s == 'q':
        break
    if s == "Yes" or s == "yes":
        if guesses == 1:
            print("I guessed in ", guesses, "guess")
        else:
            print("I guessed in ", guesses, "guesses")
        break
    elif s == "No" or s == "no":
        print("is it more or less ?")
        s = input()
        if s == "more" or s == "More" or s == '>':
            min = ans
        elif s == "less" or s == "Less" or s == '<':
            max = ans