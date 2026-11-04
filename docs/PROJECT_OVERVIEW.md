
# AI E-commerce Operations Platform

## Project Overview & System Architecture

**Project:** AI E-commerce Operations Platform
**Initial Problem:** Missing Pickup Scan Investigation
**Development Approach:** Modular Monolith
**Project Status:** Product Discovery Completed — Architecture and Implementation Beginning

---

# 1. Project Overview

The AI E-commerce Operations Platform is an intelligent operational investigation system designed to help e-commerce sellers identify, investigate, and manage shipment-related operational discrepancies.

The initial focus is a specific operational problem: **Missing Pickup Scan**.

A seller may physically hand over a parcel to a courier, but the expected pickup event may not appear in the marketplace or logistics system.

This creates uncertainty for the seller.

The platform aims to compare seller handover records with marketplace pickup events, identify potential discrepancies, organize supporting evidence, and assist sellers in preparing factual support-case summaries.

The system will use deterministic software logic for data processing and reconciliation, while AI will assist with language-based tasks.

Human approval will remain essential for important decisions and external actions.

# 2. Problem Statement

Consider this example:

1. A seller prepares an order.
2. The seller hands the parcel to a courier.
3. The seller records the handover.
4. The expected pickup scan does not appear in the marketplace data.
5. The seller cannot easily determine whether the scan is delayed, missing, or unsupported by available evidence.
6. The seller may need to investigate the discrepancy and contact marketplace support.

The problem is not necessarily that the courier failed to collect the parcel.

The specific problem is the discrepancy between the seller's handover record and the expected digital pickup event.

The platform will help investigate this discrepancy without automatically assuming responsibility or inventing proof.

# 3. Product Vision

Build a reliable operational investigation platform that helps e-commerce sellers:

- Import operational records.
- Validate and normalize data.
- Reconcile seller handover records with marketplace events.
- Detect potential missing pickup scans.
- Identify delayed, duplicate, and conflicting events.
- Organize supporting evidence.
- Maintain investigation history.
- Generate AI-assisted factual case summaries.
- Review and manage investigation outcomes.

The long-term vision may expand to other seller operational problems, but the initial implementation will remain focused.

# 4. Initial MVP Scope

## Included

1. Standard CSV uploads.
2. Seller handover record imports.
3. Marketplace pickup-event imports.
4. CSV structure and data validation.
5. Common event normalization.
6. Order and event reconciliation.
7. Potential missing pickup detection.
8. Delayed event handling.
9. Duplicate import and event handling.
10. Investigation management.
11. Evidence organization.
12. Audit history.
13. Basic AI-assisted support-case summaries.
14. Human review and approval.

## Excluded from Initial MVP

- Automatic marketplace API integrations.
- Automatic support complaint submission.
- Return dispute investigation.
- Predictive AI.
- Autonomous agents making consequential decisions.
- Advanced analytics.
- Multiple marketplace integrations without demonstrated need.
- Unnecessary microservices and infrastructure.

# 5. Core Business Workflow

The proposed initial workflow:

1. Seller creates an account.
2. Seller uploads the handover CSV.
3. Seller uploads the marketplace events CSV.
4. System validates both files.
5. System records import information and errors.
6. Valid records are normalized into a common event structure.
7. The reconciliation engine compares records.
8. Potential discrepancies are identified.
9. The system creates or updates investigations.
10. Seller reviews the investigation.
11. Seller uploads relevant evidence.
12. AI assists with factual case summarization.
13. Seller verifies and approves the summary.
14. Seller manually submits the support case.
15. Investigation history and outcome are maintained.

# 6. Conceptual System Architecture

The initial architecture follows a modular monolith approach.

```text
                 SELLER / USER
                       |
                       v
              APPLICATION FRONTEND
                       |
                       v
                 FASTAPI BACKEND
                       |
       +---------------+----------------+
       |               |                |
       v               v                v
   CSV IMPORT      INVESTIGATION     EVIDENCE
     MODULE          MODULE          MODULE
       |               |                |
       v               v                v
   VALIDATION      RECONCILIATION    DOCUMENT
     MODULE           ENGINE         MANAGEMENT
       |               |                |
       +---------------+----------------+
                       |
                       v
                EVENT PROCESSING
                       |
          +------------+------------+
          |                         |
          v                         v
    POSTGRESQL DATABASE        AI ASSISTANCE
          |                         |
          v                         v
    AUDIT HISTORY          CASE SUMMARIZATION
                                    |
                                    v
                              HUMAN REVIEW
```

