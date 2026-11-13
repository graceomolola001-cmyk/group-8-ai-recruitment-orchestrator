# Review findings and execution safeguards

Reviewed November 13, 2026. This is a **static/offline review** of the publicly shared workflows and selected JavaScript nodes, not a complete integration test.

## Blocking issues before end-to-end execution

1. **Legacy intake export `02-capstone-project.json`:** The Webhook leads to `Edit Fields`, whose output is disconnected. The separate loop/update chain cannot be reached from the trigger. Preserve this as historical evidence; use the main `03-` workflow for controlled testing instead.
2. **Older offer module `13-offer-approval-request.json`:** The exported `update audit` node originally branched independently to both candidate notification nodes as well as the manager approval step. **The direct notification edges have now been removed in GitHub, and notifications are routed through the `If approved` decision.** This correction has passed static graph inspection, but live approval/rejection tests have not been run. **Keep the workflow inactive until that testing is complete.**
3. **Main capstone `03-`**: An `Edit Fields` node is disconnected. The demonstrated evaluator is a **JavaScript mock**, not a verified live Gemini evaluation.
4. **Human-review export `19-`:** Previous team notes flagged approval form defaults, duplicate recruiter-notes fields and incomplete Airtable update mapping. Test one fictional candidate in a sandbox before using the review branch.
5. **Environment bindings:** Replace Airtable base/table IDs, child workflow references, credentials and scheduled trigger settings. All imported workflows remain inactive by default.

## Offline checks

- All ten workflow exports parse as JSON.
- Every directed connection points to a node in its corresponding exported workflow.
- Embedded JavaScript compiled in the local syntax checks.
- One synthetic `CAP26-` record with missing `resumeUrl` was correctly flagged INVALID by the primary capstone JavaScript validator.

None of these checks proves successful Airtable writes, Google Calendar event creation, email delivery, AI inference, or end-to-end recruitment routing.

## Safe next testing sequence

Use a separate test n8n instance and fictional Airtable base. Verify a one-candidate intake first, then CV extraction, then scoring-contract validation. Check recruiter approval, rejection and offer stages **with all outbound email/calendar nodes pinned or disabled** until control flow is proven. Record execution IDs, expected and actual outcomes. The historical team defense materials are available in the [Group 8 Drive folder](https://drive.google.com/drive/folders/1SirXxtXzJOiOH5pcO_K0COzGttZO66Ro).
