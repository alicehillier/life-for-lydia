"""Import datetime to display current time and date in Chapter Two"""
from datetime import datetime
import getpass
import time
import sys
import os


# THIS CODE IS FROM https://www.101computing.net/python-typing-text-effect/
# and sys, os were imported according to this guide.


def typing_print(text):
    """Creates a typewriter effect for the app."""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)

# THIS CODE IS FROM:
# https://www.codingninjas.com/studio/library/how-to-clear-a-screen-in-python
# and customised.


def clear():
    """Clears the console. Used after every decision point."""
    # Use 'cls' to clear console in Windows.
    if os.name == "nt":
        os.system('cls')
    # If the system is not Windows, (e.g. Linux) use 'clear'.
    else:
        os.system("clear")


# IMPORTANT STORY FUNCTIONS below.

def error_statements(decide):
    """
    The error statements that will be displayed to the user if they do not
    enter an assigned value. The statements take into account alphabet, only
    spaces, no input, and a general statement to cover remaining scenarios.
    """
    if decide.isalpha():
        print(f" You entered {decide}. That's not a number!\n"
              " Please enter a valid number from the options above!\n")
    elif decide.isspace():
        print(" You didn't enter anything!\n"
              " Please enter a valid number from the options above!\n")
    elif not decide:
        print(" You didn't enter anything!\n"
              " Please enter a valid number from the options above!\n")
    else:
        print(f" You entered {decide}.\n"
              " Please enter a valid number from the options above!\n")


def make_decision(options):
    """
    Takes the argument 'options', which will be defined differently as a
    dictionary in each function. Dictionaries must have four key-value pairs,
    with keys as numbers 1-4, for this function to execute.
    Processes the user's input, calling the relevant function in accordance
    with the user's selection. Raises ValueError if the user enters an invalid
    value and loops the input requirement until the value is considered valid.
    """
    typing_print(f"\n 1. {options[1]}\n 2. {options[2]}\n")
    while True:
        decide = getpass.getpass(prompt="\n Enter 1 or 2.\n")
        try:
            # If the first option is selected, run the function assigned to
            # number 3.
            if int(decide) == 1:
                clear()
                options[3]()
            # If the second option is selected, run the function assigned to
            # number 4.
            elif int(decide) == 2:
                clear()
                options[4]()
            # If the user enters 0, return to main menu after a short delay.
            elif int(decide) == 0:
                typing_print(" Looking for the right page...\n")
                time.sleep(3)
                typing_print(" Aha! Found it!\n")
                time.sleep(1)
                clear()
                introduction()
            else:
                # If the user enters something else, display the relevant error
                # statement.
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue


def go_to_next_step(options):
    """
    Takes the argument 'options', which will be defined differently as a
    dictionary in each function. Dictionaries must have two key-value pairs,
    with keys as numbers 1-2, for this function to execute.
    Processes the user's input, calling the relevant function in accordance
    with the user's selection. Raises ValueError if the user enters an invalid
    value and loops the input requirement until the value is considered valid.
    """
    print(f"\n 1. {options[1]}\n")
    while True:
        decide = getpass.getpass(prompt=" Enter 1.\n")
        try:
            if int(decide) == 1:
                clear()
                options[2]()
            elif int(decide) == 0:
                typing_print(" Looking for the right page...\n")
                time.sleep(2)
                typing_print(" Aha! Found it!\n")
                time.sleep(1)
                clear()
                introduction()
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

# MAIN MENU code below.


def introduction():
    """
    Displays the title of the story and an introduction to the app. It also
    provides instructions for the game.
    """
    title = "LIFE FOR LYDIA"
    print(title.center(80))
    author = "by Alice Hillier\n"
    print(author.center(80))
    print("\n Welcome to 'Life for Lydia', an interactive story written by "
          "Alice Hillier\n for the third milestone project in Code "
          "Institute's Software Development\n (E-Commerce) programme.\n")
    print("\n To play this game, you'll need to use the number keys on your "
          "keyboard\n and the enter key. If you would like to leave the game "
          "and return to this page\n at any point, type '0' and press the "
          "enter key. Be warned though, your\n progress will not be saved!\n"
          "\n Now, I think you're ready to play! Follow the instructions "
          "below to get\n started.\n")
    options = {
        1: "Select a Chapter.",
        2: story_selector
    }
    go_to_next_step(options)


