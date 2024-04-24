## Arabic Calligraphy

HI! Welcome to my project website showcasing the various styles of Arabic Calligraphy.

# Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

# Introduction

The purpose of this project is to showcase the various styles of Arabic Calligraphy, its History and where it originated from. 
It is an art form that utilises pens, brush, hammer and chisel all made by either hand or machine. Many artists use this artform 
as a means of expression and the result shows the passion they have for a specific art style. Many have mastered the craft as it 
requires a steady hand, creativity, imagination yielding near to perfection result and the amount of time spent crafting that is often overlooked when we pass a
picture frame hanging on the walls in our homes , places of work, marketplaces etc.

# Features

- Gallery showcasing various styles.
- Ease of access to history of specific style when clicked on it.
- Menu in the top left corner to redirect to selected page.
- Logout option in the top right corner.
- Easy-to-navigate

## Requirements

- Python 3.0 (latest version)
- Virtual environment activated
- GIT installed
- Pip (python package installer)
- Code editor IE. Pycharm, VS code etc
- Docker installed

##  Installation

1. **Clone the repository:**

   git clone https://github.com/StormBo1/Consolodation.git

2. **Navigate to Project directory:
   cd ConsolodationP

3. ** Install Dependancies:**
   Run the following command to install the below dependancies: pip install -r requirements.txt
   GIT installed
   (in your terminal type the following)
   pip install
   pip install django
   pip install pillow

5. ** Run the project after looking at the USAGE section in the README:**

   python manage.py runserver

## Usage

- Once the installation is done...run the project by typing in: python manage.py runserver 
Make sure your are in the right directory.
![manage](https://github.com/StormBo1/Consolodation/Images/148717363/manage.jpeg)

- Once you have successfully run the project a URL will appear in the terminal...click on it
![development server](https://github.com/StormBo1/Consolodation/Images/148717363/development_server.jpeg)


- A login page will pop up. select login
![login](https://github.com/StormBo1/Consolodation/Images/148717363/login.jpeg)

- After selecting login change the following
- from http://127.0.0.1:8000/login/
- to http://127.0.0.1:8000/signup/
Once you have successfuly change the page you will see the following:
![signup](https://github.com/StormBo1/Consolodation/Images/148717363/signup.jpeg)

- After succesfully signing up you will be redirected to the Display page of the project:
![webpage](https://github.com/StormBo1/Consolodation/Images/148717363/webpage.jpeg)

- Once you are done viewing the webpage, dont forget to logout and end the server in your terminal by pressing CTRL BREAK buttons together

## Usage with venv

1. Set up the Virtual Environment (venv)
- Navigate to the project directory in your terminal.
- Create a virtual environment using the following command:
  - python -m venv venv
- Activate the virtual environment:
  - On Windows:
  - venv\Scripts\activate
- On macOS and Linux:
  - source venv/bin/activate

2. Run the project:
- python manage.py runserver

## Usage with Docker

1. Build Docker Image:
- Ensure Docker is installed and running:
  - docker build -t arabic_calligraphy .

2. Run Docker Container:
- Once the image is built, run the Docker container:
    - docker run -d -p 8000:8000 arabic_calligraphy

## Credits

[Arabic Calligraphy](https://en.wikipedia.org/wiki/Arabic_calligraphy)

[Islamic Calligraphy](https://en.wikipedia.org/wiki/Islamic_calligraphy)

## URL to repository

[Consolodation](https://github.com/StormBo1/Consolodation)
