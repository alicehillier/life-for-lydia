from chapter1 import(error_statements, wrong_decision)
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

date = datetime.now()
today = date.strftime("%A, %B %d, %Y")
time_now = datetime.now().time()
time = time_now.strftime("%H:%M")

def chapter2():
    print("The officer dropped the file onto the desk and leant over to turn on the recorder.")
    print(f"'Interview with suspect, Lydia Simmons, at {time} on {today}.'")
    print("'Officers present are Smith, badge 247800, and Anderson, badge 310010.'")
    print("'Lydia, is this information correct?'") 
    print("The officer opened his file at the first page and pointed to the information.")
    print(lydia)
    print("I nod.")
    print("'Any idea why you are here?'")
    first_decision()

def first_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. Yes.\n2. No.\n')
        try:
            if int(decide) == 1:
                yes()
                break
            elif int(decide) == 2:
                no()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def yes():
    print("I nod slightly.\n 'Enlighten me,' he says.")
    print("'My husband,' I say.")
    print("The officer turns to the next page in the file and spins it around to show me.")
    print(simon)
    print("'Is this your husband, Lydia?' the officer asks.")
    print("'Yes,' I say.")
    print("'What happened with your husband?' he asks.")
    second_decision()

def no():
    print("I curl my lip, raise my eyebrows and stare at the table.")
    print("'Care to explain why you were covered in blood when we found you, or why you tried to flee?'")
    print("'Perhaps you would like to explain the situation in your bedroom?'")
    second_decision()

def second_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. Explain.\n2. Say nothing.\n')
        try:
            if int(decide) == 1:
                explain()
                break
            elif int(decide) == 2:
                say_nothing()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def explain():
    print("'I found out that he was having an affair,' I say.")
    print("'So you killed him?' the officer asks.")
    print("'No,' I say.")
    third_decision()

def say_nothing():
    print("'Given that we found your husband dead, with several stab wounds, in your bedroom...'")
    print("'and you were covered in blood and running away...'")
    print("'It looks bad for you,' the officer says.")
    third_decision()

def third_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. It was an accident.\n2. It was self-defence.\n')
        try:
            if int(decide) == 1:
                accident()
                break
            elif int(decide) == 2:
                self_defence()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def accident():
    print("'“'I was trying to hurt myself. He just…got in the way,' I say.")
    print("'And how many times did he get in the way?'”' the officer asks.")
    print("'See, his body had multiple stab wounds...' he continues")
    print("'Did you accidentally stab him six or seven times?'")
    fourth_decision()

def self_defence():
    print("'I told him that I knew he was having an affair,' I say. 'He was angry.'")
    print("'Why would he be angry at you for that?' the officer asks.")
    fifth_decision()

def fourth_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1.\n")
    while True:
        decide = input('1. He was drunk.\n')
        try:
            if int(decide) == 1:
                he_was_drunk()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def fifth_decision():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. He was aggressive.\n2. He was drunk.\n')
        try:
            if int(decide) == 1:
                he_was_aggressive()
                break
            elif int(decide) == 2:
                he_was_drunk()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def he_was_drunk():
    print("'He seemed to be inebriated,' I say.")
    print("'He was drunk?' the officer asks.")
    print("I nod. 'He\'s a different person when he\'s drunk,' I say.")
    print("'In what way?' he asks.")
    print("'He can be unpredictable. Scary, even,' I say.")
    print("'I see… It\'s interesting you say that, Lydia,' he says,")
    print("'because the toxicology report showed no trace of alcohol.'")
    print("'In fact, it found nothing at all,' he says.")
    eighth_question()

def he_was_aggressive():
    print("'He could be aggressive,' I say.")
    print("'He could be, or he was?' the officer asks.")
    print("'He was. He was controlling and he didn\’t have control this time,' I say.")
    print("'Was he drunk?' he asks.")
    sixth_question()

def sixth_question():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1 or 2.\n")
    while True:
        decide = input('1. He was drunk.\n2. He might not have been drunk.\n')
        try:
            if int(decide) == 1:
                he_was_drunk()
                break
            elif int(decide) == 2:
                he_was_not_drunk()
                break
            else:
                raise ValueError
        except ValueError:
            error_statements(decide)
            continue

def he_was_not_drunk():
    print("'Why would you confront a man who you say is aggressive towards you?' the officer asks.")
    print("'I didn\’t know it would be this bad,' I say.")
    print("The officer sighs. 'Let\’s get to the point,' he says.")
    seventh_question()

def seventh_question():
    """
    Processes the user's input, calling the relevant function in accordance with the user's selection.
    Raises ValueError if the user enters an invalid value and loops the input requirement until the value
    is considered valid.
    """
    print("Enter 1.\n")
    while True:
        decide = input('1. We argued.\n')
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
    print("Enter 1.\n")
    while True:
        decide = input('1. Question the findings.\n')
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
    print("'I was having a drink and packing my bag when he came home,' I say.")
    print("'I was just going to stay with my sister for a while.'")
    print("'He came home and found me upstairs. I told him what I knew and we argued,' I say.")
    print("'And then?' The officer asks.")
    print("'He got mad. I got scared,' I continue.")
    print("'He lunged at me and I dropped the wine glass. It smashed.'")
    print("'I stepped back when he got close to me and I tripped on something.'")
    print("'I saw the broken glass and I just… I thought he was going to hurt me.'")
    print("'I\’d never seen him look like that before.'")

def question_findings():
    print("'He certainly seemed drunk to me,' I say.")
    print("'So the report is incorrect?' the officer asks.")
    print("'It could be,' I say.")
    print("The officer smiles. 'Then what happened?'")