def story_selector():
    """
    Asks the user to select a story. Selecting either 1 or 2 (as per the
    instructions) will trigger the confirm_story function.
    """
    chapters = {
        1: "Chapter One: The Morning After",
        2: "Chapter Two: The Interview",
        3: chapter1,
        4: chapter2
    }
    make_decision(chapters)

# CHAPTER 1: THE MORNING AFTER code below.


def chapter1():
    """
    Prints the opening lines of the story and brings the user to the first
    decision point, which will direct the user to the next part of the story.
    """
    chapter_one = "Chapter One: The Morning After\n"
    typing_print(chapter_one.center(80))
    time.sleep(1)
    typing_print("\n The winter is colder than usual. We haven't had snow in "
                 "years, but\n now it envelops everything in sight. The birds "
                 "are long gone, and even the\n rats that swarmed the street "
                 "in summer are either in hiding or dead. Webs\n of ice have "
                 "gathered on the windows and I can barely make out the "
                 "shapes\n of cars under snowy rubble. I'm tired, but I know "
                 "it must be done today.\n")
    options = {
        1: 'Do it.',
        2: 'Delay it.',
        3: do_it,
        4: delay_it
    }
    make_decision(options)


def do_it():
    """
    Runs when the user selects '1. Do it.' at the decision point in chapter1
    or delay_it functions. Prints the next part of the story and brings the
    user to the next decision point.
    """
    typing_print(" I slowly climb the stairs, my hand slipping as I try to "
                 "hold onto the\n rail. I tighten my grip and continue "
                 "upwards. As I turn to the bedroom, I\n take a deep breath. "
                 "Standing in the doorway, I look at him. I look at the\n "
                 "mess I've made.\n")
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
    typing_print(" I make a cup of tea. I can't put this off much longer…\n")
    options = {
        1: 'Do it.',
        2: do_it
    }
    go_to_next_step(options)


def try_to_wake_him():
    """
    Runs when the user selects '1. Try to wake him.' at the decision point in
    the do_it function. Prints the next part of the story and brings the user
    to the next decision point.
    """
    typing_print(" At this point, it seems pointless to try to wake him up.\n")
    options = {
        1: 'Clean up.',
        2: clean_up
    }
    go_to_next_step(options)


def clean_up():
    """
    Runs when the user selects '2. Clean up.' at the decision point in do_it
    function or '1. Clean up.' at the decision point in the try_to_wake_him
    function. Prints the next part of the story and brings the user to the next
    decision point.
    """
    typing_print(" I start by clearing the area around the bed, kicking "
                 "clothes to the\n side to clear a path. I'll need something "
                 "to clear up the glass.\n")
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
    typing_print(" I don't think a mop is the best choice here.\n")
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
    typing_print(" I retrieve the dustpan and brush from the cupboard under "
                 "the kitchen\n sink and begin to clear up the glass. Now "
                 "that's done, I need to get rid of\n all this blood.\n")
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
    typing_print(" Tissues aren't going to be enough…\n")
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
    typing_print(" It takes a few towels, but they soak up most of the blood. "
                 "I'll have\n to use a mop for the rest.\n")
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
    typing_print(" As I make my way downstairs, I hear a barrage of heavy "
                 "bangs on the\n front door. I look down at my clothes. I "
                 "can't see any stains. Should I\n open the door?\n")
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
    typing_print(" Are you sure?\n")
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
    typing_print(" I continue downstairs, quickly and quietly. As I go to "
                 "open the\n storage cupboard under the stairs, I notice "
                 "blood on my hands. I rush back\n to the stairs and check "
                 "the bannister. Long streaks of blood have stained\n the "
                 "white-painted wood. That's why my hand slipped earlier...\n "
                 "I hear the squeak of metal and look at the door. The "
                 "letterbox is open and\n dark eyes glare at me.\n")
    options = {
        1: 'Escape.',
        2: escape
    }
    go_to_next_step(options)


