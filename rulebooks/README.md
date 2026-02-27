# RMU Rulebooks

Processed reference material extracted from the RMU PDF rulebooks, used to develop
gamagama-rmu features such as character sheet schemas.

## What is committed

- `<book>/chapters/*.md` — per-chapter markdown files, split from the full converted markdown

## What is NOT committed (local only)

- Raw PDF files — large and copyrighted
- `<book>/<stem>.md` — full unsplit markdown (intermediate, produced by `convert`, consumed by `split-md`)
- `<book>/<stem>.json` — full docling JSON (intermediate, produced by `convert`, consumed by `extract-tables`)

These intermediates are reproducible from the PDFs at any time using the commands below.

## Source PDFs

| Book | Filename |
|------|----------|
| Core Law | `gcp-rmu-001-RMUCoreLaw-online-20230312.pdf` |
| Spell Law | `gcp-rmu-002-RMU-Spell_Law-online_20230616.pdf` |

PDFs are assumed to be at `/workspace/Downloads/`. Adjust the path if yours differ.

## Prerequisites

`gg-pdf` must be installed (see `gamagama-pdf` repo):

```bash
pipx install path/to/gamagama-pdf
```

## Generating the files

Run all commands from the `gamagama-rmu/` repo root.

### Step 0 — inspect bookmarks (optional but recommended before first run)

```bash
gg-pdf bookmarks /workspace/Downloads/gcp-rmu-001-RMUCoreLaw-online-20230312.pdf
gg-pdf bookmarks /workspace/Downloads/gcp-rmu-002-RMU-Spell_Law-online_20230616.pdf
```

Review the output to verify the bookmark structure looks sensible. The default
`--heading-strategy bookmarks` is appropriate for these PDFs.

### Step 1 — convert PDFs to markdown + JSON

```bash
gg-pdf convert /workspace/Downloads/gcp-rmu-001-RMUCoreLaw-online-20230312.pdf \
    -o rulebooks/core-law/

gg-pdf convert /workspace/Downloads/gcp-rmu-002-RMU-Spell_Law-online_20230616.pdf \
    -o rulebooks/spell-law/
```

Each command produces `<stem>.md` and `<stem>.json` in the output directory.
These are large intermediate files; do not commit them.

### Step 2 — split markdown into per-chapter files

```bash
gg-pdf split-md rulebooks/core-law/gcp-rmu-001-RMUCoreLaw-online-20230312.md \
    -o rulebooks/core-law/chapters/

gg-pdf split-md rulebooks/spell-law/gcp-rmu-002-RMU-Spell_Law-online_20230616.md \
    -o rulebooks/spell-law/chapters/
```

### Step 3 — clean up intermediate markdown

```bash
rm rulebooks/core-law/gcp-rmu-001-RMUCoreLaw-online-20230312.md
rm rulebooks/spell-law/gcp-rmu-002-RMU-Spell_Law-online_20230616.md
```

The `chapters/` files are the committed artifact. The full `.md` is no longer needed.

### Step 4 — extract tables (not yet implemented)

`gg-pdf extract-tables` is not yet implemented. Until it is, the full docling `.json`
files from Step 1 are retained locally for development purposes.

Once implemented, the commands will be:

```bash
gg-pdf extract-tables rulebooks/core-law/gcp-rmu-001-RMUCoreLaw-online-20230312.json \
    -o rulebooks/core-law/tables/

gg-pdf extract-tables rulebooks/spell-law/gcp-rmu-002-RMU-Spell_Law-online_20230616.json \
    -o rulebooks/spell-law/tables/
```

After that, the full `.json` files can also be removed.
