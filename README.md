
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
- [x] I click the header cart icon and the modal cart opens from the right.
- [x] The cart displays the cart contents, a thumbnail, item quantity, and subtotal. 
- [x] I change the quantity and click the update icon link. The cart subtotal and total changes to reflect the new quantity.
- [x] I click on the delete item icon and the item is deleted from the cart.
- [x] I click on the View Cart button and am redirected to the cart page.
- [x] I click on the Continue to Checkout button and am redirected to the checkout page. 
- [x] I click the close icon in the top right of the cart modal and the modal closes.
- [x] I click anywhere outside of the cart modal and the modal closes.
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
Form fields are required, and I have implemented Bootstrap 5 JS validation. Regex has been added text and email fields to accept English and German letters. Regex min/max character validation added to inputs. Regex special characters excluded from validation success requirements.
- [x] I click submit without entering anyting into the form and the bootstrap danger styles kick in and display error messages. 
- [x] I enter text into one field at a time and the styling changes to success once the regex requirement has been passed. 
- [x] I click submit when the form is complete, and a success message informs me the message has been sent. 
- [x] I check my email and I have received a confirmation email from Shop for Buddhas informing me they have received my message.
- [x] I check the admin, and a copy of the message has been saved in the profile admin. 

---
### Footer
- [x] **Social icons** 
	- [x] **Facebook Icon -** I click on the Facebook icon and it opens to the Facebook page for KIBI (Karmapa International Buddhist Institute) in a separate browser tab.
	- [x] **Github -** I click on the Github icon and it links to my Github profile in a separate tab. 
	- [x] **Linkedin -** I click on the Linkedin icon and it links to my Linkedin profile in a separate browser tab. 
- [x] **Terms and Conditions link -** I click on the Terms and conditions link and it opens the Terms and Conditions page.
- [x] **Privacy Policy link -** I click on the Privacy Policiy link and it opens the Privacy Policy Page. 
- [x] **Contact Us link -** I click on the Contact Us link and it opens the home page, and scrolls to the contact section of the home page.
---
### Product Page
#### Product Content View
- [x] **Product Grid view** I open the product page and the products are displayed in a responsive Bootstrap 5 grid.
- [x] **Product Layout and view**
	- [x] **Image links -** I click on the image and it redirects me to the product details page. 
	- [x] **Title links -** I click on the product name and it redirects me to the product details page. 
	- [x] **Rating Stars -** The rating stars are displaying the correct rating per expectation.
	- [x] **Category links -** I click on the product category tag and it redirects me to the product page filtered by the selected category. 
	- [x] **Price -** The price is displaing correctly as expected.
	- [x] **Favorite Icon** 
		- [x] **Favorited -** A read heart is displayed for items added to favorites.
		- [x] **Not favorited -** An outlined heart with no fill is displayed for items not added to favorites. 
	- [x] **Product Owner Links**
		- [x] **Edit link -** The edit product link is displayed for products owned by teh session user. 
		- [x] **Delete link -** The delete product link is displayed for products owned by teh session user. 
- [x] **Search filter sorting by** 
	- [x] **Price -**  I click the select input filter by price high to low, and the products are sorted in price order from high to low. Likewise from low to high, the products are filtered accordingly.
	- [x] **Rating -**   I click the select input filter by rating high to low, and the products are sorted in rating order from high to low. Likewise from low to high, the products are filtered accordingly.
	- [x] **Name -**   I click the select input filter by name high to low, and the products are sorted in name order from high to low. Likewise from low to high, the products are filtered accordingly.
	- [x] **Category -**   I click the select input filter by category high to low, and the products are sorted in category order from high to low. Likewise from low to high, the products are filtered accordingly.
- [x] **On hover -** On hovering over a product, a quick view icon block becomes visible. (a favorite icon, a view icon, and a cart icon)
	- [x] **Quick add to favorites** 
		- [x] **Anonomous Users -** As an anonomous user, I click on the favorite icon, and I am redirected to the login page. A message asks me to log in to add items to favorites. 
		- [x] **Session Users -** 
			- [x] **Add to Favorites -** As a session user, I click on the product favorite icon, and a message informs me the product has been added to my favorites. The heart changes color to a red filled heart. 
			- [x] **Remove from Favorites -** As a session user, I click on the product red favorite icon , and a message informs me the product has been removed from my favorites. The heart changes color to a outlined heart with no fill color. 
	- [x] **Quick view button -** I click on the quick view button and the image opens in a lightbox. I click outside the lightbox and it closes.
	- [x] **Quick add button -** I click on the quick add to cart icon and the item is added to the shopping cart. A message appears informing me the item has been added to the cart.
