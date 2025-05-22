import game_logic

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown","testtesttest"]

def main():
    """
    play the game and at the end ask if want to continue
    """
    while True:
        game_logic.play_game()
        get_user_answer = input("Do you want to play again? y/n: ").lower()
        if get_user_answer == "n":
            break
        else:
            print("Please type y or n")


if __name__ == "__main__":
     main()