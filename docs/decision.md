
# Architecture & Product Decision Log

This document records important product, architectural, and technical decisions made during the development of the AI E-commerce Operations Platform.

Decisions are recorded chronologically with their context, reasoning, alternatives, trade-offs, and status.

**Decision statuses:**

- Proposed
- Accepted
- Rejected
- Superseded

---

## ADR-001: Adopt a Modular Monolith Architecture

**Status:** Accepted

**Category:** Architecture

**Date:** 2026-11-04

### 1. Context

The platform requires multiple functional modules, including:

- CSV Import
- Data Validation
- Event Normalization
- Reconciliation
- Investigation Management
- Evidence Management
- AI Assistance
- Audit History

We need an architecture that supports clear separation of responsibilities without introducing unnecessary operational complexity.

### 2. Decision

Adopt a **Modular Monolith Architecture** for the initial implementation.

The application will run as one deployable backend application, with logically separated modules and clearly defined internal interfaces.

Modules will communicate through internal Python functions, classes, and interfaces rather than independent HTTP services.

### 3. Alternatives Considered

**Option A — Modular Monolith**

- One application and deployment.
- Independent logical modules.
- Internal communication through Python interfaces.
- Simpler local development and testing.

**Option B — Microservices**

- Multiple independently deployed services.
- Network-based communication.
- Independent deployment and scaling.
- Additional infrastructure and operational complexity.

### 4. Reasoning

A modular monolith is appropriate for the initial product because:

1. The MVP has a focused workflow.
2. Independent service deployment is not currently required.
3. Internal Python communication is sufficient.
4. It allows clear module boundaries.
5. It reduces infrastructure and debugging complexity.
6. It allows future architectural evolution if actual requirements justify it.

### 5. Consequences and Trade-offs

**Advantages:**

- Simpler deployment.
- Easier local development.
- Easier debugging.
- Lower operational complexity.
- Clear separation of business responsibilities.

**Trade-offs:**

- Modules share one application runtime.
- Modules cannot be independently deployed.
- Poor module boundaries could create tight coupling.
- Scaling individual modules independently is not straightforward.

### 6. Architectural Guidelines

- Each module must have a clearly defined responsibility.
- Modules should communicate through controlled interfaces.
- Avoid unnecessary cross-module dependencies.
- Keep business logic separate from API routing.
- Do not introduce microservices without a demonstrated requirement.

### 7. Reconsideration Conditions

Reconsider this decision if:

- A module requires independent deployment.
- Independent scaling becomes necessary.
- Different modules require substantially different operational characteristics.
- Team ownership requires service-level separation.

### 8. Final Decision

The initial backend will use a modular monolith architecture with internal Python communication.

This decision applies to the initial implementation and can be explicitly superseded if future evidence justifies a different architecture.

---

## ADR-002: FastAPI Router-Based API Organization

**Status:** Accepted and Implemented

### Context

Initially, the FastAPI application and health-check endpoint were defined together in `main.py`.

As the application grows, more endpoints will be required for imports, investigations, reconciliation, and other business capabilities.

Keeping all endpoints in one file would make the application harder to maintain and extend.

### Decision

Use FastAPI's `APIRouter` to organize API endpoints into separate modules based on their responsibilities.

The application entry point will register the required routers using `app.include_router()`.

Initial implementation:

- `src/ecommerce_ops/main.py` — Creates and configures the FastAPI application.
- `src/ecommerce_ops/api/health.py` — Handles health-check endpoints.

Future API routers will be created when their respective features are implemented.

### Alternatives Considered

1. Keep every endpoint inside `main.py`.
2. Organize endpoints using separate FastAPI router modules.
3. Create separate microservices for different capabilities.

### Rationale

The router-based approach provides:

- Separation of concerns.
- Better code organization.
- Easier testing and maintenance.
- A clear place for new API endpoints.
- Compatibility with the Modular Monolith architecture.

### Trade-offs

**Advantages:**
- Individual API modules have clear responsibilities.
- The main application file remains small.
- New routes can be added without continuously expanding `main.py`.

**Disadvantages:**
- Requires additional files.
- Routers must be explicitly registered with the application.

### Reconsideration Conditions

The API organization can be refactored if the number of endpoints or complexity of the application makes the current structure difficult to maintain.

Separate services will only be considered if there is a demonstrated architectural need.

### Implementation Evidence

- Created `api/health.py` using `APIRouter`.
- Registered the health router in `main.py`.
- Verified the `/health` endpoint.
- Confirmed that both automated health-check tests pass.

---

## ADR-003: Adopt the Python src/ Package Layout

**Status:** Accepted and Implemented

### Context

Initially, the application code was located directly in the project root.

As the project grows, application code, configuration, tests, documentation, and supporting files need clear separation.

Python projects commonly use a `src/` layout to keep application packages separate from the project root.

### Decision

Adopt the `src/` layout for the application.

The main application package is:

`src/ecommerce_ops/`

The package contains the application entry point and feature-specific modules.

Initial structure:

- `src/ecommerce_ops/main.py` — FastAPI application entry point.
- `src/ecommerce_ops/api/` — API route modules.
- `tests/` — Automated tests.
- `docs/` — Project documentation.
- `notes/` — Research and working notes.

Configure Hatchling as the package build backend and install the project through `uv`.

### Alternatives Considered

1. Keep application code in the project root.
2. Use a `src/` layout with an installable Python package.

### Rationale

The `src/` layout provides:

- Separation between application code and project configuration.
- A clear Python package boundary.
- More reliable package import and installation behaviour.
- Better alignment between development and deployment environments.
- Easier long-term project organization.

### Trade-offs

**Advantages:**
- Cleaner project root.
- Explicit application package.
- Encourages correct package installation and imports.

**Disadvantages:**
- Requires package configuration.
- Requires an installation or configured source path for development and testing.

### Reconsideration Conditions

The layout can be reconsidered if packaging or deployment requirements change significantly.

### Implementation Evidence

- Created `src/ecommerce_ops/`.
- Migrated the FastAPI application into the package.
- Migrated the health router into `api/health.py`.
- Configured Hatchling in `pyproject.toml`.
- Configured pytest to use `src/`.
- Successfully installed the package using `uv sync`.
- Verified package imports.
- Successfully ran two automated tests.
- Verified the application through Uvicorn and FastAPI documentation.
