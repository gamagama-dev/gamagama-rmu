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

Books are identified by their numeric prefix:

| Prefix | Book | Output directory |
|--------|------|-----------------|
| `gcp-rmu-001` | Core Law | `rulebooks/core-law/` |
| `gcp-rmu-002` | Spell Law | `rulebooks/spell-law/` |

PDFs are assumed to be at `/workspace/Downloads/`. Adjust the path if yours differ.

## Prerequisites

`gg-pdf` must be installed (see `gamagama-pdf` repo):

```bash
pipx install path/to/gamagama-pdf
```

## Generating the files

Run all commands from the `gamagama-rmu/` repo root.

### Step 0 — verify PDF locations

Each prefix must match exactly one file. Confirm before proceeding:

```bash
ls /workspace/Downloads/gcp-rmu-001-*.pdf   # must show exactly one file
ls /workspace/Downloads/gcp-rmu-002-*.pdf   # must show exactly one file
```

If a pattern matches zero or more than one file, locate the correct PDF and adjust
the path accordingly.

### Step 1 — inspect bookmarks (optional but recommended before first run)

```bash
gg-pdf bookmarks /workspace/Downloads/gcp-rmu-001-*.pdf
gg-pdf bookmarks /workspace/Downloads/gcp-rmu-002-*.pdf
```

Review the output to verify the bookmark structure looks sensible. The default
`--heading-strategy bookmarks` is appropriate for these PDFs.

### Step 2 — convert PDFs to markdown + JSON

```bash
gg-pdf convert /workspace/Downloads/gcp-rmu-001-*.pdf -o rulebooks/core-law/
gg-pdf convert /workspace/Downloads/gcp-rmu-002-*.pdf -o rulebooks/spell-law/
```

Each command produces `<stem>.md` and `<stem>.json` in the output directory.
These are large intermediate files; do not commit them.

### Step 3 — split markdown into per-chapter files

```bash
gg-pdf split-md rulebooks/core-law/gcp-rmu-001-*.md -o rulebooks/core-law/chapters/
gg-pdf split-md rulebooks/spell-law/gcp-rmu-002-*.md -o rulebooks/spell-law/chapters/
```

### Step 4 — clean up intermediate markdown

```bash
rm rulebooks/core-law/gcp-rmu-001-*.md
rm rulebooks/spell-law/gcp-rmu-002-*.md
```

The `chapters/` files are the committed artifact. The full `.md` is no longer needed.

### Step 5 — extract tables (not yet implemented)

`gg-pdf extract-tables` is not yet implemented. Until it is, the full docling `.json`
files from Step 2 are retained locally for development purposes.

Once implemented, the commands will be:

```bash
gg-pdf extract-tables rulebooks/core-law/gcp-rmu-001-*.json -o rulebooks/core-law/tables/
gg-pdf extract-tables rulebooks/spell-law/gcp-rmu-002-*.json -o rulebooks/spell-law/tables/
```

After that, the full `.json` files can also be removed.
