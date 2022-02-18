from ast import Gt
import re
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    Name: str
    Price: str
    Status: Optional[str]= None
class UpdateItem(BaseModel):
    Name: Optional[str] = None
    Price: Optional[str] = None
    Status: Optional[str]= None

inventory = {}

@app.get("/get_item/{item_id}")
def get_item(item_id: int = Path(None, description="ID of the element", gt=0)):
    return inventory[item_id]

@app.get("/get_by_name/{item_id}")
def get_item(*, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id].Name==name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Name not found")

@app.post("/create_item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item present")
    inventory[item_id]= item
    return inventory[item_id]

@app.put("/update_item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="ID not found")
    if item.Name != None:
        inventory[item_id].Name = item.Name
    if item.Price != None:
        inventory[item_id].Price = item.Price
    if item.Status != None:
        inventory[item_id].Status = item.Status
    
    return inventory[item_id]

@app.delete("/delete_item")
def delete_item(item_id: int = Query(..., description="Enter item id of item to be deleted")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="ID not found")
    del inventory[item_id]