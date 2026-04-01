from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

coffees = []

templates = Jinja2Templates(directory="templates")


class Coffee(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        context={"coffees": coffees, "welcome_message": "Have one, not a hundred!"},
    )


@app.get("/coffees/{coffee_id}")
def read_coffee(coffee_id: int, quantity: int | None = None):
    return {"coffee_id": coffee_id, "coffee": coffees[coffee_id], "quantity": quantity}


@app.post("/coffees")
def create_coffee(coffee_name: str, price: float, is_offer: bool | None):
    coffee = {"name": coffee_name, "price": price, "is_offer": is_offer}

    coffees.append(coffee)

    response = {"coffee_id": len(coffees) - 1, "coffee": coffee}

    return response


@app.put("/coffees/{coffee_id}")
def update_coffee(coffee_id: int, coffee: Coffee):
    # print("coffees", coffees)

    coffees[coffee_id].update(coffee)

    # print("coffees[coffee_id]", coffees[coffee_id])

    response = {"coffee_name": coffees[coffee_id]["name"], "coffee_id": coffee_id}

    # print("response", response)

    return response
