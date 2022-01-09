![](/documentation/images/mochup-light.png)     

# Welcome
## Code Institute: Milestone Project 4
### Shop for Buddhas - Daiden Sacha - Full Stack Web Developer
View the [Shop for Buddhas](https://shop-for-buddhas.herokuapp.com/) on Heroku.
[TESTING/](/documentation/testing.md) outlines my testing strategy, development, deployment and post-deployment.

## UX DESIGN
### 1. Strategy
Crafts like the lost wax method of making Vajrayana Buddha statues are in danger of being lost. Younger generations choose not to take up the craft handed down through generations of their forebears.

With this in mind, I decided that this site would be an excellent project to explore creating a market for the artisans to register and sell their works. The intention is to pass those sale proceeds directly to the artisans to support them to continue their work. It gives them access to markets they would not otherwise have.

#### User Stories:
[TESTING/User Stories Review](/documentation/testing.md/#user-stories-review-development-deployment)

### User Stories

1. **As a vendor:**
- I want to be able to register to sell my work.
- I want to create a profile.
- I want to be able to upload my products to be sold in the Shop.
- I want to edit, update or delete my listed products.
- I want to be able to see a current list of my items listed for sale.
- I want to be able to see a current list of my sold items
- I would like to be informed when something sells.
- I want customers to be able to commission particular works with specific preferences.

2. **As a customer:**
	- I want to buy quality statues.
	- I want to be able to contact the seller if I have questions about the product.
	- I want to be able to commission work for items I cannot find in the shop.
	- I'm interested in knowing about the statue-making process and the artisans that make the statues.    
	- ***Browsing Products***
		- I want to be able to view items by category.
		- I want to be able to sort the items in ascending, descending order.
		- I want to be able to search statues by name.    
	- ***Accounts & Registration***
		- I want a seamless registration process.
		- I want to be able to log in with an email and password.
		- I want to be able to have a profile to save time for future purchases.
		- I want an option to be able to close my account.    
	- ***Orders & Checkout***
		- It's important that I can easily and intuitively navigate the site.
		- I want to select and pay for items easily.
		- I want to receive confirmation of purchase.
		- I want a record of my orders attached to my account profile.  

3. **As the site owner:**
- I want to support grass root artists to continue their work.
- I want to provide a website where grassroots artists can sell their work.
- I want to educate potential customers about the complexity of producing quality statues.
- I want to help to preserve the rich tradition of statue making.
- I want to provide quality handmade Buddhist dharma products to Buddhist practitioners.
- I want to make a nominal commission to pay for the maintenance of the site.

### 2. Scope
#### Required Features
##### ALL USERS:
- **Navbar:** A simple navbar with the site logo, links to landing page sections, the shop, and the contact form. A search bar, and the shopping cart.
- **Landing Page Banner:** A full-screen banner with a link to the shop and a simple callout message to engage the visitor's attention.
- **Contact Form:** A simple contact form for users to contact the site administrator.
- **Testimonial Carousel:** A Testimonial carousel to display customer feedback.
- **Blog:** A blog to display providing information about the site, products, vendors, and other information to inform customers about the site and its activities.
- **Shop:** An e-commerce shop to display the products produced and uploaded by the vendors.
- **Shopping Cart:** A shopping cart to display items selected by customers to purchase.

##### REGISTERED VENDOR USERS:
- **Profile:** A user profile displaying the vendor's registration information.
- **Profile Management** A profile management section where the user can update information.
- **Order History** Show a list of the user's order history.
- **Sales History** Show a list of the vendor's sales history.
- **Product List** Show a list of the vendor's products.
- **Favorites List** Show a list of the user's favorites.
- **Product Management** The vendor should be able to create and upload, edit, and delete products.

##### REGISTERED CUSTOMER USERS:
- **Profile:** A user profile displaying the customer's registration information.
- **Profile Management** A profile management section where the user can update information.
- **Order History** Show a list of the user's order history.
- **Favorites List** Show a list of the user's favorites.
- **Checkout:** The user should be able to select and purchase items.

#### Functional Requirements
- **Navbar:** Links to the landing page sections and the shop.
- **Search bar:** The user can search for shop items by name or category.
- **Register Form:** New users can register an account.
- **Login Form:** Users can log in to their profile.
- **Login Form:** Users can update their password.
- **Profile management:** Users can update their profile details.
- **Blog posts** Blog page displays posts in a list view.
- **Blog Featured Post** A superuser can select posts to display as featured posts.
- **Blog pagination** Pagination displays blog posts over multiple pages.
- **Blog tags and categories** Post tags and categories will allow for easy filtering of posts.
- **Blog archive** A blog archive will display posts by year and month.
- **Blog comments** A comment form will follow all blog posts to comment on the posts.
- **Testinmnial Carousel** A carousel will display published user testimonials once approved by the superuser.
- **Testimonial Form** Logged in users will have access to a link on the testimonial carousel that will take them to a form to leave a testimonial.
- **Contact Form:** Users can send a message easily using the simple form at the bottom of the landing page.
- **Product Page:** The website shop will display products in a responsive grid. Users can select a product to view more detail and to purchase.
- **Product Favorites:** An icon will allow users to select an item to be added to a favorites list. The same button will also allow the user to remove the items from the favorite list. The icon's color will show the product's status, a red heart when favorited, and an outlined heart when not favorited.
- **Quick view/add:** The user can add or view the products in the list view by clicking on the quick view icons.
- **Simple Navigation:** Links and buttons provide straightforward navigation options for the user to have a seamless experience navigating the site.
- **Search Filters:** Users can select products by category and subcategory links in the main navbar. Users will further be able to filter by ascending and descending order.
- **Product Display:** Each product will display images, along with details of the product and an add to cart button.
- **Messages:** User actions will prompt the display of messages in a div that the user can then close.
- **Shopping Cart:** When the user adds items to the cart, the cart will display items along with a link to the secure checkout. The cart will be easily accessible in a side modal and enable the user to quickly delete items from the cart without leaving the products page.
- **Secure Checkout:** Transactions will be processed using Stripe, which will save the order to the user profile when the transaction is processed.
- **Image lightbox:** Images will be easily viewable in an image lightbox by clicking a quick view icon in the product list view.
- **Admin Management** The site owner will be able to log in to the admin panel to view and manage products and users.
- **Products Management:** In the admin panel, the admin user can add, update and delete products.
- **User Management:** In the admin panel, the admin user can add, update and delete users.

#### Content Requirements

1. **Inform and Educate:**
-   The landing page's primary focus will be to engage the site visitor, inform and educate them about Buddhist statues, the complexities of time-consuming processes involved in making them. I want users to understand the history of the art and how it is becoming lost. It is essential to understand that quality comes at a price.
- The motivation for the site is a not-for-profit site providing support to grassroots artists making Traditional Tibetan Buddhist Statues.

2. **Display and Sell:**
- The site will provide a shop displaying the artist's works for sale. Each product will show images, along with information about the items.
- The site will focus on selling quality handmade Buddhist Dharma items to support practicing Buddhists.
- The items will also be available for novice practitioners or those appreciative of the art.

### 3. Structure
#### Interaction Design
Visitors to the site will be greeted by a full-screen dark banner, with callout text greeting them and a link to the shop.

The landing page will display cascading sections, flowing logically into the next.

Navbar | Jumbotron | Services | Features | Testimonials | Contact

The home page's goal is to engage the user by contrasting color and content. It is to be an out-of-the-box clean and crisp design. Interest engaged, curiosity then leads the user to visit the shop to view the works on offer.

The flow of information and the structure is to be easy and intuitive to navigate, an adventure to discover and enjoy.

#### Information Architecture
**Navigation**
Fixed minimal navbar at the top of the page. It is always visible on all pages to easily access the navigation.
- **Navbar Links:**

- ***Logo*** links to the homepage so users can be directed to the homepage when clicking it.

- ***Shop:*** I included a megamenu dropdown that displays all products, categories, and filter links in one view. The user can easily see all available shop viewing options in one view. I also included Images to improve the visual stimulation and curiosity of the user.

- ***Blog:*** I included a link to the blog in the primary nav, so the user can always open the blog page to view contents.

- ***Contact:*** The link in the navbar scrolls the page to the contact form on the bottom of the homepage. Importantly the user can open the contact form from anywhere in the site at the click of one link.

- ***Search:*** The search icon in the navbar opens a fill page modal, with a placeholder asking users to Search the shop. I added links to the products and filters by category or price to inspire users. I also included links to the blog and profile.

- ***Login/ Logout link:*** In the top right above the navbar, I added a link that displays ```Login``` or ```Logout``` depending on whether the user is is_authenticated or anonymous. This provides direct visual confirmation for the user at all times, so they know if they are logged in or not. It also provides quick access to the login or logout pages.

- ***Social icons:*** Facebook, Linkedin, and Github icons are to the right of the login/ logout link.

- ***Linkedin*** and ***Github*** icons link to my user profiles of those platforms.

- The ***Facebook*** icon links to the K.I.B.I. (Karmapa International Buddhist Institute) Facebook page, an exciting resource for users interested in Buddhism.

- ***My account Icon:***
When the user hovers the account icon, a dropdown displays different links for users depending on the type of user.

- ***Anonymous users:***
	- Register: Links to the register page.
	- Login - Links to the login page

- ***Authenticated Customer:***
	- My Profile: links to the user's profile page.
	- Logout: Links to the logout page.
- ***Authenticated Vendor***
	- Products management - Links to the page to add products
	- My Profile: links to the user's profile page.
	- Logout: Links to the logout page.

- ***Shopping Cart Icon***
	- The shopping cart icon has a purple circle that shows the number of items in the shopping cart. The circle is a visual confirmation for the user of the cart's status if the cart has items and the number of items.
	- Clicking this icon opens a side modal shopping cart where the user can see the items in the cart, adjust the quantity, or delete items from the cart.

**Services Section**
- The services section on the home page informs the user briefly of the services offered by Shop for Buddhas.

**Features**
- A section that displays the main products of the site. Hand-crafted Buddha statues and meditation malas. It is a place to introduce the user to the products to know what the shop sells.

**Testimonial Section**
- A carousel displaying user testimonials is provided to submit comments of their experience.
- Displaying user testimonials is for users to read other users' experiences dealing with Shop for Buddhas or their comments about the products.
- A link to leave a testimonial is only visible for logged-in users. It takes them to the form to leave a testimonial and rating out of 5.

**Contact Form**
- Simple form with name, email, subject, and message for users to quickly contact the site administrator. It is in plain sight at the bottom of the home page, and there are links are various places to take users to it.

**Footer**
- Contains social icons linking to Facebook, Github, and Linkedin. These are visible from the contact form and above the copyright and website name so users can open links to see more information.
- Contains 2021 copyright and website name.

**Shop**
- Products are laid out in grid format, displaying the product image that users can select to view more info. Clicking on the link will open the product display page, showing all images for the product, along with the product information, rating, price, and add to cart button.

**Shopping Cart**
- The cart is easily accessible by clicking the cart icon in the header navbar. It opens from the right in a modal, displaying the cart items, quantity, and price.
- There are update and remove buttons to update or remove items from the cart easily.
- Success toast messages that appear from the left of the screen show the details and status of the action.
- The cart has a link to view the cart or the secure checkout.

**Secure Checkout**

***Anonymous User***
- Users not logged in are required to enter their personal information into the form to complete the purchase.
- There are links to log in or register to save the details to their profile so users can reference the information in their user profile order tab.

***Authenticated User***
- When the authenticated user goes to the secure checkout, their profile details are automatically added to the payment information form.
- The cart contents are displayed, along with price and total cost.
- Links are provided below the form so the user can return to edit the cart or proceed with the payment.

**User Profile**
The user clicks on the "My Profile" link in the dropdown visible when they hover over the user account icon in the navbar to view the User Profile page. The user profile is displayed using Bootstrap 5 side pills for desktops, and the pills move to inline view for smaller screens. The tabs displayed depend on the type of user.

##### CUSTOMERS
1. **Profile:** A read-only view of the user's registration information. It shows the user name, username, email, user account type, date joined, and last login.
2. **Account Info:**
	- ***Section 1:*** The user can update their profile information and add personal profile information about themselves.
	- ***Section 2:*** Links to update the password and the email information are provided. The user can add an email, change the primary email, or remove an email. Allauth provides this functionality using the Allauth forms.
3. **Orders:** A list of the user order history is displayed. The user can click on the order number to view the order's details.
4. **Favorites:** The user's favorite list displays all items in the list, with a remove link so the user can remove the items from the list. When the user clicks on the remove link, it removes the item from the user's favorite list, remaining on the profile page.

**Customer Profile Tabs**    
![](/documentation/images/profile-customer.jpg)    

##### VENDORS
In addition to the above tabs in the user profile, the profile provides the vendor with two additional tabs.

1. **Products:**
- The user's list of products is displayed in the products tab. A button links to the form for the user to add new products.
- Under each item in the user's product list are links to edit or delete the product.
- Clicking the edit button takes the user to the page to edit the product details.
- Clicking the delete button opens a modal styled with Bootstrap danger class, asking the user to confirm they want to delete the product. A cancel button and a delete button are in the modal. Clicking delete removes the product from the database.

2. **Sales:**
- A list of the vendor product sales is displayed with a link to view the sales. The user can have a history of what they have sold, with all the details saved in the order.     

**Vendor Profile Tabs**     
![](/documentation/images/profile-vendor.jpg)     

### Database Schema     
#### Shop for Buddhas Database Schema     
![](/documentation/images/db-schema.jpg)     

Being new to Django, planning the database schema was a big challenge. The schema I started with gave me a roadmap to create what I needed. The reality on the way was that I sometimes needed to change, add, or adapt certain aspects to incorporate and fully achieve what my goal was.

**Django Models**

1. **Accounts Model**
I needed to create a custom user registration to select their type of account, a customer, or a vendor. With no experience, this presented several problems.
- The Allauth registration form template does not include the first and last name fields. I fixed this after creating the user profile when I realized that I should have included it in the initial registration
- Adding a select for the ```user_type``` required additional form fields and required ensuring that I saved the information to the database.

	To do this, I extended the ```AbstractUser``` model, adding a select field to the allauth user registration form with the option for users to select the type of account.

	```python3
	# models.py
	user_type = (
		('is_admin', "Admin"),
		('is_customer', "Customer"),
		('is_vendor', "Vendor")
		)

	"""Add user_type field to user profile model"""
	user_type = models.CharField(max_length=25, choices=user_type, blank=True)
	```

	```python3
	# forms.py
	"""
	Note: I intentionally excluded the is_admin option in the signup form as I did not want this choice available to users in the registration process. I included this option purely for use in the administration panel.
	"""

	user_type = (
		('is_customer', "Customer"),
		('is_vendor', "Vendor")
		)

	"""Add user_type field to user profile model"""
	user_type = forms.ChoiceField(
		choices=user_type,
		label='Register as a customer or vendor?',
		required=True)
	```

	This choice allows users to register either as a customer or a vendor.  

	[See more: README/Development-Writeup](/README.md/#development-notes)

2. **Products Model**
- My products model is an extended version of the same model used in the Boutique Ado project. I needed to add additional fields to allocate ownership of the product to a vendor or admin. I added the ```created_by``` field, which references the ```user_id```.

- Adding the functionality for users to add products to a favorite list was initially problematic. I tried creating a separate table for the favorites. That table referenced the primary keys of the user and the product. I encountered issues displaying the items I wanted, so I changed to a more straightforward method.

- I added a ```favorites``` ```ManyToManyField``` to the product model, referencing the user's primary key. The products favorites column then contains a list of users who added it to their favorites. I then filtered each product for the authenticated user to return their favorites list and display the result on the products page and in the user's profile. 

	**Favorites: Product List Page**    
	![](/documentation/images/favorites-products.jpg)     

	**Favorites: User Profile Page**    
	![](/documentation/images/favorites-profile.jpg)     

3. **Testimonial Model**
The testimonial model was reasonably straightforward. I allow authenticated users to create a testimonial, which, once approved, is then displayed in the home page testimonial carousel.

	Here I wanted the user's rating in the HTML to display the user's rating using icons. For this, I added the select options to the user form.

	In the Django model.

	```python3
	rating = (('1', '1/5 stars'),
			  ('2', '2/5 stars'),
			  ('3', '3/5 stars'),
			  ('4', '4/5 stars'),
			  ('5', '5/5 stars')
			  )
	```

	In the HTML, I then looped the rating, adding one whole star for each loop.

	```html+jinja
	{% for star in stars %}
		{% if star < testimonial.user_rating|add:"1" %}
			<span class="text-warning"><i class="fas fa-star"></i></span>
		{% endif %}
		{% if star > testimonial.user_rating|add:"0"%}
			<span class="text-warning"><i class="far fa-star"></i></span>
		{% endif %}
	{% endfor %}
	```

	**User Rating**    
	![](/documentation/images/user-rating.jpg)    

	I incorporated this into the product model as well for the product rating.

4. **Blog Model**
I wasn't sure how complex it could be, and with limitations on time, I wanted to limit the scope to ensure it didn't blow out.

	I created a ```Post``` model, a ```Category``` model, and a ```Comment``` model. In addition to this, I added ```django-taggit==2.0.0``` to add tags to the posts.

	Displaying the posts was relatively straightforward. I had many issues returning and displaying the category and search query results without conflicts. The root of the issue always seemed to come back to the featured article. The search did not include it in the filter, or when it was, the result displayed as a featured article.

	It now displays correctly, and the tag, category, and blog search query work as expected.

	**NOTE** I changed the comments model. It now requires users to login to leave comments. I added a foreign key reference to the user in the comments model.   
	[Testing.md/Changes to Comment Model](/documentation/testing.md#note-changes-to-the-blog-comment-model)

5. **Checkout Model**
I based my checkout model on the Boutique Ado model, with minor changes as my handling of products' sizes' differs, using a charfield.

6. **UserProfile Model**
I also based the UserProfile model on the Boutique Ado project. By including the user type field in the user registration, I used the same profile model to display the same profile information for customers and vendors.

In the HTML, I have included additional tabs in the vendor profile, one for vendor sales and one for vendor products.

I was able to do this by filtering the order line items and product models to list the vendors selling products and listed products.

The vendors can upload their products by completing a form linked from their profile menu or the vendor's products list in their profile.

### 4. Skeleton
#### Wireframing:
I created the wireframes for the project in Adobe XD. Wireframes are basic and only a guide.

**Change in navbar color from wireframe**
After creating the HTML template, I changed the color of the navbar from the dark, as shown in the wireframes, to light. The whole page contrasts sections flowing from light to dark, and the light navbar fits the design much more. It is lifting and very clear. I felt this was necessary to and best compliments the site.    
[View the wireframes/](/documentation/wireframes.md)     

### 5. Surface
**Visual Design:**
The selection of colors for the site displays a stark contrast between dark and light, giving a clean and crisp feel. The choice of purple and green gives a fresh and uplifting feeling and highlights UI focus points.

I used a side modal for the shopping cart, easily accessible and on all pages. The navigation is minimal, offering a home, shop, blog, and contact links. A megamenu drops down to display all the shop categories.

A contact form is at the bottom of the home page, and the menu link scrolls to the form. As the user navigates the site, I have placed links and buttons anticipating the user's desire to move to other parts of the site or shopping process.

Toast messages inform the user of the success of their interactions. The toast messages slide in, then slide off the screen automatically. 

The design intention is for the experience of visiting the site to be seamless and enjoyable.

## TECHNOLOGIES USED

**Languages Used**

1. HTML
2. CSS3
3. SCSS
4. JavaScript
5. jQuery
6. Python
7. Jinja
8. Markdown

**Frameworks, Libraries, Programs used**
1. [Django 3.2](https://www.djangoproject.com/)
"The web framework for perfectionists with deadlines".
2. [sqlite3](https://docs.python.org/3/library/sqlite3.html)
A relational database used for project data storage in development.
3. [PostgreSQL](https://www.postgresql.org)
The relational database used for project data storage on Heroku in production
4. [Bootstrap 5](https://getbootstrap.com/)
The responsive framework I chose for this project.
5. [Heroku](https://www.heroku.com/home)
Hosting the production version of the project.
6. [AWS](https://aws.amazon.com/de/free/?trk=c25dd0aa-ac63-4039-9735-8633c6c683f6&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P%7CPS-GO%7CBrand%7CDesktop%7CSU%7CCore-Main%7CCore%7CDACH%7CDE%7CText&ef_id=EAIaIQobChMIp6PEmqKQ9QIV1uF3Ch1XdQQREAAYASAAEgKoAvD_BwE:G:s&s_kwcid=AL!4422!3!560181736076!e!!g!!aws&ef_id=EAIaIQobChMIp6PEmqKQ9QIV1uF3Ch1XdQQREAAYASAAEgKoAvD_BwE:G:s&s_kwcid=AL!4422!3!560181736076!e!!g!!aws&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)
I set up AWS S3 Bucket to store static files and product images.
8. [Font Awesome](https://fontawesome.com/)
Icons used in the website.
9. [GitHub](https://github.com/)
Used to host project repository and to deploy the project live via GitHub Pages
10. [Git Version Control](https://git-scm.com/)
I used it to commit blocks of work to the GitHub repository and create branches to work on specific changes or testing.
11. [Gitpod](https://gitpod.io/workspaces)
The editor used to work on the project.
12. [Adobe XD](https://www.adobe.com/products/xd.html)
Used to create wireframes
13. [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)
I used the software to work on the project images.
14. [Adobe Illustrator](https://www.adobe.com/de/products/illustrator.html)
Used to create my 404, 405, and 500 error images to display if users encountered missing or broken page links.
15. [Squoosh](https://squoosh.app/)
I used it to compress images to optimize load performance.
16. [Quire](https://quire.io/)
I used this free project and task planning application for adding and planning tasks for the project.
17. [Depositphotos](https://depositphotos.com/?gclsrc=aw.ds&&utm_source=google&utm_medium=cpc&utm_campaign=DP_EU_EN_Brand_Search&utm_term=depositphotos&gclid=CjwKCAjwuvmHBhAxEiwAWAYj-EVeHDBPdjs594mAT_HDLeFGM_g2IVcGn78NSArH7vXIYqfoO1BuhBoCv_kQAvD_BwE)
I use this source for stock images used in projects.
18. [StackEdit](https://stackedit.io/)
It's a free, online note-taking and markdown application. I used it to create the README file for GitHub.
19. [Webmaker App](https://webmaker.app/app/) It is a free application similar to codepen, used to create and save the work locally. I use it to implement and experiment with components of different frameworks that I plan to use. Then I am familiar with using them when implementing them in my work.

## TESTING
[TESTING/Testing Checklist](/documentation/testing.md#testing-checklist-development-deployment)
### Research
#### Boostrap 5 Theme Templates
I researched Bootstrap 5 themes to look for inspiration and style ideas that would fit the motivation for building this site. I found two themes that I liked, neither in their entirety, but as they were relatively inexpensive, I bought them both and used part of them on the site to build the pages.

**Theme 1.** [Shopapp](http://pxdraft.com/wrap/shopapp/home/index.html#).
I used this as my central theme, namely for the navbar, modal cart, homepage search modal, and shop product detail page.

**Theme 2.** [Amino Bootstrap 5 Theme](https://template.hasthemes.com/amino/amino/blog-list-right-sidebar.html) Offered a freshness that I liked for the blog. The greens complimented the purples of the Shopapp theme perfectly.

The Bootstrap 5 Shoppapp theme is fully customized and perfectly fits what I wanted to achieve. I integrated that theme, adding parts of the css for the blog sections I used from the Amino theme.

#### Images
I photographed all products on the site and photoshopped them to clean up the backgrounds and add subtle drop shadows.

#### Fixtures
I created JSON files for the products and product categories to add the products to the shop easily. 

[TESTING/Research](/documentation/testing.md/#research)

### Development
[TESTING/Development](/documentation/testing.md/#development)

#### Create Project
**Create Project Repository**
I used the Code Institute [gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template). I clicked on "Use this template" and created my project repository name, "shop-for-buddhas". I then opened this in GitPod to start the project.

**Initialise Git**
I started with `git init` to initialize git within the project.

**Git Ignore**
I created a **.gitignore** file to add files and directories I didn't want to upload to GitHub.

`git echo "file_name" >> .gitignore` is the terminal command I used to add files and directories to **.gitignore**.

**Install Django and initialize the project**
```bash
pip3 install django
django-admin startproject shop-for-buddhas .
```


**Create env.py**: Important for securing sensitive data
```bash
touch env.py
```

### DEVELOPMENT NOTES
#### Signup - Extening Allauth
**Useful links to Allauth documentation**

[Allauth Configuration](https://django-allauth.readthedocs.io/en/latest/configuration.html) Crucial information if you are changing the account authentication method.    
[Allauth Views](https://django-allauth.readthedocs.io/en/latest/views.html) This is especially handy for linking to Allauth password and email management forms if you want to add this functionality to the user profile management.    
[Allauth Custom User Models](https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-user-models)    
[Allauth Adding fields to the signup form](https://django-allauth.readthedocs.io/en/latest/forms.html#signup-allauth-account-forms-signupform)    
[Django Choices](https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-choices)    

**App Settings**

In ```settings.py```:
1. Set ACCOUNT_FORMS to use your custom form class.
2. Set the default AUTH_USER_MODEL to your custom model class
3. Set the other settings per your specific requirement. Refer to the Allauth configuration link above.

```python3
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_FORMS = {
	"signup": "accounts.forms.CustomSignup"
}
AUTH_USER_MODEL = "accounts.UserModel"
```

**Form**

In ```forms.py``` import Allauth SignUp form and Django forms.

```python3
from allauth.account.forms import SignupForm
from django import forms

user_type = (
    ('is_customer', "Customer"),
    ('is_vendor', "Vendor")
)

class CustomSignup(SignupForm):
    """Add additional fields to the custom signup form"""
    first_name = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={'class': 'form-control-sm rounded-3',
                                      'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={'class': 'form-control-sm rounded-3',
                                      'placeholder': 'Last Name'})
    )
    user_type = forms.ChoiceField(
        choices=user_type,
        label='Register as a customer or vendor?',
        required=True)

    def save(self, request):
        user = super(CustomSignup, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
```

The standard Allauth form has a username, email, password, and password (again) fields.

In my case, I wanted to add the option for customers and vendors to register as they have different needs that require different functionality.

I created the choice field tuple for customers and vendors in the above code from my project. I then added it into my ```CustomSignup``` form. Note that I added the fields first. Per Allauth documentation, you must save the Signup form first, ```user = super(CustomSignup, self).save(request)```. (Here was my lesson on python ```super```. If you don't know it, google it.) Then the additional field data is added to the model variable and saved. This order is important if you want to save the extra field data.

**Model**

In ```models.py``` import Django models and the AbstractUser model.

```python3
from django.db import models
from django.contrib.auth.models import AbstractUser

user_type = (
    ('is_admin', "Admin"),
    ('is_customer', "Customer"),
    ('is_vendor', "Vendor")
)


class UserModel(AbstractUser):
    """Create AbstractUser model class for the user registration form."""
    first_name = models.CharField(
        verbose_name='first_name',
        max_length=40,
        unique=False,
    )

    last_name = models.CharField(
        verbose_name='last_name',
        max_length=40,
        unique=False,
    )
    username = models.CharField(
        verbose_name='Username',
        max_length=40,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Email Address',
        unique=True,
    )

    """Add user_type field to user profile model"""
    user_type = models.CharField(max_length=25, choices=user_type, blank=True)
```
**NOTE:** I added the admin user type but did not include this in the signup form. I wanted it as an option to set a user to ```is_admin``` in the admin panel. I did not want this as an option in the signup process. It is now possible for me to use this in the future.

**Accounts Apps**

I learned from my mistakes and evaluated the pros and cons of my decisions as the project unfolded.

**ISSUES - RESOLUTIONS.**

1. **Signup - First and Last names**

For example, initially, I omitted the first_name and last_name fields. When I came to work on the profiles, I realized that the users had not registered their names, and I needed this. It was clear that it needed to be at the first point of registration, so I could use those names in my templates if needed. I added the first and last names when I worked on the profile templates. I made a mistake then by setting the fields to ```unique=True```. I only discovered this mistake when registering a second account with the same first name. The server returned a 500 error as unique names were required. So I changed the ```first_name``` and ```last_name``` in my model to```unique=False```.

2. **App names**

I chose to extend the AbstractUser to keep it simple. Most of the examples I found to do this also extend the ```BaseUserManager``` model, which means tampering with the admin. I didn't want to do this in my project.

With the experience of hindsight, I would create one app for accounts and profiles rather than have it in two separate apps. Naming the app accounts is problematic, as I discovered when first opening the admin. I had two apps called ```ACCOUNTS```, the Allauth ```accounts``` and my app ```accounts```. Rather than deleting and starting over, I added the following into the ```accounts/app.py```.

```python3
from django.apps import AppConfig

	class AccountsConfig(AppConfig):
		"""Add verbose name to change name of App in Admin panel."""
		default_auto_field = 'django.db.models.BigAutoField'
		name = 'accounts'
		verbose_name = "Accounts Users"
```

I changed the name of my app in the admin to ```Accounts Users```, leaving the Allauth ```Accounts``` as it was. The Allauth ```Accounts``` has the email management, ```Accounts Users``` has the user registration info, and ```Profiles``` has the user profile information.

I'm sharing this because I needed to keep moving forward with limited time to complete my project when I discovered it. I changed what I could and made the best of this situation that I think is not ideal. I would create one app for the user account and profile and name it differently, not conflicting with the Allauth name.

#### Toast Messages    
[Testing/Toast Messages](/documentation/testing.md/#toast-messages)

**Issue 1. Positioning and responsiveness**

As my shopping cart modal opens from the right, I positioned the toast messages on the left of the screen. I gave them a fixed position off the left of the screen, so the messages could slide in and then close automatically, sliding off-screen after a short time.

With fixed widths, I had issues with the display of the messages on mobile screens.

My solution was to use the CSS ```calc`` function to determine widths, and positioning. The following CSS for mobiles is based on the 100% width of the viewers screen.

```css
.message-container {
	position: fixed;
	top: 125px;
	left: calc(-100vw);
	z-index: 99999999999;
	height: auto;
}
.toast {
	width: 100vw;
	max-width: calc(100vw); /* 100% viewport width */
	box-shadow: 0 10px 20px rgba(75, 50, 50, 0.05) !important;
}
.toast.show {
	transform: translateX(calc(100vw));
	transition: 1s;
	transition-timing-function: ease-out;
	opacity: 1;
}
.toast.hide {
	transform: translateX(calc(-100vw))!important;
	transition-timing-function: ease-in!important;
	transition: 1s;
	opacity: 0!important;
	display: block!important;
}
```

Media query for tablets, the calc function sets the toast width to 50%.

```css
/* Tablets half width toast messages */
@media (min-width: 768px) {
	.toast {
		max-width: calc(100vw / 2); /* 50% viewport width */
		box-shadow: 0 10px 20px rgba(75, 50, 50, 0.05) !important;
	}
}
```

Media query for desktops, the calc function sets the toast width to 25%.

```css
@media (min-width: 992px){
	.message-container {
		position: fixed;
		top: 125px;
		left: calc(-100vw / 4);
		z-index: 99999999999;
		height: auto;
		max-width: calc(100vw / 4);
	}
	.toast {
		max-width: calc(100vw / 4); /* 25% viewport width */
		box-shadow: 0 10px 20px rgba(75, 50, 50, 0.05) !important;
	}
	.toast.show {
		transform: translateX(calc(100vw / 4)) !important;
		transition: 1s;
		transition-timing-function: ease-out;
		opacity: 1;
	}
	.toast.hide {
		transform: translateX(calc(-100vw / 4))!important;
		transition-timing-function: ease-in!important;
		transition: 1s;
		opacity: 0!important;
		display: block!important;
	}
}
```

**Issue 2. Cart adjustment messages**

I had an issue with cart contents showing in unrelated success messages. It didn't look right, and I only wanted the cart success messages displayed for cart adjustments.

I found the Django documentation ambiguous and challenging to understand. Still, luckily a [stack overflow thread](https://stackoverflow.com/questions/43588876/how-can-i-add-additional-data-to-django-messages) provided the clarity I needed to implement the fix. I discovered that ```extra_tags``` can be added to messages and used in templates to filter the display of such messages. I added the following ```extra_tags``` to the cart ```view.py``` adjustment-related messages.

```python3
# Example
messages.success(request, f'Added {product.name} to your cart', extra_tags='is_cart')
```

Then in the success toast HTML, the cart message is only displayed if the following condition is true.

```html+jinja
{% if grand_total and "is_cart" in message.extra_tags %}
```
Now the cart success messages only show for cart adjustments.

**Issue 3. Image lightbox sizing ratio**

I used the built in bootstrap lightbox, which is actually very easy to implement.

Its as simple as adding the ```data-toggle="lightbox"``` to the ```a``` element along with the ```href``` to the image.

```html+jinja
<!-- Product Gallery -->
<div class="col-lg-6 lightbox-gallery product-gallery">
	{% if product.image %}
		<a href="{{ product.image.url }}" data-toggle="lightbox">
			<img class="img-fluid" src="{{ product.image.url }}" alt="{{ product.name }}" title="">
		</a>
	{% else %}
		<a href="">
			<img class="img-fluid" src="{{ MEDIA_URL }} noimage.png" alt="{{ product.name }}" title="">
		</a>
	{% endif %}
</div>
<!-- End Product Gallery -->
```

The bootstrap Javascript does the rest of the work, creating the lightbox modal. It adds an aspect ratio of 16:9, which is not ideal, resulting in the lightbox image being smaller than the standard view on mobiles.

I changed this by adding custom CSS to the required modal elements to change the aspect ratio to 1:1.

```css
/* Set max-width for the image lightbox on xl screens */
.modal.lightbox .modal-dialog.modal-dialog-centered.modal-xl {
	max-width: 900px;
}

/* Set the lightbox ratio */
.modal-body .lightbox-carousel .carousel-inner .carousel-item.active .ratio {
	position: relative;
	width: 100% !important;
	/* Set aspect ratio-1x1 */
	--bs-aspect-ratio: calc(100%) !important;
}
```

The following is the result on mobiles.   

![](/documentation/images/lightbox_image_ratio.jpg)    

It resulted in an image that was too large on xl screens on desktops, so I changed that to a max-width of 900px. It produces a larger image on desktops and tablets, and mobiles.

---

#### TESTING DEVICES INFORMATION

[TESTING/Testing Devices](/documentation/testing.md/#testing-devices)

**Personal Testing Devices/ Software/ Browsers**
- Macbook Pro (15-inch)
- macOS Monterey 12.1
- Safari Version 15.2 (17612.3.6.1.6)
- Chrome Version 96.0.4664.110 (Official Build) (x86_64)
- Firefox 95.0.2 (64-bit)
- Windows 10 (bootcamp)
- Microsoft Edge
- Chrome
- Firefox
- Dell 2419 Monitor
- iPad Air
- iPhone 13 Pro

**Secondary Testing Device/ Sofware/ Browser**
- HP ProDesk 600 Desktop PC
- Windows 10 Pro
- Microsoft Edge Version 90.0.818.42 (Official Build) (64-Bit)
- Firefox 78.10.0esr (64-Bit)
- Chrome Version 90.0.4430.85 (Official Build) (64-Bit)
- AOC 22E15 21.5-inch Full HD 1920x1080 at 75 Hz
---

#### Git Version Control

I used Git version control to save and commit work incrementally throughout the project.

I created development branches (```dev_account, dev_blog, dev_profiles```) at stages throughout the project to develop applications without compromising the stable body of completed work.

**Detached Head**

At one point, after migrating data for my profile model, my database became corrupted, and I went back to look at a previous commit in my code. I was looking at a way to recover the database. However, I needed to create my data fresh. The head became detached, and I needed to save the work without losing it.

[Circleci Blog](https://circleci.com/blog/git-detached-head-state/) outlined the steps to recover from the detached head state.

```bash
# Create a new branch and check out to it to reattach the head
git checkout -b temp-branch

# Then I could commit the work to save it
git commit -m "temp-branch"

# Then, I can merge the changes into the main branch
git checkout main
git merge temp-branch
git commit -m "merged detached head and work into the main branch."
```

The solution above saved me from losing my work. Although I needed to resolve some conflicts, it was far better than losing the work outright.

Thanks to Ron Powell for writing a great article that helped me in that time of need.

**ERROR Pages**

I created the following custom error pages in the base level template folder.

1. **400 Bad Request** "The server can't process the request due to an apparent error."
2. **403 Forbidden Error** "Looks like you don't have access to this page."
3. **404 Error** "Sorry, the page was not found."
4. **500 Internal Server Error** "Sorry, the server is a bit confused."

### Deployment

[TESTING/Deployment](/documentation/testing.md/#deployment)

**Create Heroku App**

1. Navigate to [Heroku](https://id.heroku.com/login), create an account, and or login.
2. Select **New** > **Create new app**.
3. Enter app name
4. Select the region closest to yourself

**Add Postgres SQL Database**

1. Click on the **Resources** tab
2. Under **Add-ons**, enter ```Postgres``` in the search field, and select ```Heroku Postgres```.
3. Select the free plan

**Set Database environment variable in Heroku**

```python3
# Set environ variables in Heroku
# Set SECRET_KEY and other environ variables in the settings in Heroku
DATABASE_URL
EMAIL_HOST_PASS
EMAIL_HOST_USER
SECRET_KEY
STRIPE_PRICE_ID
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
```

**Back in Gitpod install:**

```bash
# Install dependencies for migration to Heroku PostgresSQL
pip3 install dj_database_url
pip3 install psycopg2-binary
pip3 freeze > requirements.txt
```
**In settings.py**
```python3
import dj_database_url

# Use postgresSQL if DATABASE_URL when in Heroku production
if 'DATABASE_URL' in os.environ:	
	DATABASES = {
	'default': 	dj_database_url.parse(os.environ.get('DATABASE_URL'))
	}
	
else:
	# Use sqlite3 when in Gitpod development environment
	DATABASES = {
		'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
}
```

Migrate the models to Heroku, create a superuser, then load the fixture JSON data files. In this oder for this project. 
```bash
# Applies all migrations to postgresSQL to setup database
python3 manage.py migrate

# Create superuser first as the database requires the user id field to install the products.
python3 manage.py createsuperuser
# enter a username, email, password, password again

python3 manage.py loaddata categories
python3 manage.py loaddata products
```
With this finished, the Heroku app and database are ready to go.

Change database settings to access Postgres DB on Heroku or mysqlite3 in Gitpod.

```bash
# Install gunicorn to act as the webserver
pip3 install gunicorn
pip3 freeze > requirements.txt

# create Procfile to tell Heroku to create a web dyno that will run gunicorn and serve the Django app.
touch Procfile

# Note that "Heroku login" doesn't work in Gitpod; enter as follows instead
heroku login -i
# Enter email and password for Heroku login

# Disable collect static, so static files are not stored in Heroku
heroku config:set DISABLE_COLLECTSTATIC=1

# Add "--app" plus your app name if you have more than one app
heroku config:set DISABLE_COLLECTSTATIC=1 --app yourappname
```

Add the hostname of your Heroku app to allowed hosts in settings.py
```python3
# Add localhost, so the site is also available in Gitpod.
ALLOWED_HOSTS = ['yourappname.herokuapp.com', 'localhost']
```

```bash
# git add, commit and push to github
# Set environ variables in Heroku
# Set SECRET_KEY and other environ variables in the settings in Heroku

# initialize git Heroku remote
heroku git:remote -a yourappname
git push heroku main
```

At this point, the project is deployed without static files.

**Connect to Github Repository**
1. Click on the **Deploy** tab.
2. Select **Github** > **Connect to GitHub**
3. Search for the Repository name, select, and click connect.
4. Click **enable automatic deployment**

The project will be automatically pushed to Heroku when commits are made to the GitHub repository.
```python3
# settings.py
DEBUG = 'DEVELOPMENT' in os.environ
```

**NOTE:**
I used the AWS S3 bucket to store Shop for Buddhas static files and product images. If you want to do this, you will need to:
1. Open AWS account
2. Create an account and continue
3. Enter a credit card in case you go above the limit.
4. Sign in to the management console
5. Create your S3 bucket and dependencies required for storing the project static files. This is a complex process that I will not describe here, as AWS is constantly evolving. Any outline I give here could become problematic in the future.

Using AWS will require adding environment variables to Heroku for the following
- AWS_ACCESS_KEY_ID ```Requires AWS S3 bucket setup```
- AWS_SECRET_ACCESS_KEY ```Requires AWS S3 bucket setup```
- USE_AWS ```Requires AWS S3 bucket setup```

[TESTING/Testing Checklist](/documentation/testing.md#testing-checklist-development-deployment)

#### Forking or Cloning [Shop for Buddhas](https://github.com/daidensacha/shop-for-buddhas)    

1. If you're interested in forking the project to experiment with the code or propose changes, navigate to the [Shop for Buddhas](https://github.com/daidensacha/shop-for-buddhas), and click on the fork button.  

	![](/documentation/images/fork-project.png)    
2. You have forked the project but will not yet have files locally on your computer.
3. Navigate to the [Shop for Buddhas Repository](https://github.com/daidensacha/shop-for-buddhas)
4. **Get Clone URL:** Click **Code**, then click the **copy icon** on the right of the HTTPS URL.    

	![](/documentation/images/clone-project.jpg)    

5. **Clone the project:** Open your IDE of choice, and in terminal enter ```git clone repository-url```.
6. **Open locally:** Open the project in your IDE of choice and create your virtual environment if required.
7. **Install dependencies:** Enter ```pip3 install -r requirements.txt``` to install project dependencies.
8. **Create superuser:** In the terminal, enter ```python3 manage.py createsuperuser```, and create your username, email, and password to access the project admin.
9. **Create database** ```python3 manage.py makemigrations``` and then ```python3 manage.py migrate```.

At this point, you have a working version of the site locally, without any data added.

1.  You can add products, product categories, testimonials, and blog posts to populate the site's pages with content.
2.  You can register customer and vendor accounts to test the functionality and explore code.

[Github documentation on forking](https://docs.github.com/en/get-started/quickstart/fork-a-repo)     

[Github documentation on cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)   

### Feedback

[add feedback about the site/ project]

### Credits

1. **Code Institute** Boutique Ado project was a significant guide for developing this project. Especially the sections on adding products and the checkout app. The project introduced me to Django, and I referenced the code regularly to understand things. It was a great help and formed the foundation of this project.
2. [Very Academy](https://www.youtube.com/channel/UC1mxuk7tuQT2D0qTMgKji3w) Throughout the project, while researching, I came across clear and informative youtube videos from Very Academy.
	- Setup/ Custom admin
	- Creating a blog
	- [Creating a Bookmark/Favorites Features](https://www.youtube.com/watch?v=H4QPHLmsZMU) I found their input on using a ManyToManyField for adding favorites helpful. I had to adapt it and then create my filters, but it opened a doorway that helped me to get it done.
3. **Boostrap 5 Theme** Using and customizing Boostrap 5 themes enabled me to focus more on creating the site's apps and code. I want to acknowledge and thank the creators of the two themes I used.
	-	[Shopapp Bootstrap 5 Theme](http://pxdraft.com/wrap/shopapp/home/index.html#)
	-	[Amino Bootstrap 5 Theme](https://template.hasthemes.com/amino/amino/blog-list-right-sidebar.html)
4. [Django and DRF Testing Series](https://www.youtube.com/watch?v=KIIdbVs7e8I&list=PLP1DxoSC17LZTTzgfq0Dimkm6eWJQC9ki) by Kenyan Engineer was beneficial with creating unit tests using pytest and pytest-cov.
5. [Scroll to top button with vanilla js](https://dev.to/ljcdev/scroll-to-top-button-in-vanilla-js-beginners-2nc) Thanks to the author of this post for the vanilla JS back to top button. I customized the CSS to fit with the style of the site.
6. Last but not least, I want to thank my Code Institute mentor, [Daisy McGirr](https://www.linkedin.com/comm/in/daisy-mcgirr?midToken=AQHg3jBTM8UfHg&midSig=097cw4mle3rW41&trk=eml-email_m2m_invite_single_01-hero-3-prof%7Ename&trkEmail=eml-email_m2m_invite_single_01-hero-3-prof%7Ename-null-dcfqat%7Eky257r5e%7Ext-null-neptune%2Fprofile%7Evanity%2Eview&lipi=urn%3Ali%3Apage%3Aemail_email_m2m_invite_single_01%3B0Rc%2BfihnTEqUiTp1Yks1OQ%3D%3D).    
When I was most stressed or needed input, Daisy was available and generous with her time and support. Thank you, Daisy!!

## NOTES

To prepare the project for submission and for final checking, I created 3 customers, and 3 vendors in addition to myself as the superuser. 

**Registered users**    
![](/documentation/images/registered_users.png)     

The above image lists the  user types, how many favorites they have added, how many vendor products and vendor sales, customer order and lineitems. 

**User Orders**    
![](/documentation/images/user_orders.png)     
 
The above image lists orders, customer, lineitem qualtity and the product vendor.

**Testimonials**
I created one testimonial for each customer, and published them to the testimonial carousel. I unpublished my testing testimonials which are still saved but not published.

## IMPROVEMENTS/ FUTURE FEATURES


**Blog**
- **Image Sizes** I will add the option in the admin to change the size of images in blog posts.
- **Comment replies** I planned to add comment replies, but I did not have time to implement them before submitting the project. I plan to do it soon.
- Currently, the featured post is displayed at the top of all blog post list pages. I will make this, so it only shows at the top of page 1 of the paginated pages. 

**Products**
- Products currently have one image. I want to make it possible to have multiple images for each product in a gallery. 
- Product zoom feature when hovering over the product image. 
-

**Checkout**
- Coupon management functionality, creating and managing coupons, and integrating it with the payment system.
- Email confirmation for vendors' product sales. I didn't have time to implement this now, but it is in the pipeline for development.

**Ajax to update info without refreshing page**
There are cases where the use of Ajax would be far preferable to refreshing the page or redirecting the user to another page.
- Quick add items to the shopping cart.
- Updating the cart quantity.
- Deleting items from the shopping cart.
- Adding or removing items from the favorites list.

	The pages refresh for the above actions, which returns the user to the top of the page or a different page view. It's not ideal, and it will be a priority to address this issue.

**Vendor and Product Management**
- I would like to improve the vendor registration process. I need to manage this process to vet vendors, ensuring the site's integrity is maintained.
- Product reviews. At this point, vendors can register and upload products. Still, it is necessary to review products intended for sale on the site. This site supports artisans, but it is also where vendors can sell quality items suitable for Buddhist practice. It is not a marketplace for selling items that are not quality.

**Other Features**
- **Currencies** I would like to add multi-currency functionality. Euro, GBP, $US.
- **Languages** I would like to add German, French, Italian, Spanish translations for users to select from. 
- **Social Media login** I had so much to do, I didn't have time to implement this, but it is a priority. 



## BUGS and ISSUES

See also [TESTING/Issues and Fixes](/documentation/testing.md/#issues-and-fixes)    

**Django Admin**
Shop for Buddhas is my first Django project, so I'm happy with the result. I have learned a lot and would do some things differently. 
Some things you can only learn from experience and cannot know before. 
I stressed a lot creating my models, and it was the hardest thing for me to do to start the project. At one point, I just had to accept and jump without knowing how it would turn out. 
- **Django User Model**
I wanted to implement customer and vendor user types. I decided to use the same table for both types of users and distinguish them using the ```user_type```. I'm not sure if it was the best way or if it might have been better to create different tables for the user types. For example, in Product Admin, I have the situation that I need to write filters to limit the ```user_type```displayed. The dropdown lists all users, not only vendors, when selecting a product owner. In the blog posts, when selecting ```created_by```, it lists all users, not only the superuser. I need to look at this, talk to someone more knowledgeable, and get advice on the best way to deal with it. 
For now, it is fine, but not a long-term issue that I want to leave unaddressed. There has to be a better way to improve the usability from the admin perspective.

 **Django Admin Notes addendum**

- **Issue Fix In Products ProductAdmin using filter**    
[A solution found via Google](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/filter_fk_dropdown.html) helped me to resolve this issue. I had to change a few references, but it works.

	```python3
	# Import Q
	from django.db.models import Q
	# Add to the ProductAdmin class
	def  formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'created_by':
				kwargs['queryset'] = UserModel.objects.filter(
				Q(user_type__in=['is_vendor']) |
				Q(is_superuser=True)
				)
		return  super().formfield_for_foreignkey(db_field, request, **kwargs)
	```
	The product model referenced the UserModel foreign key and displayed all users un the admin ```created_by``` select. The above filters the users and only returns the vendors and superusers to the list.    

- **Issue Fix In Blog PostAdmin using filter**    
The same issue in the blog PostAdmin was resolved as follows.

	```python3
	# Import Q
	from django.db.models import Q
	# Add to the PostAdmin class
	def  formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'author':
			kwargs['queryset'] = UserModel.objects.filter(
				Q(user_type__in=['is_admin']) |
				Q(is_superuser=True)
				)
		return  super().formfield_for_foreignkey(db_field, request, **kwargs)
	```

	The author field now displays superusers and admin users using the above filter.    

- **Issue Fix in Checkout OrderAdmin**    
When opening an order to view the details in the checkout OrderAdmin, the ```user_profile``` select displayed a list of all users. I don't see that this should be displayed, as it only creates a possibility for mistakes. 
I set the field to read-only, and now instead of the select showing all users, it shows a link to the order's user_profile.   

	![](/documentation/images/order_user_profile.png)    