# Twitter Clone

A simplified Twitter clone project built using Django. This project allows users to post content, follow other users, like posts, and manage their profile with a full authentication system. It includes features like creating, editing, and deleting posts, following users, and liking posts. All operations are managed through the **Explore** page.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Application Structure](#application-structure)
6. [Authentication System](#authentication-system)
7. [CRUD Operations](#crud-operations)
8. [How to Contribute](#how-to-contribute)
9. [License](#license)

---

## Project Overview

This project is a Twitter clone where users can:
- Explore posts
- Create posts
- Like/unlike posts
- Follow/unfollow users
- Edit or delete their posts
- Manage user profiles

Everything from post creation to interactions such as likes and follows is handled via the **Explore** page.

---

## Features

- **User Authentication**: Sign up, log in, log out, and password management (change, reset).
- **Profile Management**: Users can edit their profile information and change their profile picture.
- **Create, Read, Update, Delete (CRUD) operations** for posts.
- **Follow system**: Users can follow and unfollow each other.
- **Like system**: Users can like and unlike posts.
- **Responsive design** using HTML, CSS, and JavaScript for interactive user experience.

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/m-hasan-2004/twitter-clone.git
    ```

2. Navigate to the project directory:

    ```bash
    cd twitter-clone
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Visit the app at `http://127.0.0.1:8000/home/` and start exploring the features.

---

## Usage

### Home Page
The home page serves as an explore page where users can view all posts, follow/unfollow users, like/unlike posts, and create new posts. You must be logged in to access the explore page and interact with posts.

### CRUD Operations

#### 1. **Create Post**:
   - Go to the Explore page.
   - Click on **"Create Your Custom Post"** button.
   - Fill in the title, description, and optionally upload an image.
   - Submit the form to create a new post.

#### 2. **Read Post**:
   - Posts are displayed on the **Explore** page. Users can see the title, description, image (if any), and the number of likes/comments.
   
#### 3. **Edit Post**:
   - Only the post author can edit their post.
   - On the **Explore** page, if you are the author of a post, you will see an **Edit** button beneath your post.
   - Click on **Edit**, make changes, and submit the form to update your post.

#### 4. **Delete Post**:
   - Only the post author can delete their post.
   - On the **Explore** page, if you are the author of a post, you will see a **Delete** button beneath your post.
   - Click on **Delete** to remove the post.

### Like/Unlike Posts
   - On the **Explore** page, each post has a like button.
   - Click the heart icon to like a post. If you have already liked it, clicking again will unlike it.
   - The like count updates dynamically.

### Follow/Unfollow Users
   - If you're not following a user, you'll see a **Follow** button beside their profile on their post in the **Explore** page.
   - Once followed, the button does not change.

---

## Application Structure

The application is organized into three Django apps:

1. **Social**: Handles all social functionalities like posts, likes, follows, and comments.
2. **Users**: Manages user registration, authentication, and profile management.
3. **Core**: Handles the common functionality of the project.

### **Social App**
- Handles **CRUD** for posts, likes, and follows.
- Views for post creation, updates, and deletions.
- Manages the Explore page where all operations take place.

### **Users App**
- Manages user registration, login, logout, profile updates, and password management.
- Templates for **sign up, log in, change password**, and **edit profile**.

### **Core App**
- Contains settings and root configurations for the project.

---

## Authentication System

The project uses Django’s built-in authentication system with custom extensions for user profiles.

### Features:
- **Sign Up**: Allows new users to register for an account. 
- **Log In**: Existing users can log in with their credentials.
- **Password Management**: Users can change or reset their password.
- **Profile Management**: Users can update their profile information, including uploading a profile picture.
  
The authentication system is integrated with Django’s user model, and the custom user forms are defined in the **Users App**.

---

## CRUD Operations (Detailed)

All CRUD operations (Create, Read, Update, Delete) for posts are handled in the **Explore** URL. 
- **Create**: Users can create posts directly from the Explore page.
- **Update**: Post authors can edit their own posts.
- **Delete**: Post authors can delete their own posts.
- **Read**: All posts are visible on the Explore page.

Each action is accompanied by server-side validation and proper authentication checks. For instance, only the author of a post can edit or delete it.

---

## How to Contribute

If you want to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-or-bugfix-name
   ```
3. Commit your changes and push them to your forked repository:
   ```bash
   git push origin feature-or-bugfix-name
   ```
4. Create a pull request and explain your changes.
