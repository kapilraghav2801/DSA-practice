from fastapi import FastAPI,HTTPException
from datetime import datetime

app = FastAPI(title="Digital Store API")

inventory = [
    {"id":1, "name": "Laptop", "price": 25000, "stock": 10},
    {"id":2, "name": "Printer", "price": 2500, "stock": 15},
    {"id":3, "name": "Laptop", "price": 42000, "stock": 2},
    {"id":4, "name": "Laptop", "price": 55000, "stock": 3}

]

@app.get("/")
async def home():
    return {
        "store_name": "Digital Store",
        "version" : 1.0,
        "endpoints": ["/items", "/items/{id}", "/health"]
    }

@app.get("/health")
async def health():
    return {
        "status": "operational",
        "timestamp": datetime.now().isoformat(),
        "items_in_stock": len([i for i in inventory if i["stock"] > 0])
    }

@app.get("/items{item_id}")
async def get_item(item_id: int):

    item = next((item for item in inventory if item[id] == item_id), None)

    if not item:
        raise HTTPException(status_code=404, detail=f"item{item_id} not found")
    
    return item

@app.get("/items/search/")
async def search_item(name: str, min_price: float = 0.0):

    results = [
        item for item in inventory
        if name.lower() in item["name"].lower() and item["price"] >= min_price
    ]
    return {"results": results, "count": len(results)}