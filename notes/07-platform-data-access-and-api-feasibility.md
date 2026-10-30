# Platform Data Access & API Feasibility Research

## 1. Purpose

This research investigates whether a third-party application can legitimately and reliably access e-commerce platform data required to investigate seller-side operational exceptions.

The platforms examined are:

- Amazon
- Flipkart
- Meesho
- Shopify

The objective is to understand API availability, authentication, permissions, accessible operational data, and integration limitations before designing the application's integration architecture.

This research is preliminary. Documented API capabilities do not automatically establish that our application can obtain production access or retrieve every required field.

---

## 2. Research Questions

The investigation focuses on the following questions:

1. Does the platform provide an official API for third-party applications?
2. Can a seller authorize an external application to access their data?
3. Can the application retrieve order and shipment information?
4. Can it retrieve return-related information?
5. Does the platform support event notifications or webhooks?
6. Are there permission, approval, or historical-data restrictions?
7. Can the available data help investigate operational discrepancies?

---

## 3. Amazon — Selling Partner API (SP-API)

### API Availability

Amazon provides the Selling Partner API (SP-API), which allows authorized applications to interact with Amazon seller and vendor data.

Official documentation:

- https://developer-docs.amazon.com/sp-api/
- https://developer-docs.amazon.com/sp-api/docs/connecting-to-the-selling-partner-api
- https://developer-docs.amazon.com/sp-api/docs/roles-in-the-selling-partner-api

### Authentication and Authorization

- Applications must follow Amazon's developer registration and authorization process.
- Seller authorization uses an OAuth-based workflow.
- Applications receive access according to their approved roles.
- Certain restricted operations and data require additional security requirements.

### Relevant Data Areas

The API documentation covers several potentially useful areas:

- Orders
- Shipments and fulfillment
- Inventory
- Returns and related operations
- Notifications

The exact availability of fields and operations depends on the API, seller authorization, and assigned roles.

### Potential Project Relevance

Amazon could provide a useful source of operational records.

Potential application uses:

- Retrieve authorized order information.
- Retrieve available shipment and fulfillment information.
- Maintain a timeline of platform-recorded events.
- Identify missing or inconsistent status transitions.
- Support an investigation using available platform records.

### Limitations and Unknowns

- Production access and application approval must be tested.
- Exact availability of pickup and handover information needs investigation.
- API rate limits and notification reliability need verification.
- Access to platform records does not independently prove physical logistics events.

### Preliminary Assessment

Amazon has a documented official API path.

It is a potential integration candidate, but actual access and the suitability of individual API fields remain to be tested.

---

## 4. Flipkart — Seller APIs

### API Availability

Flipkart provides seller-facing API documentation for integrating applications with its marketplace operations.

Official documentation:

- https://seller.flipkart.com/api-docs/

### Authentication and Authorization

The documented integration process supports seller-authorized applications.

The documentation describes application registration and authorization workflows, including authorization-code-based access.

### Relevant Data Areas

Documented API areas include:

- Order management
- Shipment management
- Returns
- Notifications

The documentation also describes operational shipment and return states.

### Potential Project Relevance

Flipkart may provide access to records useful for investigating:

- Order processing
- Shipment status changes
- Return progress
- Pickup and handover-related discrepancies
- Operational event timelines

### Limitations and Unknowns

- Exact API fields must be examined before implementation.
- Access to individual operations may depend on authorization and application configuration.
- Production access must be tested.
- The relationship between platform-recorded events and physical logistics events needs validation.

### Preliminary Assessment

Flipkart has a documented seller API path and is a potential integration candidate.

The actual usefulness of its available operational data remains unverified.

---

## 5. Meesho — API and Integration Availability

### Current Research Status

An official public third-party developer API onboarding path has not yet been established through this research.

This is an unknown, not proof that Meesho has no API or approved integration program.

Official seller portal:

- https://supplier.meesho.com/

Existing seller documentation describes operational workflows, but seller-facing documentation alone does not establish that an independent application can retrieve those records through an API.

### Questions Requiring Verification

- Does Meesho provide an official third-party developer program?
- Can sellers authorize external applications?
- Are order and shipment records available through an approved API?
- Are return and reverse-logistics events accessible?
- Are there approved integration partners?
- Are event notifications supported?

### Preliminary Assessment

Meesho integration feasibility is currently unknown.

The application must not promise direct Meesho integration until an official access path has been verified.

---

## 6. Shopify — Admin GraphQL API

### API Availability

Shopify provides the Admin GraphQL API for applications that interact with merchant stores.

Official documentation:

- https://shopify.dev/docs/api/admin-graphql
- https://shopify.dev/docs/api/usage/access-scopes
- https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps

### Authentication and Authorization

- Applications obtain access through Shopify's app installation and authorization process.
- Access is controlled using scopes.
- An application must request the permissions required for its functionality.
- Protected customer data has additional requirements.

### Relevant Data Areas

Potentially useful areas include:

- Orders
- Fulfillment
- Returns
- Order-related events
- Webhooks and event-driven updates

### Important Order-History Restriction

Shopify documents a default order access window covering the most recent 60 days.

Access to older orders requires the additional `read_all_orders` scope and the relevant approval.

This restriction must be considered when designing historical investigations.

### Potential Project Relevance

Shopify provides a documented path for applications to retrieve authorized merchant data.

Potential uses include:

- Retrieve order information.
- Access fulfillment records.
- Access return information.
- Receive supported event notifications.
- Maintain an operational event timeline.

### Limitations and Unknowns

- Required scopes must be requested and approved where applicable.
- Protected customer data requirements must be respected.
- Historical order access is restricted by default.
- Webhook delivery and reconciliation behavior must be tested.
- Carrier-level physical evidence may require another data source.

