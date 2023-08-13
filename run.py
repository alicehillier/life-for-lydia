from chapter1 import *

# Each dictionary contains information about the story selected.
lydia = {
    "Protagonist": "Lydia",
    "Title": "The Morning After",
    "Genre": "Crime"
    }

simon = {
    "Protagonist": "Simon",
    "Title": "The Date",
    "Genre": "Drama"
    }

anita = {
    "Protagonist": "Anita",
    "Title": "Night",
    "Genre": "Supernatural"
    }

def story_selector():
    """
    Asks the user to select a story. When the player does so, they are able to view general information about the story 
    before confirming their selection. Once confirmed, the relevant story will play out.
    """
    print("Enter 1, 2 or 3 to view the corresponding story's plot:\n")
    print("1. Lydia's Story.\n2. Simon's Story.\n3. Anita's story.")
    while True:
        story_selected = input("")
        try:
            if int(story_selected) == 1:
                print("Start reading?\n")
                print("1. Yes.\n2. No.\n")
                while True:
                    confirm_story = input("")
                    if int(confirm_story) == 1:
                        name = "lydia"
                        return name
                    elif int(confirm_story) == 2:
                        story_selector()
            if int(story_selected) == 2:
                print("Start reading?\n")
                print("1. Yes.\n2. No.\n")
                while True:
                    confirm_story = input("")
                    if int(confirm_story) == 1:
                        name = "simon"
                        return name
                    elif int(confirm_story) == 2:
                        story_selector()
            if int(story_selected) == 3:
                print("Start reading?\n")
                print("1. Yes.\n2. No.\n")
                while True:
                    confirm_story = input("")
                    if int(confirm_story) == 1:
                        name = "anita"
                        return name
                    elif int(confirm_story) == 2:
                        story_selector()
        except ValueError as e:
            if story_selected.isalpha():
                print(f"You entered {story_selected}. That's not a number! Please enter a valid number from the options above!\n")
            else:
                print(f"You entered {story_selected}. Please enter a valid number from the options above!\n")
            continue

# name = story_selector()
# print(name)

chapter1()