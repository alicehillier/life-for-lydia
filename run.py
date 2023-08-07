# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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
def clean_up():
    """
    Runs if the user selects the second option in the do_it function. 
    Prints lines of the story and calls for the user to make the next decision.
    """
    print("I start by clearing the area around the bed, kicking clothes to the side to clear a path to the bed.") 
    print("I’ll need something to clear up the glass.")


start()