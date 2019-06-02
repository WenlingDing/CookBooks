My project: Cookbooks
====

UX
--
my entity relationship diagram is in todo_mysql/entityRalationship.png.
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.
In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

For this project, the goal is to provide an easy to use recipe repository website for users to view and contribute recipes. The target users of my website will be those who are looking for a particular recipe or simply browsing for an interesting receipe to cook.

There are 3 key features for this project

Feature 1 - Search recipe
Feature 2 - View recipe
Feature 3 - Maintain recipe

Feature 1 - Search recipe
As a user, I want to see all available recipes in the website so that I can view all recipes 
As a user, I want to be able to search the recipes by country or cusine so that I can narrow down the recipe I am looking for
As a user, I want to be able to view receipes in order of recipe name,  author, cusine or date so that I can have an ordered view

Feature 2 - View recipe
As a user, I want to be able to select and view a recipe in a single page so that I can see more information about the recipe

Feature 3- Maintain recipe
As a user, I want to be able to add new recipe in the website so that I can contribute to the website
As a user, I want to edit a recipe so that I can update the recipe
As a user, I want to be able to delete a recipe so that I can remove an outdated recipe 

Features
--
Existing Features
---
Feature 1 - Search recipe
The design is focus on simplicity yet fully functional to achieve the goal of the project.
For the home page, I decided to display all available recipes along with a short introduction and key attributes of a recipe for eg. type of cusine i.e "Italian"to showcase the recipe library and to immediately draw the interest of a user. There is also a simple to use search function right at the top along with filters and order mechanism to allow a user to find the recipe he/she desire conveniently 

Feature 2 - View recipe
If the user has interest in a recipe, he/she can click view more to see the ingredients and process to make the recipe. Through this design, i hope to interact with user to not only search a recipe he/she have in mind but to explore what other recipe options the website can offer to encourage repeat visits.

Feature 3- Maintain recipe
For the maintenance of recipe, I provide 3 main functions to do so:
1. Add recipe - A  user can add recipe through a form and submit to the website
2. Edit recipe - A user can make changes to the recipe to update it where necessary
3. Delete recipe - A user can delete an outdated recipe


Features Left to Implement
---
1. Upload photos function - For recipe
2. Enhance the search function to have an advanced search filter 
3. Need to change add page and edit page style to materialize 0.100.2(Now I used bootstrap because when used materialize some buttons cannot work, I am not familiar with materialize and failed to fix it)

Technologies Used<br>
HTML 5<br>
CSS 3<br>
Javascript<br>
jquery 3.3.1<br>
python3<br>
phpmyadmin<br>
flask<br>
materialize 0.100.2<br>
bootstrap 3.3.0<br>

Testing
---
I tested the HTML and CSS By Chrome Developer Tools to ensure that it displays correctly at all screen sizes.

HOME PAGE<br>
I tested by loading the page and check the page display all the recipes from the database.<br>

To test the functions of search, order, delete and edit, I have to test the "Add" function first to ensure there is a good representation of recipes in the database to test the function.<br>

I test the search functions:<br>
1. By name - search function work by searching recipe name that matches the character(s) inputted
2. By country - search function work by retrieving all recipes made by an author of a country
3. By cuisine - search function work by retrieving all receipes made by the cuisine country


I test the order functions:<br>
1. By name - order function displays recipe by name in descending order 
2. 
2. By author - order function display recipe by authors name in descending order
3. 
3. By cusine - order function display recipe by cusine name in descending order
4. 
4. By date - order function display recipe by date added from earliest to latest 

I test the delete function:<br>

1. I click "Delete" for a recipe, and it was succesfully deleted from the database. 

I test the edit function:<br>
1. I click "Edit" for a recipe, and i was brought to the edit page to edit the recipe.
2. On "Edit" page, the page retrieve the recipe so i can make updates while referencing the current information. Upon save, the changes are updated into database and i can see from the home page its successfully updated
3. I tried to submit with an empty value but was not able to.


I test the add functions<br>

1. I tested the add page can work by adding a recipe. 
2. The add function is tested by first trying a sucessful test case whereby all fields are entered with a value.
3.I then tested a negative test case where i attempt to submit when any of the fields are not entered with a value. I was unable to do so and a error message to indicate the mandatory was displayed.
4. Finally I test the UI by adding a row in the instruction page and then deleting the row before submitting it. I check to see the deleted row was not saved in the database.

Deployment
---
GitHub:https://github.com/WenlingDing/CookBooks
Heroku:https://cookbooks-project.herokuapp.com/
Datebase : https://remotemysql.com/phpmyadmin/

Credits
--
Content

The text for recipe was copied from website https://www.allrecipes.com/recipes/


