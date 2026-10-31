
# Comparative Problem Validation — Evidence Availability

## 1. Purpose

This document compares two e-commerce seller operational problems:

- Candidate A: Physical shipment handover is reported by the seller, but the marketplace has not recorded the expected pickup scan.
- Candidate B: A return is marked delivered or completed, but the seller reports that the returned shipment was not received.

The focus is evidence availability.

The objective is to understand:

1. What evidence can the seller independently possess?
2. What information must be requested from a marketplace or carrier?
3. What can be established from available records?
4. What cannot be established without external cooperation?
5. Whether an application could improve the investigation workflow.

Neither problem has been selected as the initial product use case.

---

## 2. Candidate A — Missing Pickup Scan

### Problem Description

A seller prepares a shipment and hands it over to a logistics partner.

However, the marketplace continues to display a status such as:

`WAITING_FOR_PICKUP`

Possible explanations:

- Physical pickup did not occur.
- Pickup occurred but the parcel was not scanned.
- A scan occurred but was not communicated to the marketplace.
- The marketplace has not processed the event.
- The seller has identified the wrong shipment or order.

These possibilities must be investigated separately.

### Evidence Categories

| Evidence                      | Potential purpose                             | Limitation                                                  |
| ----------------------------- | --------------------------------------------- | ----------------------------------------------------------- |
| Signed pickup manifest        | Supports that listed parcels were handed over | Must identify the affected shipment and indicate acceptance |
| Pickup receipt                | Supports a handover transaction               | Availability depends on carrier workflow                    |
| Pickup associate confirmation | Supports seller's account of collection       | May not be independently verifiable                         |
| CCTV footage                  | Shows a physical handover                     | Must identify the relevant parcel and time                  |
| Marketplace event history     | Shows platform-recorded events                | Cannot independently prove an unscanned physical handover   |
| Seller statement              | Records what the seller reports               | Not independent confirmation                                |

### Official Marketplace Process — Amazon

Source:

https://sellercentral.amazon.in/help/hub/reference/external/GKNZKMGSV38C2RTZ

Amazon's Easy Ship Pickup Miss FAQ explains:

- A pickup miss occurs when an Easy Ship order is not picked up within its assigned pickup slot.
- Sellers can use the Pickup Miss Form through Manage Orders.
- The form requests the registered email address, order IDs, and reason for the pickup miss.
- Amazon reviews the issue and attempts to reattempt pickup.

The official guidance does not establish a signed manifest as a universal requirement for this form.

### Cross-Platform Evidence — Shopsy

Official source:

https://seller.shopsy.in/faq/

Shopsy's seller FAQ describes a situation where the product is picked up but the dashboard does not reflect the pickup yet.

It explains that there can be a time lag between scanning and physical handover.

This supports the existence of a potential difference between physical operations and platform-recorded status.

### Potential Application Value

A future application could help sellers:

1. Record the affected shipment.
2. Record the reported handover time.
3. Associate a manifest or receipt with the shipment.
4. Compare the seller-reported event with platform records.
5. Identify missing or conflicting information.
6. Prepare a structured investigation summary.
7. Record the marketplace support reference.
8. Track the final outcome.

### Important Limitation

The application cannot automatically conclude that a parcel was physically handed over merely because the seller reports it.

Evidence provenance and verification status must remain explicit.

---

## 3. Candidate B — Return Marked Delivered but Not Received

### Problem Description

A customer return is collected and transported through a reverse-logistics process.

The marketplace or logistics system reports:

`RETURN_COMPLETED`

However, the seller reports that the parcel has not physically arrived.

Possible explanations:

- The shipment was delivered to another location.
- The parcel was marked delivered incorrectly.
- Delivery was recorded before physical receipt.
- The parcel was accepted by another person.
- Tracking information is delayed or inaccurate.
- The seller's receiving records are incomplete.

### Evidence Categories

| Evidence                  | Potential purpose                         | Limitation                                  |
| ------------------------- | ----------------------------------------- | ------------------------------------------- |
| Digital proof of delivery | Shows the recorded delivery details       | Actual detail depends on the POD format     |
| Receiving register        | Records whether a parcel was received     | Depends on accurate recordkeeping           |
| CCTV footage              | May establish whether a delivery occurred | Coverage and retention may be limited       |
| Return tracking           | Shows reverse-logistics events            | Status alone may not prove physical receipt |
| Return waybill/AWB        | Identifies the shipment                   | Does not prove receipt or parcel contents   |
| Unboxing video            | Shows parcel contents and condition       | Only possible after physical receipt        |
| Seller statement          | Records the seller's report               | Not independent proof                       |

### Official Marketplace Process — Shopsy

