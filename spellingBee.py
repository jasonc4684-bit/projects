WordBank={
"ALTER":5,"ALERT":5,
"LATER":5,
"LATE":4,"REAL":4,
"TEAR":4,"TALE":4,
"ART":3,"EAR":3,
"ARE":3,"TEA":3,
"LET":3,"ATE":3,
"RAT":3}

def main():
    print(" Welcome to spelling bee challenge!")
    print(" Letters are E, R, T, L, A")

    while len(WordBank)>0:
        print(f"Words remaining: {len(WordBank)}")
        guess=input("Enter your guess: ").upper()
        if guess in WordBank:
            WordBank.pop(guess)
            print(f"Correct! {len(WordBank)} words left.")
main()        
