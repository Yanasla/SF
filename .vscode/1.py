guessed = False
attempts = 0
left = 0
right = 1001
 
while not guessed:
    number = (left + right) // 2
    print("I think is", number)
    answ = input(": ")
    if not answ in ("<", ">", "="):
        print("Wrong input!")
        continue
    if answ == "<":
        right = number
    elif answ == ">":
        left = number
    else:
        guessed = True
    attempts += 1
 
print("Guessed by", attempts, "attempts.")