def look_for_stains():
    """
    Runs when the user selects '1. Look for stains.' at the decision point in
    the open_the_door function. Prints the next part of the story and brings
    the user to the next decision point.
    """
    typing_print(" I check my clothes again and see some splashes of blood on "
                 "my\n slippers. As I pull my gown towards me to get a better "
                 "look, the fabric\n sticks to my hands. I pry them away and "
                 "see that they are still wet with\n blood. I hear the squeak "
                 "of metal and look at the door. The letterbox is\n open and "
                 "dark eyes glare at me as I stand on the stairs.\n"
                 " 'We\'re responding to a call. Open the door, ma\'am,' the "
                 "man says.\n")
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
    typing_print(" I try to compose myself and open the door with a soft "
                 "smile. In front\n of me are two police officers.\n"
                 " 'Ma\'am?' the older man says, his brows furrowed.\n"
                 " The younger officer is staring at my hands. I look down at "
                 "them and see\n that they are still wet with blood.\n"
                 " 'Can we come in?'”' The older man asks.\n"
                 " I try to think of a response, but my mind is blank. I feel "
                 "as though my\n heart has stopped. The man steps towards "
                 "me.\n")
    options = {
        1: 'Think of an excuse.',
        2: think_of_excuse
    }
    go_to_next_step(options)


def think_of_excuse():
    """
    Runs when the user selects '1. Think of an excuse.' at the decision point
    in open_it function. Prints the next part of the story and brings the user
    to the next decision point.
    """
    typing_print(" 'I... sorry, I was just about to go out,' I say.\n"
                 " 'In your dressing gown, Miss?' the older officer says.\n"
                 " I slam the door shut.\n")
    options = {
        1: 'Escape.',
        2: escape
    }
    go_to_next_step(options)


def escape():
    """
    Runs when the user selects '1. Escape.' at the decision point in the
    ignore_it, look_for_stains or think_of_excuse function. Prints the next
    part of the story and brings the user to the next decision point.
    """
    typing_print(" I rush to the kitchen to escape out the back door. As I "
                 "trudge\n through the thick snow, my slippers drenched and "
                 "my feet freezing, I reach\n the back alley. I hear the "
                 "officers shouting something at me.\n")
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
    typing_print(" I look to my left at the end of the alley and see an "
                 "officer rushing\n towards me.\n 'Stop!' he yells.\n"
                 " I glance to my right. I know I cannot outrun him. I raise "
                 "my hands and he\n approaches me.\n 'Lets have a talk,' he "
                 "says.\n")
    typing_print("\n To be continued...\n")
    options = {
        1: 'Continue reading.',
        2: 'Return to main menu.',
        3: chapter2,
        4: introduction
    }
    make_decision(options)


def keep_running():
    """
    Runs when the user selects '2. Keep running.' at the decision point in the
    escape function. Prints the next part of the story and brings the
    user to the next decision point.
    """
    typing_print(" I kick off my slippers and my feet are raw. I head right "
                 "and follow\n the alley as it winds between houses. I glance "
                 "behind me briefly and see\n the two officers.\n"
                 " 'Stop!' one of the men yells.\n"
                 " I have to outrun them. As I turn a corner, something sharp "
                 "cuts into my\n foot. I scream and fall forwards, hearing a "
                 "crack as my knee hits the\n ground. The men stand over me. "
                 "I'm done.\n")
    typing_print("\n To be continued...\n")
    options = {
        1: 'Continue reading.',
        2: 'Return to main menu.',
        3: chapter2,
        4: introduction
    }
    make_decision(options)

# CHAPTER 2: THE INTERVIEW code below.


lydia = {
    'Name': 'Lydia Simmons',
    'Date of Birth': '17/04/1983',
    'Status': 'Married',
    'Profession': 'Sales Assistant',
    'Previous Convictions': 'None',
    'Reason for Arrest': 'Suspicion of murder'
}

