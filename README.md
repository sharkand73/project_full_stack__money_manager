# Numus - an app to manage your spending

Numus is an app in which you log your spending transactions.  You can create "merchants", categories (known as "tags") and "budgets", and obtain reports on your spending habits.

# Index
* Setup
* What is it?
* The brief
* Planning

# Setup
You will need to have postgreSQL and flask installed.

*1. From the money_manager directory, type:

      #psql -d money_manager -f db/money_manager.sql
      
    to create the database and initiate the tables.

*2. From the same directory, then type:
      
      #flask run
      
*3. Open a browser window with the address 

      #http://localhost:5000/ 

  The app should now be available to use.


# What is it?
"Numus" is the result of a solo Python project.  The app allows you to view, create, edit and delete spending transactions, which consist of a date, a merchant, 
a tag (spending category), and an amount (£).  These transactions are stored in the relational database.  In order to get full use of their data, the user can create 
"budgets" - spending periods with an associated spending limit.  

Budgets can be viewed at three levels: 

*Basic - the dates, the spending limit, and whether the user is over or under budget (budgets that are overspent are coloured red).
*Transaction - all the transactions pertaining to a budget can be viewed.
*Breakdown - the budget is broken down into spending by merchant and spending by tag.

After the project end, a "plug-in" was added which allows the user to import an entire bank statement from a Santander bank account, providing the transactions have been saved in Santander's text format.
This part of the app is a prototype and a work in progress.  Ultimately, it would be good to offer a similar plug-in for a few of the big banks.
                    

# The brief
The brief was to create an app that tracks the user's spending.  As an extension, budgets could be set and viewed, and spending breakdowns could also be requested.  

The tech stack is:
* PostgreSQL
* Python 
* Django
* HTML
* CSS

# Planning
Class diagrams were drawn, along with pencil-sketch wireframes corresponding to the RESTful routes.  The app was completed in six days.

# END
