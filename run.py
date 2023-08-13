from chapter1 import *

def story_selector():
    """
    Asks the user to select a story. When the player does so, they are able to view general information about the story 
    before confirming their selection. Once confirmed, the relevant story will play out.
    """

    chapters = {
        1: "Chapter One: The Morning After",
        2: "Chapter Two: The Interview"
    }

    print("Enter 1 or 2 to start reading the selected chapter.\n")
    print("1. Chapter One: The Morning After.\n2. Chapter Two: The Interview.\n")
    while True:
        story_selected = int(input(""))
        try:
            if int(story_selected) == 1:
                print(f"Start reading {chapters[story_selected]}?\n")
                print("1. Yes.\n2. No.\n")
                while True:
                    confirm_story = input("")
                    if int(confirm_story) == 1:
                        chapter1()
                    elif int(confirm_story) == 2:
                        chapter2()
                    else:
                        story_selector()
        except ValueError as e:
            if story_selected.isalpha():
                print(f"You entered {story_selected}. That's not a number! Please enter a valid number from the options above!\n")
            elif story_selected.isspace():
                print("You didn't enter anything! Please enter a valid number from the options above!\n")
            else:
                print(f"You entered {story_selected}. Please enter a valid number from the options above!\n")
            continue

story_selector()

# chapter1()

def chapter2():
    print("chapter 2 here")