---
### Product Detail Page
- [x] **Product Layout and view -** I click on the product image and it opens the product detail page. 
	- [x] **Image links -** I click on the image and it links to the image lightbox.
	- [x] **Image lightbox -** I click outside the image lightbox and the lightbox closes.
	- [x] **Content as required -** The product content is all displayed correctly per design.
	- [x] **Category links -** The category tag opens to display the product list filtered by the selected category.
	- [x] **Increment/Decrement input** I click on the plus icon, and it increases the quantity, I click on the minus icon and it decreases the quantity.
		- [x] **Minimum Value -** The minimum value in I can enter in the input is 0. 
		- [x] **Maximum value -** The maximum value I can enter in the input is 99.
	- [x] **Add to Cart Button -** I click add to cart and quantity selected is entered into the shopping cart. A success message informs me the item has been added to the shopping  cart. 
	- [x] **Favorites icon -** The favorite icon is displayed beside the add to cart button. 
	- [x] **Add to favorites -** 
		- [x] **Anonomous Users -** Adding to favorites requires authentication. The outline heart is displayed for all items for anonomous users. I click on the heart and and redirected to the login page. A toast message informs me that I need to log in to add items to favorites. 
		- [x] **Session Users -** 
			- [x] I click on the outlined heart, the color changes to a red filled heart, and a toast message informs me the item has been added to favorites. 
				- [x] I navigate to my profile favorites tab, and the item is displayed in my favorites list. 
			- [x] I click on the red filled heart, it changes to an outlined heart and a message informs me the item has been removed from favorites. 
				- [x] I navigate to my profile favorites tab, and the item has been removed from my favorites list. 
	- [x] **Continue Shopping button -** I click the ```Continue Shopping``` button and I am redirected to the shop page showign all products.
	- [x] **Shopping Cart button -** I click on the ```Shopping Cart``` button and I am redirected to the shopping cart page. 
	- [x] **Product Owner Links -** I log in as a vendor. All products owned by the authenticated vendor display an edit and delete link. The edit and delete links are not visible for products not owned by me. 
		- [x] **Edit link -** I click on the edit link and I am redirected to the eidt product page, where a form containing the products information is displayed. I edit the product details, and click update product. I am redirected back to the product view and the product details have been updated. 
		- [x] **Delete link -** I click on the delete product link. A bootstrap danger styled modal opens.
			- [x] **Delete Modal**
				- [x] **Modal Content -** The content informs be the product "SKU", and product "name" will be deleted from the database. I am asked if I am sure I want to delete the product. The content is clear and correct.
				- [x] **Cancel Button -** I click the cancel button and the modal closes.
				- [x] **Delete Button -** I click the delete button and a message informs be the product has been deleted. I am returned to the product page. 
---
### Shopping Cart Page
- [x] **Empty Cart view** I naviagate to the cart page when I have an empty cart. A message informs me the cart is empty, and a link provides me a way to continue shopping. 
- [x] **Cart items** I add an item to my cart, and navigate to the shopping cart page. The item is displayed, along with the subtotal, delivery cost, and grand total. 
	- [x] **Item image -** A thumbnail image of the product is visible. 
		- [x] **Image lightbox -** I click on the thumbnail and a lightbox opens displaying the product image. I close the lightbox and return to the cart page. 
	- [x] **Item Name -** The item name is displayed and in the primary link color. 
		- [x] **Links to Product View -** I click on the product name and am redirected to the product view page. It links correctly to the product page. 
	- [x] **Item price -** The item price is displayed correctly. 
	- [x] **Increment quanity** I click the plus sign beside the quantity input and with each click the quantity is incremented by one. 
	- [x] **Decrement quanity** I click the minus sign beside the quantity input and with each click the quantity is deccremented by one. 
		- [x] **Minimum Value -** The minimum value I can decrement to is 0.
		- [x] **Maximum value -** The maximum value I can increment to is 99.
	- [x] **Icon Update Button -** I change the quantity in the quantity input, and click the update icon button. The cart is updated, showing the new quantity, subtotal, and grand total. 
	- [x] **Icon Delete Button -** I click delete and the item is deleted from the cart. 
	- [x] **Item subtotal -** When i udpdate the cart quantity the item subtotal is also updated. 
		- [x] **Subtotal Updates -** When i udpdate the cart quantity the cart subtotal is also updated. 
	- [x] **Continure Shopping button -** I click the continue shopping button and am redirected to the shopping page. 
	- [x] **Coupon Code form -** I enter a value or string into the coupon input and click apply. 
		- [x] **Toast message -** A toast message informs me the entered coupon  is invalid. 
	- [x] **Cart Subtotal, Delivery, Grand Total -** Cart total, delivery, and grand total are all correct and update each time the cart is updated. 
	- [x] **Proceed to Checkout button -** I click on the proceed to checkout button and am redirected to the checkout. 
