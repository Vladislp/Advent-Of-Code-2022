# Read the encrypted strategy guide from a file
with open('Data.txt') as f:
    guide = [line.strip() for line in f]

# Calculate the total score

def first_step():
    # Read the encrypted strategy guide from a file

    # Calculate the total score
    score = 0
    for line in guide:
        opponent_move = line[0]
        my_move = line[2]
        # OPPONENT
        # A --> ROCK
        # B --> PAPER
        # C --> SCISSOR

        # ME
        # X --> ROCK
        # Y --> PAPER
        # Z --> SCISSOR

        # Calculate the score for the shape
        shape_score = 0
        # ROCK
        if my_move == 'X':
            shape_score = 1
        # PAPER
        if my_move == 'Y':
            shape_score = 2
        # SCIESSOR
        if my_move == 'Z':
            shape_score = 3

        # Calculate the score for the outcome
        outcome_score = 0
        # LOST
        if (opponent_move == 'A' and my_move == 'Z') or (opponent_move == 'B' and my_move == 'X') or (
                opponent_move == 'C' and my_move == 'Y'):
            outcome_score = 0
        # DRAW
        elif (opponent_move == 'A' and my_move == 'X') or (opponent_move == 'B' and my_move == 'Y') or (
                opponent_move == 'C' and my_move == 'Z'):
            outcome_score = 3
        # WIN
        elif (opponent_move == 'A' and my_move == 'Y') or (opponent_move == 'B' and my_move == 'Z') or (
                opponent_move == 'C' and my_move == 'X'):
            outcome_score = 6
        else:
            print(opponent_move + my_move)
        # Add the scores to the total score
        score += (shape_score + outcome_score)

        # Print the result
    return score

def second_step():

    # Calculate the total score
    score = 0
    for line in guide:
        opponent_move = line[0]
        my_move = line[2]
        # OPPONENT
        # A --> ROCK
        # B --> PAPER
        # C --> SCISSOR

        # ME
        # X --> LOSE
        # Y --> DRAW
        # Z --> WIN

        # Calculate the score for the shape
        results_score = 0
        # ROCK
        if my_move == 'X':
            results_score = 0
        # PAPER
        if my_move == 'Y':
            results_score = 3
        # SCIESSOR
        if my_move == 'Z':
            results_score = 6

        # Calculate the score for the outcome
        shape_score = 0
        # ROCK
        if (opponent_move == 'A' and my_move == 'Y') or (opponent_move == 'B' and my_move == 'X') or (
                opponent_move == 'C' and my_move == 'Z'):
            shape_score = 1
        # PAPER
        elif (opponent_move == 'A' and my_move == 'Z') or (opponent_move == 'B' and my_move == 'Y') or (
                opponent_move == 'C' and my_move == 'X'):
            shape_score = 2
        # SCISSORS
        elif (opponent_move == 'A' and my_move == 'X') or (opponent_move == 'B' and my_move == 'Z') or (
                opponent_move == 'C' and my_move == 'Y'):
            shape_score = 3
        else:
            print(opponent_move + my_move)
        # Add the scores to the total score
        score += (shape_score + results_score)

        # Print the result
    return score

# Print the results
part1 = first_step()
print(f'Total score first round: {part1}')

part2 = second_step()
print(f'Total score second round: {part2}')
