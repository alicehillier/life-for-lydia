from chapter1 import error_statements, getpass, make_decision
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
    for key, value in lydia.items():
        print(f"\n{key}: {value}")

def simons_file():
    for key, value in simon.items():
        print(f"\n{key}: {value}")

date = datetime.now()
today = date.strftime("%A, %B %d, %Y")
time_now = datetime.now().time()
time = time_now.strftime("%H:%M")

def chapter2():
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
    print("'I was trying to hurt myself. He just... got in the way,' I say.\n"
    "'And how many times did he get in the way?'' the officer asks.\n"
    "'See, his body had multiple stab wounds. Did you accidentally stab\n"
    "him six or seven times?'\n")
    fourth_decision()

def self_defence():
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

def fourth_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("1. He was drunk.\n")
    while True:
        decide = getpass.getpass(prompt = "Enter 1.\n")
        try:
            if int(decide) == 1:
                he_was_drunk()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def he_was_drunk():
    print("'He seemed to be inebriated,' I say.\n"
    "'He was drunk?' the officer asks.\n"
    "I nod. 'He\'s a different person when he\'s drunk,' I say.\n"
    "'In what way?' he asks.\n"
    "'He can be unpredictable. Scary, even,' I say.\n"
    "'I see… It\'s interesting you say that, Lydia,' he says, 'because the\n"
    "toxicology report showed no trace of alcohol, or anything else.'\n")
    eighth_question()

def he_was_aggressive():
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

def he_was_not_drunk():
    print("'Why would you confront a man who you say is aggressive towards you?'\n"
    "the officer asks.\n"
    "'I didn\’t know it would be this bad,' I say.\n"
    "The officer sighs. 'Let\’s get to the point,' he says.\n")
    seventh_question()

def seventh_question():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("1. We argued.\n")
    while True:
        decide = getpass.getpass(prompt = "Enter 1.\n")
        try:
            if int(decide) == 1:
                we_argued()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def eighth_question():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("1. Question the findings.\n")
    while True:
        decide = getpass.getpass(prompt = "Enter 1.\n")
        try:
            if int(decide) == 1:
                question_findings()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def we_argued():
    print("'I was having a drink and packing my bag when he came home,' I say.\n"
    "'I was just going to stay with my sister for a while.\n"
    "He came home and found me upstairs. I told him what I knew and we argued.'\n"
    "'And then?' The officer asks.\n"
    "'He got mad. I got scared,' I continue.\n"
    "'He lunged at me and I dropped the wine glass. It smashed. I stepped back\n"
    "when he got close to me and I tripped on something. I saw the broken glass\n"
    "and I just… I thought he was going to hurt me. I\’d never seen him look\n"
    "like that before.'\n")
    tenth_question()

def question_findings():
    print("'He certainly seemed drunk to me,' I say.\n"
    "'So the report is incorrect?' the officer asks.\n"
    "'It could be,' I reply.\n"
    "The officer smiles. 'Then what happened?'\n")
    ninth_question()

def ninth_question():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("1. He attacked me.\n")
    while True:
        decide = getpass.getpass(prompt = "Enter 1.\n")
        try:
            if int(decide) == 1:
                he_attacked_me()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def he_attacked_me():
    print("'He smashed the wine glass and threatened me with a large piece,'\n"
    "I say. 'I tried to leave, but he stood between me and the door. I begged\n"
    "him to let me go and he just... attacked me,' I say.\n"
    "'And then?' the officer asks.\n"
    "'I don't remember,' I say.\n")
    eleventh_question()

def tenth_question():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("1. Listen to the officer.\n")
    while True:
        decide = getpass.getpass(prompt = "Enter 1.\n")
        try:
            if int(decide) == 1:
                listen_to_officer_1()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def eleventh_question():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("1. Listen to the officer.\n")
    while True:
        decide = getpass.getpass(prompt = "Enter 1.\n")
        try:
            if int(decide) == 1:
                listen_to_officer_2()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def listen_to_officer_1():
    print("'Look, Lydia,' the officer says. 'Charges are going to be made.'\n"
    "I nod, close to tears.\n"
    f"'Interview closing at {time}. Suspect is detained and awaiting charges,'\n"
    "the officer says.\n")
    twelfth_question()

def listen_to_officer_2():
    print("'Lydia, what you\’ve shared with us today has been nothing short of\n"
    "preposterous,' the officer says. 'First you said you were trying to hurt\n"
    "yourself, then you said he was drunk - even questioning the toxicology\n"
    "report. Next, your husband was attacking you with a broken wine glass,'\n"
    "despite the fact that you were the one drinking from it,' he continues.\n"
    "'Charges are going to be made and you\’ve made things much worse for\n"
    "yourself. Officer Anderson will return you to your cell.'\n"
    f"'Interview closing at {time}. Suspect is detained and awaiting charges,'\n"
    "the officer says.\n")
    thirteenth_question()

def twelfth_question():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("1. View Charges.\n")
    while True:
        decide = getpass.getpass(prompt = "Enter 1.\n")
        try:
            if int(decide) == 1:
                view_charges_1()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def thirteenth_question():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("1. View Charges.\n")
    while True:
        decide = getpass.getpass(prompt = "Enter 1.\n")
        try:
            if int(decide) == 1:
                view_charges_2()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue
    
def view_charges_1():
    lydia.popitem('Reason for Arrest')
    lydia.update({'Charges': 'Manslaughter'})
    lydias_file()

def view_charges_2():
    lydia.pop('Reason for Arrest')
    lydia.update({'Charges': 'Murder'})
    lydias_file()