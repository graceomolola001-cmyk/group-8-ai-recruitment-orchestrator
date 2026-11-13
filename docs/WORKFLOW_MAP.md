# Recruitment workflow map

The JSON exports under `workflows/` represent separate Group 8 modules. They are intended to be imported, configured and tested individually. A file being present does not guarantee its handoffs were connected successfully.

| Export | Purpose | Nodes |
| --- | --- | ---: |
| `02-capstone-project.json` | Early application intake | 7 |
| `03-capstone-project.json` | Main orchestration, including **mock JS evaluator** | 22 |
| `04-cv-extraction-and-cleaning.json` | Resume extraction | 6 |
| `09-capstone-interview-scheduling-airtable-google-calendar.json` | Calendar and interview coordination | 12 |
| `12-group-8-offer-approval-test-capstone-airtable-rebuilt.json` | Offer approval module | 20 |
| `13-offer-approval-request.json` | Offer approval requests | 8 |
| `14-my-sub-workflow-1.json` | Supporting sub-workflow | 4 |
| `15-interview-reminder-workflow.json` | Scheduled reminders | 12 |
| `16-saving-questions-to-n8n-and-update-record.json` | Screening question persistence | 5 |
| `19-the-review-ai-shortlist-and-human-approval.json` | Screening review and human oversight | 12 |

## Team-contributed Python module

`python-screening-generator/main.py` is the submitted LangChain/Gemini question-generation source. It may require updated model configuration to execute. The code is included for reproducibility, with authorship credited to the Group 8 team.

## Integration notes

- Match Airtable business IDs to the appropriate existing records before using Update or Upsert.
- Recreate the screening question and recruiter decision fields used by the chosen module.
- Review all conditions in imported workflow nodes: some exported modules have incomplete or environment-specific mappings.
- Verify every parent-to-child Execute Workflow reference and every downstream transition; IDs from the original instance are not portable.
- Use only the [synthetic test data](https://github.com/graceomolola001-cmyk/group-8-recruitment-test-data).
- Record test outcomes for each module separately. See [replication checklist](REPLICATION_CHECKLIST.md).
