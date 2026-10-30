# Operational Data Requirements Research

## 1. Purpose

This document defines the operational information required to investigate seller-side logistics discrepancies.

The example scenario is:

A seller hands a shipment to a logistics partner, but the marketplace continues to show the shipment as awaiting pickup.

The objective is to identify:

- Which information is required.
- Where that information might originate.
- Which events can be compared.
- Which discrepancies can be detected deterministically.
- Which situations require additional evidence or human confirmation.

This is a data-requirements investigation, not a finalized product specification.

---

## 2. Example Problem Scenario

### Expected Workflow

1. Seller prepares an order.
2. Shipment is created.
3. Seller hands over the parcel to a logistics partner.
4. Logistics partner records the pickup.
5. Marketplace updates the shipment status.
6. Shipment progresses through the delivery network.

### Potential Discrepancy

The seller reports that the parcel was handed over, but the marketplace still shows:

`AWAITING_PICKUP`

Possible explanations include:

- Pickup was completed but the platform has not updated.
- The logistics partner did not scan the parcel.
- The pickup event was recorded but not communicated to the marketplace.
- The parcel was not actually collected.
- The seller is referring to a different shipment.
- The available records are incomplete.

The application must investigate these possibilities instead of assuming one explanation.

---

## 3. Required Data Categories

### A. Shipment Identity

The application must identify the exact shipment being investigated.

Potential fields:

| Field | Purpose |
|---|---|
| platform | Marketplace or commerce platform |
| seller_id | Authorized seller identifier |
| order_id | Original order reference |
| shipment_id | Unique shipment reference |
| package_id | Package identifier, when available |
| tracking_number | Carrier tracking reference |
| carrier_code | Logistics provider identifier |
| sku | Relevant product identifier, if needed |

Important:

A single order may contain multiple shipments or packages.

The application must not assume:

`One order = One shipment = One package`

### B. Expected Operation

These fields describe what should happen.

| Field | Purpose |
|---|---|
| shipment_created_at | When the shipment was created |
| dispatch_by_at | Dispatch deadline, when available |
| expected_pickup_at | Expected pickup time, when available |
| pickup_window_start | Beginning of pickup window |
| pickup_window_end | End of pickup window |
| current_platform_status | Current recorded shipment status |
| last_platform_update_at | Last known platform update |

Not every platform will expose every field.

Missing values must remain explicitly unknown.

### C. Recorded Operational Events

Every event should be represented independently.

| Field | Purpose |
|---|---|
| event_id | Internal event identifier |
| platform_event_id | Original event identifier, when available |
| shipment_id | Related shipment |
| event_type | Pickup, shipped, delivered, etc. |
| event_status | Recorded status |
| occurred_at | When the event reportedly happened |
| received_at | When our application received it |
| source | Marketplace, carrier, seller, etc. |
| location | Event location, when available |
| raw_reference | Reference to original source data |

Important distinction:

`occurred_at` and `received_at` are not interchangeable.

An event may occur at one time but reach the application later.

This difference may help identify delayed event reporting.

### D. Supporting Evidence

Potential evidence includes:

- Pickup manifest
- Handover receipt
- Carrier confirmation
- Tracking history
- Seller-uploaded document
- Relevant support communication
- Manual seller confirmation

Suggested evidence metadata:

| Field | Purpose |
|---|---|
| evidence_id | Internal evidence identifier |
| shipment_id | Related shipment |
| evidence_type | Document, API record, confirmation, etc. |
| source | Where the evidence came from |
| uploaded_at | When the application received it |
| event_time | Time associated with the evidence, if known |
| file_reference | Stored file reference |
| verification_status | Whether it has been reviewed |
| notes | Additional context |

Evidence should preserve its original source.

An AI-generated summary must never be treated as original evidence.

### E. Investigation Information

| Field | Purpose |
|---|---|
| investigation_id | Unique investigation |
| shipment_id | Shipment under investigation |
| detected_at | When the discrepancy was identified |
| discrepancy_type | Type of inconsistency |
| missing_information | Information still required |
| investigation_status | Current progress |
| actions_taken | Recorded investigation actions |
| follow_up_at | Next follow-up date |
| outcome | Final result, if known |
| outcome_source | Evidence supporting the outcome |

