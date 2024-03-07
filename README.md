# Users database WebAPI

Please note: This WebAPI is still a work in progress. The current functionality is limited and a UI has yet to be added.

**How to run**

You will need to install the framework fastapi:

```console
$ pip install fastapi

---> 100%
```


You will also need a server, to run the API such as <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a>.


```console
$ pip install "uvicorn[standard]"

---> 100%
```


Run the server with:

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720] using WatchFiles
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Open your browser at http://127.0.0.1:8000/

You will see a JSON response of the current database of users.

Go to http://127.0.0.1:8000/docs

There you can see an interactive API documentation provided by Swagger UI.
You can find the four CRUD methods which this API provides:

<details><summary>GET - fetch users</summary>
  If you collapse the GET method, you can press the button *Try it out*.
  If you now press the button *Execute* you can view the response down below.
  The Code *200* means that the request was successful.
  Inside the *response body* you can see the results of the request - the current users in the database.
</details>
<details><summary>POST - register users</summary>
  If you collapse the POST method, you can press the button *Try it out*.
  With the POST request you are able to register a new user.
  Inside the *Request body <sup>required</sup>* you can find the variables where you can assign the values for a user that you want to create.
  
  The *id* variable is optional, as the API will assign a UUID automatically if none is provided. Be aware that only valid UUIDs are accepted.
  
  The *first_name* and *last_name* are required fields. Please enter the first and last name of the new user inside the quotation marks where "string" is written.
  
  The *middle_name* is optional. You may delete this row if you do not wish to assign a middle name to the user.
  
  The *gender* is required. You can assign either *male*, *female*, or *other* by writing it inside the quotation marks.
  
  The *roles* is required. You can assign multiple roles to a user. The following roles are available and can be written inside the quotation marks:
  admin, teacher, assistant, student, researcher
  If you want to assign several roles to a user, add a comma after the quotation marks of the first role and add the next role in a new set of quotation marks.
  
  
  If you now press the button *Execute* you can see in the response down below code 200, meaning the request was a success, and see in the response body the *id* assigned to the new user.
</details>
<details><summary>DELETE - delete users</summary>
  If you collapse the DELETE method, you can press the button *Try it out*.
  With the DELETE request you are able to remove an existing user from the database.
  Enter the UUID of an existing user into the *user_id* field and press *Execute*.
  In the response window down below the code 200 shows that the request was a success. If you want to confirm which users are left in the database, you can do a GET request as described above.
</details>
<details><summary>PUT - update users</summary>
  If you collapse the PUT method, you can press the button *Try it out*.
  With the PUT request you are able to update the data of an existing user.
  First you need to enter the UUID of that user in the *user_id* field.
  Then you can change the values which you would like to update in the request body below.
  Be aware to delete the variables from the request body, which you do not want to update.
  When you press the button *Execute* you will see the code 200 below, meaning the request was a success and the user information was updated. If you want to confirm the updated user information, you can do a GET request as described above.
</details>
