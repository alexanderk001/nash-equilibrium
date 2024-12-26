# 🔍 Nash Equilibrium Finder

This repository contains a Python script and a Jupyter Notebook for calculating the Nash Equilibrium in two-player games based on their payoff matrix. The Nash Equilibrium is a key concept in game theory that describes a stable state where no player can benefit by unilaterally changing their strategy.

## What is a Nash Equilibrium?

In game theory, the **Nash Equilibrium** is a central concept that describes a combination of strategies in which no player can improve their outcome by changing their strategy, provided the other players keep their strategies unchanged. It represents a stable state in which the strategies of all players are optimal given the strategies of the others.

### Example: Payoff Matrix

Consider the following payoff matrix for two players:

| Player 1 / Player 2 | Strategy A | Strategy B |
| ------------------- | ---------- | ---------- |
| **Strategy X**      |   (3, 2)   |   (1, 4)   |
| **Strategy Y**      |   (2, 1)   |   (4, 3)   |

Here:
- The first value in each cell represents Player 1's payoff.
- The second value in each cell represents Player 2's payoff.

**Nash Equilibrium:** In this example, the pair of strategies (Player 1: Strategy Y, Player 2: Strategy B) forms a Nash Equilibrium because neither player can improve their payoff by unilaterally changing their strategy.

## Code Overview

The Python script includes:
- `best_response_player1(matrix)`: Computes the best responses for Player 1.
- `best_response_player2(matrix)`: Computes the best responses for Player 2.
- `strict_equilibrium(matrix)`: Identifies all Nash Equilibria in pure strategies.

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/alexanderk001/nash-equilibrium.git
   ```

2. Modify the `matrix` variable in the script to test different scenarios.

3. Run the script with your own payoff matrix:
   ```bash
   python nash.py
   ```

See the Jupyter Notebook for further explanations

## Example Input

The following is an example payoff matrix defined in the script:
```python
matrix = [
    [(3, 3), (1, 4)],
    [(4, 1), (2, 2)]
]
```

The combination of strategy 2 (Player 1) and strategy 2 (Player 2) is a pure Nash equilibrium with payoffs (2, 2).

This example is a so-called **Prisoner's dilemma**.

## License

This project is licensed under the MIT License.