### Preliminary Assessment

Shopify is a promising integration candidate because of its documented application platform and APIs.

Actual data coverage must still be compared against the operational investigation requirements.

---

## 7. Platform Comparison

| Capability | Amazon | Flipkart | Meesho | Shopify |
|---|---|---|---|---|
| Official API path | Documented | Documented | Unverified | Documented |
| Seller authorization | Supported | Supported | Unverified | Supported |
| Order data | Available API area | Available API area | Unverified | Available API area |
| Shipment/fulfillment data | Available API area | Available API area | Unverified | Available API area |
| Return data | Relevant API operations documented | Relevant API area documented | Unverified | Available API area |
| Event notifications | Supported API area | Documented notifications | Unverified | Webhooks |
| Production access tested | No | No | No | No |

Important:

"Available API area" does not mean every required field is accessible.

This table represents preliminary documentation research, not successful integration testing.

---

## 8. Critical Technical Finding: Platform Events vs Physical Events

An API can tell an application what the platform has recorded.

It cannot automatically establish that the physical event actually occurred.

Consider this example:

1. A seller hands a parcel to a logistics partner.
2. The platform is expected to record a pickup or handover event.
3. The platform continues showing an awaiting-pickup status.
4. The seller needs to investigate the discrepancy.
5. Supporting evidence may be required.

Potential evidence sources:

- Marketplace API records
- Carrier tracking information
- Pickup manifests
- Handover receipts
- Seller-uploaded documents
- Manual confirmations

The application must distinguish between:

- Platform-recorded events
- External carrier events
- Seller-provided evidence
- AI-generated summaries or interpretations

It must never present an unverified event as a confirmed physical fact.

---

## 9. Preliminary Architecture Implications

These are design observations, not finalized architectural decisions.

### A. Separate Platform Integrations

Each platform has different authentication, permissions, data structures, and operational workflows.

A future implementation should avoid tightly coupling business logic to one platform's API format.

### B. Normalize Data Carefully

A common internal event representation may eventually help compare operational events across platforms.

However, normalization must preserve platform-specific information rather than discard meaningful differences.

### C. Preserve Evidence Provenance

Every operational record should eventually identify its origin.

Possible origins:

- Marketplace API
- Carrier API
- Uploaded document
- Manual seller input

### D. Separate Detection from Interpretation

Deterministic code should handle structured comparisons wherever possible.

Examples:

- Compare timestamps.
- Detect missing status transitions.
- Identify inconsistent records.
- Calculate elapsed time.

AI may assist with:

- Summarizing an investigation.
- Organizing supporting evidence.
- Drafting a support-case explanation.

AI must not invent missing evidence or independently claim that a disputed physical event occurred.

### E. Design for Partial Integration

The product should not assume that every platform provides equivalent data.

An integration may provide order information while lacking the exact pickup or return evidence required for an investigation.

The application should represent missing data explicitly.

---

## 10. Major Unresolved Questions

| Question | Status |
|---|---|
| Can a new application obtain Amazon production access? | Not tested |
| Which Amazon fields expose pickup and handover events? | Not verified |
| Can Flipkart provide all required shipment event details? | Not verified |
| Can Meesho provide an approved third-party API? | Unknown |
| Can Shopify provide the required fulfillment and return event history? | Not tested |
| Can carrier APIs supply missing logistics evidence? | Not researched |
| What are the relevant API rate limits and retention policies? | Not researched |
| Can historical events be reliably reconstructed? | Not tested |

---

## 11. Research Conclusion

The preliminary research establishes that Amazon, Flipkart, and Shopify have documented official API paths for authorized application integrations.

Meesho's third-party API access remains unverified.

However, API availability alone does not establish that the proposed operational exception-management workflow is technically feasible.

The most important unresolved issue is whether the platforms and other legitimate data sources expose enough information to distinguish a genuine operational discrepancy from a delayed or incomplete system update.

The project should not commit to a cross-platform integration strategy until this has been investigated.

### Current Position

- Amazon: Potential integration candidate.
- Flipkart: Potential integration candidate.
- Shopify: Potential integration candidate.
- Meesho: Integration feasibility unknown.
- Carrier data: Requires separate investigation.
- Cross-platform normalization: Possible design direction, not finalized.

No production integration has been implemented or tested.

---

## 12. Next Research Milestone

Investigate the actual operational data needed to detect and investigate logistics discrepancies.

Focus on:

1. What exact events are required?
2. Which platform or external source can provide each event?
3. What happens when an event is missing?
4. Can the application detect a discrepancy reliably?
5. What evidence would be needed to support an investigation?
6. Which parts can be automated safely?

The next milestone should move us from general API availability toward a concrete data-requirements and feasibility assessment.

---

## 13. Research Sources

### Amazon

- SP-API documentation: https://developer-docs.amazon.com/sp-api/
- Connecting to SP-API: https://developer-docs.amazon.com/sp-api/docs/connecting-to-the-selling-partner-api
- SP-API roles: https://developer-docs.amazon.com/sp-api/docs/roles-in-the-selling-partner-api

### Flipkart

- Seller API documentation: https://seller.flipkart.com/api-docs/

### Meesho

- Official seller portal: https://supplier.meesho.com/

### Shopify

- Admin GraphQL API: https://shopify.dev/docs/api/admin-graphql
- Access scopes: https://shopify.dev/docs/api/usage/access-scopes
- Returns apps: https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps

---

## Research Integrity

This document records preliminary documentation research.

It does not claim:

- That seller demand has been validated.
- That production API access has been obtained.
- That every required data field is available.
- That all platforms support equivalent integrations.
- That a technical integration has been tested.
- That the proposed product is commercially viable.

Further verification and practical testing are required.
