from chapter1 import error_statements, getpass, make_decision, go_to_next_step
from datetime import datetime

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
        print(f"\n{key}: {value}")


def simons_file():
    """
    Prints all keys and values in the 'simon' dictionary as plain text.
    """
    for key, value in simon.items():
        print(f"\n{key}: {value}")

date = datetime.now()
today = date.strftime("%A, %B %d, %Y")
time_now = datetime.now().time()
time = time_now.strftime("%H:%M")


def chapter2():
    """
    Prints the opening lines of the story, displays the formatted lydia 
    dictionary via the lydias_file function. Contains the first decision, which
    will direct the user to the next part of the story. 
    """
    print("\nThe officer drops the file onto the desk and leans over to turn on\n"
    "the recorder.\n"
    f"'Interview with suspect, Lydia Simmons, at {time} on {today}.\n"
    "Officers present are Smith, badge 247800, and Anderson, badge 310010.'\n"
    "'Lydia, is this information correct?' he asks.\n"
    "The officer opens his file at the first page and points to the text.\n")
    lydias_file()
    print("\nI nod.\n"
    "'Any idea why you\'re here?' he asks.\n")
    options = {
        1: 'Yes.',
        2: 'No.',
        3: yes,
        4: no
    }
    make_decision(options)


def yes():
    """
    Runs when the user selects '1. Yes.' at the decision point in the chapter2 
    function. Prints the next part of the story, displays the formatted simon 
    dictionary and brings the user to the next decision point.
    """
    print("I nod slightly.\n'Enlighten me,' he says.\n'My husband,' I say.\n"
    "The officer turns to the next page in the file and spins it around to\n"
    "show me.\n")
    simons_file()
    print("\n'Is this your husband, Lydia?' the officer asks.\n"
    "'Yes,' I say.\n"
    "'What\'s happened with your husband?' he asks.\n")
    options = {
        1: 'Explain.',
        2: 'Say nothing.',
        3: explain,
        4: say_nothing
    }
    make_decision(options)


def no():
    """
    Runs when the user selects '2. No.' at the decision point in the chapter2 
    function. Prints the next part of the story and brings the user to the next
    decision point.
    """
    print("I curl my lip, raise my eyebrows and stare at the table.\n"
    "'Care to explain why you were covered in blood when we found you,\n"
    "or why you tried to flee? Perhaps you would like to explain the \n"
    "situation in your bedroom?'\n")
    options = {
        1: 'Explain.',
        2: 'Say nothing.',
        3: explain,
        4: say_nothing
    }
    make_decision(options)


def explain():
    """
    Runs when the user selects '1. Explain.' at the decision point in the yes
    or no function. Prints the next part of the story and brings the user to 
    the next decision point.
    """
    print("'I found out that he was having an affair,' I say.\n"
    "'So you killed him?' the officer asks.\n"
    "'No,' I say.\n")
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
    print("'Given that we found your husband dead, with several stab wounds,\n"
    "in your bedroom, and you were covered in blood and running away...'\n"
    "'It looks bad for you,' the officer says.\n")
    options = {
        1: 'It was an accident.',
        2: 'It was self-defence.',
        3: accident,
        4: self_defence
    }
    make_decision(options)


