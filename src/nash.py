# Nash Equilibrium Finder

def best_response_player1(matrix):
    """Find the best responses for Player 1."""
    best_responses = []

    for col in range(len(matrix[0])):
        max_payoff = max(row[col][0] for row in matrix)
        best_responses.extend(
            [(row_idx, col) for row_idx, row in enumerate(matrix) if row[col][0] == max_payoff]
        )
    return best_responses


def best_response_player2(matrix):
    """Find the best responses for Player 2."""
    best_responses = []

    for row_idx, row in enumerate(matrix):
        max_payoff = max(cell[1] for cell in row)
        best_responses.extend(
            [(row_idx, col_idx) for col_idx, cell in enumerate(row) if cell[1] == max_payoff]
        )
    return best_responses


def strict_equilibrium(matrix):
    """Check for Nash equilibria in pure strategies."""
    best_responses_1 = best_response_player1(matrix)
    best_responses_2 = best_response_player2(matrix)
    
    equilibria = [
        (row, col)
        for row, col in best_responses_1
        if (row, col) in best_responses_2
    ]

    if equilibria:
        for row, col in equilibria:
            print(f"The combination of strategy {row + 1} (Player 1) and strategy {col + 1} (Player 2) "
                  f"is a pure Nash equilibrium with payoffs {matrix[row][col]}.")

    else:
        print("There is no Nash equilibrium in pure strategies.")

# Edit the Payoff Matrix
matrix = [[(3,3), (1,4)],
          [(4,1), (2,2)]]

# Find the Nash Equilibrium
strict_equilibrium(matrix)
