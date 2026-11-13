# Team credits and evidence boundaries

**Group 8, TechCrush AI Automation capstone: From Application to Hire**

**Team lead:** Grace Omolola Odukoya. Grace coordinated implementation and integration, defined the workflow architecture and responsibilities, built the first-stage application intake, and independently created all **50 synthetic CV profiles and PDF test files** in the [test-data repository](https://github.com/graceomolola001-cmyk/group-8-recruitment-test-data).

**Collaborative contributions:** Group 8 teammates developed or supported CV retrieval and extraction, job context, AI evaluation, business routing, screening question generation, recruiter review, scheduling, reminders, offer approval and presentation documentation. Attribution belongs to the respective authors and the team. Python screening-generator source in this repository was **team-contributed**, not independently authored by Grace.

## What was demonstrated

- Synthetic candidate intake and initial Airtable registration using n8n
- Candidate CV download and parsing stages
- Structured candidate scoring contract. **API limits blocked use of the intended connected AI evaluation node during the demonstration, so the team substituted a JavaScript mock to test the surrounding workflow.** The mock output was simulated, not live model inference.
- Module-level screening outputs and Airtable test records as described in the defense materials
- Additional exported modules for approvals, scheduling, reminders and offers

## Reason for the disconnected AI stage

The AI node was designed to be connected in the intended orchestration. API limits during the team's demonstration prevented the planned live AI testing, so a temporary mock evaluator allowed the team to exercise and demonstrate downstream stages. This explains the intentional workaround without establishing that the live AI integration succeeded.

## What remains unverified

- A complete live Gemini evaluation of the full candidate batch
- Complete recruiter decision persistence through all handoffs
- End-to-end application-to-hire progression across the exported modules
- Production readiness, bias assessment and real candidate suitability

Use the [team capstone folder](https://drive.google.com/drive/folders/1SirXxtXzJOiOH5pcO_K0COzGttZO66Ro) for historical documentation. Exported files can contain incomplete or environment-specific nodes; import into a sandbox and test before relying on them.
