from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_home():
    return {"Hello": "World"}


@app.get("/coffees/{coffee_id}")
def read_coffee(coffee_id: int, q: str | None = None):
    return {"coffee_id": coffee_id, "q": q}