simon = {
    'Name': 'Simon Simmons',
    'Date of Birth': '23/07/1979',
    'Status': 'Married',
    'Profession': 'IT Support',
    'Previous Convictions': 'Drunk driving',
    'Cause of Death': 'Stabbing',
    'Toxicology Report': 'No toxins found'
}


def lydias_file():
    """
    Prints all keys and values in the 'lydia' dictionary as plain text.
    """
    for key, value in lydia.items():
        typing_print(f"\n {key}: {value}")


def simons_file():
    """
    Prints all keys and values in the 'simon' dictionary as plain text.
    """
    for key, value in simon.items():
        typing_print(f"\n {key}: {value}")


# The date and time are formatted below so that it is displayed as clear text
# to the user in the relevant sections.

date = datetime.now()
today = date.strftime("%A, %B %d, %Y")
get_time_now = datetime.now().time()
time_now = get_time_now.strftime("%H:%M")


def chapter2():
    """
    Prints the opening lines of the story, displays the formatted lydia
    dictionary via the lydias_file function. Contains the first decision, which
    will direct the user to the next part of the story.
    """
    time.sleep(1)
    chapter_two = "Chapter Two: The Interview\n"
    typing_print(chapter_two.center(80))
    time.sleep(1)
    typing_print("\n The officer drops the file onto the desk and leans over "
                 "to turn on\n the recorder.\n 'Interview with suspect, Lydia "
                 f"Simmons, at {time_now} on {today}.\n Officers present are "
                 "Smith, badge 247800, and Anderson, badge 310010.'\n"
                 " 'Lydia, is this information correct?' he asks.\n The "
                 "officer opens his file at the first page and points to the "
                 "text.\n")
    lydias_file()
    typing_print("\n\n I nod.\n"
                 " 'Any idea why you\'re here?' he asks.\n")
    options = {
        1: 'Yes.',
        2: 'No.',
        3: answer_yes,
        4: answer_no
    }
    make_decision(options)


def answer_yes():
    """
    Runs when the user selects '1. Yes.' at the decision point in the chapter2
    function. Prints the next part of the story, displays the formatted simon
    dictionary and brings the user to the next decision point.
    """
    typing_print(" I nod slightly.\n"
                 " 'Enlighten me,' he says.\n"
                 " 'My husband,' I say.\n"
                 " The officer turns to the next page in the file and spins "
                 "it around to\n show me.\n")
    simons_file()
    typing_print("\n\n 'Is this your husband, Lydia?' the officer asks.\n"
                 " 'Yes,' I say.\n"
                 " 'What\'s happened with your husband?' he asks.\n")
    options = {
        1: 'Explain.',
        2: 'Say nothing.',
        3: explain,
        4: say_nothing
    }
    make_decision(options)


def answer_no():
    """
    Runs when the user selects '2. No.' at the decision point in the chapter2
    function. Prints the next part of the story and brings the user to the next
    decision point.
    """
    typing_print(" I curl my lip, raise my eyebrows and stare at the table.\n"
                 " 'Care to explain why you were covered in blood when we "
                 "found you,\n or why you tried to flee? Perhaps you would "
                 "like to explain the \n situation in your bedroom?'\n")
    options = {
        1: 'Explain.',
        2: 'Say nothing.',
        3: explain,
        4: say_nothing
    }
    make_decision(options)


def explain():
    """
    Runs when user selects '1. Explain.' at the decision point in answer_yes
    or answer_no function. Prints the next part of the story and brings user to
    the next decision point.
    """
    typing_print(" 'I found out that he was having an affair,' I say.\n"
                 " 'So you killed him?' the officer asks.\n"
                 " 'No,' I say.\n")
    options = {
        1: 'It was an accident.',
        2: 'It was self-defence.',
        3: accident,
        4: self_defence
    }
    make_decision(options)


def say_nothing():
    """
    Runs when the user selects '2. Say nothing.' at the decision point in the
    yes or no function. Prints the next part of the story and brings the user
    to the next decision point.
    """
    typing_print(" 'Given that we found your husband dead, with several stab "
                 "wounds,\n in your bedroom, and you were covered in blood "
                 "and running away...'\n 'It looks bad for you,' the officer "
                 "says.\n")
    options = {
        1: 'It was an accident.',
        2: 'It was self-defence.',
        3: accident,
        4: self_defence
    }
    make_decision(options)


