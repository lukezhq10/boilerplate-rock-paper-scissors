import random

moves = {}


def player(prev_play, opponent_history=[]):
  # assign Rock as default for first move
  if not prev_play:
    prev_play = 'R'
  opponent_history.append(prev_play)

  # n represents the number of moves we keep track of as a pattern
  n = 5

  guess = 'R'
  # take the most recent n moves from opponent_history and initialize as a pattern
  if len(opponent_history) > n:
    pattern = "".join(opponent_history[-n:])

    # if pattern is already in the moves dict, increase its count by 1, else add it to the dict with a count of 1
    if "".join(opponent_history[-(n + 1):]) in moves.keys():
      moves["".join(opponent_history[-(n + 1):])] += 1
    else:
      moves["".join(opponent_history[-(n + 1):])] = 1

    possible = [pattern + 'R', pattern + 'P', pattern + 'S']

    # if the move is not possible based on pattern, set moves[i] = 0
    for i in possible:
      if not i in moves.keys():
        moves[i] = 0

    # predict by getting the move with the highest count
    predict = max(possible, key=lambda key: moves[key])

    if predict[-1] == 'P':
      guess = 'S'
    if predict[-1] == 'R':
      guess = 'P'
    if predict[-1] == 'S':
      guess = 'R'

  return guess
