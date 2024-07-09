from capitals import states
import random

def randomize_states(state_list):
    random.shuffle(state_list)
    return state_list

def quiz_user_on_capitals(state_list):
    correct_answers = 0
    incorrect_answers = 0
    for state in state_list:
        answer = input(f"What is the capital of {state['name']}").strip()
        if answer.lower() == state['capital'].lower():
            print("Correct")
            correct_answers += 1
            print(f"You have {correct_answers} correct answers & {incorrect_answers} incorrect answers")
        else:
            print(f"Wrong. The capital of {state['name'] is state['capital']}.")
            incorrect_answers += 1
            print(f"You have {correct_answers} correct answers & {incorrect_answers} incorrect answers")
    print(f"\nYou got {correct_answers} out of {len(state_list)} correct!")
    




def play_game():
    while True:
        randomized_states = randomize_states(states)
        quiz_user_on_capitals(randomized_states)

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break


play_game()