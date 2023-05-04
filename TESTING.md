# Testing

Return back to the [README.md](README.md) file.

## Code Validation

In this section I ran validation for all the code I produced in the project. I found bugs in the code and fixed them, in order for it to work optimally and pass the tests.

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Before Screenshot | After Screenshot | Notes |
| --- | --- | --- | --- | --- |
| Index/Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2F) | ![screenshot](documentation/html-test-index-bugs.png) | ![screenshot](documentation/html-test-index-fixed.png) | Duplicate ID errors, Stray end tag div, all fixed |
| Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Frecipe%2F16%2F) | ![screenshot](documentation/html-test-recipe-bugs.png) | ![screenshot](documentation/html-test-recipe-fixed.png) | Duplicate ID errors, Trailing slash warning, all fixed |
| Recipe/Logged-In | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Frecipe%2F16%2F) | ![screenshot](documentation/html-test-recipe-bugs-logged-in.png) | ![screenshot](documentation/html-test-recipe-logged-in-fixed.png) | No p element in scope but a p end tag seen error, Bad value for attribute action error, The element button must not appear as a descendant of the a element errors, all fixed. This test had to be validated by input since pages that require a user to be logged-in and authenticated (CRUD functionality), will not work using uri validation method, due to the fact that the HTML Validator (W3C) doesn't have access to login to the pages. |
| About-Us | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fabout-us%2F) | ![screenshot](documentation/html-test-about-us.png) | ![screenshot](documentation/html-test-about-us.png) | Passed no errors |
| Gallery | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fgallery%2F) | ![screenshot](documentation/html-test-gallery.png) | ![screenshot](documentation/html-test-gallery.png) | Passed no errors |
| Create Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fcreate-recipe%2F) | ![screenshot](documentation/html-test-create-recipe-bugs.png) | ![screenshot](documentation/html-test-create-recipe-fixed.png) | Element p not allowed as a child of element label error, fixed |
| Update Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fupdate-recipe%2F16%2F) | ![screenshot](documentation/html-test-update-recipe-bugs.png) | ![screenshot](documentation/html-test-update-recipe-fixed.png) | Stray end tags form and divs errors, all fixed |
| Delete Recipe | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvenezuelan-cookbook.herokuapp.com%2Fdelete-recipe%2F16%2F) | ![screenshot](documentation/html-test-delete-recipe.png) | ![screenshot](documentation/html-test-delete-recipe.png) | Passed no errors |
