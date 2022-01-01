
# TESTING

![](/documentation/images/shopforbuddhas-home.jpg)

## TESTING PLAN (Pre-development)

[README](/README.md) Documentation for the project

[README/Testing](/README.md/#testing)

### RESEARCH

[README/Research](/README.md/#research)


### DEVELOPMENT

[README/Development](/README.md/#development)

#### HTML

- Incorporate Template Design using HTML5 and Bootstrap 5 with SCSS/ CSS.
    - Create Base Template
	- Nav-bar/ Off-canvas
	- Modals
	- Contact form
	- Social Icons - Incorporate Bootstrap Breakpoints as media queries in CSS for responsive display. - Use Chrome DevTools to ensure positioning of elements for each breakpoint.

#### JavaScript/ jQuery
- Initialize Bootstrap components wherre possible using Vanilla JS.

### DEPLOYMENT
[README/Deployment](/README.md/#deployment)

#### Test for production

- **Test local and Test live**

	- Create the application in Gitpod, using the python server to view the work in the browser. It has two advantages:
		- The Python server and pep8 syntax checking ensure the code is compliant and structured correctly; otherwise, the server shuts down.
		- Set `debug=True`, ensuring that Jinja errors show in the browser, with a lot of detail, so I can fix mistakes as I go.
		- Due to the nature of Python and Jinja, checking is completed in the process of development while writing route paths and functions that run the app.
		Deploy the project live to Heroku early to check the live site along the way, ensuring the behaviour I experience locally is consistent with the live site.
	- Compare and test deployed version of the website.
		- Ensure it is the same and there are no bugs.
		- Inputs, forms, features need to display and function as expected.

- **Responsiveness**
	- Chrome DevTools:
		- Test by screen sizes
		- Test by viewing media queries which will specifically include Material Design breakpoints.
		- Test on different devices, different operating systems, different browsers, screen sizes.
	- Share the application to get third-party feedback

- **Function**
	- Test on different devices, operating systems, and browsers.
	- Test all external links, inputs, forms, navigation links, and features.

- **404 Page not found**

	- Create 404 Page not found page.
	- Create 405 Method Not Allowed page
	- Create 500 Server Error page

- **User Experience**

**Feedback**: Share the application to get feedback and test the UI to see how users intuit the application process.

- **User Stories**: Check the application fulfils the needs expressed in the user stories.

### DEVELOPMENT SETUP

#### Code Editor

[Gitpod](https://www.gitpod.io/): I chose to use Gitpod to get support from Code Institute when I need it. It makes it easy to share the workspace and get help troubleshooting problems.

- Python3 Development Server: I use the Python3 command `python3 app.py` to run my application in the development server and view the work in the browser.

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


1. **All Users:**

2. **Session Users:**

3. **Admin Users:**

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
	
