# Portals/Traces — contextual field map

Working draft, version 0.15 · 24 October 2026

An exploratory map connecting five project branches with concepts, literature, creative works, ethics and people. This draft contains 394 records, including 284 named people. Counts describe the collection, not its completeness or scholarly quality.

## Open the draft

Open `index.html` in a browser. The opening screen is the map, with filters and view controls on the left and selected-record details on the right. Compact navigation opens concepts, people, partners, the full library and reading/review. The page is self-contained and needs no installation or build. It includes the five branch filters, disciplinary tags, a spatial orientation view, a complete people directory, partner roster, concept explorer and searchable register.

The spatial view displays all matching records by default. Map density can limit each layer to 60, 24 or 6 records. Layer counters show displayed/matching records. The full directories expose all records. Spatial position does not measure similarity. Connections are proposed analytical links unless the record explicitly identifies authorship.

## Files

- `index.html`: complete browser draft.
- `data.json`: editable records and coverage information.
- `refresh.py`: copies edited data into the self-contained page and checks identifiers.
- `CHANGELOG.md`: changes and outstanding work.
- `.nojekyll`: supports straightforward static hosting.

After editing `data.json`, run `python3 refresh.py` in this folder, then open `index.html` again. Changing only the JSON does not change the browser page until this command runs.

Each record has an `id`, `title`, `layer`, `branches`, `disciplines`, `note`, `citation`, `url`, `access`, `question`, `links` and `status`. References in `links` use record IDs. Preserve stable IDs. Branch numbers are: 1 AI Lens; 2 XRIT; 3 Indigenous Storytelling at Distance; 4 RAW Textiles Lab and Somatic Textiles; 5 Ocean X. An empty branch array means unassigned.

## GitHub Pages

1. Create or choose a repository under the intended GitHub account.
2. Upload this folder's contents to the repository root; keep `index.html` at the root.
3. In repository Settings → Pages, choose **Deploy from a branch**, then the intended branch and **/(root)**.
4. Use the Pages URL GitHub supplies after deployment. Repository visibility and Pages access depend on the account and repository settings.

Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

This package has not been pushed to a GitHub repository or published.

## Research and review

Source metadata checks, AI-generated interpretations and human reading are separate. The new literature records are candidates based on primary bibliographic records and descriptions; they do not imply full-text critical reading. Proposed concepts include an explicit question to investigate, with connected sources.

For an academically useful revision, select a source, read it, identify a supporting passage, record its limits, and decide whether to retain, revise or reject each proposed connection. Accumulating references is not a substitute for that work.

All 22 XR omnibus entries are represented. Two further literature-search bibliographies remain unrecovered. Chapter and reference-list screening remains incomplete. Indigenous community authority and participation cannot be inferred from including Indigenous scholarship. Partner contacts are user-nominated; individual project commitments and branch roles require evidence.

Reading notes stay in the browser. Use **Export notes and data** to keep a copy; notes are not automatically shared or written back to GitHub. An iframe or different browser may have separate storage. This archive contains bibliographic records and the interface, not the supplied PDFs or private browser notes.

Selecting a node leaves the visible sample fixed. Use **Explore connected records** in the inspector to change the sample within the current filters. **Reset sample** restores the default sample.

Concept inspectors identify people credited in linked literature and name the connecting sources. Dotted concept-to-person links represent this derived source path, not endorsement of the project interpretation.

## Source mapping audit

Open **Reading & review** for searchable assessments of all 80 current source/work records against the 31 concepts. The 318 proposed links distinguish theoretical grounding, empirical comparisons, technical analogies, policy context and unverified practice leads. Evidence access and scope are recorded. This first source-record pass is not full-text critical reading or human validation. `MAPPING_AUDIT.md` is a readable audit; `data.json` includes positive links, unestablished pairs, project relevance and source credits.


## Version 0.16 — Income sources
Sixth pink map layer and searchable Income sources directory. Includes 16 named funder/programme/infrastructure leads, 15 institutional internal-funding enquiries (one for each partner institution), and 5 broader income routes. Leads are exploratory; no awards or open calls are asserted. Institutional contacts are enquiry routes, not committed applicants. Income records carry country, route, stage, contribution type, institutional routes, evidence URL/date and next step. In-kind support is distinct from cash income. Existing academic mapping audit remains unchanged.
