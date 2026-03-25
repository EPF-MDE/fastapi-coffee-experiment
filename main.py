from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

coffees = []


class Coffee(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_home():
    return {"Hello": "World"}


@app.get("/coffees/{coffee_id}")
def read_coffee(coffee_id: int, q: str | None = None):
    return {"coffee_id": coffee_id, "q": q}


@app.post("/coffees")
def create_coffee(coffee_name: str, price: float, is_offer: bool | None):
    coffee = {"name": coffee_name, "price": price, "is_offer": is_offer}

    coffees.append(coffee)

    response = {"coffee_id": len(coffees) - 1, "coffee": coffee}

    return response


@app.put("/coffees/{coffee_id}")
def update_coffee(coffee_id: int, coffee: Coffee):
    return {"coffee_name": coffee.name, "coffee_id": coffee_id}
