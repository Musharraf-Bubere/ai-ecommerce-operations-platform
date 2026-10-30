# Problem Discovery Research Note 04

## Real Seller Workflows: Operational Exceptions

**Project:** AI E-commerce Operations Platform
**Research stage:** Seller workflow investigation
**Status:** Preliminary observations; no validated product requirements
**Last updated:** 2026-10-29

---

## 1. Purpose

Investigate what sellers actually do when marketplace order and return exceptions occur.

The objective is to understand the workflow, evidence requirements, existing workarounds, and possible friction before choosing a product problem.

This note uses publicly accessible seller-forum discussions. These are individual reports, not a representative sample of sellers.

## 2. Workflow A — Missed Pickup and Late-Handover Status

### Source

**Discussion:** Pickup not done and Amazon marked late handover

https://sellercentral.amazon.in/seller-forums/discussions/t/9bcaf774-0c06-4334-91fc-60d391641de0

**Additional source:** Easy Ship Pickup Misses: What Happens Next?

https://sellercentral.amazon.in/seller-forums/discussions/t/2cfd1c80-6b97-4a5c-abc5-d76064a7c3a6

### Reported problem

A seller reported that a scheduled pickup did not occur and that the order was subsequently marked as a late handover.

An Amazon forum representative described a process involving a missed-pickup form and a written Seller Support case.

### Observed workflow

1. Prepare an order for pickup.
2. Discover that the scheduled pickup did not happen.
3. Check the order status and any resulting account or fulfilment metric.
4. Submit the relevant missed-pickup form.
5. Open a written support case with the relevant order details and date.
6. Keep the support case ID and monitor the outcome.

### Existing workaround

Use Amazon's existing missed-pickup and Seller Support workflows.

### Potential friction to investigate

- Does the seller have to repeat information across forms and support cases?
- How does the seller remember which orders need follow-up?
- How are unresolved cases tracked?
- Does the seller have difficulty collecting evidence that the pickup was missed?
- How often does this occur for an individual seller?

### Evidence limitations

The discussion establishes that an individual seller reported this problem and that a support procedure was described. It does not establish prevalence, financial impact, or the amount of manual work involved.

## 3. Workflow B — Return Marked Delivered but Item Not Received

### Source

**Discussion:** Product Marked Delivered to Seller, But Not Received

https://sellercentral.amazon.in/seller-forums/discussions/t/0abf86d4-3fa1-453e-87f0-254dbe187ab3

**Additional source:** Return product not received

https://sellercentral.amazon.in/seller-forums/discussions/t/16cce2b2-90bc-4777-a6aa-57b3ee665014

### Reported problem

Sellers reported return products appearing as delivered in the seller interface even though the sellers said they had not physically received the items.

One discussion described uncertainty about support guidance and reimbursement eligibility.

### Observed investigation workflow

1. Identify the affected order and return.
2. Check the return status and available tracking information.
3. Compare the recorded delivery event with the seller's physical receiving records.
4. Review the support-case history.
5. Identify the applicable claim or dispute process.
6. Gather the required evidence.
7. Submit or follow up on the case within the applicable deadline.

### Existing workaround

Use the marketplace's return-management, support, and applicable reimbursement or dispute procedures.

### Potential friction to investigate

- Is relevant evidence spread across multiple pages or systems?
- Does the seller maintain a separate receiving log?
- Is it difficult to determine which evidence is required?
- Are claim deadlines and follow-up dates easy to track?
- How much time does an individual case require?

### Evidence limitations

These are individual seller reports. The research does not establish how frequently these discrepancies occur, whether the seller's records were independently verified, or whether an alternative application would improve the outcome.

Claim eligibility and deadlines must be checked against current official policies before giving operational guidance.

## 4. Shared Workflow Pattern

The two scenarios suggest a possible common process:

**Detect an exception → Verify the records → Gather evidence → Follow the correct procedure → Track the outcome.**

This is a pattern worth investigating, not a validated finding across the e-commerce seller market.

## 5. Evidence Versus Hypotheses

| Statement | Current status |
|---|---|
| Sellers have publicly reported missed pickups and incorrect late-handover status. | Supported by an individual seller discussion. |
| Amazon has a documented missed-pickup reporting procedure. | Supported by Amazon forum guidance. |
| Sellers have publicly reported returns marked delivered when the items were not physically received. | Supported by individual seller discussions. |
| These workflows are common across independent sellers and growing brands. | Unknown. |
| Evidence gathering and follow-up create significant manual work. | Hypothesis requiring investigation. |
| Sellers frequently miss claim or follow-up deadlines. | Unknown. |
| A separate application would improve these workflows. | Unvalidated product hypothesis. |
| Existing third-party products do not address these problems. | Not established. |

## 6. Questions for Seller Validation

1. Which operational exception do sellers encounter most frequently?
2. What exact steps do they take to resolve it?
3. Which pages, reports, messages, and records do they consult?
4. Do they copy information between forms or systems?
5. How do they track outstanding cases and deadlines?
6. How much time does a typical case take?
7. What happens when a case is delayed or unresolved?
8. Which existing tools already help them?
9. Would sellers try a tool that organizes evidence and follow-up actions?
10. What measurable improvement would make such a tool worthwhile?

## 7. Provisional Product Hypothesis

A possible direction is an operational exception follow-through assistant that helps sellers organize case evidence, identify the appropriate next step, and track unresolved actions.

Potential capabilities to investigate include:

- A structured exception record.
- An evidence checklist.
- A timeline of relevant events.
- A support-case summary based on supplied records.
- Follow-up reminders.
- Clear references to the original evidence.

These are research concepts, not approved features.

The tool must not invent evidence, guarantee reimbursement, or submit consequential actions without appropriate authorization.

## 8. Research Limitations

- Evidence comes from a small number of publicly accessible discussions.
- Forum reports are individual accounts and may be incomplete or subjective.
- No seller interviews have been conducted.
- No workflow timing or cost measurements have been collected.
- Existing marketplace and third-party capabilities require further investigation.
- No product-market fit or business impact has been established.
- No architecture or implementation scope has been finalized.

## 9. Next Action

Continue research before selecting a product problem.

Compare additional seller workflows and investigate whether the suspected manual work is already addressed by existing tools.

Where possible, speak with potential sellers and record their actual processes, workarounds, frequency, and measurable impact.

Do not treat the proposed exception follow-through assistant as a validated opportunity until further evidence supports it.
