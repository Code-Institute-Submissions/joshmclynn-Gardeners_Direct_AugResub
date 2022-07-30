# Gardeners_Direct


Gardeners Direct is a landscaping and gardening business, It provides garden maintenance based on a 'size of garden' model in order to give potential customers a fair and reflective price in order to carry out works. 

## Business Model

Currently gardeners direct uses a standard pricing scheme based on 'hours worked' and 'guestimations'. The use of this website and booking system is to change their current business model and employ a more personal approach to quotes and pricing. Although the business is sometimes approached in person(on the street etc) the owner of the businnes will be directing them to this application in order for them to have a personal quote.

Free marketing strategies will be taken advantage of due to the size of the business, this will include Facebook business pages and a newsletter which is available to users who enter their email address on the site. 

Although there is a generally accepted method of quoting for gardening maintenance works through size, this is rarely implemented due to the impracticallities of it, this application will hopefully streamline this ability.

## Planning

User Stories (User)-
* As a user, I want to be able to easily navigate through the website.
* As a user, I want to be able to create custom pricing schemes for myself
* As a user, I want to be able to see additional products that might be available at the time of work being carried out.
* As a user, I want to be able to see the cost of the services I am receiving before payment.
* As a user, I want to be able to purchase these services securely
* As a user, I want to be able to store personal details about myself and my garden
* As a user, I want to be able to change personal details about myself and my garden
* As a user, I want to be able to log in and log out securely
* As a user, I want to be able to create an account
* As a user, I want to be able to delete an account

User Stories (Admin)-
* As an Admin, I want to be able to add products to the shop.
* As an Admin, I want to be able to remove products from the shop
* As an Admin, I want to be able to see users who have purchesed services
* As an Admin, I want to be able to delete users orders whom have been completed

## Features
### HomePage
The homepage allows users to navigate through the application, with certain restrictions based on whether the user is logged in etc. In the navigation bar are links to:
#### Non authenticated users:
* Sign-up
* Log-in
#### Authenticated users:
* My Profile
* My Quote
* Log-Out
#### Admin
* Management
* Log-Out
There is also an email field form to add an email address to recieve any newsletters that may be available.
### User Profile
The user profile page, allows users to enter their details including address and contact number, users are also able to enter the dimensions of their garden and select whether their garden has grass and or irrigation, this information is then used to create a unique quote for the user.
This page will also contain any current purchases
The quote is based on an average price for an average 14sqm garden this price is then used to create a unique quote based on the users garden size.
i.e 28sqm - 2 x price of 14 sqm
### Quote
This page will display the generated quote, it will also list other services that are available for purchase when the gardener visits their garden, these items are generally specialities so cannot be given as a guarenteed price without prior viewing of the space.
The user will then be asked if they would like to proceed where they will be directed towards the payment page.
### Checkout
This page will contain detail about the pricing of the service they are purchasing and a card input feature. The payment system is Stripe.
### Post checkout
Users will be directed after purchase to the checkout success page, this page will list the price they paid, the subscription number and a contact number should they require help with their purchase.
### Management(ADMIN ONLY)
This page allows admin users to add products to the quote page, showing users what other services are available post checkout.
This page also shows the admin any on going orders which will need to be completed.
The page also allows the admin to remove 'jobs' which have been completed.
## Ongoing Bug discovery and fixes
* Issue = Media File Storage AWS
  ** Solution = Media files not being uploaded to s3 bucket subsequently not allowing heroku to see the images, As of yet no fix found.
* Issue = Users able to make multiple purchases in one go
  ** Solution = Will need to implement a for loop to check current orders in the users profile.
* Issue = User address not saving to sub_user_detail model after payment.
  ** Solution = Will need to access UserProfile model with a signal to copy the users address when sub_user_detail object created.
  
## Testing
### Manual Testing
There was no automated testing for this project. Each User Story was manually tested below:

### User Stories
- As a user, I want to be able to easily navigate through the website.
  - Entered Sites URL
    - Displayed Correct Page
    - Pass
  - Clicked all Possible Links on pages
    - Never redirected to 404 page.
    - Pass
  - Entered all urls of given pages
    - No broken urls
    - Pass
- As a user, I want to be able to create custom pricing schemes for myself.
  - Entered Sites url
    - Pass
  - Entered multiple different widths and lengths into the profile page inputs
    - Was given different results in the quote everytime
  - Pass
- As a user, I want to be able to see additional products that might be available at the time of work being carried out.
  - On the quote page I was able to see different products and the 'price from' attribute.
  - Pass
- As a user, I want to be able to see the cost of the services I am receiving before payment.
  - The price I was going to be paying was displayed multiple times as I navigated towards the payment section, On /quote and on /checkout
  - Pass
- As a user, I want to be able to purchase these services securely.
  - Accesed checkout page
  - Filled in the card details section using stripes test card (4242 etc) and clicked on complete payment
    - was redirected to checkout/success
  - Accessed the Stripe Dashboard
    - Accessed the events log, was able to see the charge being created and succeeding.
    - webhooks in stripe dashboard(webhooks) displayed response code 200
    -PASS
- As a user, I want to be able to store personal details about myself and my garden & As a user, I want to be able to change personal details about myself and my garden
  - Accessed the 'my profile' page
  - Entered my personal information
  - clicked update profile
  - The page refreshed and I was able to see details I had entered
  - returned to the homepage then loaded my profile pages again.
  - Saved details were still available
  -PASS
- As a user, I want to be able to log in and log out securely.
  - Accessed Login page,
  - was able to enter user details to login successfully
  - navigate to logout page
  - was able to log out successfully
  - Handled by allauth
  -PASS
