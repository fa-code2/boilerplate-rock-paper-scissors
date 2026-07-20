# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order={}):
    # Reset history on a fresh matchup (first game element will be empty)
    if not prev_play:
        opponent_history.clear()
        # Do not clear play_order completely to save memory/state across games if needed,
        # but clearing or preserving it minimally helps keep logic clean.

    # Record the opponent's last move if it exists
    if prev_play:
        opponent_history.append(prev_play)

    # Core N-Gram Prediction Strategy
    n = 3  # Lookback depth. Patterns of 3 moves give optimal performance across all 4 bots.
    
    # Standard ideal response dictionary to counter predicted moves
    ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}

    # Default move if we don't have enough history data yet
    prediction = 'P'

    # Track sequence frequencies once we have enough moves
    if len(opponent_history) >= n:
        # Reconstruct the last n-1 moves of the opponent
        last_n_minus_1 = "".join(opponent_history[-(n-1):])
        
        # Look at the actual transition that just occurred and log it
        last_n = "".join(opponent_history[-n:])
        if last_n in play_order:
            play_order[last_n] += 1
        else:
            play_order[last_n] = 1

        # Predict the next move by checking potential combinations ('R', 'P', 'S')
        potential_next_sequences = [last_n_minus_1 + move for move in ['R', 'P', 'S']]
        
        # Find which sequence has appeared most frequently in the past
        best_count = -1
        for seq in potential_next_sequences:
            if seq in play_order and play_order[seq] > best_count:
                best_count = play_order[seq]
                prediction = seq[-1]  # The predicted move is the last char of the sequence

    # Return the counter to the predicted move
    return ideal_response[prediction]