def accident():
    """
    Runs when user selects '1. It was an accident.' at the decision point in
    the explain or say_nothing function. Prints the next part of the story and
    brings the user to the next decision point.
    """
    typing_print(" 'I was trying to hurt myself. He just... got in the way,' "
                 "I say.\n"
                 " 'And how many times did he get in the way?' the officer "
                 "asks.\n 'See, his body had multiple stab wounds. Did you "
                 "accidentally stab\n him six or seven times?'\n")
    options = {
        1: 'He was drunk.',
        2: he_was_drunk
    }
    go_to_next_step(options)


def self_defence():
    """
    Runs when the user selects '2. It was self-defence.' at the decision point
    in the explain or say_nothing function. Prints the next part of the story
    and brings the user to the next decision point.
    """
    typing_print(" 'I told him that I knew he was having an affair,' I say.\n"
                 " 'He was angry.'\n"
                 " 'Why would he be angry at you?' the officer asks.\n")
    options = {
        1: 'He was aggressive.',
        2: 'He was drunk.',
        3: he_was_aggressive,
        4: he_was_drunk
    }
    make_decision(options)


def he_was_aggressive():
    """
    Runs when the user selects '1. He was aggressive.' at the decision point
    in the self_defence function. Prints the next part of the story and brings
    the user to the next decision point.
    """
    typing_print(" 'He could be aggressive,' I say.\n"
                 " 'He could be, or he was?' the officer asks.\n"
                 " 'He was. He was controlling and he didn\'t have control "
                 "this time,' I say.\n"
                 " 'Was he drunk?' he asks.\n")
    options = {
        1: 'He was drunk.',
        2: 'He might not have been drunk.',
        3: he_was_drunk,
        4: he_was_not_drunk
    }
    make_decision(options)


def he_was_drunk():
    """
    Runs when the user selects '2. He was drunk.' at the decision point
    in the self_defence function or '1. He was drunk.' in the he_was_aggressive
    function. Prints the next part of the story and brings the user to the next
    decision point.
    """
    typing_print(" 'He seemed to be inebriated,' I say.\n"
                 " 'He was drunk?' the officer asks.\n"
                 " I nod. 'He\'s a different person when he\'s drunk,' I say. "
                 "\n 'In what way?' he asks.\n"
                 " 'He can be unpredictable. Scary, even,' I say.\n"
                 " 'I see… It\'s interesting you say that, Lydia,' he says, "
                 "'because the\n toxicology report showed no trace of "
                 "alcohol, or anything else.'\n")
    options = {
        1: 'Question the findings.',
        2: question_findings
    }
    go_to_next_step(options)


def he_was_not_drunk():
    """
    Runs when the user selects '2. He might not have been drunk.' at the
    decision point in the he_was_aggressive function. Prints the next part of
    the story and brings the user to the next decision point.
    """
    typing_print(" 'Why would you confront a man who you say is aggressive "
                 "towards you?'\n the officer asks.\n"
                 " 'I didn\'t know it would be this bad,' I say.\n"
                 " The officer sighs. 'Let\'s get to the point,' he says.\n")
    options = {
        1: 'We argued.',
        2: we_argued
    }
    go_to_next_step(options)


def we_argued():
    """
    Runs when the user selects '1. We argued.' at the decision point in the
    he_was_not_drunk function. Prints the next part of the story and brings the
    user to the next decision point.
    """
    typing_print(" 'I was having a drink and packing my bag when he came "
                 "home,' I say.\n 'I was just going to stay with my sister "
                 "for a while.\n He came home and found me upstairs. I told "
                 "him what I knew and we argued.'\n 'And then?' The officer "
                 "asks.\n 'He got mad. I got scared,' I continue.\n 'He "
                 "lunged at me and I dropped the wine glass. It smashed. I "
                 "stepped back\n when he got close to me and I tripped on "
                 "something. I saw the broken glass\n and I just… I thought "
                 "he was going to hurt me. I\'d never seen him look\n like "
                 "that before.'\n")
    options = {
        1: 'Listen to the officer.',
        2: listen_to_officer_1
    }
    go_to_next_step(options)


