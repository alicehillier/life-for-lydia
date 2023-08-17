# Import getpass so the user input is not echoed in the terminal, giving it a better appearance.
import getpass

def error_statements(decide):
    """
    The error statements that will be displayed to the user if they do not enter an assigned value. The statements
    take into account alphabet, only spaces, no input, and a general statement to cover remaining scenarios.
    """
    if decide.isalpha():
        print(f"You entered {decide}. That's not a number! Please enter a valid number from the options above!\n")
    elif decide.isspace():
        print("You didn't enter anything! Please enter a valid number from the options above!\n")
    elif not decide:
        print("You didn't enter anything! Please enter a valid number from the options above!\n")
    else:
        print(f"You entered {decide}. Please enter a valid number from the options above!\n")

def make_decision(options):
    """
    Takes the argument 'options', which will be defined differently as a 
    dictionary in each function. Dictionaries must have four key-value pairs,
    with keys as numbers 1-4, for this function to execute.
    Processes the user's input, calling the relevant function in accordance with
    the user's selection. Raises ValueError if the user enters an invalid value 
    and loops the input requirement until the value is considered valid.
    """

    print(f"1. {options[1]}\n2. {options[2]}\n")
    while True:
        decide = getpass.getpass(prompt = "Enter 1 or 2.\n")
        try:
            if int(decide) == 1:
                options[3]()
                break
            elif int(decide) == 2:
                options[4]()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def go_to_next_step(options):
    """
    Takes the argument 'options', which will be defined differently as a 
    dictionary in each function. Dictionaries must have two key-value pairs,
    with keys as numbers 1-2, for this function to execute.
    Processes the user's input, calling the relevant function in accordance with
    the user's selection. Raises ValueError if the user enters an invalid value 
    and loops the input requirement until the value is considered valid.
    """
    print(f"1. {options[1]}\n")
    while True:
        decide = getpass.getpass(prompt = "Enter 1.\n")
        try:
            if int(decide) == 1:
                options[2]()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def chapter1():
    """
    Prints the opening lines of the story and brings the user to the first 
    decision point, which will direct the user to the next part of the story. 
    """
    print("The winter is colder than usual. We haven’t had snow in years, but\n"
    "now it envelops everything in sight. The birds are long gone, and even the\n"
    "rats that swarmed the street in summer are either in hiding or dead. Webs\n"
    "of ice have gathered on the windows and I can barely make out the shapes\n"
    "of cars under snowy rubble. I’m tired, but I know it must be done today.\n")
    options = {
        1: 'Do it.',
        2: 'Delay it.',
        3: do_it,
        4: delay_it
    }
    make_decision(options)

def do_it():
    """
    Runs when the user selects '1. Do it.' at the decision point in the chapter1 
    or delay_it function. Prints the next part of the story and brings the user 
    to the next decision point.
    """
    print("I slowly climb the stairs, my hand slipping as I try to hold onto the\n"
    "rail. I tighten my grip and continue upwards. As I turn to the bedroom, I\n"
    "take a deep breath. Standing in the doorway, I look at him. I look at the\n"
    "mess I’ve made.\n")
    options = {
        1: 'Try to wake him.',
        2: 'Clean up.',
        3: try_to_wake_him,
        4: clean_up
    }
    make_decision(options)
    
def delay_it():
    """
    Runs when the user selects '2. Delay it.' at the decision point in the 
    chapter1 function. Prints the next part of the story and brings the user to 
    the next decision point.
    """
    print("I make a cup of tea. I can’t put this off much longer…\n")
    options = {
        1: 'Do it.',
        2: do_it
    }
    go_to_next_step(options)

def try_to_wake_him():
    """
    Runs when the user selects '1. Try to wake him.' at the decision point in 
    the do_it function. Prints the next part of the story and brings the user to 
    the next decision point.
    """
    print("At this point, it seems pointless to try to wake him up.\n")
    options = {
        1: 'Clean up.',
        2: clean_up
    }
    go_to_next_step(options)

def clean_up():
    """
    Runs when the user selects '2. Clean up.' at the decision point in the do_it
    function or '1. Clean up.' at the decision point in the try_to_wake_him
    function. Prints the next part of the story and brings the user to the next 
    decision point.
    """
    print("I start by clearing the area around the bed, kicking clothes to the\n"
    "side to clear a path. I'll need something to clear up the glass.\n")
    options = {
        1: 'Get a mop.',
        2: 'Get a dustpan and brush.',
        3: get_a_mop_1,
        4: get_a_dustpan
    }
    make_decision(options)

def get_a_mop_1():
    """
    Runs when the user selects '1. Get a mop.' at the decision point in the 
    clean_up function. Prints the next part of the story and brings the user to 
    the next decision point.
    """
    print("I don’t think a mop is the best choice here.\n")
    options = {
        1: 'Get a dustpan and brush.',
        2: get_a_dustpan
    }
    go_to_next_step(options)

def get_a_dustpan():
    """
    Runs when the user selects '2. Get a dustpan and brush.' at the decision 
    point in the clean_up function or '1. Get a dustpan and brush.' at the 
    decision point in the get_a_mop_1 function. Prints the next part of the 
    story and brings the user to the next decision point.
    """
    print("I retrieve the dustpan and brush from the cupboard under the kitchen\n"
    "sink and begin to clear up the glass. Now that’s done, I need to get rid of\n"
    "all this blood.\n")
    options = {
        1: 'Get tissues.',
        2: 'Get towels.',
        3: get_tissues,
        4: get_towels
    }
    make_decision(options)

def get_tissues():
    """
    Runs when the user selects '1. Get tissues.' at the decision point in the 
    get_a_dustpan function. Prints the next part of the story and brings the 
    user to the next decision point.
    """
    print("Tissues aren’t going to be enough…\n")
    options = {
        1: 'Get towels.',
        2: get_towels
    }
    go_to_next_step(options)

