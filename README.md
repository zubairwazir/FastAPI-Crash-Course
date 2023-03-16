# FastAPI Crash Course


In FastAPI, path parameters and query parameters are two ways to accept data from a client.
## Path Parameter
Path parameters are used to capture parts of the URL path, and are declared by wrapping them in curly braces {} in the path. For example, in the following path "/items/{item_id}", {item_id} is a path parameter. The value of the path parameter is extracted from the URL and passed as an argument to the corresponding function in the application.<br>

Here's an example of a FastAPI endpoint that accepts a path parameter:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
In this example, the read_item function accepts a path parameter item_id of type int. When the client requests a URL like /items/42, the value 42 will be passed as the item_id argument to the function.

## Query Parameter
Query parameters are used to pass additional data in the URL query string. They are declared as function parameters with default values, and FastAPI will automatically parse the query string and populate the parameter with the corresponding value. For example, in the following URL /items?skip=0&limit=10, skip and limit are query parameters.<br>

Here's an example of a FastAPI endpoint that accepts query parameters:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

```
In this example, the read_items function accepts two query parameters skip and limit, both of type int with default values of 0 and 10 respectively. When the client requests a URL like /items?skip=20&limit=5, the function will receive skip=20 and limit=5 as the values for the corresponding parameters. If no values are provided in the URL, the function will use the default values.