---

## 4. Data Sources

Potential sources must be evaluated separately.

### A. Marketplace APIs

Potential information:

- Order records
- Shipment records
- Shipment statuses
- Platform-recorded events
- Tracking identifiers
- Return events

Examples from official documentation:

Flipkart:
https://seller.flipkart.com/api-docs/order-api-docs/NotifRef.html

Its notification documentation describes shipment lifecycle events, including pickup completion and shipment progress.

Shopify:
https://shopify.dev/docs/api/admin-graphql/latest/objects/Fulfillment

The Fulfillment object includes tracking information and fulfillment events.

Amazon:
https://developer-docs.amazon.com/sp-api/lang-us/docs/tracking-api

The documented SP-API Tracking API has a US-only availability scope in the current documentation examined.

Amazon Shipping tracking also has program and shipment-type restrictions:
https://developer-docs.shipping.amazon.com/apis/docs/tutorial-track-a-shipment

Important:

These sources do not establish equivalent tracking access across all platforms or Indian marketplaces.

Actual seller-authorized access must be tested.

### B. Carrier Tracking Systems

Potential information:

- Pickup scan
- Shipment acceptance
- Transit scans
- Delivery attempts
- Delivery confirmation
- Return movement

Limitations:

- Carrier APIs may differ.
- Tracking data may be delayed.
- Some events may be unavailable.
- Access may require commercial agreements or approved credentials.

Carrier integration feasibility remains unverified.

### C. Seller-Provided Information

Potential information:

- Physical handover confirmation
- Pickup receipt
- Manifest
- Shipment-related documents
- Manual explanation

Seller-provided information should be clearly labeled as seller-provided.

It must not be silently converted into a verified carrier event.

---

## 5. Example Event Timeline

Illustrative scenario:

| Time | Event | Source |
|---|---|---|
| 09:00 | Shipment created | Marketplace |
| 11:00 | Expected pickup | Marketplace |
| 11:30 | Seller reports physical handover | Seller |
| 12:00 | Pickup event not yet recorded | Marketplace |
| 14:00 | Carrier confirmation uploaded | Seller-provided document |
| 15:00 | Marketplace status updated | Marketplace |

This timeline demonstrates why event source and event time are important.

The application should retain the original event history instead of replacing earlier records with the latest status.

---

## 6. Deterministic Detection Opportunities

Structured comparisons should be handled using normal application logic.

### A. Missing Pickup Event

Condition:

- Expected pickup window has ended.
- No pickup event is present in the available records.

Possible result:

`POTENTIAL_MISSING_PICKUP_EVENT`

This does not prove that pickup failed.

### B. Delayed Platform Update

Condition:

- An external source reports a pickup event.
- The marketplace does not yet show a corresponding event.

Possible result:

`POTENTIAL_STATUS_UPDATE_DELAY`

The external event must have a reliable source and shipment match.

### C. Conflicting Events

Condition:

- Two sources report incompatible statuses or timestamps.

Possible result:

`CONFLICTING_EVENT_RECORDS`

The application should display both records and their origins.

### D. Missing Tracking Information

Condition:

- Shipment exists.
- Required tracking identifier is unavailable.

Possible result:

`MISSING_TRACKING_INFORMATION`

### E. No Reliable Evidence

Condition:

- Seller reports handover.
- No independent supporting event or document is available.

Possible result:

`INSUFFICIENT_EVIDENCE`

The application must not conclude that handover is verified.

---

## 7. Important Detection Rules

1. Do not compare events without confirming that they refer to the same shipment.
2. Preserve original timestamps and time zones.
3. Account for delayed event delivery.
4. Do not assume that the absence of an event proves that the physical event did not happen.
5. Do not assume that a seller statement is independent confirmation.
6. Do not overwrite earlier event records.
7. Record the source of every event.
8. Distinguish an unknown value from a negative result.
9. Make investigation outcomes traceable to supporting evidence.
10. Keep consequential actions under human authorization.

