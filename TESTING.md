# Testing

Return back to the [README.md](README.md) file.

## Code Validation

In this section I ran validation for all the code I produced in the project. I found bugs in the code and fixed them, in order for it to work optimally and pass the tests.

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Before Screenshot | After Screenshot | Notes |
| --- | --- | --- | --- | --- |
| Register | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fregister%2F) | ![screenshot](documentation/html-test-register-bugs.png) | ![screenshot](documentation/html-test-register-fixed.png) | Bad value (empty) for action on element form, fixed |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Flogin%2F) | ![screenshot](documentation/html-test-login.png) | ![screenshot](documentation/html-test-login.png) | Passed no errors |
| Index/Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2F) | ![screenshot](documentation/html-test-index-bugs.png) | ![screenshot](documentation/html-test-index-fixed.png) | Duplicate ID errors, Stray end tag div error, all fixed |
| Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Frecipe%2F16%2F) | ![screenshot](documentation/html-test-recipe-bugs.png) | ![screenshot](documentation/html-test-recipe-fixed.png) | Duplicate ID errors, Trailing slash warning, all fixed |
| Recipe/Logged-In | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Frecipe%2F16%2F) | ![screenshot](documentation/html-test-recipe-bugs-logged-in.png) | ![screenshot](documentation/html-test-recipe-logged-in-fixed.png) | No p element in scope but a p end tag seen error, Bad value for attribute action error, The element button must not appear as a descendant of the a element errors, all fixed. This test had to be validated by input since pages that require a user to be logged-in and authenticated (CRUD functionality), will not work using uri validation method, due to the fact that the HTML Validator (W3C) doesn't have access to login to the pages. |
| About-Us | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fabout-us%2F) | ![screenshot](documentation/html-test-about-us.png) | ![screenshot](documentation/html-test-about-us.png) | Passed no errors |
| Gallery | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fgallery%2F) | ![screenshot](documentation/html-test-gallery.png) | ![screenshot](documentation/html-test-gallery.png) | Passed no errors |
| Create Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fcreate-recipe%2F) | ![screenshot](documentation/html-test-create-recipe-bugs.png) | ![screenshot](documentation/html-test-create-recipe-fixed.png) | Element p not allowed as a child of element label error, fixed |
| Update Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fupdate-recipe%2F16%2F) | ![screenshot](documentation/html-test-update-recipe-bugs.png) | ![screenshot](documentation/html-test-update-recipe-fixed.png) | Stray end tags form and divs errors, all fixed |
| Delete Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fdelete-recipe%2F16%2F) | ![screenshot](documentation/html-test-delete-recipe.png) | ![screenshot](documentation/html-test-delete-recipe.png) | Passed no errors |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fcontact%2F) | ![screenshot](documentation/html-test-contact.png) | ![screenshot](documentation/html-test-contact.png) | Passed no errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Before Screenshot | After Screenshot | Notes |
| --- | --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/css-test-bugs.png) | ![screenshot](documentation/css-test-fixed.png) | Parse errors, Unknown pseudo-element error, all fixed. The warnings shown are the result of using Cloudinary and Bootstrap |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![screenshot](documentation/js-test.png) | Passed no errors |

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Before Screenshot | After Screenshot | Notes |
| --- | --- | --- | --- | --- |
| Venezuelan Food *settings.py* | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/venezuelan_food/settings.py#) | ![screenshot](documentation/settings-errors.png) | ![screenshot](documentation/settings-pass.png) | E501 line too long errors, all fixed |
| Cookbook *admin.py* | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/admin.py) | ![screenshot](documentation/admin-pass.png) | ![screenshot](documentation/admin-pass.png) | Passed no errors |
| Cookbook *urls.py* | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/urls.py) | ![screenshot](documentation/urls-pass.png) | ![screenshot](documentation/urls-pass.png) | Passed no errors |
| Cookbook *models.py* | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/models.py) | ![screenshot](documentation/models-errors.png) | ![screenshot](documentation/models-pass.png) | E501 line too long errors, all fixed |
| Cookbook *forms.py* | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/forms.py) | ![screenshot](documentation/forms-errors.png) | ![screenshot](documentation/forms-pass.png) | E501 line too long error, fixed |
| Cookbook *views.py* | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/views.py) | ![screenshot](documentation/views-errors.png) | ![screenshot](documentation/views-pass.png) | E501 line too long errors, W293 blank line contains whitespace error, all fixed |
| Cookbook *test_urls.py* | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_urls.py) | ![screenshot](documentation/test-urls-pass.png) | ![screenshot](documentation/test-urls-pass.png) | Passed no errors |
| Cookbook *test_models.py* | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_models.py) | ![screenshot](documentation/test-models-errors.png) | ![screenshot](documentation/test-models-pass.png) | E501 line too long errors, all fixed |
| Cookbook *test_forms.py* | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_forms.py) | ![screenshot](documentation/test-forms-errors.png) | ![screenshot](documentation/test-forms-pass.png) | E501 line too long errors, all fixed |
| Cookbook *test_views.py* | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_views.py) | ![screenshot](documentation/test-views-errors.png) | ![screenshot](documentation/test-views-pass.png) | E501 line too long errors, all fixed |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/chrome-test.png) | Works as expected |
| Edge | ![screenshot](documentation/edge-test.png) | Works as expected |
| Firefox | ![screenshot](documentation/firefox-test.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet.png) | Works as expected |
| Desktop (DevTools) | ![screenshot](documentation/responsive-desktop.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsive-xl.png) | Works as expected |
| 4K Monitor | ![screenshot](documentation/responsive-4k.png) | Works as expected |
| Samsung Galaxy A52s (my own phone) | ![screenshot](documentation/responsive-own-phone.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-test-home-mobile.png) | ![screenshot](documentation/lighthouse-test-home-desktop.png) | Few warnings on mobile |
| About Us | ![screenshot](documentation/lighthouse-test-about-us-mobile.png) | ![screenshot](documentation/lighthouse-test-about-us-desktop.png) | Few warnings on mobile |
| Gallery | ![screenshot](documentation/lighthouse-test-gallery-mobile.png) | ![screenshot](documentation/lighthouse-test-gallery-desktop.png) | Slow response time due to amount of images, few warnings |
| Recipe | ![screenshot](documentation/lighthouse-test-recipe-mobile.png) | ![screenshot](documentation/lighthouse-test-recipe-desktop.png) | few warnings on mobile |
| Create Recipe | ![screenshot](documentation/lighthouse-test-create-recipe-mobile.png) | ![screenshot](documentation/lighthouse-test-create-recipe-desktop.png) | few warnings on mobile |
| Update Recipe | ![screenshot](documentation/lighthouse-test-update-recipe-mobile.png) | ![screenshot](documentation/lighthouse-test-update-recipe-desktop.png) | few warnings on mobile |
| Delete Recipe | ![screenshot](documentation/lighthouse-test-delete-recipe-mobile.png) | ![screenshot](documentation/lighthouse-test-delete-recipe-desktop.png) | some minor warnings on mobile |
| Register | ![screenshot](documentation/lighthouse-test-register-mobile.png) | ![screenshot](documentation/lighthouse-test-register-desktop.png) | few warnings on mobile |
| Login | ![screenshot](documentation/lighthouse-test-login-mobile.png) | ![screenshot](documentation/lighthouse-test-login-desktop.png) | few warnings on mobile |
| Contact | ![screenshot](documentation/lighthouse-test-contact-mobile.png) | ![screenshot](documentation/lighthouse-test-contact-desktop.png) | few warnings on mobile |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| About Us Page | | | | |
| | Click on About Us link in navbar | Redirection to About Us page | Pass | |
| | Click on About Us link in footer | Redirection to About Us page | Pass | |
| Gallery Page | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Click on Gallery link in footer | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| | Click gallery images | All images links redirect user to corresponding recipe page | Pass | |
| Create Recipe Page | | | | |
| | Click on Create Recipe link in navbar | Redirection to Create Recipe page | Pass | |
| | Click on Create Recipe button | New recipe will be created and user redirected to Home page | Pass | A message will show at the top of the page to indicate the user they've created the recipe successfully |
| | Click on Create Recipe button without requiered values for recipe | An error will show on the form to indicate the user what's missing | Pass | |
| | Brute forcing the URL to get to Create Recipe page without logging in first | User will be redirected to Login page | Pass | |
| Update Recipe Page | | | | |
| | Click on Edit Recipe button in Recipe page | Redirection to Update Recipe page | Pass | |
| | Click on Edit Recipe button | Existing recipe will be updated and user redirected to the updated recipe page | Pass | A message will show at the top of the page to indicate the user they've updated the recipe successfully |
| | Click on Edit Recipe button without requiered values for recipe | The screen will reposition and focus (css) in the field where data is missing | Pass | |
| | Brute forcing the URL to get to Update Recipe page without logging in first | User will be redirected to Login page | Pass | |
| | Brute forcing the URL to get to Update Recipe page of another user's recipe | An error will show at the top of the page to indicate the user that they don't have permission to update this recipe | Pass | |
| Delete Recipe Page | | | | |
| | Click on Delete Recipe button in Recipe page | Redirection to Delete Recipe page | Pass | Confirms deletion first |
| | Click on Delete Recipe button | Existing recipe will be deleted and user redirected to home page | Pass | A message will show at the top of the page to indicate the user they've deleted the recipe successfully |
| | Click on Go Back button | User is redirected to the current recipe page | Pass | |
| | Brute forcing the URL to get to Delete Recipe page without logging in first | User will be redirected to Login page | Pass | |
| | Brute forcing the URL to get to Delete Recipe page of another user's recipe | An error will show at the top of the page to indicate the user that they don't have permission to delete this recipe | Pass | |
| Contact Page | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Click on Send button | New contact message will be created and user redirected to Home page | Pass | A message will show at the top of the page to indicate the user they've contacted the site administrator successfully |
| | Click on Send button without requiered values for contact form | An error will show on the form to indicate the user what's missing | Pass | |
| Register | | | | |
| | Click on Register link in navbar, carousel call to action or About Us page call to action | Redirection to Register page | Pass | |
| | Enter valid username | Field will accept free text format | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Register button | User is registered, logged in automatically and redirected Home | Pass | A message will show at the top of the page to indicate the user they've registered successfully |
| | Click on Register button without requiered values | An error will show on the form to indicate the user what's missing | Pass | |
| Log In | | | | |
| | Click on the Login link in navbar | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | A message will show at the top of the page to indicate the user they've logged in successfully |
| | Click Login button with wrong data | An error will show at the top of the page to indicate the user what's wrong | Pass | |
| Log Out | | | | |
| | Click Logout button | Logs out user and redirects user to home page | Pass | A message will show at the top of the page to indicate the user they've logged out successfully |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a site user, I would like to view a list of recipes, so that I can select one to read. | ![screenshot](documentation/home.png) |
| As a site user, I would like to click on a recipe, so that I can read/see the full content. | ![screenshot](documentation/recipe-unit.png) |
| As a site user/site administrator, I would like to view comments on an individual recipe, so that I can read the conversation. | ![screenshot](documentation/user-story-view-comments.png) |
| As a site user, I would like to register an account, so that I can create my own recipes. | ![screenshot](documentation/user-story-register-create.png) |
| As a site user, I would like to view a paginated list of recipes, so that I can easily select which recipe to view. | ![screenshot](documentation/user-story-pagination.png) |
| As a site user, I would like to contact the site administrator, so that I can query/recommend the site admin on different topics. | ![screenshot](documentation/contact.png) |
| As a registered site user, I would like to  make comments on a recipe, so that I can start and/or be involved in a conversation. | ![screenshot](documentation/user-story-view-make-comments.png) |
| As a registered site user, I would like to update and delete recipes, so that I can manage my recipes content. | ![screenshot](documentation/user-story-update-delete.png) |
| As a registered site user, I would like to place tags on my created recipes, so that I can indicate the meal type. | ![screenshot](documentation/user-story-place-tags.png) |
| As a registered site user, I would like to like recipes, so that I can show I liked a particular recipe. | ![screenshot](documentation/user-story-like-recipe.png) |
| As a registered site user, I would like to avail of a website with a UX based design, so that I can navigate and interact with it easily and intuitively. | ![screenshot](documentation/recipe-unit.png) |
| As a site administrator, I should be able to create, read, update and delete my own recipes and the ones created by registered users, so that I can moderate the content of the site. | ![screenshot](documentation/user-story-admin-create.png) |
| As a site administrator, I should be able to create, read, update and delete my comments and the ones created by registered users, so that I can moderate the conversations. | ![screenshot](documentation/user-story-admin-comments.png) |
| As a product owner, I would like to run automated tests, so that I can make sure everything is working as it should. | ![screenshot](documentation/user-story-automated-tests.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

This includes a series of testing across several files in my [cookbook](cookbook/) app, consisting of a total of 51 unique tests.

![screenshot](documentation/user-story-automated-tests.png)

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test cookbook `

To create the coverage report, I would then run the following commands:

`coverage run --source=cookbook manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Cookbook | test_forms.py | 100% | ![screenshot](documentation/py-test-cookbook-forms.png) |
| Cookbook | test_models.py | 100% | ![screenshot](documentation/py-test-cookbook-models.png) |
| Cookbook | test_urls.py | 100% | ![screenshot](documentation/py-test-cookbook-urls.png) |
| Cookbook | test_views.py | 100% | ![screenshot](documentation/py-test-cookbook-views.png) |

## Bugs

| Language | Bug | Before Screenshot | After Screenshot | To fix bug |
| --- | --- | --- | --- | --- |
| JS | Failed to load plugin: `tinymce.min.js:9` paste from url plugins/paste/plugin.min.js | ![screenshot](documentation/instructions-paste-plugin-js-error.png) | ![screenshot](documentation/instructions-paste-plugin-js-error-fixed.png) | I deleted the copy/paste tool from plugins and toolbar dictionaries in the tinymce init script located in base template. This particular tool is not included in the tinycloud core tools, it falls into the paid tools. |
| Django | `unrestricted access` at venezuelan-cookbook.herokuapp.com/create-recipe/. Unauthorized users could force access this page, intended only for registered users | ![screenshot](documentation/create-recipe-auth-fail.png) | ![screenshot](documentation/create-recipe-auth-success.png) | I used the @login_required decorator in the createRecipe view and redirected user to login page. |
| Django | `unrestricted access` at venezuelan-cookbook.herokuapp.com/update-recipe/. Unauthorized users could force access this page, intended only for registered users | ![screenshot](documentation/update-recipe-auth-fail.png) | ![screenshot](documentation/update-recipe-auth-success.png) | I used the @login_required decorator in the updateRecipe view and redirected user to login page. |
| Django | `no permission access` at venezuelan-cookbook.herokuapp.com/update-recipe/. Logged in users without permission to edit another user's recipe could force access this page, intended only for recipe's owner | ![screenshot](documentation/update-recipe-permission-fail.png) | ![screenshot](documentation/update-recipe-permission-success.png) | I used a conditional in the updateRecipe view to check if the logged in user was in fact the recipe owner, if they don't match, then an error indicating to the user that they don't have permission to edit the recipe will be shown and the user will be redirected to home page. |
| Django | `unrestricted access` at venezuelan-cookbook.herokuapp.com/delete-recipe/. Unauthorized users could force access this page, intended only for registered users | ![screenshot](documentation/delete-recipe-auth-fail.png) | ![screenshot](documentation/delete-recipe-auth-success.png) | I used the @login_required decorator in the deleteRecipe view and redirected user to login page. |
| Django | `no permission access` at venezuelan-cookbook.herokuapp.com/delete-recipe/. Logged in users without permission to delete another user's recipe could force access this page, intended only for recipe's owner | ![screenshot](documentation/delete-recipe-permission-fail.png) | ![screenshot](documentation/delete-recipe-permission-success.png) | I used a conditional in the deleteRecipe view to check if the logged in user was in fact the recipe owner, if they don't match, then an error indicating to the user that they don't have permission to delete the recipe will be shown and the user will be redirected to home page. |
| Python | `bash: coverage: command not found` Coverage not installed. Tried to run unit tests using coverage but coverage hadn't been installed yet. | ![screenshot](documentation/coverage-error.png) | ![screenshot](documentation/coverage-error-fixed.png) | I installed coverage using `pip3 install coverage`. |
| Python | `E501 line too long` (87 > 79 characters). | ![screenshot](documentation/test-forms-errors.png) | ![screenshot](documentation/test-forms-pass.png) | This error replicated along all my python files. To fix it, I followed my mentor's suggestion which was to press enter right after the first bracket so I dind't have to 'guess' where the proper indentantion was. |

## Unfixed Bugs

There are no remaining bugs that I am aware of.