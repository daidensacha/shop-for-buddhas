![](/documentation/images/shopforbuddhas.jpg)

# Welcome

## Code Institute: Milestone Project 4

### Project Name - Daiden Sacha - Full Stack Web Developer

View the [Project_name](project-URL) on Heroku.

[TESTING/](/documentation/testing.md) outlines my testing strategy, development, deployment and post-deployment.

## UX DESIGN

### 1. Strategy
#### User Stories:
[TESTING/User Stories Review](/documentation/testing.md/#user-stories-review-development-deployment)

### User Stories
1. **As an vendor:**
	- I want to be able to register to sell my work.
	- I want to create a profile.
	- I want to be able to upload my products to be sold in the shop.
	- I want to be able to edit, update or delete my listed products.
	- I want to be able to see a current list of my items listed for sale.
	- I want to be able to see a current list of my sold items
	- I would like to be informed when something sells. 
	- I want customers to be able to commission particular works with specific preferences. 


2. **As a customer:**  
	- I want to buy quality statues.
	- I want to be able to contact the seller if I have questions about the product.
	- I want to be able to commission work for items I cannot find in the shop.
	- I'm interested in knowing about the statue making process and the artisans that make the statues.  

	***Browsing Products***
	- I want to be able to view items by category. 
	- I want to be able to sort the items by ascending, descending order.
	- I want to be able to search statues by name.
	
	***Accounts & Registration***
	- I want a seamless registration process.
	- I want to be able to log in with an email and password, or with my social network account.
	- I want to be able to have a profile to save time for future purchases.
	- I want an option to be able to close my account.
	
	***Orders & Checkout***
	- It's important that I can easily and intuitively navigate the site.
	- I want to easily select and pay for items.
	- I want to receive confirmation of purchase.
	- I want a record of my orders attached to my account profile.

3. **As the site owner:**
	- I want to support grass root artists to continue their work.
	- I want to provide a website where grass root artists can sell their work.
	- I want to educate about the complexity of producing quality statues.
	- I want to help to preserve the rich tradition of statue making.
	- I want to provide quality hand made Buddhist dharma products to Buddhist practitioners.
	- I want to make a nominal commission to pay for the maintenance of the site.


### 2. Scope

#### Required Features
##### ALL USERS: 
- **Navbar:** A simple navbar with the site logo, links to landing page sectons the shop, and the contact form. A search bar, and the shopping cart. 
- **Landing Page Banner:** I full screen banner with a link to the shop, simple callout message to engage the visitors attention.
- **Contact Form:** A simple contact form for users to be able to contact the site administrator.
- **Testimonial Carousel:** A Testimonial carousel displaying customer feedback.
- **Blog:** A blog displaying providing information about the site, products, vendors, and other inforamtion to inform customers about the site and its activities.
- **Shop:** An e-commerce shop to display the products produced and uploaded by teh vendors.
- **Shopping Cart:** A shopping cart to display items selected by customers to purchase.

##### REGISTERED VENDOR USERS: 
- **Profile:** A user profile displaying the vendors registration information.
    - **Profile Management** A profile management section where the user can update information.
    - **Order History** Show a a list of the users order history.
    - **Sales History** Show a a list of the vendors sales history.
    - **Product List** Show a a list of the vendors products.
    - **Favorites List** Show a a list of the users favorites.
- **Product Management** The vendor should be able to create and upload, edit, and or delete products.

##### REGISTERED CUSTOMER USERS: 
- **Profile:** A user profile displaying the customers registration information.
    - **Profile Management** A profile management section where the user can update information.
    - **Order History** Show a a list of the users order history.
    - **Favorites List** Show a a list of the users favorites.
- **Checkout:** The user should be able to select and purchase items.


#### Functional Requirements
- **Navbar:** Links to landing page sections, and to the shop. 
- **Search bar:** The user can search for shop items by name or category.
- **Register Form:** New users can register an account.
- **Login Form:** Users can login to their profile.
- **Login Form:** Users can update their password.
- **Profile management:** Users can update their profile details.
- **Blog posts** Blog posts will be displayed in a list view.
- **Blog Featured Post** Superusr can select posts to be displayed as featured posts.
- **Blog pagination** Pagination will enable blog posts to be displayed on multiple pages.
- **Blog tags and categories** Post tags and categories will allow for easy filtering of posts.
- **Blog archive** A blog archive will display posts by year and month.
- **Blog comments** A comment form will follow all blog posts so users can comment on the posts.
- **Testinmnial Carousel** A carousel will display user testimonials that are publoished once approved by the superuser.
- **Testinmnial Form** Logged in users will have access to a link on the testimonial carousel that will take them to a form to leave a testimonial.
- **Contact Form:** Users can send a message easily using the simple form at the bottom of the landing page.
- **Product Page:** The website shop will display products in a responsive grid. Users can select a product to view more detail and to purchase.
- **Product Favorites:** An icon will allow users to select item to be added to a favorites list. The same button will also allow the user to remove the items from the favorite list. The status of the product will be evident by the color of the icon which will be a red heart when favorited, and an outlined heart when not favorited.
- **Quick view/add:** Icons enable the user to easily add or view the products in the list view.
- **Simple navigation:** Links and buttons provide easy and clear navigation options for the user to have a seamless experience navigating the site.
- **Search Filters:** Users can select products by category and sub category. Links from the main navbar. Users will further be able to filter by ascending and descending order.
- **Product Display:** Each product will display images, along with details of the product, and a add to cart button.
- **Messages:** User actions will prompt messages that will be displayed in a drop down message div, that the user can then close. 
- **Shopping Cart:** When the user adds items to the cart, it will be displayed along with a link to the secure checkout. The cart will be easily accessible in a side modal, and enable the user to easily delete items from the cart without leaving the products page.
- **Secure Checkout:** Transactions will be processed using Stripe, and will save the oder to the user profile when the transaction is processed.
- **Image lightbox:** Images will be easily viewable in an image lightbox by clicking a quickview icon in the product list view.
- **Admin Management** The site owner will be able to log in the the admin panel to view and manage products and users. 
- **Products Management:** In the admin panel, the admin user can add, update and delete products. 
- **User Management:** In the admin panel, the admin user can add, update and delete users. 


#### Content Requirements
1. **Inform and Educate:** 
	- The main focus of the landing page will be to engage the site visitor, to inform and to educate them about Buddhist statues, the complexities time-consuming processes involved in making them. I want users to understand the history of the art, and how it is becoming lost. It is important to understand that quality comes at a price. 
	- The motivation for the site is a not for profit site providing suppor to grass root artists making Traditional Tibetan Buddhist Statues. This is a theme that is imortant to convey.
2. **Display and Sell:** 
	- The site will provide a shop displaying the artists works for sale. Each product will show images, along with information about the items. 
	- The site will focus on selling qualtiy hand made Buddhist Dharma items to support practicing Buddhists. 
	- The items will also be available for novice practitioners or those appreciative of the art.



### 3. Structure
#### Interaction Design
Visitors to the site will be greeted by a full screen dark banner, with with callout text gteeting them, and a link to the shop. 
The landing page will display cascading sections, each flowing into the next in a logical order. 
Navbar | Jumbotron | Services | Features | Testimonials | Contact
The home page goal is to engage the user, though the contrast in color, and interesting content. It is meant to be an out of the box clean and crisp design. Interest engaged, the user is then led to visit the shop out of curiosity to view the works on offer. 
The flow of informatin and the structure is meant to be easy and intuitive to navigate. An adventrure to discover and enjoy. 

#### Information Architecture
- ***Navigation***
	- Fixed minimal navbar at the top of the page.
		- Navbar: Logo links to the homepage. Links to Shop, Services, Statue Making, Artisans, Contact. Search bar for searching products. My account link. Shopping cart to show added products and link to the secure checkout.
- ***Services Section***
	- Outlines the sites services.
- ***Features***
	- A section displaying the main products of the site. Hand crafted Buddha statues, and meditation malas. 
- ***Testimonial Section***
	- A carousel displaying user testimonials. A link for logged in users will guide them to the form to leave the testimonial.
- ***Contact Form***
	- Simple form with name, email, subject and message for users to be able to easily contact the site adminsistrator.
- ***Footer***
	- Contains social icons linking to Facebook, Github and Linkedin.
	- Contains 2021 copyright and website name. 
- ***Shop***
	- Products laid out in grid format, displaying the product image that users can select to view more info. Clicking on the link will open the product display page, showing all images for the product, along with the product infomation, rating, price and add to cart button. 
- ***Shopping Cart***
	- Clicking on the add to cart button adds the product to the shopping cart. A success message appears informing the user the item was added to the cart, along with the total. The cart information and a link to the secure checkout also appears. 
- ***Secure Checkout***
	- The user can edit the cart contents, and click the link to the secure checkout, or click the link to continue shopping. At the secure checkout, the user is required to fill out the form with their details, to complete the transaction. They can also create an account or login to save the order information to their account. The carts contents with the order total is also displayed.
- ***My Account***
	- The user can login to view, and or update their account profile. All orders are displayed on this page, with a link to view the order information. The admin user can also add, update or delete product information on from the user profile. A section in the profile will also display the list of users selected favorites.

### Database Schema
**Django Models**

### 4. Skeleton

#### Wireframing:
[notes about creating wireframges]

[wireframe images] ???



### 5. Surface

**Visual Design:**

***Clean, with contrast:***  Blacks and whites, a stark contrast with a nice clean feel.

## TECHNOLOGIES USED

**Languages Used**
1.  HTML
2.  CSS3
3.  SCSS
4.  JavaScript
5.  jQuery
6.  Python
7.  Jinja
8.  Markdown

**Frameworks, Libraries, Programs used**


1. [Django](https://www.djangoproject.com/) 
     "The web framework for perfectionists with deadlines".
2. [Bootstrap](https://getbootstrap.com/)
	The responsive framework of choice for this project.
3. [Heroku](https://www.heroku.com/home)
	Hosting the project.
7. [Font Awesome](https://fontawesome.com/)
	Icons used in the website.
8. [GitHub](https://github.com/)
	Used to host project repository and to deploy the project live via 	GitHub Pages
9. [Git Version Control](https://git-scm.com/)
	I used it to commit blocks of work to the GitHub repository and create branches to work on specific changes or testing.
10. [Gitpod](https://gitpod.io/workspaces)
	The editor used to work on the project.
11. [Adobe XD](https://www.adobe.com/products/xd.html) 
	Used to create wireframes
12. [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)
	I  used the software to work on the project images.
13. [Adobe Illustrator](https://www.adobe.com/de/products/illustrator.html)
	Used to create my 404, 405, and 500 error images to display if users encountered missing or broken page links.
14. [Squoosh](https://squoosh.app/)
	I used it to compress images to optimize load performance.
15. [Quire](https://quire.io/)
Free project and task planning application used for adding and planning tasks for the project.
16. [Depositphotos](https://depositphotos.com/?gclsrc=aw.ds&&utm_source=google&utm_medium=cpc&utm_campaign=DP_EU_EN_Brand_Search&utm_term=depositphotos&gclid=CjwKCAjwuvmHBhAxEiwAWAYj-EVeHDBPdjs594mAT_HDLeFGM_g2IVcGn78NSArH7vXIYqfoO1BuhBoCv_kQAvD_BwE)
My source of choice for stock images.
17. [StackEdit](https://stackedit.io/)
	It's a free, online note-taking and markdown application. I used it to create the README file for GitHub.
18. [Webmaker App](https://webmaker.app/app/) It is a free application similar to codepen, used to create and save the work locally. I use it to implement and experiment with using components of different frameworks that I am using, so I am familiar with how to use them when I come to implementing them in my work. 

## TESTING
[TESTING/Testing Checklist](/documentation/testing.md#testing-checklist-development-deployment)
### Research

[TESTING/Research](/documentation/testing.md/#research)

---

[notes about research for project elements]

- ***Stock images*** [Deposit Photos](https://depositphotos.com/?gclsrc=aw.ds&&utm_source=google&utm_medium=cpc&utm_campaign=DP_EU_EN_Brand_Search&utm_term=depositphotos&gclid=CjwKCAjwuvmHBhAxEiwAWAYj-EVeHDBPdjs594mAT_HDLeFGM_g2IVcGn78NSArH7vXIYqfoO1BuhBoCv_kQAvD_BwE), my first stop for stock images when I need them. I found the pictures I needed for the image slider and also for the parallax. 



### Development
[TESTING/Development](/documentation/testing.md/#development)


[notes about creating the project]

#### Create Project

- **Create Project Repository** I used the Code Institute [gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template). I clicked on "Use this template" and created my project repository name "mp3-garden-journal". I then opened this in GitPod to start the project. 

-   **Initialise Git**  To begin my project, I started with  `git init`  to initialize git within the project.
    
-   **Git Ignore**  I created a  **.gitignore**  file to add files and directories I didn't want to upload to GitHub.
    
    `git echo "file_name" >> .gitignore`  is the terminal command I used to add files and directories to  **.gitignore**.

- **Create Application File Structure**
	 - Once I had the project in GitPod,  I created the initial file structure needed to get started.
	 ***Create folders***
		```bash
		mkdir templates static static/css static/js static/images 
		mkdir documentation documentation/images documentation/images/wireframes
		```
		
		***Create files*** [update file structure]
		```bash		
		touch app.py env.py Procfile README.md css/style.css js/main.js 
		touch templates/base.html templates/home.html
		```
		```bash
		|-- documentation
		|	|-- images
		|	|	|-- wireframes
		|-- static
		|	|-- css
		|	|	|-- style.css
		|	|-- js
		|	|	|-- main.js
		|-- templates
		|	|-- base.html
		|	|-- home.html
		|--	.gitignore
		|-- app.py
		|--	env.py
		|--	Procfile
		|--	README.md
		|--	requirements.txt

		```
		
- **Implement Django** [notes about implementation of Django]

 - **Implement  Templates** [notes about the template implementation]

- **Create login and register page and function** [user profile notes?]

[crud notes if any?]

 - **Add Create Functionality**
 
 - **Add Update Functionality**		

 - **Add Delete Functionality**

 
#### TESTING DEVICES INFORMATION (update operating systems)
[TESTING/Testing Devices](/documentation/testing.md/#testing-devices)
**Personal Testing Devices/ Software/ Browsers**

-   Macbook Pro (15-inch)
    -   macOS Big Sur 11.2.3
        -   Safari Version 14.0.3 (16610.4.3.1.7)
        -   Chrome Version 90.0.4430.72 (Official Build) (x86_64)
        -   Firefox 88 (64-bit)
    -   Windows 10 (bootcamp)
        -   Microsoft Edge
        -   Chrome
        -   Firefox
-   Dell 2419 Monitor
-   iPad Air
-   iPhone 11 Pro

**Secondary Testing Device/ Sofware/ Browser**

-   HP ProDesk 600 Desktop PC
    -   Windows 10 Pro
        -   Microsoft Edge Version 90.0.818.42 (Official Build) (64-Bit)
        -   Firefox 78.10.0esr (64-Bit)
        -   Chrome Version 90.0.4430.85 (Official Build) (64-Bit)
-   AOC 22E15 21.5-inch Full HD 1920x1080 at 75 Hz
- 
#### Git Version Control 
[notes about use of git version control]

**ERROR Pages**
[404, 405, 500 error pages]

### Deployment
[TESTING/Deployment](/documentation/testing.md/#deployment)
[Deployment notes]

[TESTING/Testing Checklist](/documentation/testing.md#testing-checklist-development-deployment)

#### Forking or Cloning [project]
[instructions on how to fork or clone the project]

### Feedback
[add feedback about the site/ project]

### Credits
[add credits for any code used from other parties]

## NOTES
[additional notes about the project, if any]

## IMPROVEMENTS/ FUTURE FEATURES

## BUGS and ISSUES
See also [TESTING/Issues and Fixes](/documentation/testing.md/#issues-and-fixes)
See also [README/Database Issues and Notes](/README.md/#database-issues-and-notes)

##### ISSUE: [NUMBER]
**ISSUE_NAME**
**Issue**
**Description**
**Troubleshooting**