---
### Checkout Page
- [x] **Order Summary -** An order summary displays the cart contents, order total, delivery cost, and grand total. The details are corrrect. 
- [x] **Shipping address form -**
	- [x] **Non-authenticated users**
		- [x] **Form unfilled -**
		- [x] **Create an account link -**
		- [x] **Login link -**
	- [x] **Authenticated users**
		- [x] **Form automatically filled -** In the form, my saved account registration and profile details are already filled in. 
		- [x] **Save to profile checkbox -** The "save this delivery information to my profile is also checked"
- [x] **Adjust Cart button -** I click the adjsut cart button and am redirected back to the cart. 
- [x] **Payment: Credit Card Details -** I enter the payment details as follows, CVC, Expiry date, and card number.

**Requires:**  

	Any CVC
	Any date in the future for expiry date
	Any 5 digit number for postal code
	Card 4242424242424242 - Successful payment test
	Card 4000000000009995 - Failed payment test
	Card 4000002500003155 - Requires authentication test

- [x] **Test Successful Payment -** I enter card number 4242424242424242, click complete order, a success message informs me the payment was successful and I am redirected to the checkout success page displaying the order details. 
- [x] **Test Failed payment -** I enter card number 4000000000009995, click complete order, I am returned to the shckout page and an error message informs me the card has insufficient funds. 
- [x] **Test Requires authentication -** I enter card number 4000002500003155, click complete order, a Stripe modal appears asking form authentication. I click the complete authentication, a success message informs me the order has been processedm and I am redirected to the checkout success page displaying the order details. 
- [x] **Test Stripe Webhooks -**
- [x] **Complete Order button -** In all the above tests the complete oder button works. 
- [x] **Payment success confirmation message -** In all the above cases a toast message was displayed informing me of the success or failure of the action. 
- [x] **Payment success confirmation email -** I received confirmation emails for both the above successful purchases. 
- [x] **Order details saved to profile -** I navigate to my profile orders tab and the order has been added to my orders list.

---
### Stripe Webhooks 
- [x] **payment_intent.payment_failed -** Send a test event to a webhook endpoint. 
Event type - payment_intent.payment_failed
Response - Test webhoook sent successfully.
Webhook received: payment_intent.payment_failed  
![](/documentation/images/payment_intent_failed.png)  
- [x] **payment_intent.succeeded -** Send a test event to a webhook endpoint.  
Event type - payment_intent.succeeded
Response - Test webhoook sent successfully.  
Webhook received: payment_intent.succeeded | SUCCESS: Created order in webhook  
![](/documentation/images/payment_intent_succeeded.png)  


