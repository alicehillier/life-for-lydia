# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def start():
    print("The winter is colder than usual. We haven’t had snow in years, but now it envelops everything in sight.")
    print("The birds are long gone, and even the rats that swarmed the street in summer are either in hiding or dead.")
    print("Webs of ice have gathered on the windows and I can barely make out the shapes of cars under snowy rubble.")
    print("I’m tired, but I know it must be done today.\n")
    first_decision()
    
def first_decision():
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
    print('option 1')
    
def delay_it():
    print('option 2')

start()