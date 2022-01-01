
# TESTING

  ![](documentation/images/autumn-readme.png)   

## TESTING PLAN (Pre-development)

[README](/README.md) Documentation for the project

[README/Testing](/README.md/#testing)

### RESEARCH

[README/Research](/README.md/#research)

#### Required elements

- Research and read about Django Models.
- Investigate what components will be suitable and meet the needs of this project.
- Research how the components work and how to write code to implement them.
- It is crucial to understand how the components function and what I can expect from them.
- Use [Web Maker App](https://webmaker.app/app/) to experiment, learn, and implement instances of the components to see which are better suited for Shop for Buddhas.
- Research and study up on Django Models to see how to best design a Schema that will fulfil the needs of Shop for Buddhas.

### DEVELOPMENT

[README/Development](/README.md/#development)

#### HTML

- Incorporate core feature components using HTML5 and Bootstrap5. 
- Core components to incorporate:
	- Header will be a main feature of the site
		- Nav-bar/ Off-canvas
		-  Search bar
		- Shopping cart.
	- A full page modal incorporating the shop search.
	- A quick view modal side shopping cart to view the cart items. 
	- Carousel to display testimonials.
	- Contact form.
	- Product forms for adding, updating and removing items. 
	- Tab Pills for the User Account Profile page.
	- Social Icons 
- Incorporate Bootstrap Breakpoints as media queries in CSS for responsive display. - Use Chrome DevTools to ensure positioning of elements for each breakpoint.

#### JavaScript/ jQuery
- As Bootstrap 5 now uses Vanilla JS, my goal is where possible to learn and use this in other scripts as well. jQuery may be used in some functions of working with the shop functions.

### DEPLOYMENT
[README/Deployment](/README.md/#deployment)

#### Test for production

- **Test local and Test live**

	- Create the application in Gitpod, using the python server to view the work in the browser. It has two advantages:
		- The Python server and pep8 syntax checking ensure the code is compliant and structured correctly; otherwise, the server shuts down.
		- Set `debug=True`, ensuring that Jinja errors show in the browser, with a lot of detail, so I can fix mistakes as I go.
		- Due to the nature of Python and Jinja, checking is completed in the process of development while writing route paths and functions that run the app.
		Based on experience, I need to deploy the project live to Heroku to check the live site along the way, ensuring expected behaviour is consistent in the live site.
	- Compare and test development and deployed versions of the website.
		- Ensure the deployed site is the same and there are no bugs.
		- Inputs, forms, features need to display and function as expected.

- **Responsiveness**
	- Chrome DevTools:
		- Test by screen sizes
		- Test by viewing media queries which will specifically include Bootstrap breakpoints.
		- Test on different devices, different operating systems, different browsers, screen sizes.
	- Share the application to get third-party feedback

- **Function**
	- Test on different devices, operating systems, and browsers.
	- Test all external links, inputs, forms, navigation links, and features.

- **Custom Error Pages**

	- Create 404 Page not found page.
	- Create 405 Method Not Allowed page
	- Create 500 Server Error page

- **User Experience**

**Feedback**: Share the application to get feedback and test the UI to see how users intuit the application process.

- **User Stories**: Check the application fulfils the needs expressed in the user stories.

### DEVELOPMENT SETUP

#### Code Editor

[Gitpod](https://www.gitpod.io/): I chose to use Gitpod to develop the site. This enables me to get support from Code Institute if needed. It makes it easy to share the workspace and get help troubleshooting problems.

- Python3 Development Server: I use the Python3 command `python3 manage.py runserver` to run my application in the development server and view the work live in the browser. This enables me to check incrementally as I develop code, so it is clear where errors might be.

My preferred browser for development is Chrome DevTools. I have a USB-C to dual HDMI hub for my MacBook Pro, with 2 x Dell U2419H monitors, a wireless keyboard, and a mouse.

### TESTING DEVICES

[README/Testing Devices Info](/README.md/#testing-devices-information)

#### MacBook Pro 15 inch

```shell
- Operating System
- macOS Big Sur 11.2.3
- Safari Version 14.0.3 (16610.4.3.1.7)
- Chrome Version 90.0.4430.72 (Official Build) (x86_64)
- Firefox 88 (64-bit)
- Windows 10 Pro (Boot Camp installation)
- Microsoft Edge Version
- Firefox
- Chrome Version
- External Monitors
- 2 x Dell U2419H Monitor 23.8-inch Full HD 1920 x 1080 at 60 Hz
```

#### HP ProDesk 600 Desktop PC

```shell
- Operating System
- Windows 10 Pro
- Microsoft Edge Version 90.0.818.42 (Official Build) (64-Bit)
- Firefox 78.10.0esr (64-Bit)
- Chrome Version 90.0.4430.85 (Official Build) (64-Bit)
- Monitor
- AOC 22E15 21.5-inch Full HD 1920x1080 at 75 Hz
```

  

#### Apple iPad Air Gen 1 9.7 inches 4:3 ratio

  

```shell
- Operating System
- iOS 12.5.2 (16H30) released March 26
- Screen resolution
- 1536 x 2048 pixels, 4:3 ratio (~264 ppi density)
```

#### Apple iPhone 11 Pro
 
```shell
- Operating System
- iOS 14.4.2
- Screen resolution
- 2436‑by-1125‑pixel resolution at 458 ppi
- 5.8‑inch (diagonal) all‑screen OLED Multi‑Touch display
- Width: 2.81 inches (71.4 mm)
- Height: 5.67 inches (144.0 mm)
```

---------- 

## TESTING CHECKLIST (Development-Deployment)

[README/Testing](/README.md/#testing)

Testing of the site will cover the needs and requirements of different user types. Here I will define the user types to be referred to in the testing as follows.
1. **Anonomous User** refers to all users not logged in.
2. **Session User** refers to all registered and logged in users.
3. **Customer** refers only to a registered and logged in customer. 
4. **Vendor** refers to a registered and logged in vendor.

## Home Page 
### Header
#### Navbar Links
- [x] I click on the logo and it links to the home page.
- [x] I click on the Home link in the navbar and it links to the home page.
- [x] I click the Shop/By Price link and it opens the product page, with products filtered by price
- [x] I click on the Shop/By Rating and it opens the product page, with products filtered by rating.
- [x] I click on the Shop/By Category and it opens the product page, with products filtered by category.
- [x] I click on the Shop/All Products and it opens the product page, displaying all products.
- [x] I click on the Shop/Oxidised and it opens the product page, displaying oxidised Buddha statues.
- [x] I click on the Shop/Half Gold and it opens the product page, displaying Half Gold Buddha statues.
- [x] I click on the Shop/Full Gold and it opens the product page, displaying Full Gold Buddha statues.
- [x] I click on the Shop/All Buddhas and it opens the product page, displaying all Buddha statues.
- [x] I click on the Shop/108 Beads and it opens the product page, displaying all malas with 108 beads.
- [x] I click on the Shop/Wrist Malas and it opens the product page, displaying all wrist malas.
- [x]  I click on the Shop/All Malas and it opens the product page, displaying all malas.
- [x] I click on the blog link and it opens the blog page.
- [x] I click on the contact link and it scrolls the home page to the contact form at the bottom of the page.
- [x] I click the Facebook icon in the top right of the navbar and it open a Facebook page for the KIBI (Karmapa International Buddist Institute).
- [x] I click the GitHub icon in the top right of the navbar  and it links to my githib profile. 
- [x] I click on the Linkedin icon in the top right of the navbar  and it links to my Linkedin profile.
#### Navbar Login/ Logout views
**Anonomous Users**
- [x] The login link is visible in the top right of the navbar for anonomous users.
- [x] I click the login link and it opens the login page with a link also to the register page. 
- [x] I hover on the "Account Icon" and a dropdown appears displaying login and register links. 
- [x] I click the login link and the login page opens. 
- [x] I click the register link and the register page opens.

**Customers**
- [x] The logout link is visible in the top right of the navbar. 
- [x] I click the logout link and it opens the logout page with buttons to confirm the logout.
- [x] I hover over the "Account" icon and a dropdown appears displaying a link to my profile, and a logout link.
- [x] I click the "My Profile" button and am redirected to my account profile page. 
- [x] I click the logout link and it opens the logout page with a button to confirm the logout.

**Vendors**
- [x] The logout link is visible in the top right of the navbar. 
- [x] I click the logout link and it opens the logout page with buttons to confirm the logout.
- [x] I hover over the "Account" icon and a dropdown appears displaying a link to my profile, a Product Management link, and a logout link. 
- [x] I click the "My Profile" button and am redirected to my account profile page. 
- [x] I click the product management link and am redirected to the add product page.
- [x] I click the logout link and it opens the logout page with a button to confirm the logout.

#### Navbar Shopping Cart Icon
- [x] The cart icon has a bubble showing the cart quantity of items. This is updates as products are added to the cart. I confirm this by adding items to the cart. 
- [x] When I click on the icon, the quick view modal cart opens showing the cart contents. 
---
#### Modal Quickview Cart
---
### Jumbotron
The Jumbotron is the main feature of the landing page. It is full screen with a repeating dark background image, and a buddha image positioned to the right of the screen. In the center of the page is some text, with a "Shop Now" button. 
- [x] I confirm the content is well balanced and positioned for all screens. 
- [x] I click the shop now button and it takes me to the shop page.
---
### Services Section
Six blocks layed out in a grid, each explaining in breif a different aspect of what Shop for Buddhas has to offer. 
- [x] I confirm the scope of services as outlined in user stories is covered in this brief explanation of services on offer.
---

### Our Products Section
This block describes the primary products sold by Shop for Buddhas. An image accompanied by a brief explanation is designed to invoce curiosity. 

---
### Testimonial Section
- [x] I confirm that the testimonial carousel is working and displays the user testimonials. 
- [x] I confirm that the rating stars display the correct rating selected by the user. 

**Session Users**
A button is visible for session users and positioned on the top left of the testimonial carousel. It is meant to be non intrusive, and expands when hovered over showing text "Leave a testimonial". 
- [x] I click on the button and am redirected to a page with the testimonial form. 
- [x] I complete the form and submit it. A success toast is displayed informing me the testimonial has been submitted. 
- [x] The testimonial is not displayed as it needs to be approved.
- [x] I check in the admin and approve the testimonial. It is then shown in the testimonial carousel. 
---
### Contact Section
The contact section displays a phone number, address and the office hours. 
#### Contact Form
The contact form is uses Bootstrap 5 elements, with crispy forms and the Django "csrf_token" to prevent cross site request forgery attacks. 

**Form Validation**
Form fields are required, and I have implemented Bootstrap 5 JS validation. Regex has been added text and email fields to include English and German letters.
- [x] I click submit without entering anyting into the form and the bootstrap danger styles kick in with error messages. 
- [x] I enter text into one field at a time and the styling changes to success once the regex requirement has been passed. 
- [x] I click submit when the form is complete, and a success message informs me the message has been sent. 
- [x] I check my email and I have received a confirmation email from Shop for Buddhas informing me they have received my message.
- [x] I check the admin, and a copy of the message is in the admin. 
---

### Footer
---
### Product Page
#### Product Content View
- [x] I hover over the procuct and the icon block containing add to favorites icon, quick view icon, and the quick add icon appears.
Icon - Add to Favorites
- [x] **Favorite Icon - Anonomous Users:** I click the add to favorites icon and I am redirected to the login page. An  info toast appears asking me to login to add items to favorites. 
- [x] **Favorite Icon - Session Users:** I click on the add to favorites icon and it changes from an outline heart icon, to a red filled heart icon. A toast message appear informing me the product has been added to my favorites. the Icon is now red. I am still on the same page.
- [x] I click on a red icon and the heart changes from a red filled heart to an outlined heart. A toast message appears informing me the product has been reomoved from my favorites. I am still on the same page.
- [x] I click the quick view icon and an image lightbox appears showing the product image.
- [x] I click outside the lightbox and the lightbox closes.
- [x] I click the quick add icon and the item is added to my cart. A toast message appears informing me the product has been added to my cart. 
- [x] I click the product image and it opens the product detail page.
- [x] I click the product name and it opens the product detail page. 
- [x] I click the product category and it opens the product page showing all items in the category.
- [x] The rating stars are displaying the product rating.
- [x] The price is displayed.
- [x] In the top right of each product, a heart is displayed, indicating if the item has been added to favorites or not.
---
### Product Detail Page

---

### Shopping Cart Page

---
### Checkout Page

---
### Blog Page

---


4. **All Users:**

5. **Session Users:**

6. **Admin Users:**

---

### ALL USERS

### SESSION USERS

### ADMIN USERS


#### 404 Errors

##### ALL USERS

- [x] Test

##### USERS NOT LOGGED IN

- [x] Test


## USER STORIES REVIEW (Development-Deployment)

[Readme/User Stories](/README.md/#user-stories)

[notes about the user stories]

### User Story Reviews

---
### As the user, ...

**As the user:**
> User story
- User Story Review

### As the owner, ...
**As the owner:**
> User story
- User Story Review

![](/documentation/images/)  


### Issues and Fixes

See also [README/BUGS and ISSUES](/README.md/#bugs-and-issues)

##### ISSUE: 1
***Issue Name***

## Validation

### Form Validation

I have multiple protections for the forms.

-   **Browser Validation** 
-   **Regex:** 


### HTML Validation
HTML validated by W3C Markup Validation Service
Source code from all pages was copied and added into the W3C validation, for the URL's as shown in the following image.
W3C Validion success for all pages: Document checking completed. No errors or warnings to show.

![](/documentation/images/validation_html.png)

### CSS Validation
CSS validated by W3C CSS Validation Service
CSS was copied and pasted into the W3C CSS Validador for all CSS files created by me.

**NOTE:**
1. All CSS was put through the [Github autoprefixer](https://autoprefixer.github.io), to add backward complatibility for the 4 last browser releases. This adds webkit prefixes that are not recognised by the W3C CSS Validator, and this is a known issue. It raises warnings for such prefixes.
2. I have used a a Bootstrap theme and included the Boostrap CSS (see static/css/bootstrap_theme.css) in my site. Bootstrap run through the W3C Validation raises many warnings, that are not critical and autoprefixing this CSS also increases the validation warnings.
3. No errors have been raised for any of my CSS.

![](/documentation/images/validation_css.png)

### JS Validation
JS was validated using [JS Hint](https://jshint.com/), and no errors were noted.

![](/documentation/images/validation_js.png)

### Python Validation
All Python files where copied and pasted into the [PEP8 online](http://pep8online.com) Python validator.
Python is PEP8 compliant, and shows one error in `settings.py`. `env' imported but unused flake8(F401) [18,5]`. The error as described is not actually an error as `env.py` is used to import protected sensitive data.
 

![](/documentation/images/validation_python.png)