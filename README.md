# FastAPI Crash Course
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints. It provides a simple and intuitive way to create robust, scalable, and maintainable web APIs. FastAPI leverages the latest Python features and the powerful data validation and serialization capabilities of the Pydantic library to provide a more efficient development experience with fewer bugs. FastAPI is also designed to be easy to learn and use, with excellent documentation and an active community of developers contributing to its development and support.Some of its notable features include:

1. High Performance: FastAPI is designed for high performance, thanks to its use of asynchronous programming and modern Python features like type hints.

2. Easy to Use: FastAPI is easy to learn and use, with a simple and intuitive API that makes it quick to get up and running.

3. Data Validation: FastAPI leverages the powerful data validation and serialization capabilities of the Pydantic library to ensure that data is well-formed and properly typed.

4. Integration with Popular Databases and ORMs: FastAPI seamlessly integrates with popular databases and ORMs such as PostgreSQL, MySQL, SQLite, MongoDB, SQLAlchemy, and Tortoise ORM, providing flexibility to developers to utilize their preferred database technology and ORM to manage their data.

5. Automatic API Documentation: FastAPI automatically generates comprehensive and interactive API documentation based on the code itself, making it easy to explore and understand the API.

6. OpenAPI and JSON Schema: FastAPI fully supports the OpenAPI and JSON Schema standards, providing a standardized way to describe APIs and their data.

7. Fast Development: FastAPI provides a smooth development experience with features like live reload, interactive API documentation, and an easy-to-use development server.

8. Testability: FastAPI is highly testable, with built-in support for testing and debugging APIs.

### Terms related to FastAPI:
Here's a brief explanation of some of the terms related to FastAPI:

1. Path operation functions: In FastAPI, a path operation function is a Python function that handles a specific HTTP request method (such as GET, POST, PUT, DELETE, etc.) and URL path.

2. Path parameters: Path parameters are part of the URL path that are used to capture specific values from the client's request. They are defined in the path of a route using braces {}.

3. Query parameters: Query parameters are additional parameters that can be added to the end of a URL path to modify the behavior of an API endpoint. They are defined after a ? in the URL and can be accessed using the request object.

4. Request body: The request body is the data sent by the client in the request payload. FastAPI can automatically parse the request body and generate appropriate type hints for the data.

5. Response model: In FastAPI, you can specify the structure of the response data using Pydantic models. This allows for automatic serialization of response data into the appropriate format (such as JSON).

6. Pydantic: Pydantic is a data validation and serialization library that is used heavily in FastAPI. It provides a simple and intuitive way to validate and convert data between Python objects and JSON.

7. OpenAPI: OpenAPI is a specification for building APIs, including a standardized way to describe APIs and their data. FastAPI fully supports the OpenAPI standard and provides tools to generate OpenAPI documentation automatically.

8. Swagger UI: Swagger UI is a web-based tool for exploring and testing APIs. FastAPI automatically generates a Swagger UI page that allows developers to test and explore the API endpoints.

9. JSON Schema: JSON Schema is a vocabulary for describing JSON data, including its structure, data types, and validation constraints. FastAPI uses JSON Schema extensively for data validation and serialization.

10. ASGI: ASGI (Asynchronous Server Gateway Interface) is a protocol for building asynchronous web applications in Python. FastAPI is built on top of ASGI and provides a high-performance web server that is optimized for handling large volumes of traffic.

Overall, FastAPI is a powerful and flexible web framework that makes it easy to build high-performance APIs in Python. Its support for asynchronous code, automatic API documentation generation, and Pydantic data validation make it a great choice for building modern web applications.

## Exploring Key Features and Code Examples
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
def get_item(item_id: int, q: str = None):
    item = items.get(item_id)
    if not item:
        return {"error": "Item not found"}
    if q:
        item.update({"q": q})
    return item
