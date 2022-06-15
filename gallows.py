

def hangman_stages(attempts):
    """
    Displays various stages of the hangman gallows according
    to number of attempts left
    """
    stages = [  # final stage: head, torso, both arms and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
            # head , torso, both arms and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                """,
            #  head, torso and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                """,
            # head, torso and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                """,
            # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
            # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
            # empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """,
    ]
    return stages[attempts]