def question_findings():
    """
    Runs when user selects '1. Question the findings.' at the decision point
    in the he_was_drunk function. Prints the next part of the story and brings
    the user to the next decision point.
    """
    typing_print(" 'He certainly seemed drunk to me,' I say.\n"
                 " 'So the report is incorrect?' the officer asks.\n"
                 " 'It could be,' I reply.\n"
                 " The officer smiles. 'Then what happened?'\n")
    options = {
        1: 'He attacked me.',
        2: he_attacked_me
    }
    go_to_next_step(options)


def he_attacked_me():
    """
    Runs when the user selects '1. He attacked me.' at the decision point
    in the question_findings function. Prints the next part of the story and
    brings the user to the next decision point.
    """
    typing_print(" 'He smashed the wine glass and threatened me with a large "
                 "piece,'\n I say. 'I tried to leave, but he stood between me "
                 "and the door. I begged\n him to let me go and he just... "
                 "attacked me,' I say.\n"
                 " 'And then?' the officer asks.\n"
                 " 'I don't remember,' I say.\n")
    options = {
        1: 'Listen to the officer.',
        2: listen_to_officer_2
    }
    go_to_next_step(options)


def listen_to_officer_1():
    """
    Runs when user selects '1. Listen to the officer.' at the decision point
    in the we_argued function. Prints the next part of the story and brings
    the user to the next decision point.
    """
    typing_print(" 'Look, Lydia,' the officer says. 'Charges are going to be "
                 "made.'\n"
                 " I nod, close to tears.\n"
                 f" 'Interview closing at {time_now}. Suspect is detained and "
                 "awaiting charges,'\n the officer says.\n")
    options = {
        1: 'View charges.',
        2: view_charges_1
    }
    go_to_next_step(options)


def listen_to_officer_2():
    """
    Runs when user selects '1. Listen to the officer.' at the decision point
    in he_attacked_me function. Prints the next part of the story and brings
    the user to the next decision point.
    """
    typing_print(" 'Lydia, what you\'ve shared with us today has been nothing "
                 "short of\n preposterous,' the officer says. 'First you said "
                 "you were trying to hurt\n yourself, then you said he was "
                 "drunk - even questioning the toxicology\n report. Next, "
                 "your husband was attacking you with a broken wine glass,'\n"
                 " despite the fact that you were the one drinking from it,' "
                 "he continues.\n 'Charges are going to be made and you\'ve "
                 "made things much worse for\n yourself. Officer Anderson "
                 "will return you to your cell.'\n"
                 f" 'Interview closing at {time_now}. Suspect is detained and "
                 "awaiting charges,'\n the officer says.\n")
    options = {
        1: 'View charges.',
        2: view_charges_2
    }
    go_to_next_step(options)


def view_charges_1():
    """
    Runs when the user selects '1. View charges.' at the decision point
    in listen_to_officer_1 function. Removes the 'Reason for arrest' key and
    its value from the lydia dictionary and adds a new key and value. Triggers
    the lydias_file function, which will display the information to the user.
    """
    lydia.popitem()
    lydia.update({'Charges': 'Manslaughter'})
    lydias_file()
    typing_print("\n To be continued...\n")
    options = {
        1: 'Return to main menu.',
        2: introduction
    }
    go_to_next_step(options)


def view_charges_2():
    """
    Runs when the user selects '1. View charges.' at the decision point
    in listen_to_officer_2 function. Removes the 'Reason for arrest' key and
    its value from the lydia dictionary and adds a new key and value. Triggers
    the lydias_file function, which will display the information to the user.
    """
    lydia.popitem()
    lydia.update({'Charges': 'Murder'})
    lydias_file()
    typing_print("\n To be continued...\n")
    options = {
        1: 'Return to main menu.',
        2: introduction
    }
    go_to_next_step(options)


introduction()
