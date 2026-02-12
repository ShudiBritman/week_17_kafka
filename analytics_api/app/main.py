from fastapi import FastAPI



app = FastAPI()


@app.get("/analytics/top-customers")
def customrs_with_more_orders():
    pass


@app.get("/analytics/customers-without-orders")
def customers_without_orders():
    pass


@app.get("/analytics/zero-credit-active-customers")
def customers_with_zero_credit_limit():
    pass



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)