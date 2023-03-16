from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

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
  },
  3: {
    "name": "orange",
    "price": 0.35,
    "description": "A round citrus fruit with a tough bright reddish-yellow rind and juicy acid pulp."
  },
  4: {
    "name": "pear",
    "price": 0.4,
    "description": "A sweet juicy fruit that is narrow at the top and wider towards the bottom."
  },
  5: {
    "name": "grape",
    "price": 0.1,
    "description": "A small round fruit with a smooth skin and juicy flesh ranging in color from green to dark purple."
  }
}
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


@app.get("/")
def index():
    return {"welcome": "first Page"}


@app.get("/get_item_by_id/{item_id}")
def get_item_by_id(item_id: int = Path(None, description="The id of item", gt=0, lt=4)):
    return items[item_id]


@app.get("/get_item_by_name")
def get_item_by_name(*, name: Optional[str] = None, price: float):
    for item_id in items:
        if items[item_id]["name"] == name:
            return items[item_id]
    return {"Data": "Not Found!"}


@app.get("/get_item/{item_id}")
def get_item(item_id: int, q: str = None):
    item = items.get(item_id)
    if not item:
        return {"error": "Item not found"}
    if q:
        item.update({"q": q})
    return item


@app.post("/create_item")
def create_item(item_id: int, item: Item):
    if item_id in items:
        return {"error": "Item already exists!"}
    items[item_id] = item
    return items[item_id]