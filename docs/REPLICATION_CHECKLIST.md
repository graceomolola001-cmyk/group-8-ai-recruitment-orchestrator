# Reproduction checklist

## Environment

- [ ] Set up local or authorized hosted n8n with no production customer data
- [ ] Create an Airtable **test** base with Candidates, Jobs, Screening, Interviews, Offers and Audit as required
- [ ] Create a fictional job record with Job ID `JOB-001`
- [ ] Configure private Airtable / Google Calendar / Gmail credentials
- [ ] Import one workflow at a time from `workflows/`; keep them disabled until checked

## One-candidate walkthrough

1. Start the main intake workflow in webhook test mode.
2. Send a synthetic `CAP26-001` candidate with the correct PDF URL from [the test-data repository](https://github.com/graceomolola001-cmyk/group-8-recruitment-test-data).
3. Inspect validation, CV download and extraction, Airtable candidate record and normalized output.
4. Verify the JavaScript evaluator is identified as a **mock** in the recorded main workflow. Do not claim live Gemini output without testing it.
5. Validate the business routing against synthetic expectations.
6. Test screening and recruiter approval with **one** fictitious record before larger batches.
7. Test interview and offer modules independently; check that state updates target the intended candidate.

## Negative tests

- [ ] Missing `resumeUrl` fails before download
- [ ] Invalid `jobId` produces a recorded failure
- [ ] Repeated webhook does not unintentionally duplicate candidate data
- [ ] Missing reviewer decision does not default to approval
- [ ] Rejected candidate does not progress to interviews or offers
- [ ] No test notification goes to an unauthorised recipient

Record actual results and timestamps. The checkboxes above are test instructions, **not** proof that the cases have passed.