Source:

https://seller.shopsy.in/faq/

The official FAQ explicitly describes this situation:

A seller has not received the return, but the dashboard displays `Return Completed`.

The seller is instructed to raise an incident requesting proof of delivery through Seller Support.

This is important because it demonstrates an existing marketplace process for obtaining delivery evidence.

### Official Seller Education — Meesho

Source:

https://www.youtube.com/watch?v=w5ymvRpGVGo

Meesho's verified seller education material describes:

- Checking the delivery partner's SMS or email for a digital POD link.
- Requesting proof of delivery through the Supplier Panel when necessary.
- A seven-day window for requesting POD in the described workflow.
- Tracking claims and support outcomes.

The same material describes unboxing video requirements for wrong or damaged returns.

Important distinction:

An unboxing video can support a wrong-item or damaged-item claim after a parcel has been received.

It cannot establish that a parcel that never arrived was physically delivered.

The applicability of the stated deadline should be checked against current seller guidance before implementation.

### Amazon SAFE-T

Official source:

https://sellercentral.amazon.in/help/hub/reference/external/GKEF6ZPBRL6VG9NV

Amazon's SAFE-T overview describes reimbursement requests for certain Amazon-controllable losses involving returned products that were not received in their original condition.

Claims are evaluated under Amazon's program policies.

### Potential Application Value

A future application could help sellers:

1. Record the disputed return.
2. Capture the marketplace's reported delivery status.
3. Record the seller's non-receipt statement.
4. Request and associate POD.
5. Record receiving-register checks.
6. Associate relevant CCTV references.
7. Identify missing information.
8. Track claim and support deadlines.
9. Prepare a structured investigation summary.
10. Record the marketplace response and final outcome.

### Important Limitation

The application may not have direct access to the delivery provider's POD or GPS records.

The seller may need to request these from the marketplace or carrier.

The application must distinguish between requested evidence and received evidence.

---

## 4. Evidence Availability Comparison

| Evidence category      | Candidate A                        | Candidate B                            |
| ---------------------- | ---------------------------------- | -------------------------------------- |
| Seller statement       | Available                          | Available                              |
| Marketplace status     | Potentially available              | Potentially available                  |
| Platform event history | Depends on API access              | Depends on API access                  |
| Carrier tracking       | Depends on carrier                 | Depends on carrier                     |
| Signed manifest        | Potentially available              | Not normally the primary evidence      |
| Pickup receipt         | Potentially available              | Not normally the primary evidence      |
| Proof of delivery      | Not normally the primary evidence  | Important                              |
| Receiving register     | Not normally the primary evidence  | Potentially useful                     |
| CCTV                   | Potentially useful                 | Potentially useful                     |
| Unboxing video         | Not applicable to initial handover | Relevant only if a parcel was received |

The availability of each evidence type depends on the seller's operational workflow and logistics partner.

---

## 5. What Can Be Established Independently?

### Candidate A

The seller may possess:

- A manifest.
- A pickup receipt.
- CCTV footage.
- A record of the scheduled pickup.
- Marketplace shipment information.

These records may support the seller's account of handover.

However, they do not always establish that a particular parcel was accepted by the carrier.

A reliable investigation may require carrier confirmation.

### Candidate B

The seller may possess:

- Receiving records.
- CCTV footage.
- Marketplace return status.
- Return tracking information.
- A digital POD obtained from the marketplace or carrier.

The seller may need external cooperation to obtain the actual delivery proof.

A marketplace status of `Delivered` should not automatically be treated as independent confirmation that the correct parcel reached the seller.

---

## 6. External Cooperation Requirements

| Requirement                | Candidate A          | Candidate B                   |
| -------------------------- | -------------------- | ----------------------------- |
| Marketplace event data     | Useful               | Useful                        |
| Carrier confirmation       | Potentially required | Often important               |
| Marketplace support        | May be needed        | May be needed                 |
| Physical seller records    | Useful               | Useful                        |
| Delivery proof request     | Usually not central  | Often central                 |
| Claim or complaint process | Pickup-miss process  | Return/SAFE-T/support process |

Both candidates involve external systems.

Candidate B may have a greater dependency on obtaining delivery evidence from the marketplace or carrier.

This is a preliminary assessment, not a measured comparison.

---

## 7. Potential Product Responsibilities

### Deterministic Application Logic

For both candidates:

- Match order and shipment identifiers.
- Preserve original event timestamps.
- Compare event timelines.
- Identify missing information.
- Associate evidence with investigations.
- Track support references.
- Calculate follow-up dates.
- Preserve investigation history.

### Potential AI Responsibilities

