# GPT assisted

from game_logic import GameLogic


class Game:
    TARGET_SCORE = 10000

    def __init__(self):
        self.total_score = 0
        self.current_round = 1
        self.game_logic = GameLogic()

    def reset_game(self):
        self.total_score = 0
        self.current_round = 1
    
    def welcome_message(self):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")

    def play_round(self):
        print(f"Round {self.current_round}:")
        round_score = 0
        remaining_dice = 6

        while remaining_dice > 0:
            roll = self.game_logic.roll_dice(remaining_dice)
            print(f"Dice roll: {roll}")

            scoring_dice = self.game_logic.get_scorers(roll)
            if not scoring_dice:
                print("****************************************")
                print("**        Zilch!!! Round over         **")
                print("****************************************")
                return 0

            while True:
                try:
                    user_input = input("Enter dice to keep, or (q)uit: ")
                    if user_input.lower() == 'q':
                        return None
                    dice_to_keep = tuple(map(int, user_input.split()))

                    if not all(die in scoring_dice for die in dice_to_keep):
                        raise ValueError("You have selected non-scoring dice.")

                    if not self.game_logic.validate_keepers(roll, dice_to_keep):
                        raise ValueError("Invalid dice selection. Try again.")

                    kept_score = self.game_logic.calculate_score(dice_to_keep)
                    round_score += kept_score
                    break
                except ValueError as e:
                    print(e)

            remaining_dice -= len(dice_to_keep)

            if remaining_dice == 0:
                remaining_dice = 6

            print(f"You have {round_score} unbanked points and {remaining_dice} dice remaining.")
            
            decision = input("(r)oll again, (b)ank your points or (q)uit: ").lower()
            if decision == "b":
                self.total_score += round_score
                print(f"You banked {round_score} points in round {self.current_round}")
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
        user_decision = input(">  ").lower()

        if user_decision == "y":
            while True:
                round_result = self.play_round()
                if round_result is None or round_result >= self.TARGET_SCORE:
                    break
        

        print(f"Thanks for playing. You earned {self.total_score} points.")


def main():
    game = Game()
    game.play_game()


if __name__ == "__main__":
    main()
