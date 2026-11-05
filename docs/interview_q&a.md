# AI E-commerce Operations Platform — Interview Q&A

This document contains technical, architectural, product, and engineering interview questions related to the project.

Answers should reflect the actual implementation and documented decisions.

---

## Q1. Why did you choose a Modular Monolith architecture instead of Microservices?

**Answer:**

I chose a Modular Monolith architecture because the initial version of the AI E-commerce Operations Platform has a focused workflow and does not require independently deployed services.

The application contains multiple functional modules, such as CSV Import, Validation, Reconciliation, Investigation Management, Evidence Management, and AI Assistance.

Although these modules have separate responsibilities, they can initially operate within one backend application.

They communicate through internal Python interfaces instead of network-based communication between independently deployed services.

This approach provides:

- Clear separation of responsibilities.
- Simpler development and debugging.
- Easier testing.
- Lower deployment complexity.
- Less infrastructure overhead.

Microservices would introduce additional complexity, including service communication, independent deployments, distributed failure handling, and service-level monitoring.

I would reconsider microservices if individual modules eventually required independent deployment, scaling, or operational ownership.

**Key Interview Concept:**

A Modular Monolith is one deployable application organized into logically independent modules with controlled dependencies. It provides modularity without requiring distributed infrastructure.

**Related Concepts:**
- Software architecture
- Modular design
- Separation of concerns
- Tight coupling and loose coupling
- Microservices
- Deployment complexity

**Implementation Status:** Architecture decision accepted; implementation pending.

---

## Q2. Why did you use FastAPI APIRouter?

**Answer:**

I used FastAPI's `APIRouter` to organize API endpoints into separate modules based on their responsibilities.

For example, the health-check endpoint is implemented in `api/health.py`, while the main application is configured in `main.py`.

The main application registers the router using `app.include_router()`.

This approach provides separation of concerns, improves maintainability, and allows new API modules to be added without making the main application file unnecessarily large.

---

## Q3. Why did you choose the src/ layout in your Python project?

**Answer:**

I chose the `src/` layout to separate application code from project-level files such as configuration, documentation, tests, and dependency management.

My application package is located at `src/ecommerce_ops/`.

I configured Hatchling as the build backend and used `uv` to install the package.

This approach establishes a clear package boundary and helps ensure that the application is imported as an installed package rather than accidentally relying on the project root being on Python's import path.
