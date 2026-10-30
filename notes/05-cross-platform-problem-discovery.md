# Problem Discovery Research Note 05

## Cross-Platform E-commerce Problem Discovery

**Project:** AI E-commerce Operations Platform
**Research stage:** Cross-platform desk research
**Status:** Preliminary evidence; product opportunity not validated
**Last updated:** 2026-10-30

---

## 1. Purpose

Investigate operational problems and exception-management workflows across four e-commerce platforms:

1. Amazon India
2. Flipkart / Shopsy
3. Meesho
4. Shopify-based stores

The objective is to identify recurring operational problems, understand existing platform capabilities, and discover whether a specific unmet need exists.

This research combines official platform documentation, seller discussions, and third-party operational guidance.

These sources have different levels of reliability and must not be treated as equivalent.

## 2. Platform A — Amazon India

### Evidence A1 — Missed Pickup and Late Handover

**Source:** Amazon India Seller Forums

https://sellercentral.amazon.in/seller-forums/discussions/t/9bcaf774-0c06-4334-91fc-60d391641de0

**Reported problem:**

A seller reported that a scheduled pickup did not happen, but the order was subsequently marked as a late handover.

**Documented response:**

An Amazon forum representative advised the seller to:

- Submit the missed-pickup issue form for each affected order.
- Open a written Seller Support case.
- Include affected order IDs and the relevant date.
- Keep the support case ID for records.

**Research observation:**

The reported workflow involves identifying affected orders, gathering order details, submitting a complaint, and tracking the support case.

**Evidence limitation:**

This is an individual seller report. It does not establish the frequency or financial impact of missed pickups.

### Evidence A2 — Return Pickup Follow-up

**Source:** Amazon India Seller Forums

https://sellercentral.amazon.in/seller-forums/discussions/t/6fa346b9-adde-484b-af80-9fa6e404c1b9

The discussion provides guidance on tracking return pickups, waiting for the relevant period after a missed pickup, raising a support case, and keeping affected order IDs.

**Research observation:**

Tracking unresolved return-pickup exceptions and maintaining relevant order information are explicit parts of the described workflow.

## 3. Platform B — Flipkart / Shopsy

### Evidence B1 — Return Marked Completed but Product Not Received

**Source:** Shopsy Seller FAQ

https://seller.shopsy.in/faq/

The seller FAQ describes a situation where the return status shows completed even though the seller has not received the product.

The documented next step is to raise an incident requesting proof of delivery through Seller Support.

**Research observation:**

The discrepancy between a system-recorded return status and physical receipt is a concrete problem worth investigating.

### Evidence B2 — Pickup and Scanning Discrepancy

**Source:** Shopsy Seller FAQ

https://seller.shopsy.in/faq/

The FAQ describes a situation where a product has been picked up but the dashboard still shows that it has not been picked up.

The explanation refers to a delay between scanning and the physical handover event.

**Research observation:**

Operational records may not always reflect physical events immediately.

### Evidence B3 — Failed Handover Support Workflow

**Source:** Eshopbox operational guide

https://help.eshopbox.com/portal/en/kb/articles/how-to-raise-a-ticket-on-flipkart-for-failed-to-handover-orders

The guide describes raising a Flipkart seller-support ticket for failed handovers.

The workflow includes selecting the logistics-related issue, providing order details, uploading multiple affected orders when applicable, and tracking the resulting ticket number.

**Evidence limitation:**

This is third-party operational guidance, not official Flipkart documentation. Its current accuracy and applicability require verification.

## 4. Platform C — Meesho

### Evidence C1 — Supplier Shipping and Return Workflows

**Source:** Meesho Supplier Documentation

https://supplier.int.meeshogcp.in/shipping

Meesho documents:

- Order acceptance and processing through the Supplier Panel.
- Shipment preparation and pickup.
- Dispatch timelines.
- Customer returns.
- Return to Origin (RTO) shipments.
- Return-related charges and tracking information.

**Research observation:**

Meesho already provides seller-facing workflows for managing shipping, returns, and RTO information.

A new product should not simply duplicate these capabilities.

### Evidence C2 — Disputed and Tampered Return Shipments

**Source:** Meesho Revised SOP for Return & RTO Shipment Acceptance

https://images.meesho.com/images/marketing/1678700972767.pdf

The published SOP describes a process for handling tampered or disputed shipments.

It refers to:

- Recording shipment condition.
- Adding appropriate remarks to proof of delivery.
- Providing supporting evidence, such as an unboxing video.
- Raising a claim through the applicable support process.

**Research observation:**

Evidence collection and correct documentation can be important in disputed return workflows.

**Evidence limitation:**

The SOP dates from 2023. Its current applicability must be checked against Meesho's latest policies.

### Evidence C3 — Repeated Pickup Failures

**Source:** Public seller complaint on LinkedIn

https://www.linkedin.com/posts/dp-khosla-61b00587_meesho-xpressbees-sellersupport-activity-7489789727835910144-kD45

A seller publicly described repeated pickup failures, support tickets, and claimed business impact.

**Research observation:**

This is another reported example of a seller dealing with repeated logistics problems and support follow-ups.

**Evidence limitation:**

It is an individual public complaint. The business impact has not been independently verified.

## 5. Platform D — Shopify-based Stores

### Evidence D1 — Order Management

