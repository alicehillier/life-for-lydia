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
    print("explain")

def say_nothing():
    print("say nothing")