---
### Profile Page
Navigate to the user profile by clicking the ```My Profile``` link in the header account icon dropdown. 
- [x] **Personalised Profile Heading -** The heading of the profile page is personalised, with ```first_name last_name's Profile```. 
- [x] **Personalised Welcome message -** There is also a message, ```Welcome first_name!```.
- [x] **User Profile Menu**
	- [x] **All Users (Customers and Vendors)**
		- [x] **Profile Tab**
		My registration informtion is displayed in read only format. (Name, Username, Email, User Type, Date Joined, Last Login)
		- [x] **Account Info Tab**
			- [x] **Default Delivery and Profile Info**
		My profile information is displayed in a form that can be edited and updated. I update my information and click the update information button. A success message is displayed, and I am returned to the main profile tab. I check in the Account Info tab and the information has been updated. 
			- [x] **Account Management**
				- [x] **Change Password -** I click the change password link and I'm redirected to the Change Password page. 
					- [x] I enter my current password, a new password, the new password again, and click "Change Password". 
					- [x] A success message confirms the password has been updated.
					- [x] I log out, and then login again using my new password. I confirm that the password has been updated.
				- [x] **Manage Email -** I click "Manage Email" and am redirected to the email management page. 
					- [x] **BUG in Allauth template** The radio boxes with the emails and the email status were not being displayed. There was an issue with the positioning of the radio box label closing tag. I move it to the end of the label, then the check boxes were showing. Then I added jinja to display each email beside the radio box. I added Bootstrap 5 classes and grid for responsive display. 
					- [x] I enter an email in the add email address, click add email and a message informs me a confirmation email has been sent to my new email.
					- [x] The page refreshes and the new email is displayed in the list of account emails.
					- [x] It is tagged as unverified.
					- [x] I check my email, and click on the verify email link, and verify the email.
					- [x] Checking my email management page and the email is now verified.
					- [x] I select the new email and click "Make Primary". The primary email is changed.
					- [x] I check in the admin and confirm the primary email has been changed.
					- [x] I select an email and click re-send verification, and a verification email is sent to the email, with a link to click and verify the email.
					- [x] I select an email and click remove. A success message informs me the email has been removed from my account.
				- [x] **Close Account -** I click "Close Account", a bootstrap danger styled modal opens warning me the account will be closed and I will no longer have access. 
					- [x] I click Cancel and the modal closes.
					- [x] I click Close Account and A message informs me the accoutn has been closed. I am logged out to a page that informs me the account is not active. 
		- [x] **Orders Tab -** I open the profile order tab and a list of my orders is displayed.
			- [x] **Order Details -** The order number, order date, order items, item quantity, and order total is displayed for each order. 
			- [x] **Order Number Link -** The order number a link. 
				- [x] I click on a order number link and I am redirected to the order confirmation page displaying the order details. 
				- [x] A toast message informs me I am viewing a past order.
		- [x] **Favorites Tab -**
			- [x] **Favorites Products Grid -** I click on the favorites tab and the favorites list is displayed in a bootstrap grid.
			- [x] **Image Lightbox -** I click on the image and it opens in an image lightbox. 
			- [x] **Product Name Link -** I click the product name and am redirected to the product detail page. 
			- [x] **Product Category Link -** I click the category and it opens a page displaying all the products in that category. 
			- [x] **Product Price -** The product price is displayed.
			- [x] **Remove Link button -** I click on the remove link below an item and the page refreshes. A toast message informs me the item has been removed from my favorites. 
				- [x] **ISSUE:** When the page refreshes it goes to the profile tab. This is not ideal, and I plan to implement Ajax to update the list without refreshing the page.
	- [x] **Vendor/ Admin Only Tabs -** The following two tabs are displayed for vendors only.
		- [x] **Products Tab -**
			- [x] **Product Layout Grid -** I open the profile products tab and a list of the vendors products is dispplayed. 
			- [x] **Only Vendors Products Displayed -** I confirm that only the vendors items are displayed by changing ownership of some products in the admin. The products are no longer displayed in this vendors  profile. 
			- [x] **Image lightbox -** I click the image and it opens the image lightbox.
			- [x] **Product Name Link -** I click the product name and it redirects me to the product detail page. 
			- [x] **Product Category Link -** I click the category and it opens a page displaying all the products in that category. 
			- [x] **Product Price -** The product price is displayed.
				- [x] **Edit link -** I click on the edit link and I am redirected to the eidt product page, where a form containing the products information is displayed. I edit the product details, and click update product. I am redirected back to the product view and the product details have been updated. 
				- [x] **Delete link -** I click on the delete product link. A bootstrap danger styled modal opens.
					- [x] **Delete Modal**
						- [x] **Modal Content -** The content informs be the product "SKU", and product "name" will be deleted from the database. I am asked if I am sure I want to delete the product. The content is clear and correct.
						- [x] **Cancel Button -** I click the cancel button and the modal closes.
						- [x] **Delete Button -** I click the delete button and a message informs be the product has been deleted. I am returned to the product page. 
		- [x] **Sales Tab**
			- [x] **Vendor Sales List -** I open the vendor sales tab and a list of the vendor product sales is displayed.
				- [x] To test this, I create an order for 4 seaparate items, in different quantities, belonging to 3 different vendors. 
				- [x] I check the order, and the line items in the Django admin. The details are correct, and showing the different line items product owners. 
				- [x] In the profile for each vendor, the items for each vendor are showing in the vendor sales tab. The totals are correct. 
			- [x] **Sales Details -** The date, order number, vendor, item quantity, order items, and line item total is displayed for each item. 
			- [x] **Sale Order Number Link -** The order number links to the vendor sale order details. 
				- [x] I click on a order number link and I am redirected to the sale  confirmation page displaying the sale item details. 
				- [x] A toast message informs me I am viewing a sale confirmation for a past sale.
