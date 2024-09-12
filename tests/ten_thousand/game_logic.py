import random
from collections import Counter

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score of a given dice roll.

        Parameters:
        dice_roll (tuple): A tuple of integers representing the dice roll.

        Returns:
        int: The score calculated based on the game's scoring rules.
        """

        score = 0  # Initialize the score to 0.
        count = Counter(dice_roll)  # Create a Counter object to count the frequency of each die value.

        # Check for a Straight (1-6)
        if len(count) == 6:
            return 1500  # Return a score of 1500 if all dice values are unique, indicating a straight.

        # Check for Three Pairs
        if len(count) == 3 and all(value == 2 for value in count.values()):
            return 1500  # Return a score of 1500 if there are exactly three pairs.

        # Iterate through each unique number and its frequency in the roll
        for num, freq in count.items():
            if freq >= 3:
                # Scoring for three or more of a kind
                if num == 1:
                    score += 1000 * (freq - 2)  # Score 1000 points for each 1 beyond the first two.
                else:
                    score += num * 100 * (freq - 2)  # Score 100 points per die value for each die beyond the first two.

            # Scoring for single 1's and 5's (less than three of a kind)
            if num == 1 and freq < 3:
                score += freq * 100  # Score 100 points for each 1.
            elif num == 5 and freq < 3:
                score += freq * 50  # Score 50 points for each 5.

        return score  # Return the total calculated score.

    @staticmethod
    def roll_dice(number_of_dice):
        """
        Roll dice and return a tuple of random integers between 1 and 6.

        Parameters:
        number_of_dice (int): The number of dice to roll.

        Returns:
        tuple: A tuple containing the result of the dice roll.
        """

        # Validate the number of dice is between 1 and 6
        if not 1 <= number_of_dice <= 6:
            raise ValueError("Number of dice must be between 1 and 6")

        # Generate and return a tuple of random integers between 1 and 6
        return tuple(random.randint(1, 6) for _ in range(number_of_dice))

    @staticmethod
    def validate_keepers(current_roll, dice_to_keep):
        # Validate if the dice to keep are part of the current roll
        count_roll = Counter(current_roll)
        count_keep = Counter(dice_to_keep)
        return all(count_keep[dice] <= count_roll[dice] for dice in count_keep)
    
    @staticmethod
    def get_scorers(dice_roll):
        
        if not dice_roll:
            return tuple()

        count = Counter(dice_roll)

        if len(count) == 6:
            return dice_roll 

        
        if len(count) == 3 and all(value == 2 for value in count.values()):
            return dice_roll  

        scoring_dice = []

        for num, freq in count.items():
            if freq >= 3:
                scoring_dice.extend([num] * freq)  
            elif num == 1 and freq < 3:
                scoring_dice.extend([1] * freq) 
            elif num == 5 and freq < 3:
                scoring_dice.extend([5] * freq) 

        return tuple(scoring_dice)