- As a user, I want to be able to create an account
  - Accesed Sign-Up page
  - Was asked to enter basic information
  - Was able to log out and then log back in using these details
  - PASS
- As a user, I want to be able to delete an account
  - When logged in
  - Accessed 'my profile' page
  - Was given the option to delete my account
  - Tried to log back in- unsuccessful
  - PASS
### User Stories(ADMIN)
- As an Admin, I want to be able to add products to the shop.
  - Whilst logged in as admin
  - Accessed Manage page
  - Was given the option to add products
  - These items were successfully loaded back onto the manage page as items
  - PASS
- As an Admin, I want to be able to remove products from the shop
  - Whilst logged in as admin
  - Accessed Manage page
  - Was given the option to delete products via a button located on the product card
  - When pressed these products were succesfully removed from the manage page and model
  - PASS
- As an Admin, I want to be able to see users who have purchesed services
  - Whilst logged in as admin
  - Accessed Manage page
  - Was able to see sub user details listed on the page
  - PASS
- As an Admin, I want to be able to delete users orders whom have been completed
  - Whilst logged in as admin
  - Accessed Manage page
  - Under sub users cards was a completed option, this button removed them from the interface and model
  - PASS
## Validation
  ### w3 plug-in VS-CODE
  All pages had no warning in the terminal in vscode.
  ### CSS(jigsaw)
 No Errors
  ### PEP8
  #### Admin-Products
  - admin.py PASS
  - forms.py PASS
  - models.py PASS
  - urls.py PASS
  - views.py PASS
  #### Calculator
  - admin.py PASS
  - forms.py PASS
  - models.py PASS
  - urls.py PASS
  - views.py PASS
  #### GardensDirect
  - urls.py PASS
  - views.py PASS
  #### main
  - forms.py PASS
  - models.py PASS
  - urls.py PASS
  - views.py PASS
  #### Profiles
  - forms.py PASS
  - models.py PASS
  - urls.py PASS
  - views.py PASS
## Web Marketing
### SEO
The goal of this site is to streamline the quoting process for he company gardeners direct. I used word tracker to generate key words connected with 'Garden maintenance personal quote'
The most common searches werent neccesarily related to the site due to quote having a few different meanings.
### Facebook
Below is a copy of the facebook mockup with links to the companys website and posts related to the occupation of the company.
### Newsletter
On the homepage there is an area to sign up for a newsletter, this model collates emails for the owner to access whenever there are any announcements etc
### Information Architecture
#### Data Storage
Admin_product - Products Model items:
- product : product = models.CharField(max_length=50, blank=True, null=False, unique=True)
- description : descriptions = models.CharField(max_length=250, blank=True, null=False)
- price = models.IntegerField()
- sale = models.BooleanField()

Calculator - Sub_user_details Model items:
- subscription_number = models.CharField(max_length=32, null=False, editable= False, unique=True)
- user = models.OneToOneField(User,on_delete=models.CASCADE)
- subscription_cost = models.FloatField(default=0)
- address = models.CharField(max_length=100,)
- paid = models.BooleanField(default=False,)

Main - Newsletter Model items:
- email = models.EmailField(max_length=50, unique=True)

Profile - UserProfile Model items:
- user = models.OneToOneField(User, on_delete=models.CASCADE)
- phoneNumber = models.CharField(max_length=20, null=True, blank=True)
- First_line_address = models.CharField(max_length=80, null=True, blank=True)
- Post_code = models.CharField(max_length=20, null=True, blank=True)
- garden_width = models.FloatField(default=0, blank=True)
- garden_length = models.FloatField(default=0, blank=True)
- irrigation = models.BooleanField(default=False)
- grass = models.BooleanField(default=False)
- quote = models.FloatField(default=0, editable=True, blank=True)

## Technologies Used

### Languages
- HTML5
- CSS
- JAVASCRIPT
- PYTHON
### Libraries
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [JQUERY](https://jquery.com/)
### Packages
- [Django](https://www.djangoproject.com/)
- [Allauth](https://django-allauth.readthedocs.io/en/latest/index.html)
- [CrispyForms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
- [SweetAlert2](https://sweetalert2.github.io/)
- [Stripe](http://stripe.com/)
### Storage
- [AWS S3](https://aws.amazon.com/s3/)
### Deployment
This project was produced on VScode and is deployed on [HEROKU](https://www.heroku.com/), The static and media files are stored on a AWS S3 bucket.
Below is how to set up on heroku:

1 - Set up a (or log into an existing) Heroku account.

2 - Select add new app and give it a unique name

3 - Select 'Resources' and search for/install the Heroku Postgres add-on.

4 - Select 'Settings' and click 'Reveal Convig Vars'

5 - You will find the DATABASE URL already added, copy this to the env.py file mentioned previously.

6 - You will need the following convig vars:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
SECRET_KEY = your secret key must match the secret key in your `env.py` file
EMAIL_HOST_USER = your chosen email account's address
EMAIL_HOST_PASS = your chosen emaiil account's password or dedicated access key
STRIPE_PUBLIC_KEY = which you will find from your strip dashboard
STRIPE_SECRET_KEY = which you will find from your strip dashboard
STRIPE_WH_SECRET = which you will find from your strip dashboard
USE_AWS = TRUE

Migrate and Run
Finally, all that remains is to makemigration by entering the following command:

python3 manage.py makemigrations
Then migrate using the following:

python3 manage.py migrate
And run the app locally:

python3 manage.py runserver

### Amazon s3 bucket set-up:

As this is my first time using AWS is opted to follow a user guide on the amazon web server website below is the attatched link
[S3 bucket set-up](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)

## Future Development

Currently the UI is lacking severly, this will be improved drastically in the next version.






  






