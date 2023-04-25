# VENEZUELAN FOOD COOKBOOK

Venezuelan Food Cookbook, is a website designed to provide a space wherein users can create their own venezuelan food recipes, upload them and share their culinary skills with everybody. Users can also avail of the recipes already uploaded on the site. They can learn and try new dishes from a tropical country such as Venezuela, wherein, food is one of its main features. The point of this initiative is to broaden the knowledge about Venezuelan dishes. Nowadays, users can see these recipes being cooked anywhere in the world, thanks to the large exodus of Venezuelan people across the globe, the necessary ingredients can be found in several stores, some particular ones can be found in foreign-goods shops. Users can register to the site and once logged in they have access to all the site's features. Not only can they upload, update and delete their own recipes but they can also participate in conversations related to a particular recipe by writing comments and they can like or unlike recipes. This site seeks to provide a service required by users world-wide looking to expand and share culinary knowledge.

![screenshot](documentation/am-i-responsive.png)

## UX

### Colour Scheme

* To select the colors, I used the [ColorSpace](https://mycolor.space/) website which provides the option to input any color you want and then it will provide a selection of matching/compatible colors that relate well to that "base" color you selected in the first place.
* Once I had my base color selected which is [#0000FF](https://mycolor.space/?hex=%230000FF&sub=1), I used ColorSpace and it gave me a wide variety of compatible colors to work with from which I chose several of them and referenced them accordingly in the css style sheet.   

![Colors](documentation/color-selection.png)

### Typography

* Since the google fonts page feature for fonts pairing suggestions was discontinued, I used an alternative tool available to select the fonts for the site.
* I browsed [heyreliable](https://heyreliable.com/ultimate-google-font-pairings/) google fonts pairings available in their collection and selected number 13 based on the look and mood wanted for the site.
    
![Fonts](documentation/fonts-selection.png)

* These fonts are clear to read, they have a friendly yet professional style which is compatible with a culinary website.

- [Merriweather](https://fonts.google.com/specimen/Merriweather) was used for the primary headers and titles.

- [Mulish](https://fonts.google.com/specimen/Mulish) was used for all other secondary text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

### Site Users

- As a site user, I would like to view a list of recipes, so that I can select one to read, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/3).
- As a site user, I would like to click on a recipe, so that I can read/see the full content, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/4).
- As a site user, I would like to view comments on an individual recipe, so that I can read the conversation, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/5).
- As a site user, I would like to register an account, so that I can create my own recipes, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/6).
- As a registered site user, I would like to make comments on a recipe, so that I can start and/or be involved in a conversation, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/7).
- As a registered site user, I would like to update and delete recipes, so that I can manage my recipes content, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/8).
- As a registered site user, I would like to place tags on my created recipes, so that I can indicate the meal type, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/9).
- As a site user, I would like to view a paginated list of recipes, so that I can easily select which recipe to view, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/10).
- As a site user, I would like to avail of a website with a UX based design, so that I can navigate and interact with it easily and intuitively, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/12).
- As a registered site user, I would like to like recipes, so that I can show I liked a particular recipe, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/13).

### Site Admin

- As a site administrator, I should be able to  create, read, update and delete my own recipes and the ones created by registered users, so that I can moderate the content of the site, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/1).
- As a site administrator, I should be able to create, read, update and delete my comments and the ones created by registered users, so that I can moderate the conversations, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/2).
- As a site administrator, I should be able to view comments on an individual recipe, so that I can read the conversation, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/5)

### Product Owner

- As a product owner, I should be able to run automated tests, so that I can make sure everything is working as it should, [Link here](https://github.com/leonardo-simeone/venezuelan-food-cookbook/issues/11)

## Wireframes

To wireframe the website I used [Whimsical](https://whimsical.com/wireframes).

![Wireframe](documentation/wireframe.png)

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