---
### Blog All Pages  
I navigate to the blog, and the content is displayed as per design. A featured article, the blog posts, and a right sidebar.
- [x] **Blog Right Sidebar**
	- [x] **Blog Search -** I enter various search terms in the blog search input, and it returns related results for the serach term within the blog posts. 
	- [x] **Blog Categories -** I click on the category in the blog sidebar and the related items within that category are returned.
	- [x] **Recent Posts -** In the recent posts, the four most recent posts are displayed. This is by design. 
	- [x] **Blog Archives -** The blog archives displays Year, and month with the total items from that month. Clicking on the month displays the posts from that month. 
	- [x] **Blog Tags -** I click on the blog tags and the items with that tag are displayed. 
- [x] **Blog Featured Post**
	- [x] A featured post is displayed at the top of the page. This option is checked in the Post admin. 
	- [x] In the post admin I uncheck the option and the featured post is no longer visible. 
	- [x] I click on the post image, or read more link, it opens and displays the post.
	- [x] **Note** The featured post is currently displayed on all ```blog_posts``` pages. I intend to change this so it is visible only on the first ```blog_posts``` page. 
- [x] **Blog Posts Page**
	- [x] Regular posts are displayed below the featured post.
	- [x] The posts are paginated, 2 posts per page.
	- [x] I click on the image or readme link of the regular post. The post is opened and displayed.
- [x] **Post Detail Page**
	- [x] **Post -** The blog detail page is per design. The date, posted by, article title, article image, article and article tags. Below the article is a form for the user to leave a comment. 
- [x] **Blog Post Comments**
	- [x] The post comment form is available for authenticated users. As a logged out user I confirm that ```Register``` and ```Login``` links are displayed for users if they want to leave a comment.
	![](documentation/images/blog-comments-login.png)  
	- [x] I log in and on the same page now there is a "```Leave a comment```" link displayed instead.  
	![](documentation/images/blog-comments-logged-in.png)  
	- [x] I click on the "```Leave a comment```" link and the comment form toggles open and is now visible.  
	![](documentation/images/blog-comments-form.png)  
		- [x] I enter my name and a comment, and click submit. 
		- [x] A toast message informs me the comment has been posted. It is now displayed below the article. 
		- [x] The page refreshes, the comment form no longer visible, and the comment is displayed below the "```Leave a comment```" link.
	- [x] **Comments View -**
		- [x] The comment is displayed in a blockquote, with my name, and how long ago it was posted.
		- [x] The comment section heading displays teh numbe rof comments in brackets. This is updated when I add a comment. 
		- [x] The comments are posted in date order, newest comments are at the top. 

---
### Toast Messages

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
***Safari Jumbotron Background Image***
There is a bug that is limited to Safari on iPhones. On an iPhone 13 Pro, the Buddha background image is not present. The same issue is not present when checking the iPhone in Chrome and Safari web developer tools. It is not present on tablets, or on Apple or PC desktops. 
On my macbook pro I checked the iPhone source code in the Safari developer tools, and was unable to locate the error. 
At this point, I put it down to apple, but am contiuing to investigate. The issue is not critical as the dark background on the small screen of the iPhone is acceptable. 

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