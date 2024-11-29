# Bulls and Cows Game

## Overview

The **Bulls and Cows** game is a classic number guessing game. The goal is to guess a secret 4-digit number, where each digit is unique. After each guess, the player is given feedback in the form of "bulls" and "cows":
- **Bulls**: The number of digits that are correct and in the correct position.
- **Cows**: The number of digits that are correct but in the wrong position.

This project implements the game in Python, with additional functionality for calculating **entropy** to help the player make more informed guesses.

## File Structure

### **1. `main.py`**
- **Purpose**: This is the entry point of the game. It initializes the game with a secret number and runs the game loop.
- **Key Components**:
  - Starts the game with a pre-defined secret number (`1708`).
  - Prompts the player if they want to play again after the game ends.

### **2. `game.py`**
- **Purpose**: This file contains the core logic of the game, managing the gameplay, including the secret number, guesses, bulls, cows, and entropy calculations.
- **Key Classes**:
  - **`BullsAndCowsGame`**: Manages the overall game logic. Handles the game loop, processes guesses, and calculates bulls and cows for each guess.
- **Key Methods**:
  - **`__init__(secret)`**: Initializes the game with a secret number and calculates all possible 4-digit combinations.
  - **`play()`**: Runs the game loop, where the user guesses the secret number, receives feedback, and entropy is recalculated after each guess.

### **3. `utilities.py`**
- **Purpose**: Contains utility classes to handle entropy calculations and determine bulls and cows for a guess.
- **Key Classes**:
  - **`EntropyMI`**: Provides functionality for calculating the entropy of the remaining possible secret numbers.
  - **`SearchLogic`**: Handles the comparison of a guess to the secret and returns the number of bulls and cows.
- **Key Methods**:
  - **`get_entropy(values)`**: Calculates entropy based on the remaining possible secrets, helping the player make more informed guesses.
  - **`check_bac(secret, guess)`**: Compares a guess to the secret and returns the number of bulls and cows.

## How to Play

1. Run the program by executing `main.py`.
2. The game will ask for your guess in the form of a 4-digit number (e.g., `1708`).
3. After each guess, you'll receive feedback in the form of bulls and cows:
   - **Bulls**: Number of digits that are correct and in the right position.
   - **Cows**: Number of digits that are correct but in the wrong position.
4. The program will also calculate the **entropy** of the remaining possible secrets after each guess to help optimize your next guess.
5. The game continues until you guess the correct number (i.e., 4 bulls).
6. After winning, the game will ask if you'd like to play again.


## Entropy Calculation

The entropy calculation is used to measure the uncertainty of the remaining possible secret numbers. This value is computed after each guess to help the player make more informed decisions on subsequent guesses. The goal is to minimize the entropy, which will lead to fewer remaining possibilities and a faster solution.

## Requirements

- Python 3.x
- No external dependencies

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Clone or download the repository.
3. Navigate to the directory where the files are located.
4. Run the game by executing:
   ```bash
   python main.py

