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
    print(f"'Interview with suspect, Lydia Simmons, {time}, {today}.'")
    print("'Officers present are Smith, badge 247800, and Anderson, badge 310010.'")
    print("'Lydia, is this information correct?'") 
    print("The officer opened his file at the first page and pointed to the information.")
    print(lydia)
    print("I nod.")
    print("'Any idea why you are here?'")