# Tic-Tac-Toe AI

This project is a solution to the Tic-Tac-Toe problem as part of Harvard's CS50 AI course. It implements an intelligent agent capable of playing Tic-Tac-Toe optimally using the **Minimax algorithm**. The AI ensures that it will either win or tie every game.

## Features

- Fully interactive Tic-Tac-Toe game between a human and an AI.
- AI uses the Minimax algorithm to evaluate optimal moves.
- Handles all game rules, including checking for wins, draws, and invalid moves.
- Supports a clean and intuitive command-line interface for playing the game.

## Getting Started

### Prerequisites
To run this project, you need Python installed on your system. The project is compatible with Python 3.6 and above.

### Running the Project
To start the Tic-Tac-Toe game, run:
```bash
python runner.py
```
Follow the on-screen prompts to make your move. The AI will respond immediately.

## Project Structure

```
tic-tac-toe-ai/
├── tictactoe.py       # Core game logic and AI implementation
├── runner.py          # Game interface and execution
├── README.md          # Project documentation
```

## How It Works

### Minimax Algorithm
The AI uses the Minimax algorithm to evaluate the game state and determine the optimal move. This ensures:
- **Maximization:** The AI plays to maximize its chances of winning.
- **Minimization:** The AI assumes the opponent will play optimally to minimize the AI's score.

The algorithm evaluates all possible moves recursively and assigns scores based on terminal states:
- +1 for a win
- -1 for a loss
- 0 for a tie

### Game Rules
1. Players take turns placing their marker (X or O) on the grid.
2. A player wins if they align 3 of their markers in a row, column, or diagonal.
3. The game ends in a draw if the grid is full without a winner.

## Contributing
Contributions are welcome! If you'd like to improve the project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.



