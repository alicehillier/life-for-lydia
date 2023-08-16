from chapter1 import *
from chapter2 import *

def story_selector():
    """
    Asks the user to select a story. Selecting either 1 or 2 (as per the instructions) will trigger the confirm_story
    function.
    """
    chapters = {
        1: "Chapter One: The Morning After",
        2: "Chapter Two: The Interview",
        3: chapter1,
        4: chapter2
    }
    make_decision(chapters)

story_selector()
