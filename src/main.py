from fastapi import FastAPI
from .database import Base, engine
from .api.product_routes import router as product_router
from .api.category_routes import router as category_router
from .seed import seed_database

Base.metadata.create_all(bind=engine)
seed_database()


app = FastAPI()

app.include_router(product_router)
app.include_router(category_router)

@app.get("/health")
def health():
    return {"status": "UP"}
