def error_statements(decide):
    if decide.isalpha():
        print(f"You entered {decide}. That's not a number! Please enter a valid number from the options above!\n")
    elif decide.isspace():
        print("You didn't enter anything! Please enter a valid number from the options above!\n")
    else:
        print(f"You entered {decide}. Please enter a valid number from the options above!\n")

def wrong_decision():
    while True:
        decide = input("")
        try:
            if int(decide) == 1:
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def chapter1():
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
        except ValueError:
            error_statements(decide)
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
        except ValueError:
            error_statements(decide)
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
        except ValueError:
            error_statements(decide)
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
        except ValueError:
            error_statements(decide)
            continue

def get_tissues():
    print("Tissues aren’t going to be enough…\n")
    print("1. Get towels.\n")
    wrong_decision()
    get_towels()

def get_towels():
    print("It takes a few towels, but they soak up most of the blood. I’ll have to use a mop for the rest.\n")
    fifth_decision()

def fifth_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1.\n")
    while True:
        decide = input('1. Get a mop.\n')
        try:
            if int(decide) == 1:
                get_a_mop_2()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def get_a_mop_2():
    print("As I make my way downstairs, I hear a barrage of heavy bangs on the front door.") 
    print("I look down at my clothes. I can’t see any stains. Should I open the door?")
    sixth_decision()

def sixth_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. Open the door.\n2. Ignore it.\n')
        try:
            if int(decide) == 1:
                open_the_door()
                break
            elif int(decide) == 2:
                ignore_it()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def open_the_door():
    print("Are you sure?")
    seventh_decision()

def seventh_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. Look for stains.\n2. Open it.\n')
        try:
            if int(decide) == 1:
                look_for_stains()
                break
            elif int(decide) == 2:
                open_it()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def ignore_it():
    print("I continue downstairs, quickly and quietly.") 
    print("As I go to open the storage cupboard under the stairs, I notice blood on my hands.")
    print("I rush back to the stairs and check the bannister.")
    print("Long streaks of blood have stained the white-painted wood.")
    print("That’s why my hand slipped earlier…")
    print("I hear the squeak of metal and look at the door.")
    print("The letterbox is open and dark eyes glare at me.")
    ninth_decision()

def look_for_stains():
    print("I check my clothes again and see some splashes of blood on my slippers.")
    print("As I pull my gown towards me to get a better look, the fabric sticks to my hands.")
    print("I pry them away and see that they are still wet with blood.")
    print("I hear the squeak of metal and look at the door.")
    print("The letterbox is open and dark eyes glare at me as I stand on the stairs.")
    print("'We are responding to a call. Open the door, please,' the man says")
    ninth_decision()

def open_it():
    print("I try to compose myself and open the door with a soft smile.")
    print("In front of me are two police officers.")
    print("'Miss?' the older man says, his brows furrowed.") 
    print("The younger officer is staring at my hands.")
    print("I look down at them and see that they are still wet with blood.")
    print("'Can we come in?'”' The older man asks.")
    print("I try to think of a response, but my mind is blank.")
    print("I feel as though my heart has stopped. The man steps towards me.")
    eighth_decision()

def eighth_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. Think of an excuse.\n')
        try:
            if int(decide) == 1:
                think_of_excuse()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def think_of_excuse():
    print("'I… sorry, I was just about to go out,' I say.")
    print("'In your dressing gown, Miss?' the older man says.")
    print("I slam the door shut.")
    ninth_decision()

def ninth_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1.\n")
    while True:
        decide = input('1. Escape.\n')
        try:
            if int(decide) == 1:
                escape()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def escape():
    print("I rush to the kitchen to escape out the back door.")
    print("As I trudge through the thick snow, my slippers drenched and my feet freezing, I reach the back alley.")
    print("I hear men shouting something at me.")
    tenth_decision()

def tenth_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. Surrender.\n2. Keep running.\n')
        try:
            if int(decide) == 1:
                surrender()
                break
            elif int(decide) == 2:
                keep_running()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def surrender():
    print("I look to my left at the end of the alley and see the officer rushing towards me.")
    print("'Stop!' he yells. I glance to my right. I know I cannot outrun him.")
    print("I raise my hands and he approaches me.")
    print("'Lets have a talk,' he says.")

def keep_running():
    print("I kick off my slippers and my feet are raw.")
    print("I head right and follow the alley as it winds between houses.")
    print("I glance behind me briefly and see the two officers.")
    print("'Stop!' one of the men yells. I have to outrun them.")
    print("As I turn a corner, something sharp cuts into my foot.")
    print("I scream and feel myself falling forwards.")
    print("I hear a crack as my knee hits the ground. The men stand over me.")
    print("I’m done.")