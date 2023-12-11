# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

# our team always plays 10 matches in the championship
# Given a list of game scores
# Want to look at each game
# Determine who won the game
# If team x wins add 3 points to season total
# If team x ties with team y add 1 point to season total
# Once wee checked every game, return season total


def solution(games_scores):
    season_total = 0
    for scores in games_scores:
        x,y = scores.split(':')
        if x > y:
            season_total += 3
        elif x == y:
            season_total +=1
    return season_total   