```
In this example, the endpoint is defined using the @app.get decorator, which specifies that it responds to HTTP GET requests. The endpoint path includes a path parameter, item_id, which is defined by enclosing it in curly braces {}. The endpoint also includes a query parameter, q, which is optional and has a default value of None.

When the endpoint is called, the value of item_id is taken from the path parameter in the URL, and the value of q is taken from the query string, if it is present. The endpoint returns a JSON response containing both parameter values. 

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
 
 The **@app.get**, **@app.post**, **@app.put**, **@app.patch**, **@app.delete**, **@app.options**, and **@app.head decorators** are used to create endpoints that respond to the corresponding HTTP methods.
## Request Body and Post Method
In FastAPI, you can define a request body using the BaseModel class from the pydantic module. A request body is the data that the client sends to the server as part of a POST request. <br>

Here's an example of how to define a request body for adding a new item to the items dictionary using the POST method:

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

items = {}

@app.post("/create_item")
def create_item(item_id: int, item: Item):
    if item_id in items:
        return {"error": "Item already exists!"}
    items[item_id] = item
    return items[item_id]
```
In this example, we first define a new Item class that inherits from the BaseModel class in FastAPI's pydantic module. The Item class has three fields: name, price, and description.

Next, we define the create_item endpoint with the @app.post decorator. In the create_item function, we define a parameter called item with the type Item, which is the class we defined earlier. This means that the request body should have JSON data with the same keys as the attributes of the Item class. This endpoint takes an Item object as the request body, which is automatically parsed and validated by FastAPI based on the field types and validation rules specified in the Item class.

Inside the endpoint, we generate a new item_id based on the current length of the items dictionary, add the new item to the dictionary with the item_id as the key, and return a response containing the new item_id.

## PUT Method
Here's an example of using the PUT method in FastAPI:
```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None

items = {
  1: {
    "name": "apple",
    "price": 0.5,
    "description": "A sweet fruit with a red or green skin and a core containing seeds."
  },
  2: {
    "name": "banana",
    "price": 0.25,
    "description": "A long curved fruit with a yellow skin and soft sweet flesh."
  }
}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: UpdateItem):
    if item_id not in items:
        return {"error": "Item not found"}
    
    if item.name != None:
        items[item_id]["name"] = item.name
    if item.price != None:
        items[item_id]["price"] = item.price
    if item.description != None:
        items[item_id]["description"] = item.description

    return {"message": "Item updated successfully"}
```
In this example, we have defined a PUT endpoint that updates an existing item by ID. We have used the Item class that we defined earlier, and we have assumed that we already have a dictionary called items that contains the existing items.

The endpoint takes two parameters - item_id and item. The item_id parameter is a path parameter that specifies the ID of the item that needs to be updated. The item parameter is a request body parameter that contains the updated information for the item.

We first check if the specified item_id exists in the items dictionary. If it doesn't, we return an error message. If it does, we update the corresponding item with the data from the item parameter. We use the dict() method of the Item object to convert it to a dictionary before updating the items dictionary.

Finally, we return a message indicating that the item was updated successfully.

## DELETE Method

In FastAPI, you can define a DELETE method to handle HTTP DELETE requests. The DELETE method is typically used to delete a specific resource identified by a unique identifier.<br>

Here's an example of how you can implement a DELETE method to delete an item from the items dictionary based on its ID:
```
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "Item not found"}
    del items[item_id]
    return {"message": "Item deleted successfully"}

```
In this example, the delete_item function takes a item_id parameter which is passed in through the path parameter of the URL. If the item with the specified ID does not exist in the items dictionary, the function returns an error message. Otherwise, it deletes the item from the dictionary using the del keyword, and returns a success message.

Note that it's important to handle errors gracefully in your application to provide informative error messages to clients. In this example, if the item is not found, we return an error message with an appropriate HTTP status code (e.g. 404 Not Found).

**Author:** [Zubair Ahmad](https://zubairwazir.github.io/)

**Contact:** Follow me on [LinkedIn](https://www.linkedin.com/in/zubairwazir/) and [Twitter](https://twitter.com/zubairwazir777)
