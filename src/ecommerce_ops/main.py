from fastapi import FastAPI

from ecommerce_ops.api.health import router as health_router

app = FastAPI(
    title="AI E-commerce Operations Platform",
    description="An operational investigation platform for e-commerce sellers.",
    version="0.1.0",
)

app.include_router(health_router)
