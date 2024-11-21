"""
Online Reputation Management Game

Description:
This project simulates an Online Reputation Management Game where players make decisions in various scenarios that affect the reputation of a fictional company. The game aims to teach the principles of online reputation management through interactive gameplay.

Development Process:
1. Environment Setup: Ensure local Python or online Python is operational and set up a project folder.
2. Understand the CSV Format: Scenarios and scores are managed through CSV files.
   - Scenarios CSV Format: Each row represents a different scenario with columns for the scenario description, options for responses, and the impact on reputation for each option.
   - Scores CSV Format: Used to save player names and their final scores with columns for the player's name and score.
3. Implement CSV Reading and Writing: Use Python's `csv` module to read scenarios from a CSV file and to write final scores to another CSV file.
4. Game Logic Development: Develop the game's core logic, including presenting scenarios to the player, processing player choices, and updating the reputation score accordingly.
5. Create User Interface: Implement a simple command-line interface for the game, allowing players to read scenarios, make choices, and view their reputation score.
6. Debugging and Testing: Test the game thoroughly to ensure all functionalities work as expected and debug any issues.
7. Documentation: Comment the code and create a README file explaining how to set up and play the game.

CSV File Usage:
- Scenarios CSV: The file should have the following columns:
  1. Description: A text description of the scenario.
  2. Options: The choices available to the player, formatted as 'A: Option A. B: Option B. C: Option C.'
  3. Impact: The impact on reputation for each choice, formatted as 'A: ImpactA, B: ImpactB, C: ImpactC'.
  Example row: "A customer posts a negative review online.","A: Ignore the comment. B: Respond politely and offer help. C: Publicly refute the comment.","A: -5, B: +10, C: -10"

- Scores CSV: This file records the players' names and their final scores, with two columns:
  1. PlayerName: The name of the player.
  2. Score: The final reputation score of the player.

How to Run the Game:
1. Prepare the CSV files with scenarios and ensure they are placed in the correct path.
2. Execute the script to start the game. Follow the on-screen prompts to interact with the game.
3. Upon completion, the game will display your final reputation score and save it to the scores CSV file.

This project blends programming skills with marketing concepts, providing a practical tool for understanding the importance of online reputation management.
"""

import csv

def load_csv_as_tuples(file_name):
    """
    Loads data from a CSV file, given the updated format, and converts each row into a tuple.

    This function adapts to the new CSV format where each scenario, its options, and impacts are in separate columns:
    'Question', 'OptionsA', 'OptionsB', 'OptionsC', 'ImpactA', 'ImpactB', 'ImpactC'. It reads the file, skips the header, and for each row, creates a tuple that includes the scenario description, options, and impacts, aligning with the structure of the updated CSV.

    Parameters:
    - file_name (str): The path to the CSV file. The file should follow the updated format with separate columns for each option and impact.

    Returns:
    - list of tuples: Each tuple represents a row from the CSV file, organized as (Question, OptionsA, OptionsB, OptionsC, ImpactA, ImpactB, ImpactC).

    Example usage:
    >>> file_name = 'updated_csv_format.csv'  # Replace with the actual file path
    >>> scenarios = load_csv_as_tuples(file_name)
    >>> for scenario in scenarios:
    ...     print(scenario)
    ('A customer posts a negative review online', 'A: Ignore the comment', 'B: Respond politely and offer help', 'C: Publicly refute the comment', 'A: -5', 'B: +10', 'C: -10')

    The CSV file must include a header row as described, and this function assumes that the header is present and correctly formatted.
    """
    scenarios = []  # This will hold the tuples
    with open(file_name, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # Skip the header row
        for row in csv_reader:
            # Each row is already structured to match the tuple format directly
            scenario_tuple = tuple(row)
            scenarios.append(scenario_tuple)
    return scenarios


#file_name = 'scenarios_batch.csv'
#scenarios = load_csv_as_tuples(file_name)
#for scenario in scenarios:
#    print(scenario)


def score_to_percentage(score, original_min=-245, original_max=530, new_min=-100, new_max=100):
    """
    Converts a given score from the original range to a percentage scale.

    Parameters:
    - score (int or float): The score to convert.
    - original_min (int or float): The minimum value of the original range. Default is -245.
    - original_max (int or float): The maximum value of the original range. Default is 530.
    - new_min (int or float): The minimum value of the new range. Default is -100 (representing -100%).
    - new_max (int or float): The maximum value of the new range. Default is 100 (representing 100%).

    Returns:
    - float: The converted score as a percentage.
    """
    # Ensure the division does not result in a division by zero error
    if original_max == original_min:
        raise ValueError("Original max and min cannot be the same.")
    
    # Convert the score to the new range
    new_value = ((score - original_min) / (original_max - original_min)) * (new_max - new_min) + new_min
    return new_value

# Example usage
#print(score_to_percentage(530))  # Expected output: 100
#print(score_to_percentage(-245))  # Expected output: -100
#print(score_to_percentage(0))  # Output will be within the range -100 to 100, based on the linear transformation