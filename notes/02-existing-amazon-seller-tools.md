# Problem Discovery Research Note 02

## Existing Amazon India Seller Tools

**Project:** AI E-commerce Operations Platform
**Research stage:** Desk research
**Status:** Preliminary findings; product gap not validated
**Last updated:** 2026-10-29

---

## 1. Purpose

Investigate the existing tools Amazon India provides for order management, returns, fulfilment, and seller support.

The objective is to understand what already exists before proposing a new application or AI-powered feature.

## 2. Sources Reviewed

### Source A — Manage Orders

**Source:** Amazon Seller Central Help

**Link:** https://sellercentral.amazon.in/help/hub/reference/external/G131?locale=en-IN%23BSA

**Documented capability:** Sellers can view orders, search and filter order records, and monitor shipping-related statuses.

**Implication:** A new application should not simply duplicate basic order viewing and filtering.

### Source B — Easy Ship Return FAQ

**Source:** Amazon Seller Central Help

**Link:** https://sellercentral.amazon.in/gp/help/external/G201726020

**Documented capability:** Sellers can access return tracking information through the seller-fulfilled returns workflow. The documentation also describes a process for reporting certain returns that have not been received.

**Implication:** Return tracking and discrepancy reporting already have platform-specific workflows.

**Limitation:** The exact eligibility requirements and complete workflow must be reviewed before designing any alternative process.

### Source C — Returns, Refunds, Cancellations, and Claims

**Source:** Amazon Seller Central Help

**Link:** https://sellercentral.amazon.in/help/hub/reference/external/G69126?itemid=69034&locale=en-in

**Documented capability:** Amazon provides workflows for seller-fulfilled returns, refunds, cancellations, and applicable claims.

**Implication:** The proposed product must provide value beyond merely presenting these existing workflows in another interface.

### Source D — Amazon Seller Support

**Source:** Sell on Amazon India

**Link:** https://sell.amazon.in/sell-online/help

**Documented capability:** Amazon describes seller support, learning resources, and access to third-party service providers.

**Implication:** Existing support and assistance options must be considered when evaluating whether sellers need another tool.

### Source E — Fulfilment by Amazon

**Source:** Sell on Amazon India

**Link:** https://sell.amazon.in/shipping-and-fulfillment/fulfillment-by-amazon/fba-faq

**Documented capability:** Under FBA, Amazon handles storage, packing, shipping, customer service, and returns for eligible orders.

**Implication:** The operational problems experienced by FBA sellers may differ from those experienced by sellers who fulfil their own orders.

---

## 3. Preliminary Capability Comparison

| Capability | Existing Amazon support | Research implication |
|---|---|---|
| View and search orders | Documented | Do not duplicate basic order management |
| Review return requests | Documented | Investigate whether any unmet need exists beyond the existing workflow |
| Track eligible return shipments | Documented | Determine whether sellers need additional cross-record investigation |
| Report certain return discrepancies | Documented | Review the existing process before proposing alternatives |
| Access seller support | Documented | Determine whether case preparation or follow-up creates a genuine unmet need |
| Combine information from multiple permitted sources | Not established by this research | Investigate before claiming a gap |
| Automatically prepare evidence-based case summaries | Not established by this research | Potential feature hypothesis requiring validation |

## 4. Preliminary Research Finding

Amazon already provides order-management, return-management, fulfilment, and seller-support capabilities.

Therefore, building another basic order dashboard or return tracker is not currently justified.

A potential direction worth investigating is whether sellers need help combining information from permitted sources, identifying inconsistencies across records, organizing evidence, or preparing case summaries.

This is a hypothesis, not a validated product opportunity.

## 5. Questions Still Unanswered

1. Which operational tasks remain difficult after sellers use the existing Amazon tools?
2. Do sellers manually combine information from multiple pages, reports, or support cases?
3. How frequently does this happen, and how much time does it take?
4. Do existing third-party applications already address the same workflow?
5. Which seller types experience the problem most acutely?
6. What information can a third-party application access through permitted interfaces?
7. Would sellers be willing to test a separate application for this task?

## 6. Important Constraints

- Official documentation describes platform capabilities, not how well every seller's needs are met.
- The research does not establish the prevalence or financial impact of any problem.
- The available sources have not established a gap in Amazon's existing workflows.
- API access, permissions, data availability, and applicable policies remain to be investigated.
- No seller interviews or prototype tests have been conducted.
- No feature scope or architecture has been finalized.

## 7. Provisional Decision

**Decision:** Do not commit to building a duplicate order-management or return-tracking dashboard.

**Status:** Provisional research direction.

**Reason:** Amazon already documents capabilities in these areas.

**Revisit when:** Further research and seller feedback identify a specific unmet need that existing tools do not adequately address.

## 8. Next Action

Investigate seller discussions and existing third-party tools to identify specific operational tasks that remain difficult despite the capabilities documented above.

Record the source, reported workflow, existing workaround, explicit impact, and remaining uncertainty.

Do not treat a potential product gap as confirmed until it is supported by evidence.