def accident():
    """
    Runs when the user selects '1. It was an accident.' at the decision point in
    the explain or say_nothing function. Prints the next part of the story and
    brings the user to the next decision point.
    """
    print("'I was trying to hurt myself. He just... got in the way,' I say.\n"
    "'And how many times did he get in the way?'' the officer asks.\n"
    "'See, his body had multiple stab wounds. Did you accidentally stab\n"
    "him six or seven times?'\n")
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
    print("'I told him that I knew he was having an affair,' I say.\n"
    "'He was angry.'\n"
    "'Why would he be angry at you for that?' the officer asks.\n")
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
    print("'He could be aggressive,' I say.\n"
    "'He could be, or he was?' the officer asks.\n"
    "'He was. He was controlling and he didn\’t have control this time,' I say.\n"
    "'Was he drunk?' he asks.\n")
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
    print("'He seemed to be inebriated,' I say.\n"
    "'He was drunk?' the officer asks.\n"
    "I nod. 'He\'s a different person when he\'s drunk,' I say.\n"
    "'In what way?' he asks.\n"
    "'He can be unpredictable. Scary, even,' I say.\n"
    "'I see… It\'s interesting you say that, Lydia,' he says, 'because the\n"
    "toxicology report showed no trace of alcohol, or anything else.'\n")
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
    print("'Why would you confront a man who you say is aggressive towards you?'\n"
    "the officer asks.\n"
    "'I didn\’t know it would be this bad,' I say.\n"
    "The officer sighs. 'Let\’s get to the point,' he says.\n")
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
    print("'I was having a drink and packing my bag when he came home,' I say.\n"
    "'I was just going to stay with my sister for a while.\n"
    "He came home and found me upstairs. I told him what I knew and we argued.'\n"
    "'And then?' The officer asks.\n"
    "'He got mad. I got scared,' I continue.\n"
    "'He lunged at me and I dropped the wine glass. It smashed. I stepped back\n"
    "when he got close to me and I tripped on something. I saw the broken glass\n"
    "and I just… I thought he was going to hurt me. I\’d never seen him look\n"
    "like that before.'\n")
    options = {
        1: 'Listen to the officer.',
        2: listen_to_officer_1
    }
    go_to_next_step(options)


def question_findings():
    """
    Runs when the user selects '1. Question the findings.' at the decision point
    in the he_was_drunk function. Prints the next part of the story and brings 
    the user to the next decision point.
    """
    print("'He certainly seemed drunk to me,' I say.\n"
    "'So the report is incorrect?' the officer asks.\n"
    "'It could be,' I reply.\n"
    "The officer smiles. 'Then what happened?'\n")
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
    print("'He smashed the wine glass and threatened me with a large piece,'\n"
    "I say. 'I tried to leave, but he stood between me and the door. I begged\n"
    "him to let me go and he just... attacked me,' I say.\n"
    "'And then?' the officer asks.\n"
    "'I don't remember,' I say.\n")
    options = {
        1: 'Listen to the officer.',
        2: listen_to_officer_2
    }
    go_to_next_step(options)


def listen_to_officer_1():
    """
    Runs when the user selects '1. Listen to the officer.' at the decision point
    in the we_argued function. Prints the next part of the story and brings 
    the user to the next decision point.
    """
    print("'Look, Lydia,' the officer says. 'Charges are going to be made.'\n"
    "I nod, close to tears.\n"
    f"'Interview closing at {time}. Suspect is detained and awaiting charges,'\n"
    "the officer says.\n")
    options = {
        1: 'View charges.',
        2: view_charges_1
    }
    go_to_next_step(options)


def listen_to_officer_2():
    """
    Runs when the user selects '1. Listen to the officer.' at the decision point
    in the he_attacked_me function. Prints the next part of the story and brings 
    the user to the next decision point.
    """
    print("'Lydia, what you\’ve shared with us today has been nothing short of\n"
    "preposterous,' the officer says. 'First you said you were trying to hurt\n"
    "yourself, then you said he was drunk - even questioning the toxicology\n"
    "report. Next, your husband was attacking you with a broken wine glass,'\n"
    "despite the fact that you were the one drinking from it,' he continues.\n"
    "'Charges are going to be made and you\’ve made things much worse for\n"
    "yourself. Officer Anderson will return you to your cell.'\n"
    f"'Interview closing at {time}. Suspect is detained and awaiting charges,'\n"
    "the officer says.\n")
    options = {
        1: 'View charges.',
        2: view_charges_2
    }
    go_to_next_step(options)


def view_charges_1():
    """
    Runs when the user selects '1. View charges.' at the decision point
    in the listen_to_officer_1 function. Removes the 'Reason for arrest' key and
    its value from the lydia dictionary and adds a new key and value. Triggers
    the lydias_file function, which will display the information to the user.
    """
    lydia.popitem('Reason for Arrest')
    lydia.update({'Charges': 'Manslaughter'})
    lydias_file()


def view_charges_2():
    """
    Runs when the user selects '1. View charges.' at the decision point
    in the listen_to_officer_2 function. Removes the 'Reason for arrest' key and
    its value from the lydia dictionary and adds a new key and value. Triggers
    the lydias_file function, which will display the information to the user.
    """
    lydia.pop('Reason for Arrest')
    lydia.update({'Charges': 'Murder'})
    lydias_file()