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

name = story_selector()
print(name)

def wrong_decision():
    while True:
        decide = input("")
        try:
            if int(decide) == 1:
                break
            else:
                raise ValueError
        except ValueError as e:
            if decide.isalpha():
                print(f"You entered {decide}. That's not a number! Please enter 1!\n")
            else:
                print(f"You entered {decide}. Please enter 1!\n")
            continue

def start():
    """
    Prints the opening lines of the story and calls for the user to make their first decision.
    """
    print("The winter is colder than usual. We haven’t had snow in years, but now it envelops everything in sight.")
    print("The birds are long gone, and even the rats that swarmed the street in summer are either in hiding or dead.")
    print("Webs of ice have gathered on the windows and I can barely make out the shapes of cars under snowy rubble.")
    print("I’m tired, but I know it must be done today.\n")
    first_decision()
    
def first_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. Do it.\n2. Delay it.\n')
        try:
            if int(decide) == 1:
                do_it()
                break
            elif int(decide) == 2:
                delay_it()
                break
            else:
                raise ValueError
        except ValueError as e:
            if decide.isalpha():
                print(f"You entered {decide}. That's not a number! Please enter 1 or 2!\n")
            else:
                print(f"You entered {decide}. Please enter 1 or 2!\n")
            continue

def do_it():
    """
    Runs if the user selects the first option in the start function. 
    Prints lines of the story and calls for the user to make the next decision.
    """
    print("I slowly climb the stairs, my hand slipping as I try to hold onto the rail.")
    print("I tighten my grip and continue upwards. As I turn to the bedroom, I take a deep breath.")
    print("Standing in the doorway, I look at him. I look at the mess I’ve made.")
    second_decision()

def second_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. Try to wake him.\n2. Clean up.\n')
        try:
            if int(decide) == 1:
                try_to_wake_him()
                break
            elif int(decide) == 2:
                clean_up()
                break
            else:
                raise ValueError
        except ValueError as e:
            if decide.isalpha():
                print(f"You entered {decide}. That's not a number! Please enter 1 or 2!\n")
            else:
                print(f"You entered {decide}. Please enter 1 or 2!\n")
            continue
    
def delay_it():
    """
    Runs if the user selects the second option in the start function. 
    Prints lines of the story and calls for the user to make the next decision.
    """
    print("I make a cup of tea. I can’t put this off much longer…\n")
    print("1. Do it.\n")
    wrong_decision()
    do_it()

def try_to_wake_him():
    """
    Runs if the user selects the first option in the do_it function. 
    Prints lines of the story and calls for the user to make the next decision.
    """
    print("At this point, it seems pointless to try to wake him up.")
    print("1. Clean up.\n")
    wrong_decision()
    clean_up()

def clean_up():
    """
    Runs if the user selects the second option in the do_it function. 
    Prints lines of the story and calls for the user to make the next decision.
    """
    print("I start by clearing the area around the bed, kicking clothes to the side to clear a path to the bed.") 
    print("I’ll need something to clear up the glass.")
    third_decision()

def third_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. Get a mop.\n2. Get a dustpan and brush.\n')
        try:
            if int(decide) == 1:
                get_a_mop_1()
                break
            elif int(decide) == 2:
                get_a_dustpan()
                break
            else:
                raise ValueError
        except ValueError as e:
            if decide.isalpha():
                print(f"You entered {decide}. That's not a number! Please enter 1 or 2!\n")
            else:
                print(f"You entered {decide}. Please enter 1 or 2!\n")
            continue

def get_a_mop_1():
    print("I don’t think a mop is the best choice here.")
    print("1. Get a dustpan and brush.\n")
    wrong_decision()
    get_a_dustpan()

def get_a_dustpan():
    print("I retrieve the dustpan and brush from the cupboard under the kitchen sink and begin to clear up the glass.") 
    print("Now that’s done, I need to get rid of all this blood.")
    fourth_decision()

def fourth_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. Get tissues.\n2. Get towels.\n')
        try:
            if int(decide) == 1:
                get_tissues()
                break
            elif int(decide) == 2:
                get_towels()
                break
            else:
                raise ValueError
        except ValueError as e:
            if decide.isalpha():
                print(f"You entered {decide}. That's not a number! Please enter 1 or 2!\n")
            else:
                print(f"You entered {decide}. Please enter 1 or 2!\n")
            continue

def get_tissues():
    print('get tissues now')
def get_towels():
    print('get towels now')

start()