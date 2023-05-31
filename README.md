# Gymnation Blog

![Gymnation blog on desktop](/media/images/desktop-image.png)

## Contents

- [Gymnation Blog](#gymnation-blog)
  - [Contents](#contents)
  - [About](#about)
  - [User Experience](#user-experience)
    - [User Stories](#user-stories)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Deployment \& Local Development](#deployment--local-development)
    - [Database Creation:](#database-creation)
    - [Image Hosting:](#image-hosting)
    - [Setting up for deployment in Django:](#setting-up-for-deployment-in-django)
    - [Deploying the Site:](#deploying-the-site)
    - [Local Development](#local-development)
  - [Testing](#testing)
  - [Credits](#credits)

## About

Gymnation is a blog targeted towards athletes and gym enthusiasts, providing them with useful and inspirational content to help motivate them towards their goals. Users can browse posts from different authors, like and comment on posts to engage with the content and also favourite certain posts so that they can view them again later, without having to search through them again.

## User Experience

### User Stories

- As a **visitor**, I want to be able to **browse through various fitness articles** to **find inspiration and information on different workout routines and healthy living.**
- As a **visitor or registered user**, I want to be able to **click on a specific article on the fitness blog** to **view more details and read the full content**. When browsing through the list of articles, I expect each article to have a clickable title or preview image that will lead me to a dedicated page for that article. On the article page, I anticipate seeing a clear and visually appealing layout that presents the complete content, including any accompanying images, videos, or embedded media. I also want to have the ability to easily navigate back to the list of articles
- As a **visitor or registered user**, I want to be able to **view comments on a post in the fitness blog** to **engage in discussions and gain further insights**. When I navigate to a specific post, I expect to see a section below the article that displays existing comments from other users. Each comment should include the author's name, timestamp, and their comment text.
- As a **registered user**, I want to be able to **comment on articles** to **share my thoughts, ask questions, and engage in discussions with other users and the author.**
- As a **visitor or registered user**, I want to be able to **view the number of likes on a fitness blog post** to **gauge its popularity and community engagement**. When I access a post, I expect to see a visible count of the total likes the post has received. This information will provide me with insights into the article's impact and resonate with other readers. Additionally, I would appreciate if the post's likes are displayed prominently, either near the post title or in close proximity to the article itself, allowing me to quickly assess its level of appreciation within the community.
- As a **registered user**, I want to be able to **like a post on the fitness blog** to **express my opinion and engage with the content**. I want to click a "like" button to show appreciation for a well-written or helpful article.
- As a new **visitor** to the fitness blog, I want to be able to **register an account** to **access personalized features and participate in the community**. I expect to see a prominent "Sign Up" or "Register" button on the website's homepage or navigation menu. Upon clicking the button, I should be directed to a registration page where I can provide my desired username, email address, and password. The registration form should include validation checks for the input fields. After verifying my account, I should be able to log in using my chosen credentials and enjoy the benefits of being a registered user, such as liking articles and participating in discussions.
- As an **administrator** of the fitness blog website, I want to be able to **create draft articles** so that **I can work on them at my convenience and finish them later**. Once I am satisfied with the draft, I should have the ability to publish it and make it visible to the readers of the fitness blog.
- As an **administrator** of the fitness blog website, I want to be able to **create, update and delete new articles** to **share valuable content with the readers.** I want the ability to publish the article, making it visible to the visitors and readers of the fitness blog. I also want to be able to delete and update articles after they have been created.
- As an **administrator**, I want to be able to **moderate user comments** to **ensure a positive and respectful community environment within the blog.**
- As a **registered user** of the fitness blog website, I want to be able to **favorite certain posts**, so that I can **easily find and view them** again later.

## Features

## Technologies Used

### Languages Used

- HTML
- CSS
- JavaScript
- Python

### Frameworks, Libraries & Programs Used

- Django - Web Framework
- Cloudinary - Image Hosting
- ElephantSQL - PostgreSQL as a Service
- Heroku - Web Hosting
- CodeAnywhere - Cloud Development
- GitHub - Repositiory Storage
- TinyPNG - Image Compression
- FontAwesome - Font and Icon Library
- Bootsrap - Front-end Framework
- Pexels - Article Images source

## Deployment & Local Development

### Database Creation:

- For this project ElephantSQL was used for a PostgreSQL database.
- Once created, The Database URL will have to be copied.

### Image Hosting:

- Cloudinary was used for image hosting on the project.
- Once an account is created, the API key will have to be stored.

### Setting up for deployment in Django:

- A Procfile will need to be created for the site.
- The requirements in the requirements.txt wile will have to be installed, using the following command:
- `$ pip install -r requirements.txt`
- An `env.py` file will need to be created to store the configuration variables, here is an example:

```
import os

os.environ["DATABASE_URL"] = 'ENTER_DATABASE_URL_HERE'
os.environ["SECRET_KEY"] = 'ENTER_SECRET_KEY_HERE'
os.environ["CLOUDINARY_URL"] = 'ENTER_CLOUDINARY_URL_HERE'
```

### Deploying the Site:

- To deploy the site, Heorku was used for this project.
- cREATE A hEROKU app from the copy of this repository
- The Database URL, CloudInary API key and secret key will have to be added as config vars on the Heroku App.

### Local Development

Steps to fork this project using GitHub:

1. Navigate to the GitHub repository for this project.
2. Click the 'Fork' button (top right-hand side of the repository page).

For more information on how to fork a GitHub repository please click [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

Steps to clone this project using GitHub:

1. Navigate to the GitHub repository for this project.
2. Click on the 'Code' button, located above the project files.
3. Select 'HTTPS' as the method to clone the repository.
4. Copy the link provided, located under 'HTTPS'.
5. Open the Terminal in the location you would like the repository to be cloned to.
6. Type `git clone` and then the link provided in step 4

For more information on how to clone a GitHub repository please click [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Testing

## Credits

This project is based on the Code Institute I Think Therefore I Blog Walkthrough Project. The custom code is all of my own creation.
