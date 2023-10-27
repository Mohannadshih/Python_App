# Python_App
App made using existing code from online courses to help learn how to use flask to create websites

## How to run

use the  `python -m flask run` command to start the app 
or use `docker build -t <name-image-here> .` to build a docker image to use and then
`docker run -d -p 5000:5000 <container-name-here>` to run the container in the background
using port 5000. In which the first port in `-p 5000:5000` is from the computer and the second port is 
within the container, so if you want you can do `-p 5005:5000` to map your 5005 port to the 5000 port 
within the container.

## Including .env file when running the app

Make sure to create a new .env file for you machine and include the `DATABASE_URL=` variable with your url login to access the PSQL database

## Webpage locations and how to use them

The actual html files for the webpages are located in the `/templates` folder and then all the static assets like css, javascript, images, and etc are located
in the `/static` folder.

## For changes in the tables within the database using the flask models

When changing a table within the database using the models within the `/models` folder. After the change has been made to the model, use
`python -m flask db migrate` to first intialize the migration and then `python -m flask db upgrade` to actually go through with the change.
Please verify that the changes you made to the database are actually correct within the `/migrations/versions` folder and if you decide
not to go through with the change in the database, then use `python -m flask db downgrade` to revert back to the previous version of the
database.

## Acessing the App's APIs

All the APIs made for the app are currently stored within the `/resources` folder.

