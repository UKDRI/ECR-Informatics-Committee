# Contributing to the informatics website

The site is built using quarto, which has excellent documentation in it's own right that you can find [here](https://quarto.org/docs/websites/).

Simply put, the website is built from .qmd document, which allows you to have any code executable and it's output included in the final webpage.

## Steps to add/edit site

- Clone this repo to your machine
- The site content is located here [07_dissemination/01_website](https://github.com/UKDRI/ECR-Informatics-Committee/tree/main/07_dissemination/01_website)
- The subfolders here correspond to different pages of the site, choose the one you one to add to and enter it
- You'll need to create a new folder to house your page, I'd suggest just copying one that already exists and renaming it to something sensible
- Inside that folder you'll have a .qmd file to add the content of your post, and any image files can be added here as well.
- Once you're done adding content you can render the website locally by running `quarto render` from the project root, or by clicking the "Render Website" button you'll see in the build tab of RStudio if you've open the project there.
- The site is rendered to the [docs](https://github.com/UKDRI/ECR-Informatics-Committee/tree/main/docs) folder, so navigate there and open the index.html - make sure the site looks how you expect and nothing is broken!
- Once you're happy you can push changes to the repo and GitHub pages should automatically update the site after a few seconds
- Note: if you're not comfortable feel free to push your changes as a pull request and someone can review your changes before they go live

