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
