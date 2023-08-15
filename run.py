from chapter1 import *
from chapter2 import *

def story_selector():
    """
    Asks the user to select a story. When the player does so, they are able to view general information about the story 
    before confirming their selection. Once confirmed, the relevant story will play out.
    """

    chapters = {
        1: "Chapter One: The Morning After",
        2: "Chapter Two: The Interview"
    }

    print("1. Chapter One: The Morning After.\n2. Chapter Two: The Interview.\n")
    while True:
        story_selected = getpass.getpass(prompt = "Enter 1 or 2 to start reading the selected chapter.")
        try:
            if int(story_selected) == 1:
                print(f"Start reading {chapters[int(story_selected)]}?\n")
                print("1. Yes.\n2. No.\n")
                while True:
                    confirm_story = input("")
                    if int(confirm_story) == 1:
                        chapter1()
                    elif int(confirm_story) == 2:
                        story_selector()
            elif int(story_selected) == 2:
                print(f"Start reading {chapters[int(story_selected)]}?\n")
                print("1. Yes.\n2. No.\n")
                while True:
                    confirm_story = input("")
                    if int(confirm_story) == 1:
                        chapter2()
                    elif int(confirm_story) == 2:
                        story_selector()
            else:
                raise ValueError
        except ValueError:
            error_statements(story_selected)
            continue

story_selector()

# chapter1()