---

## 8. What AI Could and Could Not Do

### Suitable AI Tasks

AI may assist with:

- Summarizing an investigation timeline.
- Organizing uploaded documents.
- Extracting relevant information from documents for human review.
- Drafting a support-case explanation.
- Identifying missing information from an investigation checklist.
- Explaining why two records appear inconsistent.

### Tasks for Deterministic Code

Normal application logic should handle:

- Timestamp comparisons.
- Shipment identity matching.
- Status comparisons.
- Missing event detection.
- Time-window calculations.
- Duplicate event detection.
- Investigation status tracking.

### AI Restrictions

AI must not:

- Invent pickup confirmations.
- Fabricate timestamps.
- Claim that a physical handover occurred without evidence.
- Change original event records.
- Submit consequential support actions without authorization.
- Present an uncertain interpretation as a verified fact.

---

## 9. Important Data Quality Problems

### Duplicate Events

A platform or carrier may send the same event more than once.

The application needs a strategy for recognizing duplicates without accidentally deleting legitimate repeated events.

### Delayed Events

An event may be received long after it occurred.

The system should preserve both occurrence and receipt timestamps.

### Missing Events

A carrier may not generate or expose every physical scan.

The absence of an event must not automatically be interpreted as proof of failure.

### Conflicting Statuses

Different sources may report different statuses.

The application should preserve the conflict and identify the source of each record.

### Shipment Identity Mismatch

Tracking numbers and shipment IDs must be matched carefully.

Incorrect matching could result in investigating the wrong parcel.

### Time Zone Differences

Event timestamps may use different time zones or formats.

All timestamps must be normalized carefully while retaining their original values.

---

## 10. Preliminary Data Requirements

The minimum information needed for an initial investigation is:

1. Platform identifier.
2. Order identifier.
3. Shipment identifier.
4. Current platform status.
5. Expected pickup time or window, if available.
6. Available pickup and shipment events.
7. Event timestamps.
8. Event sources.
9. Seller-provided confirmation.
10. Supporting evidence, if available.

The system should still allow an investigation to exist when some fields are unavailable.

Missing information should be visible rather than silently filled with assumptions.

---

## 11. Preliminary Findings

The investigation requires more than a current shipment status.

A useful investigation needs:

- Shipment identity.
- Expected operational timeline.
- Actual recorded event history.
- Source attribution.
- Supporting evidence.
- A traceable investigation outcome.

A platform API may provide some of these elements, but it may not independently verify physical logistics events.

The application may therefore need multiple sources of information.

The most important technical challenge is reliable event reconciliation, not simply displaying shipment statuses.

---

## 12. Unresolved Questions

| Question | Status |
|---|---|
| Which platforms expose pickup-completion events in India? | Partially researched |
| Can Amazon India seller applications access the required tracking events? | Not verified |
| Can carrier APIs provide independent pickup confirmation? | Not researched |
| What evidence do sellers actually possess after handover? | Not validated |
| How frequently do these discrepancies occur? | Not measured |
| How long do platform status updates normally take? | Not measured |
| What should qualify as a genuine discrepancy? | Requires further investigation |
| Which evidence is accepted during marketplace disputes? | Requires further research |

---

## 13. Next Research Milestone

The next step is to investigate the evidence and resolution workflow.

Questions:

1. What evidence do marketplaces request when a seller disputes a missed pickup?
2. Which documents can sellers realistically obtain?
3. How do sellers submit and follow up on these cases?
4. Can the application prepare a useful investigation package?
5. Which actions must remain under seller control?

This will help determine whether an exception-management application can provide value beyond a normal order-tracking dashboard.

---

## Research Integrity

This document defines preliminary data requirements using documented platform capabilities and an illustrative workflow.

It does not claim:

- That the scenario is common across sellers.
- That a specific platform exposes every required field.
- That physical handover can always be independently verified.
- That carrier integrations are available.
- That the proposed detection rules have been tested.
- That the product or workflow has been validated with sellers.

Further documentation research, API testing, and seller validation are required.
