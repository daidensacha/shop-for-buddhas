![](/documentation/images/mochup-light.png)

# TESTING

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
- Research and study up on Django Models to see how to best design a Schema that will fulfill the needs of Shop for Buddhas.

  

### DEVELOPMENT
[README/Development](/README.md/#development)

#### HTML

- Incorporate core feature components using HTML5 and Bootstrap5.
- Core components to incorporate:
	- Header will be a main feature of the site
		- Nav-bar/ Off-canvas
		- Search bar
		- Shopping cart.
	- A full-page modal to incorporate the shop search.
	- A quick view modal side shopping cart to view the cart items.
	- Carousel to display testimonials.
	- Contact form.
	- Product forms for adding, updating, and removing items.
	- Tab Pills for the User Account Profile page.
	- Social Icons
- Incorporate Bootstrap Breakpoints as media queries in CSS for responsive display. - Use Chrome DevTools to ensure positioning of elements for each breakpoint.

#### JavaScript/ jQuery

- As Bootstrap 5 now uses Vanilla JS, my goal is to learn and use this in other scripts as well. I may use jQuery in some functions of working with the shop functions.

### DEPLOYMENT
[README/Deployment](/README.md/#deployment)

#### Test for production

- **Test local and Test live**

	- Create the application in Gitpod, using the python server to view the work in the browser. It has two advantages:
		- The Python server and pep8 syntax checking ensure the code is compliant and structured correctly; otherwise, the server shuts down.
		- Set `debug=True`, ensuring that Jinja errors show in the browser, with a lot of detail, so I can fix mistakes as I go.
		- Due to the nature of Python and Jinja, checking is completed in the process of development while writing route paths and functions that run the app.
	Based on experience, I need to deploy the project live to Heroku to check the live site along the way, ensuring expected behavior is consistent in the live site.
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

- **User Stories**: Check the application fulfills the needs expressed in the user stories. 

### DEVELOPMENT SETUP

#### Code Editor

[Gitpod](https://www.gitpod.io/): I chose to use Gitpod to develop the site, which enables me to get support from Code Institute if needed. It makes it easy to share the workspace and get help troubleshooting problems.

- Python3 Development Server: I use the Python3 command ```python3 manage.py runserver``` to run my application in the development server and view the work live in the browser. I incrementally check my code for errors as I develop, so it is clear where errors might be.

My preferred browser for development is Chrome DevTools. I have a USB-C to dual HDMI hub for my MacBook Pro, with 2 x Dell U2419H monitors, a wireless keyboard, and a mouse.

### TESTING DEVICES
[README/Testing Devices Info](/README.md/#testing-devices-information)

#### MacBook Pro 15 inch
```bash
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
```bash
- Operating System
- Windows 10 Pro
- Microsoft Edge Version 90.0.818.42 (Official Build) (64-Bit)
- Firefox 78.10.0esr (64-Bit)
- Chrome Version 90.0.4430.85 (Official Build) (64-Bit)
- Monitor
- AOC 22E15 21.5-inch Full HD 1920x1080 at 75 Hz
```

#### Apple iPad Air Gen 1 9.7 inches 4:3 ratio
```bash
- Operating System
- iOS 12.5.2 (16H30) released March 26
- Screen resolution
- 1536 x 2048 pixels, 4:3 ratio (~264 ppi density)
```

#### Apple iPhone 11 Pro
```bash
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

Testing the site will cover the needs and requirements of different user types. Here I will define the user types to be referred to in the testing.
1. **Anonymous User** refers to all users not logged in.
2. **Session User** refers to all registered and logged-in users.
3. **Customer** refers only to a registered and logged-in customer.
4. **Vendor** refers to a registered and logged-in vendor.

## Home Page
### Header
#### Navbar Links
- [x] I click on the logo, and it links to the home page.
- [x] I click on the Home link in the navbar, which links to the home page.
- [x] I click the Shop/By Price link, and it opens the product page, with products filtered by price
- [x] I click on the Shop/By Rating, and it opens the product page, with products filtered by rating.
- [x] I click on the Shop/By Category, and it opens the product page, with products filtered by category.
- [x] I click on the Shop/All Products, and it opens the product page, displaying all products.
- [x] I click on the Shop/Oxidised, and it opens the product page, displaying oxidized Buddha statues.
- [x] I click on the Shop/Half Gold, and it opens the product page, displaying Half Gold Buddha statues.
- [x] I click on the Shop/Full Gold, and it opens the product page, displaying Full Gold Buddha statues.
- [x] I click on the Shop/All Buddhas, and it opens the product page, displaying all Buddha statues.
- [x] I click on the Shop/108 Beads, and it opens the product page, displaying all malas with 108 beads.
- [x] I click on the Shop/Wrist Malas, and it opens the product page, displaying all wrist malas.
- [x] I click on the Shop/All Malas, and it opens the product page, displaying all malas.
- [x] I click on the blog link, opening the blog page.
- [x] I click on the contact link, and it scrolls the home page to the contact form at the bottom of the page.
- [x] I click the Facebook icon in the top right of the navbar, and it opens a Facebook page for the KIBI (Karmapa International Buddist Institute).
- [x] I click the GitHub icon in the top right of the navbar, which links to my Github profile.
- [x] I click on the Linkedin icon in the top right of the navbar, which links to my Linkedin profile.
#### Navbar Login/ Logout views
**Anonymous Users**
- [x] The login link is visible in the top right of the navbar for anonymous users.
- [x] I click the login link, and it opens the login page with a link also to the register page.
- [x] I hover on the "Account Icon," and a dropdown appears displaying login and register links.
- [x] I click the login link, and the login page opens.
- [x] I click the register link, and the registration page opens.

**Customers**
- [x] The logout link is visible in the top right of the navbar.
- [x] I click the logout link, and it opens the logout page with buttons to confirm the logout.
- [x] I hover over the "Account" icon, and a dropdown appears displaying a link to my profile and a logout link.
- [x] I click the "My Profile" button and am redirected to my account profile page.
- [x] I click the logout link, and it opens the logout page with a button to confirm the logout.

**Vendors**
- [x] The logout link is visible in the top right of the navbar.
- [x] I click the logout link, and it opens the logout page with buttons to confirm the logout.
- [x] I hover over the "Account" icon, and a dropdown appears displaying a link to my profile, a Product Management link, and a logout link.
- [x] I click the "My Profile" button and am redirected to my account profile page.
- [x] I click the product management link and am redirected to the add product page.
- [x] I click the logout link, and it opens the logout page with a button to confirm the logout.
 
#### Navbar Shopping Cart Icon
- [x] The cart icon has a bubble showing the cart quantity of items. This updates when I add products to the cart. I confirm this by adding items to the cart.
- [x] When I click on the icon, the quick view modal cart opens, showing the cart contents.
---
#### Modal Quickview Cart
- [x] I click the header cart icon, and the modal cart opens from the right.
- [x] The cart displays the cart contents, a thumbnail, item quantity, and subtotal.
- [x] I change the quantity and click the update icon link. The cart subtotal and total changes to reflect the new quantity.
- [x] I click on the delete item icon and delete the item from the cart.
- [x] I click on the View Cart button and am redirected to the cart page.
- [x] I click on the Continue to Checkout button and am redirected to the checkout page.
- [x] I click the close icon in the top right of the cart modal, and the modal closes.
- [x] I click anywhere outside the cart modal, and the modal closes.
---
### Jumbotron
The Jumbotron is the main feature of the landing page. It is full screen with a repeating dark background image and a buddha image positioned to the right of the screen. There is some text in the center of the page with a "Shop Now" button.
- [x] I confirm the content is well balanced and positioned for all screens.
- [x] I click the shop now button, which takes me to the shop page.
---
### Services Section
Six blocks are laid out in a grid, each explaining, in brief, a different aspect of what Shop for Buddhas has to offer.
- [x] I confirm the scope of services as outlined in user stories is in this brief explanation of services on offer.
---
### Our Products Section
This block describes the primary products sold by Shop for Buddhas. An image accompanied by a brief explanation invokes curiosity.

---
### Testimonial Section
- [x] I confirm that the testimonial carousel is working and displays the user testimonials.
- [x] I confirm that the rating stars display the correct rating selected by the user.
**Session Users**
A button is visible for session users and positioned on the top left of the testimonial carousel. It is meant to be non-intrusive and expands when hovered over showing text "Leave a testimonial".
- [x] I click on the button and am redirected to a page with the testimonial form.
- [x] I complete the form and submit it. A success toast is displayed, informing me I have submitted the testimonial has.
- [x] The testimonial is not displayed as it needs to be approved.
- [x] I check in the admin and approve the testimonial. I now see it in the testimonial carousel.
---
### Contact Section
The contact section displays a phone number, address, and office hours.
#### Contact Form
The contact form uses Bootstrap 5 elements, crispy forms, and the Django "csrf_token" to prevent cross-site request forgery attacks.

**Form Validation**
Form fields are required, and I have implemented Bootstrap 5 JS validation. Regex has been added text and email fields to accept English and German letters. Regex min/max character validation added to inputs. Regex excludes special characters from validation success.
- [x] I click submit without entering anything into the form, and the bootstrap danger styles kick in and display error messages.
- [x] I enter text into one field at a time, and the styling changes to success once text meets the regex requirement.
- [x] I click submit when the form is complete, and a success message informs me I have sent the message.
- [x] I check my email, and I have received a confirmation email from Shop for Buddhas informing me they have received my message.
- [x] I check the admin, and the code has saved a copy of the message in the profile admin.
---
### Footer
- [x] **Social icons**
	- [x] **Facebook Icon -** I click on the Facebook icon. It opens to the Facebook page for KIBI (Karmapa International Buddhist Institute) in a separate browser tab.
	- [x] **Github -** I click on the Github icon, which links to my Github profile in a separate tab.
	- [x] **Linkedin -** I click on the Linkedin icon, which links to my Linkedin profile in a separate browser tab.
- [x] **Terms and Conditions link -** I click on the Terms and conditions link, and it opens the Terms and Conditions page.
- [x] **Privacy Policy link -** I click on the Privacy Policy link, and it opens the Privacy Policy Page.
- [x] **Contact Us link -** I click on the Contact Us link, and it opens the home page and scrolls to the contact section of the home page.
---

### Product Page
#### Product Content View
- [x] **Product Grid view** I open the product page and see the products displayed in a responsive Bootstrap 5 grid.
- [x] **Product Layout and view****
	- [x] **Image links -** I click on the image, and it redirects me to the product details page.
	- [x] **Title links -** I click on the product name, and it redirects me to the product details page.
	- [x] **Rating Stars -***The rating stars display the correct rating per expectation.
	- [x] **Category links -** I click on the product category tag, and it redirects me to the product page filtered by the selected category.
	- [x] **Price -** The displayed price is correct as expected.
	- [x] **Favorite Icon**
		- [x] **Favorited -** Favorites are marked with a red heart.
		- [x] **Not favorited -** An outlined heart with no fill is displayed for items not added to favorites.
	- [x] **Product Owner Links**
		- [x] **Edit link -** The edit product link is displayed for products owned by the session user.
		- [x] **Delete link -** The delete product link is displayed for products owned by the session user.
- [x] **Search filter sorting by**
	- [x] **Price -** I click the select input filter by price high to low, and the products are sorted in price order from high to low. Likewise, from low to high, the products are filtered accordingly.
	- [x] **Rating -** I click the select input filter by rating high to low, and the products are sorted in rating order from high to low. Likewise, from low to high, the products are filtered accordingly.
	- [x] **Name -** I click the select input filter by name high to low, which sorts the products in name order from high to low. Likewise, from low to high, the products are filtered accordingly.
	- [x] **Category -** I click the select input filter by category high to low, which sorts the products by category order from high to low. Likewise, from low to high, the products are filtered accordingly.
- [x] **On hover -** I hover over a product, and a quick view icon block becomes visible. (a favorite icon, a view icon, and a cart icon)
	- [x] **Quick add to favorites**
		- [x] **Anonymous Users -** As an anonymous user, I click on the favorite icon, redirecting me to the login page. A message asks me to log in to add items to favorites.
		- [x] **Session Users -**
			- [x] **Add to Favorites -** As a session user, I click on the favorite product icon, and a message informs me I have added the product to my favorites. The heart changes color to a red-filled heart.
			- [x] **Remove from Favorites -** As a session user, I click on the product red favorite icon, and a message informs me I have removed the product from my favorites. The heart changes color to an outlined heart with no fill color.
	- [x] **Quick view button -** I click on the quick view button, and the image opens in a lightbox. I click outside the lightbox, and it closes.
	- [x] **Quick add button -** I click on the quick add-to-cart icon and add the item to the shopping cart. A message appears informing me I have added the item to the cart.
---
### Product Detail Page
- [x] **Product Layout and view -** I click on the product image and open the product detail page.
	- [x] **Image links -** I click on the image, which links to the image lightbox.
	- [x] **Image lightbox -** I click outside the image lightbox and the lightbox closes.
	- [x] **Content as required -** The product content is displayed correctly per design.
	- [x] **Category links -** The category tag opens to display the product list filtered by the selected category.
	- [x] **Increment/Decrement input** I click on the plus icon, and it increases the quantity. I click on the minus icon, and it decreases the quantity.
		- [x] **Minimum Value -** The minimum value I can enter in the input is 0.
		- [x] **Maximum value -** The maximum value I can enter in the input is 99.
	- [x] **Add to Cart Button -** I click add to cart, and the quantity selected is entered into the shopping cart. A success message informs me I have added the item to the shopping cart.
	- [x] **Favorites icon -** The favorite icon is displayed beside the add to cart button.
	- [x] **Add to favorites -**
		- [x] **Anonymous Users -** Adding favorites requires authentication. All products have an outlined heart for anonymous users. I click on the heart, which redirects me to the login page. A toast message informs me that I need to log in to add items to favorites.
		- [x] **Session Users -**
			- [x] I click on the outlined heart, the color changes to a red-filled heart, and a toast message informs me I have added the item to favorites.
				- [x] I navigate to my profile favorites tab and see the item displayed in my favorites list.
			- [x] I click on the red filled heart, it changes to an outlined heart, and a message informs me I have removed the item from favorites.
				- [x] I navigate to my profile favorites tab and see the item is not in my favorites list.
	- [x] **Continue Shopping button -** I click the ```Continue Shopping``` button, redirecting me to the shop page showing all products.
	- [x] **Shopping Cart button -** I click on the ```Shopping Cart``` button, redirecting me to the shopping cart page.
	- [x] **Product Owner Links -** I log in as a vendor. All products owned by the authenticated vendor display edit and delete links. The edit and delete links are not visible for products not owned by me.
		- [x] **Edit link -** I click on the edit link, redirecting me to the edit product page, where a form containing the products information is displayed. I edit the product details and click update product, redirecting me back to the product view, where the details are updated.
		- [x] **Delete link -** I click on the delete product link. A bootstrap danger-styled modal opens.
			- [x] **Delete Modal**
				- [x] **Modal Content -** The content informs me I will delete the product "SKU" and product "name" from the database. I need to confirm I want to delete the product. The content is clear and correct.
				- [x] **Cancel Button -** I click the cancel button, and the modal closes.
				- [x] **Delete Button -** I click the delete button, and a message informs me I have deleted the product. The modal closes and redirects me back to the product page.
---
### Shopping Cart Page
- [x] **Empty Cart view** I navigate to the cart page when I have an empty cart. A message informs me the cart is empty, and a link provides me a way to continue shopping.
- [x] **Cart items** I add an item to my cart and navigate to the shopping cart page. I confirm the item is in the cart, and the subtotal, delivery cost, and grand total.
	- [x] **Item image -** A thumbnail image of the product is visible.
		- [x] **Image lightbox -** I click on the thumbnail, and a lightbox opens, displaying the product image. I close the lightbox and return to the cart page.
	- [x] **Item Name -** The item name is displayed in the primary link color.
		- [x] **Links to Product View -** I click on the product name, redirecting me to the product view page. It links correctly to the product page.
	- [x] **Item price -** The item price is displayed correctly.
	- [x] **Increment quantity** I click the plus sign beside the quantity input. With each click, the quantity is incremented by one.
	- [x] **Decrement quantity** I click the minus sign beside the quantity input. With each click, the quantity is decremented by one.
		- [x] **Minimum Value -** The minimum value I can decrement to is 0.
		- [x] **Maximum value -** The maximum value I can increment to is 99.
	- [x] **Icon Update Button -** I change the quantity in the quantity input and click the update icon. The cart is updated, showing the new quantity, subtotal, and grand total.
	- [x] **Icon Delete Button -** I click delete, and the item is deleted from the cart.
	- [x] **Item subtotal -** When I update the cart quantity, the item subtotal is also updated.
		- [x] **Subtotal Updates -** When I update the cart quantity, the cart subtotal is also updated.
	- [x] **Continue Shopping button -** I click the continue shopping button and am redirected to the shopping page.
	- [x] **Coupon Code form -** I enter a value or string into the coupon input and click apply.
		- [x] **Toast message -** A toast message informs me the entered coupon is invalid.
	- [x] **Cart Subtotal, Delivery, Grand Total -** Cart total, delivery, and grand total are all correct and updated each time the cart updates.
	- [x] **Proceed to Checkout button -** I click on the proceed to checkout button, redirecting me to the checkout.
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
	Any date in the future for the expiry date
	Any five-digit number for postal code
	Card 4242424242424242 - Successful payment test
	Card 4000000000009995 - Failed payment test
	Card 4000002500003155 - Requires authentication test

- [x] **Test Successful Payment -** I enter card number 4242424242424242 and click complete order. A success message informs me the payment was successful, redirecting me to the checkout success page displaying the order details.
- [x] **Test Failed payment -** I enter card number 4000000000009995 and click complete order. An error message informs me the card has insufficient funds, redirecting me to the checkout page,
- [x] **Test Requires authentication -** I enter card number 4000002500003155, click complete order, a Stripe modal appears asking form authentication. I click the complete authentication. A success message informs me the order has been processed, redirecting me to the checkout success page displaying the order details.
- [x] **Test Stripe Webhooks -**
- [x] **Complete Order button -** In all the above tests, the complete order button works.
- [x] **Payment success confirmation message -** In all the above cases, the site displayed a toast message informing me of the success or failure of the action.
- [x] **Payment success confirmation email -** I received confirmation emails for both the above successful purchases.
- [x] **Order details saved to profile -** I navigate to my profile orders tab, and the order has been added to my orders list.

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
- [x] **Personalised Profile Heading -** The heading of the profile page is personalized, with ```first_name last_name's Profile```.
- [x] **Personalised Welcome message -** There is also a message, ```Welcome first_name!```.
- [x] **User Profile Menu**
	- [x] **All Users (Customers and Vendors)**
		- [x] **Profile Tab**
		My registration information is in read-only format. (Name, Username, Email, User Type, Date Joined, Last Login)
		- [x] **Account Info Tab**
			- [x] **Default Delivery and Profile Info**
			My profile information is in a form that I can be edit and update. I update my information and click the update information button. A success message is displayed, redirecting me to the main profile tab. I open the Account Info tab and see the updated information.
			- [x] **Account Management**
				- [x] **Change Password -** I click the change password link, redirecting me to the Change Password page.
					- [x] I enter my current password, a new password, the new password again, and click "Change Password".
					- [x] A success message confirms I have updated the password.
					- [x] I log out and then log in again using my new password. I confirm that I have updated the password.
				- [x] **Manage Email -** I click "Manage Email" and am redirected to the email management page.
					- [x] **BUG in Allauth template** The radio boxes with the emails and the email status were not displayed. There was an issue with the incorrect positioning of the label closing tag for the radio box. I moved it, and then the checkboxes showed. Then I added jinja to display each email beside the radio box. I added Bootstrap 5 classes and a grid for responsive display.
					- [x] I enter an email in the add email address input and click add an email. A message informs me a confirmation email has been sent to my new email.
					- [x] The page refreshes, and the new email is in the list of account emails.
					- [x] It is tagged as unverified.
					- [x] I check my email, click on the verify email link, and verify the email.
					- [x] Checking my email management page, and the email is now verified.
					- [x] I select the new email and click "Make Primary". The primary email is changed.
					- [x] I check in the admin and confirm I have changed the primary email.
					- [x] I select an email and click re-send verification. A verification email is sent to the email, with a link to click and verify the email.
					- [x] I select an email and click remove. A success message informs me I have removed the email from my account.
				- [x] **Close Account -** I click "Close Account", a bootstrap danger styled modal opens, warning me the account will be closed and I will no longer have access.
					- [x] I click Cancel, and the modal closes.
					- [x] I click Close Account, and A message informs me the account has been closed and I am logged out, to a page informing me the account is not active.
		- [x] **Orders Tab -** I open the profile order tab, and a list of my orders is displayed.
			- [x] **Order Details -** The order number, order date, order items, item quantity, and the order total are displayed for each order.
			- [x] **Order Number Link -** The order number a link.
				- [x] I click on an order number link, redirecting me to the order confirmation page displaying the order details.
				- [x] A toast message informs me I am viewing a past order.
		- [x] **Favorites Tab -**
			- [x] **Favorites Products Grid -** I click on the favorites tab, displaying the favorites list in a bootstrap grid.
			- [x] **Image Lightbox -** I click on the image, and it opens in an image lightbox.
			- [x] **Product Name Link -** I click the product name redirecting me to the product detail page.
			- [x] **Product Category Link -** I click the category, and it opens a page displaying all the products in that category.
			- [x] **Product Price -** The product price is displayed.
			- [x] **Remove Link button -** I click on the remove link below an item, and the page refreshes. A toast message informs me I have removed the item has from my favorites.
				- [x] **ISSUE:** When the page refreshes, it goes to the profile tab. I plan to implement Ajax to update the list without refreshing the page.
	- [x] **Vendor/ Admin Only Tabs -** The following two tabs are displayed for vendors only.
		- [x] **Products Tab -**
			- [x] **Product Layout Grid -** I open the profile products tab, and a list of the vendor's products is displayed.
			- [x] ****Only Vendors Products Displayed -**** I confirm that only the vendor's items are in their profile by changing ownership of some products in the admin. The products belonging to a different vendor are not in this vendor's profile.
			- [x] **Image lightbox -** I click the image, and it opens the image lightbox.
			- [x] **Product Name Link -** I click the product name, and it redirects me to the product detail page.
			- [x] **Product Category Link -** I click the category, and it opens a page displaying all the products in that category.
			- [x] **Product Price -** The product price is displayed.
				- [x] **Edit link -** I click on the edit link, redirecting me to the edit product page, where a form containing the products information is displayed. I edit the product details and click update product, redirecting me back to the product view with updated product details.
				- [x] **Delete link -** I click on the delete product link. A bootstrap danger-styled modal opens.
					- [x] **Delete Modal**
						- [x] **Modal Content -** The content informs me I will delete the product "SKU" and product "name" from the database. I need to confirm I want to delete the product. The content is clear and correct.
						- [x] **Cancel Button -** I click the cancel button, and the modal closes.
						- [x] **Delete Button -** I click the delete button, and a message informs me I have deleted the product, redirecting me to the product page.
		- [x] **Sales Tab**
			- [x] **Vendor Sales-List -** I open the vendor sales tab, and a list of the vendor product sales is displayed.
				- [x] To test this, I create an order for 4 separate items, in different quantities, belonging to 3 different vendors.
				- [x] I check the order and the line items in the Django admin. The details are correct and show the different line item product owners.
				- [x] In the profile for each vendor, the items for each vendor are shown in the vendor sales tab. The totals are correct.
			- [x] **Sales Details -** A table displays the date, order number, vendor, item quantity, order items, and line item total for each item.
			- [x] **Sale Order Number Link -** The order number links to the vendor sale order details.
				- [x] I click on an order number link, redirecting me to the sale confirmation page displaying the sale item details.
				- [x] A toast message informs me I am viewing a sale confirmation for a past sale.
---
### Blog All Pages
I navigate to the blog, where the content is as per design. A featured article, the blog posts, and a right sidebar.
- [x] **Blog Right Sidebar**
	- [x] **Blog Search -** I enter various search terms in the blog search input, and it returns related results for the search term within the blog posts.
	- [x] **Blog Categories -** I click on the category in the blog sidebar and see the related items within that category.
	- [x] **Recent Posts -** The four most recent posts are displayed in the recent posts, as by design.
	- [x] **Blog Archives -** The blog archives display Year and month with the total items from that month. Clicking on the month displays the posts from that month.
	- [x] **Blog Tags -** I click on the blog tags, and the items with that tag are displayed.
- [x] **Blog Featured Post**
	- [x] A featured post is displayed at the top of the page. I have selected the post as a featured post in the Post admin.
	- [x] In the post admin, I uncheck the option, and the featured post is no longer visible.
	- [x] I click on the post image or read more link. It opens and displays the post.
	- [x] **Note** The featured post is currently displayed on all ```blog_posts``` pages. I intend to change this, visible only on the first ```blog_posts``` page.
- [x] **Blog Posts Page**
	- [x] Regular posts are displayed below the featured post.
	- [x] The posts are paginated, two posts per page.
	- [x] I click on the image or readme link of the regular post and open the post.
- [x] **Post Detail Page**
	- [x] **Post -** The blog detail page as per design. The date, posted by, article title, article image, article, and article tags. Below the article is a form for users to leave comments.
- [x] **Blog Post Comments**
	- [x] The post comment form is available for authenticated users. As a logged-out user, I confirm that ```Register``` and ```Login``` links are displayed for users to leave a comment.
	![](documentation/images/blog-comments-login.png)    
	- [x] I log in, and on the same page now, there is a "```Leave a comment```" link displayed instead.    
	![](documentation/images/blog-comments-logged-in.png)    
	- [x] I click on the "```Leave a comment```" link, and the comment form toggles open and is now visible.    
	![](documentation/images/blog-comments-form.png)    
		- [x] I enter my name and a comment and click submit.
		- [x] A toast message informs me that I have posted the comment. I see the comment posted below the article.
		- [x] The page refreshes, the comment form is no longer visible, and the comment is displayed below the "```Leave a comment```" link.
	- [x] **Comments View -**
		- [x] The comment is displayed in a blockquote, with my name and how long ago I posted it.
		- [x] The comment section heading displays the number of comments in brackets. The total is updated when I add a comment.
		- [x] The comments are posted in date order. The newest comments are at the top.

#### NOTE: Changes to the Blog Comment Model
At this point in my testing, I realized that I hadn't thought out the comment process. I have added the images above.

1. The comment form was available for all users to leave comments. I changed this. Users must now register or log in to leave a comment. Logged out users see ```Register or login to leave a comment``` , with links to register or login.
2. Logged in users see a link ```Add a comment```, which toggles open the form to leave a comment.
3. I added a foreign key field to the comment model to register the authenticated user's id with the comment. Now I can monitor users that might add malicious or unfriendly content.
4. I updated the admin comment view to display the ```created_at```, ```posted_by```, ```name``` and ```post```. I also added a filter to filter by ```posted_by``` and ```name```.
5. I have updated the ER Diagram to reflect the added foreign key field in the comment model.

#### NOTE: Blog HTML Template structure.
I have divided the code into different templates within the blog. It will be easier to understand if someone needs to work on it.

```bash
|-- templates/blog/
|  |-- base.html
|  |-- blog-body.html
|  |-- blog-posts.html
|  |-- blog-detail.html
```

**Separation of HTML to reduce duplication**
Initially, I started with the ```blog-posts.html``` and ```blog-detail.html``` files. 

As I began to develop the application, it became complex as the page was long, and the sidebar code repeated in the post and detail pages.

I created the ```base.html``` page, which contains the blog sidebar. I created an ```inner_content``` block within the ```base.html```, and moved the ```post``` and ```detail``` HTML into separate pages. Those pages are included in the ```base.html``` page as required.

It saves me repeating and needing to make simultaneous changes to the sidebar on separate pages.

**Tags, categories, archive, and search query conflicts**

I found that results shown when looking for tags, categories, search queries duplicated when displaying the result in the HTML template.

My workaround was to remove the blog body from the ```blog-posts.html``` page and include it when returning the result. For this, I needed to distinguish what result was being returned and displayed.

The followign is my workaround, using jijna to include the blog body displaying the result.

```html+jinja
<!-- Include blog body -->
{% for post in posts %}
	<!-- Option 1: If there is a slug or archive item -->
	{% if category_slug != None or archive == True %}
		{% include 'blog/blog_body.html' %}
	<!-- Option 2: If there is no slug -->
	{% elif category_slug == None %}
		<!-- Option 2a: If it's a query -->
		{% if query %}
			<h5> You Searched For {{query}}</h5>
			{% include 'blog/blog_body.html' %}
		{% endif %}
		<!-- Option 2b: If its not a featured post or query -->
		{% if not post.featured and not query %}
			{% include 'blog/blog_body.html' %}
		{% endif %}
	{% endif %}
{% endfor %}
```

I'm not sure if this is the best way, but it works, and I am open to resolving the conflicts another way if there is a better way.

The same```blog-body.html``` is included on the same page but contains different contents, a way to separate the different filter results, not to display the same results.

---

### Toast Messages
[Readme/Toast Messages](/README.md/#toast-messages)

In the read me, I have outlined the style and positioning of the toast messages.

I also explained how I had used Django messages ```extra_tags``` to limit the posting of the cart-related messages.

- [x] When I add, update, or remove an item from the cart, the toast message appears, showing the cart details.
- [x] I confirm the toast messages do not show messages for messages unrelated to the cart adjustments.
- [x] I click on the toast cart link to secure checkout, and it redirects me to the checkout page.
- [x] The toast messages function per design, sliding in, then automatically closing after some seconds.

---

### Responsive Testing

To be completed.

---

### Unit Testing
****Pytest and Pytest-cov****
I unit tested using Pytest and pytest-cov. The focus was on testing models, forms, URLs, and views. It is not complete, but the pages were also extensively tested in the browser for expected behavior.

Unit testing attained 62% coverage. A screenshot of the testing printout from the terminal is as follows.     
![](/documentation/images/unit-testing.png)     

Pytest-cov report     
![](/documentation/images/pytest-cov.jpg)     

---

### Custom Error pages
Custom 400, 403, 404, and 500 error pages are in the product base template folder.

**404 Errors**
- [x] I type a [url to a page that doesn't exist](https://shop-for-buddhas.herokuapp.com/test/) in this project into the browser. The custom 404.html page is displayed.  
![](/documentation/images/404_error.jpg)   

**500 Errors**
- [x] I add an extra letter in a [blog slug url](https://shop-for-buddhas.herokuapp.com/blog/lost-wax-method-of-making-status-in-nepall/) (nepall instead of nepal), and the 500.html server error page is displayed.    
![](/documentation/images/500_error.jpg)   


---

### Page Views that Require Authentication

##### USERS NOT LOGGED IN

To be completed


##### AUTHENTICATED USERS

To be completed

---  

## USER STORIES REVIEW (Development-Deployment)

 
[Readme/User Stories](/README.md/#user-stories)

### User Story Reviews

### As a vendor, ...

**As a vendor:**
> I want to be able to register to sell my work.
- I have extended the AbstractUser model to include the possibility for users to register as a customer or a vendor.     
![](/documentation/images/vendor-registration.jpg)     

**As a vendor:**
> I want to create a profile.
- The profile is created as part of the registration process. The user can then update the profile with their details.     
![](/documentation/images/vendor-profile.jpg)     

**As a vendor:**
> I want to upload my products to be sold in the shop.
- The vendor can click the add new product button in the product tab in the vendor profile. They are redirected to the add new product page to add the product details, images and save the product.     
![](/documentation/images/vendor-profile-product.jpg)     
![](/documentation/images/vendor-add-product.jpg)     

**As a vendor:**
> I want to edit, update or delete my listed products.
- All the vendor's products have edit and delete links under them in the product list page, the product detail page, and the vendor's profile product tab. The profile view is above.
The image below is the product view, see the vendor's product with edit and delete links.     
![](/documentation/images/product-view-edit.jpg)     
The image below is the product detail view with the edit delete links.     
![](/documentation/images/product-detail-edit.jpg)     

	***Edit/ Update Product -*** Clicking the edit button opens the edit product page. The vendor can update the details and save them. See the edit and delete links in the above image.     
	![](/documentation/images/vendor-edit-product.jpg)     

	***Delete Product -*** To delete a product, it is two clicks. Click the delete under the product, then confirm by clicking delete again in the delete modal.     
	![](/documentation/images/vendor-delete-product.jpg)     

**As a vendor:**
> I want to see a current list of my items listed for sale.
- A complete list of all the vendor's products is shown in the vendor's profile product tab. The vendor can view the product there. Clicking on the image will open the image in a lightbox. Clicking the item name will redirect the vendor to the product detail page.     
![](/documentation/images/vendor-products.jpg)      

**As a vendor:**
> I want to be able to see a current list of my sold items
- The vendor profile sales tab is a list of the vendors selling items. By clicking on the sale order link, the vendor can view the details of the vendor's sold items from the customer order. It provides the vendor with the delivery address and customer contact details.     
![](/documentation/images/vendor-sales.jpg)     

**As a vendor:**
> I want customers to commission particular works with specific preferences.
- This is described as an available service in the services section on the homepage. Customers can contact us to ask if they have a particular requirement.     
![](/documentation/images/services.jpg)     

### As a customer, ...

**As a customer:**
> I want to buy quality statues.
- Over many years of visiting Nepal, India, and Tibet, we have many connections in Nepal. With a grounding in Buddhist practice, we understand the need for quality in Vajrayana Buddha statues.     
![](/documentation/images/products-quality.jpg)     

**As a customer:**
> I want to contact the seller if I have questions about the product.
- Customers can contact us via the contact form when they have particular questions for vendors. In such cases, when it is required, we connect the vendor with the customer to address those inquiries. 

**As a customer:**
> I want to commission work for items I cannot find in the shop.
- This matches with the vendor's requirement for the same. We have offered this as a possibility in the services section on the homepage.     
![](/documentation/images/services.jpg)     

**As a customer:**
> I'm interested in knowing about the statue-making process and the artisans that make the statues.
- A blog has been included in the site with this in mind. It is important to educate, inform, and raise awareness about this craft. A blog is a place where we can promote new items, vendors and publish other information of interest for customers to read.     
![](/documentation/images/blog.jpg)     

**As a customer:**
> I want to be able to view items by category.   
- The mega menu has in the navbar has links to all product categories. The customer can easily see all available categories in this view. Additionally, every product has a category tag. The user can click that tag to view all the other products within the same category.     
![](/documentation/images/megamenu.jpg)     

**As a customer:**
> I want to be able to sort the items in ascending, descending order.
- In the top right of the product page, a filter allows the user to filter by price, rating, category, and name.     
![](/documentation/images/product-filter.jpg)     

**As a customer:**
> I want to be able to search statues by name.
- In additon to the search option mentioned user story directly above, you the user can also open the search from teh navbar. SOme quick links are provided in the modal that opens, or teh user can enter a search parameter in the search input.   
![](/documentation/images/header-search.jpg)   

**As a customer:**
> I want a seamless registration process.
- Registration is a simple process. Complete the registration form. New users must provide a unique username and email. A confirmation email is sent with a link to click and confirm the provided email is correct. Once that is complete, the customer can log in.     
![](/documentation/images/vendor-registration.jpg)     

**As a customer:**
> I want to log in with an email and password.
- The user can use their username or email and password to log in.     
![](/documentation/images/login.jpg)     

**As a customer:**
> I want to have a profile to save time for future purchases.
- The user can fill in their profile, so their details are automatically entered in the checkout form when they purchase something.     
![](/documentation/images/profile-account-info.jpg)     

**As a customer:**
> I want an option to be able to close my account.
- The user can close their account by clicking the close account in their profile account info tab. See the above image.

**As a customer:**
> It's important that I can easily and intuitively navigate the site.
- The navbar is fixed and viewable at all times. The megamenu displays all the shop links. The cart icon in the navbar opens the modal side cart, which displays all cart items, and has links to the cart or checkout.
- Links are provided at all stages of the navigation process, to go on or to go back. The user can also click the links in the navbar, which link to the main pages.     
![](/documentation/images/buttons.jpg)     
![](/documentation/images/shopping-cart.jpg)     

**As a customer:**
> I want to select and pay for items easily.
- In the product list page, quick view and quick add buttons are provided so the user can easily view and add items to the cart. The user can click the go to secure checkout link in the toast success message or open the modal cart to update or navigate to the cart or checkout.     
![](/documentation/images/quickview.jpg)     
![](/documentation/images/cart.jpg)     
![](/documentation/images/toast.jpg)     

**As a customer:**
> I want to receive confirmation of purchase.
- The user receives a confirmation email of their purchase upon payment success.     
![](/documentation/images/purchase-success.jpg)     

**As a customer:**
> I want a record of my orders attached to my account profile.
- The user profile orders tab is a list of all orders, with a link to view the order details.     
![](/documentation/images/profile-orders.jpg)     

### As the site owner, ...

**As the site owner:**
> I want to support grass root artists to continue their work.
- On this site, I have made it possible for artisans to register and upload their products to sell.

**As the site owner:**
> I want to provide a website where grassroots artists can sell their work.
- It is my goal to support grass root artists. However, I also recognize that this needs to be managed to maintain quality and integrity.

**As the site owner:**
> I want to educate potential customers about the complexity of producing quality statues.
- I intend to use the blog to promote the artisans and services of the site. I also intend to educate and raise awareness by publishing articles about Buddhist philosophy.     
![](/documentation/images/blog.jpg)     

**As the site owner:**
> I want to help to preserve the rich tradition of statue making.
- My goal is that this site will provide additional support to the artisans in Nepal to sell their works. Hopefully, it will provide them with access to markets outside of what they usually have access to.

**As the site owner:**
> I want to provide quality handmade Buddhist dharma products to Buddhist practitioners.
- I have many connections around the world. I plan to use this site as a nexus to connect Buddhist practitioners and the artisans in Nepal. Providing support to the artisans and providing potential customers a way to connect directly with the creators of the works.

**As the site owner:**
> I want to make a nominal commission to pay for the maintenance of the site.
- I will plan to negotiate a small commission that will cover the costs of maintaining the site for the benefit of all those who benefit from it.

### Issues and Fixes
See also [README/BUGS and ISSUES](/README.md/#bugs-and-issues)

##### ISSUE: 1
**Safari Jumbotron Background Image**

There is a bug that is limited to Safari on iPhones. On an iPhone 13 Pro, the Buddha background image is not present. The same issue is not present when checking the iPhone in Chrome and Safari web developer tools. It is not present on tablets or Apple or PC desktops.

**UPDATE:** This issue is not evident in Chome and Safari on the laptop. There is a difference in how iOS Sarafi reads and presents the HTML and CSS. The issue also affects the iPad, which has no background image showing. 

Using Safari dev tools on my laptop, I connected to my iPhone. I spent time analyzing the issue to find a way to fix it. Using media queries to drill down in the iPhone css, I was able to change the positioning of the background image, so it is visible in the iPhone and on the iPad. 

```css
/* mobiles */
.paralsec {
	background-image: url("/media/bg_shakyamuni_vh1200.png");
}
.paral {
	height: 100vh;
	bottom: 0;
	background-attachment: fixed;
	background-size: 100vh  auto;
	background-repeat: no-repeat;
	background-position: 50%  0%;
}
/* Tablets */
@media only screen and (min-width: 768px){
	.paral {
		background-position: 40%  0%;
		}
}
/* Destops and bigger */
@media only screen and (min-width: 992px){
	.paral {
		background-position: 80%  0%;
		}
}
```
Initially, I had the background-size set to cover. I changed it to ```100vh auto```, added ```background-repeat: no-repeat;```, and tweaked the positioning for each screen size. 

The background image is now visible on mobiles and tablets. 

## Validation
### Form Validation
1. Contact form. The contact form is available from the homepage, and I considered it important to be available to anonymous users. To this end, the form includes additional protection of client-side Javascript validation, Regex patterns, and Django server-side CSRF validation. 
2. All other forms on the site user CSRF tokens and Django validation. 
3. Forms other than registration and login require authentication to access the forms. 

**Client-side validation**
In the contact form, which is accessible from the home
Client-side Javascript validation per Bootstrap 5 documentation.

**Regex patterns:**
The custom Regex patterns validate English and German language and include min and max characters for appropriate inputs. The regex patterns fail validation for some special characters.

**Server-side validation:**
Django ```csrf_token``` with Django validation included in all forms. 

### HTML Validation
HTML validated by W3C Markup Validation Service
Source code from all listed pages was copied and added into the W3C HTML validation, tested pages shown in the following image.

W3C Validation success for all pages: Document checking completed. No errors or warnings to show.     
![](/documentation/images/validation_html.png)     

### CSS Validation
CSS validated by W3C CSS Validation Service
CSS was copied and pasted into the W3C CSS Validator for all CSS files I created.

**NOTE:**
1. I put all CSS through the [Github autoprefixer](https://autoprefixer.github.io) to add backward compatibility for the four last browser releases. The Github autoprefixer adds Webkit prefixes that the W3C CSS Validator does not recognize, a known issue. It raises warnings for such prefixes.
2. I have used a Bootstrap theme and included the Boostrap CSS (see static/css/bootstrap_theme.css) in my site. Bootstrap run through the W3C Validation raises many warnings that are not critical, and autoprefixing this CSS also increases the validation warnings.

3. No errors have been raised for any of my CSS.     
![](/documentation/images/validation_css.png)     

### JS Validation
JS was validated using [JS Hint](https://jshint.com/), and JSHint noted no errors.     
![](/documentation/images/validation_js.png)     

### Python Validation
Python code from all the Python files was copied and pasted into the [PEP8 online](http://pep8online.com) Python validator.     

All Python code is PEP8 compliant and shows one error in `settings.py`. `env' imported but unused flake8(F401) [18,5]`. The error described is not an error as `env.py` is used to import protected sensitive data.   
![](/documentation/images/validation_python.png)     