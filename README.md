# FastAPI Crash Course

## HTTP Methods
FastAPI supports several HTTP methods that can be used to define different types of endpoints in an application. Here's a short description of each HTTP method in FastAPI:

- **GET**: Used to retrieve a resource or a list of resources. This method should be safe and idempotent, meaning it should not modify any data on the server.

- **POST**: Used to create a new resource. This method is not idempotent, meaning multiple requests can result in multiple resource creations.

- **PUT**: Used to update an existing resource. This method should be idempotent, meaning multiple requests should result in the same resource state.

- **PATCH**: Similar to PUT, but used to partially update an existing resource.

- **DELETE**: Used to delete an existing resource. This method should be idempotent, meaning multiple requests should result in the same resource state.

- **OPTIONS**: Used to retrieve information about the communication options available for a resource.

- **HEAD**: Similar to GET, but only retrieves the HTTP headers for a resource, without the actual content.

In FastAPI, each of these **HTTP methods can be mapped to a Python function that defines the behavior of the corresponding endpoint**.
 
 The **@app.get**, **@app.post**, **@app.put**, **@app.patch**, **@app.delete**, **@app.options**, and **@app.head decorators** are used to create endpoints that respond to the corresponding HTTP methods. <hr>

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

## Combining Path and Query Parameters
We can combine path and query parameters in FastAPI.<br>
Here's an example of how to define an endpoint that uses both path and query parameters:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def get_item(item_id: int, q: str = None):
    return {"item_id": items[item_id], "q": q}
```
In this example, the endpoint is defined using the @app.get decorator, which specifies that it responds to HTTP GET requests. The endpoint path includes a path parameter, item_id, which is defined by enclosing it in curly braces {}. The endpoint also includes a query parameter, q, which is optional and has a default value of None.

When the endpoint is called, the value of item_id is taken from the path parameter in the URL, and the value of q is taken from the query string, if it is present. The endpoint returns a JSON response containing both parameter values.