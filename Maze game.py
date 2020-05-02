escape_combo = "SSNWES"
combo = ""
turn_count = 0
turn_limit = 3
out_of_turns = False

while combo != escape_combo and not out_of_turns:

    if turn_count < turn_limit:
        combo = input("You are in the magic maze. Which way do you go? You can go N,S,E,W, with 6 steps:\n")
        turn_count += 1
        print(f"you used {turn_count} move(s)")

    else:
        out_of_turns = True

if out_of_turns:
    print("Too bad, you're out of guesses!")
   
else:
    print("Congratulations, you solved the magic maze!")