- Summarize investigation timelines.
- Extract relevant information from documents for review.
- Organize supporting evidence.
- Draft support-case explanations.
- Summarize marketplace responses.
- Highlight missing information.

### Human Responsibilities

The seller must remain responsible for:

- Confirming reported physical events.
- Reviewing extracted document information.
- Confirming evidence accuracy.
- Approving support-case content.
- Submitting complaints.
- Approving consequential actions.

AI must not create evidence or present unverified claims as facts.

---

## 8. Comparative Assessment

| Criterion                             | Candidate A               | Candidate B                             |
| ------------------------------------- | ------------------------- | --------------------------------------- |
| Clear operational trigger             | Yes                       | Yes                                     |
| Potential independent seller evidence | Manifest, receipt, CCTV   | Receiving records, CCTV                 |
| Dependence on external POD            | Lower                     | Higher                                  |
| Evidence complexity                   | Moderate                  | Moderate to high                        |
| Marketplace process exists            | Yes                       | Yes                                     |
| Potential financial impact            | Delays and seller metrics | Product loss and reimbursement disputes |
| Technical prototype feasibility       | Potentially manageable    | More complex                            |
| Frequency established                 | No                        | No                                      |
| Seller time burden measured           | No                        | No                                      |
| Willingness to pay established        | No                        | No                                      |

No numerical scores are assigned because representative measurements are unavailable.

---

## 9. Important Findings

### Finding 1 — Both Problems Exist in Marketplace Workflows

Amazon's Easy Ship guidance and Shopsy's seller FAQ describe pickup-related issues.

Shopsy also explicitly documents the process for a return marked completed when the seller has not received the product.

These sources support further investigation of both candidates.

### Finding 2 — Evidence Requirements Are Different

Candidate A focuses on handover evidence.

Candidate B focuses on delivery and receipt evidence.

A single generic evidence checklist would be inadequate.

### Finding 3 — Marketplace Processes Already Exist

Both problems have existing marketplace support processes.

A third-party application must complement those processes.

### Finding 4 — Evidence Provenance Is Important

The application must distinguish:

- Marketplace-recorded information.
- Carrier-recorded information.
- Seller-provided information.
- Documents received from external parties.
- AI-generated summaries.

### Finding 5 — Frequency and Demand Remain Unknown

Public documentation proves that workflows exist.

Individual seller complaints show that issues can occur.

Neither source establishes market frequency, average financial impact, or willingness to pay.

---

## 10. Current Position

Both candidates remain active.

Candidate A may offer a simpler initial investigation workflow.

Candidate B may offer a more substantial evidence-retrieval and claim-management challenge.

Neither has been selected.

The project should not proceed to implementation merely because one scenario is easier to simulate.

---

## 11. Validation Still Required

The next validation effort should establish:

1. How often sellers encounter each problem.
2. How many shipments are affected.
3. What financial or operational impact results.
4. How much time is spent investigating.
5. Which evidence sellers actually possess.
6. How often external support must be contacted.
7. How frequently claims are successful.
8. What existing tools sellers use.
9. Whether sellers would adopt an independent investigation workspace.
10. Whether they would pay for it.

Direct seller validation remains necessary.

---

## 12. Next Milestone

The next step is to identify a realistic validation method.

Potential methods:

- Review additional public seller cases.
- Examine current official marketplace workflows.
- Study available seller and carrier documentation.
- Seek anonymized examples of actual investigations.
- Conduct seller conversations when suitable participants become available.

The goal is to establish frequency, effort, impact, and unmet needs before selecting the initial product use case.

---

## 13. Sources

### Amazon

Easy Ship Pickup Miss FAQ:

https://sellercentral.amazon.in/help/hub/reference/external/GKNZKMGSV38C2RTZ

Easy Ship Pickup Miss guidance:

https://sellercentral.amazon.in/seller-forums/discussions/t/cc316f3b-10c3-4fbc-a2eb-29fd87e5a95e

SAFE-T overview:

https://sellercentral.amazon.in/help/hub/reference/external/GKEF6ZPBRL6VG9NV

### Shopsy

Official seller FAQ:

https://seller.shopsy.in/faq/

### Meesho

Verified seller education — returns, POD, and claims:

https://www.youtube.com/watch?v=w5ymvRpGVGo

Return and RTO acceptance SOP:

https://images.meesho.com/images/marketing/1678700972767.pdf

---

## Research Integrity

This document records preliminary comparative research.

It does not claim:

- That either problem is frequent.
- That all sellers possess the listed evidence.
- That all carriers expose equivalent tracking data.
- That every marketplace uses the same evidence requirements.
- That the proposed product has validated demand.
- That a prototype should already be built.

Further research and direct seller validation are required.