def get_towels():
    """
    Runs when the user selects '2. Get towels.' at the decision point in the 
    get_a_dustpan function or '1. Get towels.' at the decision point in the 
    get_tissues function. Prints the next part of the story and brings the user 
    to the next decision point.
    """
    print("It takes a few towels, but they soak up most of the blood. I’ll have\n"
    "to use a mop for the rest.\n")
    options = {
        1: 'Get a mop.',
        2: get_a_mop_2
    }
    go_to_next_step(options)

def get_a_mop_2():
    """
    Runs when the user selects '1. Get a mop.' at the decision point in the 
    get_towels function. Prints the next part of the story and brings the 
    user to the next decision point.
    """
    print("As I make my way downstairs, I hear a barrage of heavy bangs on the\n"
    "front door. I look down at my clothes. I can’t see any stains. Should I\n"
    "open the door?\n")
    options = {
        1: 'Open the door.',
        2: 'Ignore it.',
        3: open_the_door,
        4: ignore_it
    }
    make_decision(options)

def open_the_door():
    """
    Runs when the user selects '1. Open the door.' at the decision point in the 
    get_a_mop_2 function. Prints the next part of the story and brings the user 
    to the next decision point.
    """
    print("Are you sure?\n")
    options = {
        1: 'Look for stains.',
        2: 'Open it.',
        3: look_for_stains,
        4: open_it
    }
    make_decision(options)

def ignore_it():
    """
    Runs when the user selects '1. Ignore it.' at the decision point in the 
    get_a_mop_2 function. Prints the next part of the story and brings the user 
    to the next decision point.
    """
    print("I continue downstairs, quickly and quietly. As I go to open the\n"
    "storage cupboard under the stairs, I notice blood on my hands. I rush back\n"
    "to the stairs and check the bannister. Long streaks of blood have stained\n"
    "the white-painted wood. That’s why my hand slipped earlier...\n"
    "I hear the squeak of metal and look at the door. The letterbox is open and\n"
    "dark eyes glare at me.\n")
    options = {
        1: 'Escape.',
        2: escape
    }
    go_to_next_step(options)

def look_for_stains():
    """
    Runs when the user selects '1. Look for stains.' at the decision point in 
    the open_the_door function. Prints the next part of the story and brings the 
    user to the next decision point.
    """
    print("I check my clothes again and see some splashes of blood on my\n"
    "slippers. As I pull my gown towards me to get a better look, the fabric\n"
    "sticks to my hands. I pry them away and see that they are still wet with\n"
    "blood. I hear the squeak of metal and look at the door. The letterbox is\n"
    "open and dark eyes glare at me as I stand on the stairs.\n"
    "'We\'re responding to a call. Open the door, ma\'am,' the man says.\n")
    options = {
        1: 'Escape.',
        2: escape
    }
    go_to_next_step(options)

def open_it():
    """
    Runs when the user selects '2. Open it.' at the decision point in the 
    open_the_door function. Prints the next part of the story and brings the 
    user to the next decision point.
    """
    print("I try to compose myself and open the door with a soft smile. In front\n"
    "of me are two police officers.\n"
    "'Ma\'am?' the older man says, his brows furrowed.\n"
    "The younger officer is staring at my hands. I look down at them and see\n"
    "that they are still wet with blood.\n"
    "'Can we come in?'”' The older man asks.\n"
    "I try to think of a response, but my mind is blank. I feel as though my\n"
    "heart has stopped. The man steps towards me.\n")
    options = {
        1: 'Think of an excuse.',
        2: think_of_excuse
    }
    go_to_next_step(options)

def think_of_excuse():
    """
    Runs when the user selects '1. Think of an excuse.' at the decision point in
    the open_it function. Prints the next part of the story and brings the user 
    to the next decision point.
    """
    print("'I... sorry, I was just about to go out,' I say.\n"
    "'In your dressing gown, Miss?' the older officer says.\n"
    "I slam the door shut.\n")
    options = {
        1: 'Escape.',
        2: escape
    }
    go_to_next_step(options)

def escape():
    """
    Runs when the user selects '1. Escape.' at the decision point in the
    ignore_it, look_for_stains or think_of_excuse function. Prints the next part
    of the story and brings the user to the next decision point.
    """
    print("I rush to the kitchen to escape out the back door. As I trudge\n"
    "through the thick snow, my slippers drenched and my feet freezing, I reach\n"
    "the back alley. I hear the officers shouting something at me.\n")
    options = {
        1: 'Surrender.',
        2: 'Keep running.',
        3: surrender,
        4: keep_running
    }
    make_decision(options)

def surrender():
    """
    Runs when the user selects '1. Surrender.' at the decision point in the 
    escape function. Prints the next part of the story and brings the 
    user to the next decision point.
    """
    print("I look to my left at the end of the alley and see an officer rushing\n"
    "towards me.\n"
    "'Stop!' he yells.\n"
    "I glance to my right. I know I cannot outrun him. I raise my hands and he\n"
    "approaches me.\n"
    "'Lets have a talk,' he says.\n")

def keep_running():
    """
    Runs when the user selects '2. Keep running.' at the decision point in the 
    escape function. Prints the next part of the story and brings the 
    user to the next decision point.
    """
    print("I kick off my slippers and my feet are raw. I head right and follow\n"
    "the alley as it winds between houses. I glance behind me briefly and see\n"
    "the two officers.\n"
    "'Stop!' one of the men yells.\n"
    "I have to outrun them. As I turn a corner, something sharp cuts into my\n"
    "foot. I scream and fall forwards, hearing a crack as my knee hits the\n"
    "ground. The men stand over me. I'm done.\n")