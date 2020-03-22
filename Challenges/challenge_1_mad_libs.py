"""
Ask the user to supply the words to the story in {}'s.
Tell them the story with the words they gave inserted in.
"""

colour = input("Give me a colour: ")
colour2 = input("Give me another colour: ")
adjective = input("Give me an adjective: ")

# Write a story with some words missing
story = f"""
Roses are {colour}
Violets are {colour2}
Sugar is {adjective}
And so are you
"""

# Ask the user to provide the missing words


# Display the final story
print(story)
