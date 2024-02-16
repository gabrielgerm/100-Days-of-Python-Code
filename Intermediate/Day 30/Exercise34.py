# Instructions

# We've got some buggy code, try running the code. The code will crash and give you a KeyError. This is because some of the posts in the facebook_posts don't have any "Likes".

# Objective
# Use what you've learnt about exception handling to prevent the program from crashing.

# Example Input
# [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]
# Using the eval() function we can create a list of dictionaries that looks like this:

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]
# Example Output
# 86