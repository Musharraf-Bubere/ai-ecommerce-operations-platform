
# Product Gap Analysis

## 1. Purpose

This document compares existing marketplace and third-party e-commerce solutions against the proposed evidence-driven operational investigation workflow.

The objective is to determine:

- Which capabilities already exist.
- Which proposed features would duplicate existing products.
- Where a potential operational gap may remain.
- Whether the proposed product direction is sufficiently differentiated.
- What should be validated before implementation.

The product direction remains a hypothesis.

---

## 2. Current Product Hypothesis

The current hypothesis is:

Some e-commerce sellers may spend manual effort investigating operational discrepancies between physical logistics events and platform-recorded statuses.

This may involve:

1. Identifying an affected order or shipment.
2. Comparing available operational records.
3. Collecting supporting evidence.
4. Identifying missing information.
5. Preparing a marketplace support request.
6. Following up on the case.
7. Recording the final outcome.

The potential product is an evidence-driven operational investigation system.

It is not intended to become another generic order management or shipment tracking platform.

---

## 3. Existing Marketplace Capabilities

### A. Amazon Seller Central

Official documentation:

- Easy Ship Pickup Miss FAQ:
  https://sellercentral.amazon.in/help/hub/reference/external/GKNZKMGSV38C2RTZ
- Automated order workflow:
  https://sellercentral.amazon.in/help/hub/reference/external/G202065810
- Pickup miss guidance:
  https://sellercentral.amazon.in/seller-forums/discussions/t/cc316f3b-10c3-4fbc-a2eb-29fd87e5a95e

Existing capabilities include:

- Manage Orders.
- Shipment status visibility.
- Pickup associate contact information.
- Easy Ship Pickup Miss form.
- Automated order and return workflows.
- Seller Support.
- Support case follow-up.

The Pickup Miss FAQ describes how sellers can submit affected order IDs and report a missed pickup.

The automated order workflow also helps sellers resolve common order and return queries without immediately contacting support.

#### Gap Assessment

Amazon already provides a direct process for reporting missed pickups.

A third-party application that simply displays missed pickups or recreates the reporting form would have limited differentiation.

Potential additional value may exist in organizing evidence and investigation history across multiple sources.

This possibility is not yet validated.

---

## 4. Third-Party Solutions

### A. Veeqo

Official sources:

- https://www.veeqo.com/features
- https://www.veeqo.com/order-management-system
- https://sell.amazon.com/tools/veeqo

Existing capabilities include:

- Multichannel order management.
- Inventory management.
- Shipping and fulfillment.
- Returns management.
- Order notes and tags.
- Order activity and action history.
- Shipping and returns reporting.
- Automation.
- Carrier integrations.

Veeqo already provides substantial operational visibility.

#### Gap Assessment

A new generic order dashboard, shipping manager, or inventory manager would overlap with Veeqo.

The proposed product would need to solve a different, narrower workflow.

---

### B. AfterShip

Official sources:

- https://www.aftership.com/returns
- https://support.aftership.com/en/returns/articles/15389152-manage-returns
- https://support.aftership.com/en/returns/articles/15389184-learn-more-about-returns-tracking

Existing capabilities include:

- Returns management dashboard.
- Return request timelines.
- Return shipment tracking.
- Exception statuses.
- Notes and comments.
- Tags.
- Return-related images.
- Refund and exchange workflows.
- Automated return processing.
- Returns analytics.

AfterShip already provides functionality for tracking and managing return exceptions.

#### Gap Assessment

A generic returns dashboard or return tracking application would have substantial overlap.

The potential investigation workflow must be more specific than ordinary return management.

---

### C. Linnworks

Official sources:

- https://www.linnworks.com/features/
- https://docs.linnworks.com/article/documentation/getting-started

Existing capabilities include:

- Multichannel order management.
- Inventory management.
- Shipping integrations.
- Carrier tracking.
- Operational automation.
- Analytics and reporting.
- AI-assisted workflow recommendations.

Linnworks combines multiple operational functions into a connected commerce platform.

#### Gap Assessment

A general multichannel operations platform would duplicate substantial existing functionality.

The proposed product should not attempt to recreate an entire commerce management platform.

---

## 5. Capability Comparison

