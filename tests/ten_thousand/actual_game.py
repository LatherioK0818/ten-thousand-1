# GPT assisted

from game_logic import GameLogic


class Game:
    TARGET_SCORE = 10000

    def __init__(self):
        self.total_score = 0
        self.current_round = 1
        self.game_logic = GameLogic()

    def welcome_message(self):
        print("Welcome! Would you like to play a game? (y/n, q to quit)")

    def play_round(self):
        print(f"Round {self.current_round}:")
        round_score = 0
        remaining_dice = 6

        while remaining_dice > 0:
            roll = self.game_logic.roll_dice(remaining_dice)
            print(f"Dice roll: {roll}")

            if self.game_logic.calculate_score(roll) == 0:
                print("No scorable dice. Game over.")
                return 0

            while True:
                try:
                    user_input = input("Enter the dice to keep (separated by spaces), or 'q' to quit: ")
                    if user_input.lower() == 'q':
                        return None
                    dice_to_keep = tuple(map(int, user_input.split()))
                    if not self.game_logic.validate_dice_to_keep(roll, dice_to_keep):
                        raise ValueError

                    kept_score = self.game_logic.calculate_score(dice_to_keep)
                    if kept_score == 0:
                        raise ValueError("Selected dice are not scoring. Try again.")

                    round_score += kept_score
                    break
                except ValueError as e:
                    print(e if str(e) else "Invalid dice selection. Try again.")

            remaining_dice -= len(dice_to_keep)

            if remaining_dice == 0:
                remaining_dice = 6

            print(f"Current score: {round_score}")

            decision = input("Do you want to bank your points or roll again? (bank/roll), or 'q' to quit: ").lower()
            if decision == "bank":
                self.total_score += round_score
                print(f"Points banked. Total score: {self.total_score}")
                if self.total_score >= self.TARGET_SCORE:
                    print(f"You've reached {self.total_score} points and won the game!")
                    return self.total_score
                break
            elif decision == 'q':
                return None

        self.current_round += 1
        return self.total_score

    def play_game(self):
        self.welcome_message()
        user_decision = input("Your choice: ").lower()

        if user_decision == "y":
            while True:
                round_result = self.play_round()
                if round_result is None or round_result >= self.TARGET_SCORE:
                    break
        else:
            print("Thanks for playing! Goodbye!")

        print(f"Game over! Your final score is: {self.total_score}")


def main():
    game = Game()
    game.play_game()


if __name__ == "__main__":
    main()
