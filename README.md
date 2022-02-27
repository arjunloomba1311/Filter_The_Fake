# Filter_The_Fake

Important note - due to github constraints and a 100mb limit we haven't been  able to upload our complete code - a link to the complete code is given in this drive link - https://drive.google.com/file/d/1gbQc4_wORvQxS1ah4dnwQpVCS4LYcgOx/view

What's missing in this repo? 

Weights for our ML model, some images, some external ML supporting files. 


## What does our App look like? 

<img width="911" alt="Screenshot 2022-02-26 at 9 21 52 PM" src="https://user-images.githubusercontent.com/34513460/155869354-5e37e044-b4fb-418d-bf25-1720e677a93f.png">


<img width="917" alt="Screenshot 2022-02-26 at 9 21 48 PM" src="https://user-images.githubusercontent.com/34513460/155869355-e0c476b4-3243-4036-b9f5-5c557c1c8e5c.png">

<img width="955" alt="Screenshot 2022-02-26 at 9 21 43 PM" src="https://user-images.githubusercontent.com/34513460/155869357-c93b4ed0-af2b-4c40-8568-19df7fe81848.png">


## How does our Django Backend Work? - 

Our settings.py file defines the overall settings of the website, gives the backend information about our front-end directory, and defines the path to our data-base. 

Next, our urls.py defines the endpoints which our website must open on depending on any link that the user might click. This data is then sent to the main backend logic file - views.py. 

When a POST request is created, data is taken from the form in the front end (i.e. the image) and is sent to views.py file. In our views.py file we get the data that is sent by the user and parse it if required. We then pass this data into our implement model function which first preprocesses the data and then uses the model weights to fill in some parameters i.e. alignment, Rx number presence. 

This renders the data further onto our front end.

## How we built it

After the user uploads their image:
We setup an SQL server to which this image is pushed
The database then sends this image to our Django backend
We use OpenCv to crop the image, identify all text and colors, check for spelling errors
This cleaned image is passed to a CNN which detects the presence of the Rx symbol
The results of the model run are parsed into a user friendly format
This final format is pushed to the website wherein we display an accuracy score and all parameters are displayed