| Capability                      | Amazon Seller Central      | Veeqo                        | AfterShip                       | Linnworks                  |
| ------------------------------- | -------------------------- | ---------------------------- | ------------------------------- | -------------------------- |
| Order management                | Yes                        | Yes                          | Integration-dependent           | Yes                        |
| Shipment visibility             | Yes                        | Yes                          | Yes                             | Yes                        |
| Inventory management            | Yes, marketplace-specific  | Yes                          | Not primary focus               | Yes                        |
| Returns management              | Yes                        | Yes                          | Yes                             | Yes                        |
| Operational automation          | Yes, selected workflows    | Yes                          | Yes                             | Yes                        |
| Support workflow                | Marketplace support        | Product support              | Product support                 | Product support            |
| Return timelines                | Platform records           | Return records               | Yes                             | Operational records        |
| Internal notes                  | Workflow-dependent         | Yes                          | Yes                             | Verify exact functionality |
| Evidence organization           | Issue-dependent            | Some supporting capabilities | Return-related images and notes | Verify exact functionality |
| Cross-source investigation      | Not established            | Not established              | Not established                 | Not established            |
| Evidence-based case preparation | Marketplace-specific forms | Not established              | Not established                 | Not established            |

Important:

"Not established" does not mean a product lacks the capability.

It means this preliminary research has not verified that specific functionality.

---

## 6. Proposed Workflow vs Existing Capabilities

The following table evaluates the potential product workflow.

| Proposed activity                     | Existing coverage                   | Potential opportunity  |
| ------------------------------------- | ----------------------------------- | ---------------------- |
| View order and shipment status        | Strong                              | Low differentiation    |
| Track shipment movement               | Strong                              | Low differentiation    |
| Manage customer returns               | Strong                              | Low differentiation    |
| Detect missing status updates         | Platform and tracking dependent     | Requires investigation |
| Compare records from multiple sources | Not established in reviewed sources | Potential opportunity  |
| Organize evidence by investigation    | Partial capabilities exist          | Requires validation    |
| Identify missing evidence             | Not established in reviewed sources | Potential opportunity  |
| Prepare structured support summaries  | Not established in reviewed sources | Potential opportunity  |
| Track investigation follow-ups        | Partial capabilities exist          | Requires validation    |
| Maintain evidence-linked outcomes     | Not established in reviewed sources | Potential opportunity  |

This table identifies areas for further investigation, not confirmed competitor weaknesses.

---

## 7. Potential Product Differentiation

The most promising direction to investigate is:

An evidence-driven operational investigation workspace for e-commerce sellers.

The proposed workflow:

1. An operational discrepancy is identified.
2. The seller selects the affected order or shipment.
3. Available platform and carrier records are collected.
4. The application builds an event timeline.
5. The application identifies inconsistencies and missing information.
6. Supporting documents are associated with the investigation.
7. The application prepares an evidence-based summary.
8. The seller reviews and submits the support request through the official channel.
9. The application records the case reference.
10. The seller tracks follow-ups and records the outcome.

The application should complement existing marketplaces rather than replace their order management or support systems.

---

## 8. Where AI Could Add Value

AI should be applied only where it provides meaningful assistance.

### Potential AI Responsibilities

- Summarize a shipment investigation.
- Extract relevant information from uploaded documents.
- Organize evidence into a readable report.
- Draft support-case explanations.
- Summarize marketplace responses.
- Identify potentially missing information.

### Deterministic Responsibilities

- Match order and shipment identifiers.
- Compare timestamps.
- Detect missing events.
- Identify duplicate records.
- Compare status transitions.
- Track follow-up deadlines.
- Preserve evidence references.
- Maintain investigation status.

### Human Responsibilities

The seller must remain responsible for:

- Confirming the accuracy of evidence.
- Reviewing AI-generated summaries.
- Approving support-case content.
- Submitting complaints.
- Approving consequential actions.

AI must never invent evidence or represent an uncertain event as a verified fact.

---

## 9. Product Risks

### A. Existing Solutions May Already Be Sufficient

The proposed workflow may already be adequately handled by existing marketplace and third-party products.

This must be tested before development.

### B. Platform Integration Limitations

Different marketplaces expose different operational data.

A cross-platform investigation workflow may not be technically achievable with equivalent functionality.

### C. Evidence Availability

Sellers may not possess manifests, receipts, or independent carrier confirmation.

