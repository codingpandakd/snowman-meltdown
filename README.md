# Snowman Meltdown

Snowman Meltdown is a fun and interactive word guessing game where you try to save a snowman from melting by guessing the letters of a secret word.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and run Snowman Meltdown, you'll need to have Python installed on your computer. You can download Python from the [official Python website](https://www.python.org/downloads/).

Once you have Python installed, you can clone the Snowman Meltdown repository from GitHub:
git clone https://github.com/codingpandakd/snowman-meltdown.git

Then, navigate to the Snowman Meltdown directory:cd snowman-meltdown

## Usage

To start the game, run the `snowman.py` file:python snowman.py


## Game Rules

1. The game will select a secret word from a list of words.
2. You'll be presented with a series of underscores, each representing a letter in the secret word.
3. You'll need to guess the letters of the secret word, one at a time.
4. For each incorrect guess, a part of the snowman will melt.
5. If you guess all the letters of the secret word before the snowman melts completely, you win!
6. If the snowman melts completely before you guess the secret word, you lose.

## Code Structure

The Snowman Meltdown game is made up of three Python files:

- `snowman.py`: This is the main file that you run to start the game. It contains the `main()` function, which starts the game and asks if you want to play again when the game ends.

- `game_logic.py`: This file contains the game logic, including the `play_game()` function, which runs the game, and the `get_random_word()` function, which selects a random word from the list of words.

- `ascii_art.py`: This file contains the ASCII art for the snowman, which is displayed at each stage of the game.





