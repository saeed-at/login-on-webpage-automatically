# Auto Connect WiFi


  <p align="center">
  <img 
    width="250"
    height="250"
    src="./images/logo.png"
  >
</p>

# Introduction
<div style="text-align: justify"> This code has been written for logging automatically in the AmirKabir University's internet site. Each time when you turn on your PC or laptop, you have to connect to the university's router, then you have to open your browser and go to https://internet.aut.ac.ir and fill in your username and password on this webpage as below, after logging in you will have access to the internet with your system. </div>
  <p align="center">
  <img 
    width="700"
    height="300"
    src="./images/login_page.png"
  >
</p>

<div style="text-align: justify"> I wonder if I could write a code that logs in automatically with each startup in windows os and this code will do the trick. ( it's easy to change to code for another login page; you need to replace username, password, and Enter elements with your website's elements by using inspect in the browser; if you have any problems email me :wink:).
  
 The code will automatically try connecting to the `wifi names` list that you set in the `config.txt` file and after that, it will log in with the `username` and `password` you have put in the `config.txt` file. If no known WiFis are available, it will get you an error message that no wifi is available.</div>

# Steps to setup code to work as it should
## Step1 : Install python and required modules


First, install python and then use this command to install all required modules for the requirements.txt file with the code as below in cmd:
```
pip install -r requirements.txt
```
## Step 2 : Move copy files from `src` folder to `startup` folder and make cmd file to run it:

First, you have to find the startup folder, press `Windows + R` and then write `shell:startup` and press OK and copy all files from `src` to the window that opened by pressing OK. Now make a text file in the startup directory and write this command in it :
```
python {your_startup_path}\main.py
```
Then save the text file and change its name to `run_my_code.cmd`. Startup directroy should look like this :  <p align="center">
  <img 
    width="1000"
    height="150"
    src="./images/startup.png"
  >
</p>

## Step 3 : Set config.txt

You have to set your username, password, url, wifi names in `config.txt` as below.: (remember that there is always a space after each `:` and wifi names are your default wifi's SSIDs)
 <p align="center">
  <img 
    width="700"
    height="300"
    src="./images/config.txt.png"
  >
</p>

