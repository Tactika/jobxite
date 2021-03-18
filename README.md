# JobXite

## Project Name:

  [JobXite.com](http://www.jobxite.com)
  <br>
  JobXite App

## Project Overview:

JobXite empowers the users to have equipment rental reservations within reach of anyone with internet access, no matter if you are a homeowner or superintendent on a commercial building site.
The project will be built with the following technologies:

-	HTML
-	CSS
-	JavaScript
-	Python
-	VueJS
-	Django

## Features:

JobXite will have the following features:

- As a user I want to be able to browse through categories of equipment based on type, so I can find applicable 
  products for my project.
  - **Tasks**
    - Create site structure and style user interface (HTML/CSS)
    - Implement sorting feature based on equipment type
    - Create/Source equipment database with the following data:
        - Make/Model
        - Description
        - Prices per-hour/day/week/month
        - Images
        - Equipment Type
        - Tags (Keywords)
        - Quantity
        - Associated delivery fee

---

- As a renter, I want to be able to schedule my rentals online, so I can check the pricing and availability from 
  anywhere.
  - **Tasks**
    - Create quote form
    - Source a shared Calendar API (Google, Office, etc.)
    - Ensure rental equipment are removed from available quantity

---

-	As the app owner I want pricing and availability to only be visible after a user logs in, so I can associate rentals with specific customers.
     - **Tasks**
        - Create a login and registration pages
        - Create views for registered and anonymous users
        - Implement a user authentication API (Django, Auth0, etc.)

---

-	As a user I want to be able to add items to a shopping cart, so I can potentially rent multiple items at a time.
     - **Tasks**
        - Add a button for users to click to push items to their cart (if logged in)
        - Implement a shopping cart that stores items the user selects
---
-	As the app owner, I want to be able to have different pricing plans so premium/account customers show their correct discounts.
     - Tasks
        - Create user groups with different pricing 

---

-	As the app owner, I want to have a payment system implemented, so I can have customers pre-pay for rentals to secure their equipment rental.
     - **Tasks**
        - Implement Payment Processing (i.e., Stripe)
        - Source and implement a pdf invoicing system.

---

-	As a site admin, I want to be able to add and remove equipment listings, so I can ensure any bought or sold equipment can be as needed.
     - **Tasks**
        - Create equipment moderator profile with modification privileges
        - Create a page to allow a moderator to update available quantity as items are returned.

--- 

-	As a renter I want to be able to see equipment based on tagged keywords, so I can use associated project types with the equipment I may need.
     - **Tasks**
        - Create gallery view, showing only applicable tagged items
        - Implement search function to be able to show items based on keywords in the equipment database

---

-	As a renter I want to be able to see my upcoming and previous rentals, so I can potentially request the same equipment as a previous rent or make modification to my upcoming rents.
     - **Tasks**
        - Create a CRUD interface for users
        - Store previous transactions associate with the logged-in user

---

-	As a renter I want to be able to select an item for delivery or an option to pickup in-store, so I can have the 
     ability to pickup the equipment if I have the capability.
     - **Tasks**
        - Implement forms for users to set up rentals with an option to pickup or have item delivered.
        - Use Map API to calculate distance from delivery address to store and charge applicable delivery fee.


## General Tasks:

- [X]	Obtain domain name ‘JobXite.com’
- [X]	Create GitHub repository
- [X]   Detail project on README.md
- [X]	Submit proposal to Evan for review

## Timeline:
-	**Week 1:**
     -  Create base Vue & Django App 
     - Create equipment database (Django Sqlite)
     -  Create basic equipment list view
     - Create basic equipment detail view

-	**Week 2:**
     -  Create Login & Registration Pages
     - Create user groups
        - Standard user
        - Moderator 
     -  Implement keyword sorting 
     -  Create quote form layout

-	**Week 3:**
     -  Create CRUD User Profile page 
     -  Implement shopping cart feature 
        - Add delivery option if time permits

-	**Week 4:**
     -  Fine tune UX/UI 
     -  Ensure all basic features work 
     -  Clean-up code
     -  Deploy the app online
     -  Prepare for presentation

-	**Future Iterations:**
     
     -  Implement PDF invoices
     -  Implement Payment Processing 
     -  Create own Equipment API 
     -  Add additional user groups
        - Premium User (Invoiced Bills)
          - User credit card will not be charged on checkout 
          - The billed invoice will be emailed to customer email 
        - Associated Business Accounts
          - Accounts linked to one main account (i.e., Superintendent, Accounting, Foreman, etc.)

    
##