**Source:** Shopify Help Center

https://help.shopify.com/en/manual/fulfillment/managing-orders

Shopify documents order management capabilities including:

- Viewing and searching orders.
- Filtering order records.
- Managing payments.
- Preparing orders for fulfilment.
- Processing returns and refunds.

### Evidence D2 — Returns and Exchanges

**Source:** Shopify Help Center

https://help.shopify.com/en/manual/fulfillment/managing-orders/returns

Shopify documents:

- Creating returns.
- Sending return instructions.
- Managing exchanges.
- Issuing refunds.
- Setting return rules.
- Enabling self-service returns.

### Evidence D3 — Return Application Integrations

**Source:** Shopify Developer Documentation

https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps

Shopify supports return-management applications through its APIs.

Documented capabilities include:

- Return lifecycle management.
- Return tracking.
- Automated return workflows.
- Webhook-based event notifications.
- Integration with merchant systems.

### Evidence D4 — Order Tracking

**Source:** Shopify Help Center

https://help.shopify.com/en/manual/fulfillment/setup/order-status-page/order-tracking

Shopify documents shipment tracking through order-status pages, shipping notifications, and supported integrations.

**Research observation:**

Shopify merchants already have substantial native order and return capabilities. A potential product must address a workflow that goes beyond duplicating those screens.

**Important distinction:**

Shopify merchants generally operate their own storefronts and may coordinate their own fulfilment providers.

Their workflows differ from sellers operating inside Amazon, Flipkart, or Meesho marketplaces.

## 6. Cross-Platform Comparison

| Problem or workflow | Amazon | Flipkart / Shopsy | Meesho | Shopify |
|---|---|---|---|---|
| Missed pickup or handover | Seller-reported | Documented in seller guidance | Seller-reported | Depends on fulfilment provider |
| Incorrect or delayed status | Seller-reported | Documented | Requires further investigation | Depends on carrier and integration |
| Return marked delivered but not received | Seller-reported | Explicitly documented in FAQ | Claim/evidence process documented | Merchant processes and inspects returned items |
| Evidence collection | Support cases | Proof of delivery and incidents | Shipment evidence and claims | Merchant and fulfilment records |
| Follow-up workflow | Support cases | Seller support tickets | Supplier Panel support | Merchant's own support and applications |

## 7. Emerging Cross-Platform Pattern

The research suggests a possible recurring workflow:

**Physical event → System records event → Seller identifies discrepancy → Seller gathers evidence → Seller escalates → Seller tracks the outcome.**

Examples include:

- Pickup occurred physically, but the system does not reflect it.
- Return is marked delivered, but the seller has not received the product.
- A shipment is marked late even though the seller reports that pickup did not happen.
- A disputed return requires supporting evidence.

This is an emerging pattern from selected public sources, not a validated market-wide finding.

## 8. Evidence Versus Hypotheses

| Statement | Current status |
|---|---|
| Sellers report discrepancies between physical logistics events and recorded statuses. | Supported by selected public seller reports and official seller FAQs. |
| Sellers sometimes need to provide evidence when raising disputes. | Supported by platform documentation and support procedures. |
| These problems occur frequently across all four platforms. | Unknown. |
| Evidence gathering creates significant manual work. | Hypothesis requiring further investigation. |
| Sellers lose measurable revenue because of these workflows. | Unknown; no independently verified impact measurements. |
| Existing software does not adequately solve these problems. | Not established. |
| A cross-platform exception-management application would be valuable. | Unvalidated product hypothesis. |

## 9. Potential Product Direction

A possible direction worth investigating is an operational exception-management assistant.

Potential responsibilities could include:

- Organizing exception records.
- Maintaining an event timeline.
- Collecting relevant evidence.
- Identifying missing information.
- Preparing support-case summaries.
- Tracking unresolved follow-up actions.

These are research concepts, not approved features.

The application must not invent evidence, guarantee claims, or perform consequential actions without appropriate authorization.

## 10. Important Research Limitations

- Research is based on selected public sources, not a representative sample.
- Individual seller complaints are not independently verified.
- Official documentation describes available workflows, not the quality of every seller's experience.
- Some third-party guides may be outdated.
- Meesho's cited return SOP requires current-policy verification.
- No direct seller interviews have been conducted.
- No workflow timing or cost measurements have been collected.
- API access, permissions, and regional availability remain to be investigated.
- No product-market fit or financial impact has been established.

## 11. Provisional Decision

**Decision:** Continue investigating operational exception management rather than committing to a generic order-management or returns application.

**Status:** Provisional research direction.

**Reason:** Selected sources across multiple platforms describe situations involving discrepancies between physical events and system records, followed by evidence collection or support escalation.

**Trade-off:** A common workflow may exist, but platform-specific procedures and data sources could make a single cross-platform solution difficult.

**Revisit when:** Seller feedback, additional evidence, and technical feasibility research establish a specific unmet need.

## 12. Next Action

Investigate whether the emerging workflow creates measurable difficulty for sellers.

Prioritize:

1. Finding additional independent examples.
2. Comparing current third-party solutions.
3. Investigating data-access and integration constraints.
4. Identifying a narrow initial seller segment.
5. Validating the problem with potential users when feasible.

Do not finalize product requirements or begin implementation until a specific problem is supported by sufficient evidence.
