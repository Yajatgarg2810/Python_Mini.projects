import random
def number_guessing():
    guesses=0
    lowest_no=1
    highest_no=100
    is_running=True
    answer=random.randint(lowest_no,highest_no)
    user_guesses = []

    print("Guess the Number")
    print(f"Select a Number {lowest_no} and {highest_no}")

    while is_running:
        guess=input("Enter your guess:")
        print()

        if guess.isdigit():
            guess=int(guess)
            guesses+=1
            user_guesses.append(guess)
            
            if guess<lowest_no or guess>highest_no:
                print("Enter the number in given range ")
                print(f"Range between {lowest_no} and {highest_no}")

            elif guess>answer:
                print("Your Guess is higher")

            elif guess<answer:
                print("Your Guess is Lower")

            else:
                print("CORRECT!")
                print(f"Number of Guesses:{guesses}")

                with open("guesses.txt", 'a') as file:
                    file.write(f"Guesses: {user_guesses}, Total Guesses: {guesses}\nanswer:{answer}\n")  # Writing the number of guesses
                    is_running=False
        else:
            print("Enter Valid Number ")
            print(f"Enter the number between {lowest_no} and {highest_no}")
        
if __name__ == "__main__":
    number_guessing()