# jpmorgan-hackathon-backend
My portion of a team project built for JP Morgan's Code For Good hackathon in 2020. 

This backend is a Python API built with Flask-RESTPlus.

This API is meant to connect to a Firebase Cloud Firestore to directly add, delete, and modify data. To do this download and place the key.json file in the source folder (directions: rb.gy/nosksb). Run the app.py and interact with the database through the SwaggerUI, the app assumes it's accessing a collection specified in the users_ref variable in config.py.
