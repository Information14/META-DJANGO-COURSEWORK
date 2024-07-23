# Little Lemon App


## Main Steps
1. **Create an environment:**

    **Windows:**
    ```
    python -m venv env
    ```
    **MacOS:**
    ```
    python3 -m venv env
    ```

2. **Environment activate:**

    **Windows:**
    ```
    .\env\Scripts\activate
    ```
    **MacOS:**
    ```
    source env/bin/activate
    ```

3. **Install Django:**

    **Windows:**
    ```
    pip install django
    ```
    **MacOS:**
    ```
    pip3 install django
    ```

    **Verify Django Version:**

    **Windows:**
    ```
    python -m django version
    ```
    **MacOS:**
    ```
    python3 -m django version
    ```

4. **Start Project:**

    ```
    django-admin startproject <name> .
    ```

5. **Create APP:**

    **Windows:**
    ```
    python -m django startapp <name>
    ```
    **MacOS:**
    ```
    python3 -m django startapp <name>
    ```

    **OR**

    **Windows:**
    ```
    python manage.py startapp <name>
    ```
    **MacOS:**
    ```
    python3 manage.py startapp <name>
    ```

6. **Run Server:**

    ```
    cd myproject
    ```

    **Windows:**
    ```
    python manage.py runserver
    ```
    **MacOS:**
    ```
    python3 manage.py runserver
    ```

7. **Deactive Environment:**

    ```
    deactivate
    ```

    ## Project Overview
By working through the lessons in this course, you've learned the necessary skills and knowledge to create a website in Django by creating a project and an app.

You were provided with code snippets and tasked with using these, plus your own code, to create a website that showcases the menu pages of the Little Lemon restaurant.

Users visit the homepage and can navigate to the pages About, Menu and Book using the main menu.

The menu page contains a list of the menu items that are stored in the database. Each menu item has been added using the Django Administration user interface and contains the following information:

Name

Price

Description

Image

Each menu item contains a link that displays a dedicated page for the individual item.