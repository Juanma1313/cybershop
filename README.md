![Cybershop logo](static/cybershop_logo_025.png)
THIS PROJECT STILL UDER DEVELOPMENT

# CYBERSHOP

Cybershop is an online shop specifically customized for a retailer who has a business offering items for sale aimed at makers, tinkerers and students of technologies related to robotics, 3D printing, Computer Vision and other emerging technology areas.

On this website a customer will be able to view and purchase the products offered by the retailer, share information about their own ideas and projects related to these products, and search for information about technologies.

## Features 
This project defines an E-Commerce platform based on the Django framework, where the following features are offered:

- Base page
    > This page will be the frame for all the rest of pages
    * Contains a Navigation Bar on the top (The Main Menu).
    * Contais the placeholder for any of the rest of the pages
    * Contains a footer with company and contact information at the bottom.

- The Main menu
    * This is a base top bar menu that brings access to all the rest of the pages
    * There is a language, country and currency selector (Future feature)
    * There is a search feature where the user can search the shop's product inventory.
    * Direct access to the products page to start shopping 
    * Displays current user and ofers the user submenu options
        - If the user is signed in
            * User profile
            * End session
        - if not signed in
            * Sign in
            * register
            * End session
    * Direct Shopping Cart access
    * Direct Checkout and payment access
    * Direct access to the site Blog

- The `Home` page :  
    * It offers tech news and special deals that the user may find interesting.
    * A quick search tool is available to browse the shop's product inventory.

- The `About Us` page:  
    * Displays information about the company
    * Contains a footer with company and contact information.

- The `Sign up` page:
    * Allows a user to register with the server for future visits.
    * verify registration using e-mail validation

- The `user profile` page
    * Displays an updatable form wuth Customer specific information
        Name, delivery Address, billing Address, payment form, etc
    * Displays the list of orders placed by the user and their status.
    * Allows to review any order

- The `products` page:
    * Presents a search and filter options to find the products by specific clasifications
    * A list of products available for sale is presented with photo and price.

- The `Product detail` page
    * Displays the specific product with details
    * Allows to add the product to the shopping cart

- The `Shopping cart` page
    * Displays the list of products in the shopping cart
    * Displays individual and total costs
    * Allows to place and order with specified products form the shopping cart

- The `Order` page
    * Displays the list of products in the order
    * Displays individual and total costs
    * Inputs delivery information
    * Inputs payment information
    * Allows to place and order using a payment processing platform (Stripe) 

- The `Support` page
    * list of supported products with links to their specific tech documments.

- The `Comunity` 
    * list of news, events and the company related information

- The `Blog` Page:
    * Presents a standard blog for posting articles, information and comments 


## User Stories
### Viewing and Navigation
* [ ] `View products list` : AS A **Shopper** I can **View a list of products** So that **I canSelect some to buy**
* [ ] `View product details` : AS A **Shopper** I can **View the details of each product** So that **I canIdentify the price, description, product rating, product image and sizes available.**
* [ ] `Identify offers` : AS A **Shopper** I can **Quickly identify offers, clearance items and special offers ** So that **I canTake advantage of special savings on products I would like to buy**
* [ ] `View Purchase total` : AS A **Shopper** I can **Easily see the total of my purchases at any time** So that **I canAvoid overspending**

### Registration and User Acco
* [ ] `Register account ` : AS A **Site User** I can **Easily register an account ** So that **I canHave a personal account and be able to view my profile**
* [ ] `Log in & out` : AS A **Site User** I can **Easily log in or log out** So that **I canAccess my personal account information**
* [ ] `Restore password` : AS A **Site User** I can **Easily retrieve my password if I forget it** So that **I canRegain access to my account**
* [ ] `Validate registration` : AS A **Site User** I can **Receive a confirmation email after registration** So that **I canVerify that my account registration has been completed successfully **
* [ ] `User profile` : AS A **Site User** I can **Have a personalised user profile** So that **I canView my personal order history and order confirmations, and save my payment information**

### Sorting and Searching
* [ ] `Sort Product list` : AS A **Shopper** I can **Sort the list of available products** So that **I canEasily identify the best-rated, best-priced products sorted by category.**
* [ ] `Product category sorting` : AS A **Shopper** I can **Sort a specific product category** So that **I canFind the top-rated or most expensive product in a specific category, or sort products in that category by name.**
* [ ] `Simultaneous product categories sorting` : AS A **Shopper** I can **Sort several product categories at the same time** So that **I canSearch for top-rated or most expensive products in broad categories**
* [ ] `Search product` : AS A **Shopper** I can **Search for a product by name or description** So that **I canFind a specific product I would like to buy.**
* [ ] `View Search results` : AS A **Shopper** I can **Easily see what I have searched for and the number of results** So that **I canQuickly decide if the product I want is available.**

