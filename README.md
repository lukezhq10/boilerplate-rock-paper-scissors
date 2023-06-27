# Rock Paper Scissors

This is the boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

# Project Description - lukezhq

We define a player function which plays Rock Paper Scissors using a Markov Chain algorithm. A Markov Chain algorithm is a mathematical model that helps predict the probabilities of future states based on the current state. In the context of this project, we predict the opponent's moves based on their previous choices. Each time a pattern is played, this gets added into a moves dictionary and we increase the count of that pattern by 1. Finally, we make a prediction based on which pattern out of all the possible moves has the highest count. 

One of the opponents (abbey) does the same strategy, predicting using patterns based on the opponent's last 2 moves. We build upon this but instead keep track of the most recent 5 moves.
