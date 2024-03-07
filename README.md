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
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Open your browser at http://127.0.0.1:8000/

You will see a JSON response of the current database of users.

Go to http://127.0.0.1:8000/docs

There you can see an interactive API documentation provided by Swagger UI.
You can find the four CRUD functionalities which this API provides:

<details><summary>GET - fetch users</summary>
</details>
<details><summary>POST - register users</summary>
</details>
<details><summary>DELETE - delete users</summary>
</details>
<details><summary>PUT - update users</summary>
</details>