### Purchasing and Checkout
* [ ] `Select product` : AS A **Shopper** I can **Easily select the size and quantity of a product when buying it** So that **I canMake sure I don't accidentally choose the wrong product, quantity or size.**
* [ ] `View shopping cart` : AS A **Shopper** I can **View the items I have in my bag for purchase** So that **I canIdentify the total cost of my purchase and all the items I will receive.**
* [ ] `Change data in shopping cart` : AS A **Shopper** I can **Adjust the quantity of individual items in my bag ** So that **I canEasily modify my purchase before checking out.**
* [ ] `Payment details` : AS A **Shopper** I can **Easily enter my payment details** So that **I canCheckout quickly and smoothly**
* [ ] `Payment information` : AS A **Shopper** I can **Feel that my personal and payment information is safe and secure** So that **I canConfidently provide the information needed to make a purchase**
* [ ] `Order confirmation Insitu` : AS A **Shopper** I can **See order confirmation after checkout** So that **I canCheck that I have not made any mistakes**
* [ ] `Order confirmation by e-mail` : AS A **Shopper** I can **Receive a confirmation email after placing my order** So that **I canKeep confirmation of what I have purchased for my records.**

### Admin and Store Management
* [ ] `Add product` : AS A **Store Owner** I can **Add a product** So that **I canAdd new items to my shop**
* [ ] `Edit/update product` : AS A **Store Owner** I can **Edit/update a product** So that **I canChange prices, descriptions, images and other product criteria**
* [ ] `Delete product` : AS A **Store Owner** I can **Delete a product** So that **I canRemove items that are no longer for sale**

### Blog 
- [ ] `View post list`:   As a **Site User** I can **view a paginated list of posts** so that I can select one to read
- [ ] `Open a post`:      As a **Site User** I can **click on a post** so that **I can read the full text**
- [ ] `View likes`:       As a **Site User / Admin** I can **view the number of likes on each post** so that **I can see which is the most popular or viral**
- [ ] `View comments`:    As a **Site User / Admin** I can **view comments on an individual post** so that **I can read the conversation**
- [ ] `Comment on a post`: As a **Site User** I can **leave comments on a post** so that **I can be involved in the conversation**
- [ ] `Like / Unlike`:    As a **Site User** I can **like or unlike a post** so that **I can interact with the content**
- [ ] `Manage posts`:     As a **Site Admin** I can **create, read, update and delete posts** so that **I can manage my blog content**
- [ ] `Create drafts`:    As a **Site Admin** I can **create draft posts** so that **I can finish writing the content later**
- [ ] `Approve comments`: As a **Site Admin** I can **approve or disapprove comments** so that **I can filter out objectionable comments**

## Implemented Features

- __Navigation Bar__

  - Featured on all pages, the full responsive navigation bar includes links to the Logo, Home page, About Us  and Sign Up page, and is identical in each page to allow for easy navigation.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

![Nav Bar](doc/screenshots/navigation-bar.png)

- __The Content menu__

  - The content menú provides a way for the user to directly access to all the pages web site .
  
![Content menu](doc/screenshots/content-menu.png)

- __The Footer__ 

    - The footer section includes:
      * links to the relevant social media sites. The links will open to a new tab to allow easy navigation for the user. 
      * Name, phone number and email information for the company
      * Web site developer contact information
      
  - The footer is valuable to the user as it encourages them to keep connected via social media

![Footer](doc/screenshots/footer.png)

- __About Us Page__

  - This page will provide the user with information over the company.
  - This section is valuable to the user to identify the type of company and people behind the service. 

![About Us](doc/screenshots/about-us.png)

- __The Sign Up Page__

  - This page will allow the user to register in the web site and aloww for a more personalized experience. A profile will be created with personal, orders, delivery and billing information so the user will not need to retype it on future visits.
  - The user will be asked for a username, password, full name and email address which will be used to validate the registration. 

![Sign Up](doc/screenshots/sign-up.png)


## Features Left to Implement

## The database models

### User information
This model provides persistent support for user information. Since there are different user roles, a scheme of roles. Permissions and authorizations must be established.
Since "Django-allauth" is used as a framework, the base database model is already defined, and we have simply extended it to adapt it to the needs of this project using the object/table `auth_user` as link.


### Orders information
This model is subdivided in three submodels, first one defines the objects and storage for the  `user profiles`, the seccond defines the objects and storage for the `products`, and the third one defines the objects and storage for `purchase orders`.

![Orders model](doc/database/cybershop-orders-ERD.png)

### Blog Information

![Blog model](doc/database/cybershop-blog-ERD.png)

## Testing 

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https://8000-juanma1313-cybershop-70agewrxojr.ws-us106.gitpod.io/)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https://8000-juanma1313-cybershop-70agewrxojr.ws-us106.gitpod.io&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

### Testing on diferent device resolutions 
- Desktops (width screen resolution from 4k down to 1024)
  - All pages
  - Landing Page
  - About Us Page
  - Sign Up Page
  
- Tablets & big moviles (width screen resolution between 1024 and 768 horizontal  pixels )
  - All pages
  - Landing Page
  - About Us Page
  - Sign Up Page

- Tablets & big moviles (width screen resolution smaller than 768 horizontal pixels )
  - All pages
  - Landing Page
  - About Us Page
  - Sign Up Page

### Unfixed Bugs

  
## Deployment

- The site was deployed to HEROKU. The steps to deploy are as follows: 

The live link can be found here - https://juanma1313.github.io/cybershop/index.html

## Credits 

### Content 

- base.html Implement was addapted from the CI Boutique_Ado project
- Models for database objects `user preferences`, `products`, `orders` and `blog` are borrowed from CI Boutique_Ado and CI Django_Blog projects.

### Media
- All `static/` and `media/` files are created and designed by Juan Manuel de las Heras

