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

| File | CI URL | Raw URL | Combined |
| --- | --- | --- | --- |
| Venezuelan Food *settings.py* | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/venezuelan_food/settings.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/venezuelan_food/settings.py# |
| Cookbook *admin.py* | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/admin.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/admin.py |
| Cookbook *urls.py* | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/urls.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/urls.py |
| Cookbook *models.py* | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/models.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/models.py |
| Cookbook *forms.py* | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/forms.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/forms.py |
| Cookbook *views.py* | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/views.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/views.py |
| Cookbook *test_urls.py* | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_urls.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_urls.py |
| Cookbook *test_models.py* | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_models.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_models.py |
| Cookbook *test_forms.py* | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_forms.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_forms.py |
| Cookbook *test_views.py* | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_views.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/leonardo-simeone/venezuelan-food-cookbook/main/cookbook/test_views.py |

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

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/lighthouse-test-home-mobile.png) | Few warnings |
| Home | Desktop | ![screenshot](documentation/lighthouse-test-home-desktop.png) | Some minor warnings |
| About Us | Mobile | ![screenshot](documentation/lighthouse-test-about-us-mobile.png) | Few warnings |
| About Us | Desktop | ![screenshot](documentation/lighthouse-test-about-us-desktop.png) | Some minor warnings |
| Gallery | Mobile | ![screenshot](documentation/lighthouse-test-gallery-mobile.png) | Slow response time due to amount of images, few warnings |
| Gallery | Desktop | ![screenshot](documentation/lighthouse-test-gallery-desktop.png) | Slow response time due to amount of images, some minor warnings |