This is a conceptual design. The final module boundaries will be refined as implementation requirements become clearer.

# 7. Proposed Application Modules

## 7.1 Authentication and Seller Management

Responsibilities:

- Seller registration.
- Authentication.
- Seller account management.
- Data isolation between sellers.
- Authorization checks.

## 7.2 CSV Import Module

Responsibilities:

- Upload CSV files.
- Identify import type.
- Validate required columns.
- Track import batches.
- Detect repeated uploads.
- Report invalid records.
- Support partial-success imports.

## 7.3 Validation Module

Responsibilities:

- Required-field validation.
- Data type validation.
- Timestamp validation.
- Event type validation.
- Order identifier validation.
- Duplicate row checks.
- Clear validation error reporting.

## 7.4 Normalization Module

Responsibilities:

- Convert imported records into a common internal structure.
- Normalize timestamps.
- Normalize event types.
- Preserve original source information.
- Preserve source provenance.

## 7.5 Reconciliation Engine

Responsibilities:

- Match seller handover records with marketplace events.
- Detect missing pickup events.
- Identify delayed events.
- Detect duplicate and conflicting records.
- Account for data freshness.
- Produce explainable discrepancy results.

The reconciliation engine will primarily use deterministic Python logic.

## 7.6 Investigation Module

Responsibilities:

- Create investigations.
- Maintain investigation statuses.
- Record investigation history.
- Update investigations when new evidence arrives.
- Track resolution outcomes.

## 7.7 Evidence Management Module

Responsibilities:

- Upload supporting documents.
- Associate evidence with investigations.
- Record evidence metadata.
- Track evidence sources.
- Maintain traceability.

## 7.8 AI Assistance Module

Responsibilities:

- Extract relevant information from supported documents.
- Summarize marketplace responses.
- Prepare factual support-case drafts.
- Identify missing information.

AI output must be grounded in available records and evidence.

The seller must review and approve important outputs.

## 7.9 Audit Module

Responsibilities:

- Record important application actions.
- Maintain historical changes.
- Track investigation transitions.
- Preserve import history.
- Support traceability and accountability.

# 8. Proposed Technology Stack

| Layer                  | Technology                         | Purpose                   |
| ---------------------- | ---------------------------------- | ------------------------- |
| Programming language   | Python 3.13                        | Application development   |
| Backend framework      | FastAPI                            | REST API development      |
| Data validation        | Pydantic                           | Structured validation     |
| Database               | PostgreSQL                         | Persistent storage        |
| ORM                    | SQLAlchemy                         | Database interaction      |
| Migrations             | Alembic                            | Schema versioning         |
| CSV processing         | Python CSV / Pandas when justified | Data ingestion            |
| Frontend               | To be finalized                    | Seller interface          |
| Testing                | pytest                             | Automated testing         |
| Linting and formatting | Ruff                               | Code quality              |
| Type checking          | mypy                               | Static type checking      |
| Containers             | Docker Compose                     | Local environment         |
| CI/CD                  | GitHub Actions                     | Automated verification    |
| AI integration         | LLM API to be selected             | Language-based assistance |
| Version control        | Git and GitHub                     | Source control            |

## Technologies intentionally not required initially

- Redis
- pgvector
- LangGraph
- MCP
- Microservices

These may become useful later, but must be justified by actual product requirements.

# 9. Proposed Database Domain

The following are conceptual entities, not finalized database tables.

| Entity               | Responsibility                                 |
| -------------------- | ---------------------------------------------- |
| Seller               | Represents a platform user/business            |
| Order                | Represents a seller's order                    |
| ImportBatch          | Tracks uploaded files and import processing    |
| RawRecord            | Preserves original imported records            |
| Event                | Stores normalized operational events           |
| Investigation        | Represents a potential operational discrepancy |
| Evidence             | Stores evidence metadata and relationships     |
| InvestigationHistory | Tracks investigation changes                   |
| AuditLog             | Records important application actions          |

Important relationships:

