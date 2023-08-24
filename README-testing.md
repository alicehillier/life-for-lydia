# **Life for Lydia - Testing**

[Go back to the README index](https://github.com/alicehillier/life-for-lydia#life-for-lydia)

[Go back to the Testing section of the README](https://github.com/alicehillier/life-for-lydia#testing)

[Visit my website here](https://life-for-lydia-bf0c0403fae6.herokuapp.com/)

## **User Stories**

### **First-Time Visitor Goal**

1. I want to learn how to to play the game/interact with the story.
  - Instructions are provided in the introduction section of the app.   

2. I want to be able to quit.
  - The instructions state that the user can return to the main menu by entering '0' at any decision point. 

3. I want to make decisions.
  - Decisions are integral to the interactive story and the user is required to make decisions in order to move forward in the story.

4. I want the text to presented to me clearly.
  - Dictionaries and current time/date are formatted so that information is displayed in standard text. This ensures that the flow of the story is not interrupted and the user is not confused by the presentation.

### **Returning Visitor Goal**

1. I want to select the next chapter.
  - The user is able to select which chapter they would like to read, so they are not forced to start from the beginning every time they visit the app. If the user is reading chapter one, they have the option to read chapter two once they reach the end of the chapter. The user can also return to the main menu at any decision point and select a different chapter.

2. I want to replay the story and make different choices.
  - A variety of choices are available to the user throughout both chapters. Making different decisions may alter the outcome of the story or provide the user with more information. Therefore, replaying the story can give the user a fuller experience.

3. I want to see the consequences of my decisions.
  - The outcome of the story may be altered by the decisions the user makes. For example, in chapter two, the character faces different charges depending on the decisions made by the user. 

### **Frequent Visitor Goal**

1. I want to experience all of the possible outcomes.
  - As there are several decision points in each chapter, the user can explore different options when they replay the story. While alternate outcomes are currently limited, future chapters could be greatly influenced by the decisions made by the user early in the story.

2. I want to find out new information by making a different choice.
  - Making certain decisions in the story may reveal new information to the user or affect the story. For example, in chapter one, the user will only know there is blood on the stair bannister if they choose not to open the door. While this may not necessarily affect the outcome of the story, it gives it more depth and allows the user a greater insight into what has happened. 

## **Validation: PEP8 Linter Results**

All code passed the validation process. 

[PEP8 Linter Results](/documents/images/readme-testing-linter-results.png)

## **User Testing**

1. User feedback suggested that the instructions in the introduction weren't clear enough, as it was only mentioned that the number keys were needed. In fact, the    
  user is required to type a valid number and then press the 'enter' key. 
  - As a result of this feedback, I updated the instructions paragraph in the introduction function, providing more clarity and a better user experience.

2. User feedback highlighted minor errors where I hadn't updated the variable name from "time" to "time_now" in the second instance. This caused an issue as I had also imported the time module.
  - I checked both functions where I had called the variable and saw that I had updated the variable name in the first instance, but not the second. Once I changed the variable name accordingly, there was no longer an issue.

3. User feedback highlighted an error in one of the final functions of chapter two, view_charges_2. This prevented the user from viewing the content as an error was thrown. 
  - I reviewed the error message and saw that I had given an argument to popitem(). I checked my code in view_charges_1 and saw that I had correctly used the method pop('Reason for Arrest'), but did not do the same for view_charges_2. I changed the method to the same as the one I used in view_charges_1 and the issue no longer persisted, allowing the user to finish the chapter without issues.

4. 
  -

## **Further Testing**