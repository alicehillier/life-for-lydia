![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


# **Life for Lydia**

![*Life for Lydia* displayed on various devices]()

[Visit my website here](https://life-for-lydia-bf0c0403fae6.herokuapp.com/)

1. [Introduction](https://github.com/alicehillier/life-for-lydia/#introduction)

2. [UX Design](https://github.com/alicehillier/life-for-lydia/#ux-design)

    i. [Strategy Plane](https://github.com/alicehillier/life-for-lydia/#strategy-plane)

    ii. [Scope Plane](https://github.com/alicehillier/life-for-lydia/#scope-plane)
    
    iii. [Structure Plane](https://github.com/alicehillier/life-for-lydia/#structure-plane)

    iv. [Skeleton Plane/Wireframes](https://github.com/alicehillier/life-for-lydia/#skeleton-plane)

    v. [Surface Plane](https://github.com/alicehillier/life-for-lydia/#surface-plane)

3. [Features](https://github.com/alicehillier/life-for-lydia/#features)

    i. [Existing Features](https://github.com/alicehillier/life-for-lydia/#existing-features)

    ii. [Features to be implemented in the future](https://github.com/alicehillier/life-for-lydia/#features-to-be-implemented-in-the-future)

4. [Technology Used](https://github.com/alicehillier/life-for-lydia/#technology-used)

    i. [Main Languages](https://github.com/alicehillier/life-for-lydia/#main-languages)

    ii. [Frameworks, Libraries and Programmes](https://github.com/alicehillier/life-for-lydia/#frameworks-libraries-and-programmes)

5. [Issues and Bugs](https://github.com/alicehillier/life-for-lydia/#issues-and-bugs)

6. [Deployment](https://github.com/alicehillier/life-for-lydia/#deployment)

7. [Testing](https://github.com/alicehillier/life-for-lydia/#testing)

8. [Credits](https://github.com/alicehillier/life-for-lydia/#credits)

9. [Acknowledgements](https://github.com/alicehillier/life-for-lydia/#acknowledgements)


## **Introduction**

Welcome to *Life for Lydia*, an interactive, terminal-based story powered by Python. Consisting of two chapters, the 
interactive story is designed for readers and gamers alike. Choose your own path and make important decisions
to discover more.

*Life for Lydia* is an interactive story made with Python, created by Alice Hillier for the third project in Code Institute’s Diploma in Software Development programme.

[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)

## **UX Design**

### **Strategy Plane**

In order to gauge what makes a successful interactive story, I drew on my own experience of reading books like
*Goosebumps* and playing games like the more recent editions of *Assassin's Creed* and *Telltale's The Walking Dead*.  

#### **[Goosebumps]**

![] 

-	Offered meaningful choices to the reader.
- Players turned to the page indicated based on their choice.

#### **[Assassin's Creed]**

![]

- Offered meaningful choices to the player.
- The main story remained the same, with alterations according to the players' choices.
- Making certain choices affected the character's relationships, revealed new information and impacted the lives of other characters.

#### **[The Walking Dead]**

- Offered meaningful choices to the player.
- The main story remained the same, with alterations according to the players' choices.
- Making certain choices affected the character's relationships and future opportunities.

![]

### **User Stories**

#### **First-Time Visitor Goal**

-	I want to learn how to to play the game/interact with the story.
- I want to be able to quit.
- I want to make decisions.
- I want the text to presented to me clearly.

#### **Returning Visitor Goal**

-	I want to select the next chapter.
- I want to replay the story and make different choices.
- I want to see the consequences of my decisions.

#### **Frequent Visitor Goal**

- I want to experience all of the possible outcomes.
- I want to find out new information by making a different choice.	

[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)

### **Scope Plane**

Based on the research conducted in the Strategy Plane, I decided to include the following features in the *Life for Lydia* interactive story:

-	A main menu, which includes the title, instructions about how to play and a contents menu.

I ensured that I met the following functionality requirements:

-	Each line of text fits within the terminal for optimal user experience.
- User inputs are responded to correctly.
- Errors caused by user input are dealt with appropriately.

[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)

### **Structure Plane**

The contents of the interactive story were carefully considered and selected for their relevance and usefulness to users.

The project itself is contained within one file, and sections are clearly labelled with a comment.
- **Imports**: At the top of the file, imports are described with their specific purpose in the program.
- **Important Functions**: Next, important functions that are key to the program's execution are defined.
- **Main Menu Content**: Following this is the main menu content, made up of the introduction and story_selector functions.
- **Chapter One**: After the main menu content, the code for Chapter One is laid out.
- **Chapter Two**: Finally, the code for Chapter Two is written beneath Chapter One.

[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)

### **Skeleton Plane**

When starting to design my story, I created detailed text documents using Google Docs and flow diagrams using Figma. 
To view the story written out using Google Docs, and the flow diagram I created with Figma , please click on the links below:
- [Text Document]()
- [Flow Diagrams]()

[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)

### **Surface Plane**

After establishing the content of the interactive story, I began putting together the aesthetics. 

- Dictionaries are formatted as clean text when displayed to the user.
- Time and dates are formatted in an easy-to-read way when displayed to the user.
- Ample spacing is provided throughout the program for clarity.
- A consistent decision format is used to ensure the experience is seamless for the user.

[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)

## **Features**

### **Existing Features**

1. An introduction section, containing the title and instructions.

2. A return-to-main-menu option, which is available at every decision point and returns
the user to the introduction section.

3. Two chapters, which fleshes out the story and provides the user with more opportunities
to engage.

4. Meaningful choices which allow the user to obtain more information about the story depending
on their decision.

### **Features to be implemented in the future**

The following features would be an excellent means of creating a fuller experience for the user:

1. More chapters

2. Long-term consequences of your decisions

3. The option to save your progress

[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)

## **Technology Used**

### **Main Languages**

- Python

### **Frameworks, Libraries and Programmes**

- Google Docs: I used this to write out the story.
- Figma: I used this to create detailed flow diagrams for the story.
- Visual Studio Code: I used this local editor to write and edit my code.
- Git: I committed and recorded my work using Git.
- Github: I stored my work on Github and recorded its development.

[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)

## **Issues and Bugs**

1. 

[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)

## **Deployment**

The project was developed using Visual Studio Code as the code editor, committed to Git as a local repository, and then pushed to GitHub for storage.

### **Deployment to Heroku**

The project was deployed to Heroku using the following steps:

1.


[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)

## **Testing**

[Click here to view all testing documentation](https://github.com/alicehillier/life-for-lydia/blob/main/README-testing.md)

## **Credits**

-

## **Acknowledgements**

- 

[Back to top](https://github.com/alicehillier/life-for-lydia/#life-for-lydia)