- One seller can have many orders.
- One order can have many events.
- One seller can have many import batches.
- One investigation can have many evidence records.
- One investigation can have many history entries.

All seller-owned data must be isolated appropriately.

# 10. Important Data Engineering Principles

## Event History

Preserve historical events rather than replacing them with the latest status.

## Event Time and Ingestion Time

Store both:

- `event_time`: when the event occurred according to the source.
- `ingested_at`: when the platform received the record.

## Out-of-Order Events

Do not assume that the latest received event is the latest event that occurred.

## Idempotency

Repeated imports should not create unintended duplicate records.

## Data Provenance

Preserve where records originated and how they were processed.

## Data Freshness

A missing event in stale imported data must not automatically become a confirmed discrepancy.

## Auditability

Important changes and decisions must remain traceable.

## Human Oversight

Sellers must be able to review evidence and approve important actions.

# 11. AI and Deterministic Processing

The platform will use AI only where it provides genuine value.

### Deterministic Python

Use normal application logic for:

- Order matching.
- Event reconciliation.
- Missing event detection.
- Duplicate detection.
- Timestamp comparisons.
- Validation.
- Import processing.
- Status transitions.
- Calculations.

### AI

Use language models for:

- Document information extraction.
- Marketplace response summarization.
- Factual support-case draft generation.

### Human Approval

The seller reviews and approves important AI-generated content.

AI must not invent evidence, courier acknowledgements, timestamps, or claim outcomes.

# 12. Security and Reliability Principles

The platform must consider:

- Authentication.
- Seller data isolation.
- Authorization.
- Input validation.
- Safe file uploads.
- File size and type restrictions.
- Secure document storage.
- Sensitive data protection.
- Audit history.
- Error handling.
- Database transaction safety.
- Automated testing.

Security must be considered during implementation, not added as an afterthought.

# 13. Development Strategy

We will build incrementally.

Proposed implementation stages:

1. Project structure and development foundation.
2. Backend application foundation.
3. Database connection and migrations.
4. Seller and order domain.
5. CSV import pipeline.
6. Data validation.
7. Raw record preservation.
8. Event normalization.
9. Reconciliation engine.
10. Missing pickup investigation.
11. Evidence management.
12. Investigation lifecycle and audit history.
13. AI-assisted case summaries.
14. Frontend integration.
15. Automated testing and security hardening.
16. Deployment and observability.

Stages may be adjusted when implementation evidence reveals a better sequence.

# 14. Project Limitations and Assumptions

The initial product direction has not been commercially validated through direct seller interviews.

Public research is useful for discovering possible problems but does not prove market demand.

Marketplace API access and authorization remain unverified.

The first prototype will use standardized CSV templates rather than assume access to live marketplace data.

A missing pickup event is a discrepancy to investigate, not proof that a courier failed to collect a parcel.

# 15. Project Success Criteria

The initial technical prototype should demonstrate that it can:

- Accept standardized CSV files.
- Validate imported data.
- Preserve source records.
- Normalize operational events.
- Handle repeated imports safely.
- Reconcile handover and pickup records.
- Identify potential missing pickup scans.
- Handle delayed and out-of-order events.
- Maintain investigation history.
- Organize supporting evidence.
- Generate factual AI-assisted summaries.
- Require human approval for important actions.
- Explain why an investigation was created or resolved.

# 16. Documentation Strategy

Maintain these project documents:

- `PROJECT_OVERVIEW.md` — product and architecture overview.
- `decision.md` — chronological product and technical decisions.
- `interview_q&a.md` — project-related technical and architectural interview preparation.

Research documentation remains in the existing `notes/` directory.

Update documentation incrementally as decisions are made and features are implemented.

# 17. Engineering Philosophy

This project prioritizes:

1. Correctness over unnecessary complexity.
2. Reliable data processing over superficial AI features.
3. Explainable business logic.
4. Data integrity and traceability.
5. Human oversight.
6. Testability.
7. Maintainability.
8. Security.
9. Real product value.
10. Genuine engineering ownership.

The goal is not simply to demonstrate the use of AI technologies.

The goal is to build a reliable operational product that solves a specific problem and can be explained and defended in technical interviews.

---

**Document Status:** Initial Project Overview
**Architecture Status:** Proposed — subject to implementation evidence and explicit decisions.