The application must work honestly with incomplete information.

### D. Market Demand Is Unknown

Public seller complaints do not establish market size, frequency, willingness to pay, or product adoption.

### E. Competitive Differentiation

Evidence organization, timelines, notes, and return exception handling already exist in parts of the competitive landscape.

The product must demonstrate a meaningful end-to-end advantage.

---

## 10. Preliminary Product Direction

### Working Direction

Investigate an evidence-driven operational investigation system.

### Potential Initial Problem

A shipment has a discrepancy between the seller's reported physical handover and the platform's recorded pickup status.

### Potential Initial User Workflow

- Create an investigation.
- Identify the affected shipment.
- Record the seller's reported event.
- Add available platform or carrier records.
- Upload supporting evidence.
- Review missing information.
- Generate a structured investigation summary.
- Record the marketplace support case.
- Track the outcome.

### Explicitly Out of Scope for the Initial Investigation

- Full order management.
- Full inventory management.
- Replacing marketplace support.
- Replacing carrier tracking.
- Building a complete returns management platform.
- Automatic submission of consequential support requests.
- Claiming physical events without supporting evidence.

These are preliminary boundaries, not finalized product decisions.

---

## 11. Current Assessment

The research establishes that existing products already provide substantial functionality in:

- Order management.
- Shipping.
- Shipment tracking.
- Inventory.
- Returns.
- Automation.
- Operational reporting.

Therefore, building another general e-commerce operations dashboard would not be sufficiently differentiated.

A narrower evidence-driven investigation workflow may be worth exploring.

However, its differentiation remains unproven.

The most important question is:

Does organizing operational evidence, preparing support cases, and tracking investigations solve a sufficiently painful problem that existing products do not adequately address?

---

## 12. Validation Required Before Implementation

The following questions must be answered:

1. How frequently do sellers investigate these discrepancies?
2. How many orders or shipments are involved?
3. How much time is spent collecting evidence?
4. How many different systems or sources are used?
5. Which existing tools do sellers currently use?
6. What part of the workflow remains manual?
7. Are existing marketplace support tools sufficient?
8. Would sellers use an independent investigation workspace?
9. Would they pay for this capability?
10. Can the required data be accessed legitimately and reliably?

Direct seller validation is still missing.

Public documentation and seller discussions cannot answer all these questions.

---

## 13. Next Milestone

The next step is to narrow the initial use case and evaluate its validation requirements.

We should:

1. Compare logistics discrepancies with return disputes.
2. Identify the most specific initial user and workflow.
3. Define the problem statement.
4. Define the assumptions that must be validated.
5. Identify the evidence needed to justify implementation.
6. Decide whether a small prototype is warranted.

No architecture or implementation decision should be finalized until the problem is sufficiently understood.

---

## 14. Research Sources

### Amazon

- Easy Ship Pickup Miss FAQ:
  https://sellercentral.amazon.in/help/hub/reference/external/GKNZKMGSV38C2RTZ
- Automated order workflow:
  https://sellercentral.amazon.in/help/hub/reference/external/G202065810
- Pickup Miss guidance:
  https://sellercentral.amazon.in/seller-forums/discussions/t/cc316f3b-10c3-4fbc-a2eb-29fd87e5a95e

### Veeqo

- Features:
  https://www.veeqo.com/features
- Order management:
  https://www.veeqo.com/order-management-system
- Amazon Veeqo overview:
  https://sell.amazon.com/tools/veeqo

### AfterShip

- Returns management:
  https://www.aftership.com/returns
- Returns dashboard:
  https://support.aftership.com/en/returns/articles/15389152-manage-returns
- Returns tracking:
  https://support.aftership.com/en/returns/articles/15389184-learn-more-about-returns-tracking

### Linnworks

- Features:
  https://www.linnworks.com/features/
- Getting started:
  https://docs.linnworks.com/article/documentation/getting-started

---

## Research Integrity

This document records preliminary competitive research.

It does not claim:

- That existing competitors lack investigation functionality.
- That the proposed product has a validated competitive advantage.
- That sellers are dissatisfied with existing tools.
- That the market is sufficiently large.
- That sellers would pay for the proposed application.
- That all required integrations are feasible.

Competitor capabilities must be investigated further where necessary, and direct seller validation remains important.
