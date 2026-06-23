# EnerVision: AI-Powered Digital Twin for Predictive Energy Intelligence

This repository contains the LaTeX source code and assets for the **EnerVision** IDP project report. This document provides instructions, dependencies, and critical context for other AI agents or developers working on this project.

## Project Structure

- **`Main.tex`**: The root LaTeX file that configures document classes, packages, variables (like `\IDPProject`), and imports all other chapters.
- **`Chapter1/` to `Chapter6/`**: Individual chapter `.tex` files containing the core content.
- **`AuxFiles/ProjectBib.bib`**: The BibTeX database containing all bibliography references.
- **`Appendix/Apndx.tex`**: Appendix contents, including source code listings.
- **`Figures/`**: Contains all images and diagrams referenced in the document.

## Dependencies

- **LaTeX Distribution**: A modern LaTeX distribution like MiKTeX or TeX Live.
- **pdflatex**: Required for PDF compilation.
- **bibtex**: Required for bibliography generation (this project uses the `biblatex` package with the `ieee` style and a `bibtex` fallback backend).

## Compilation Instructions

To ensure all citations, cross-references, and the Table of Contents are correctly resolved, you **must** use the following multi-pass compilation sequence:

```bash
pdflatex -interaction=nonstopmode Main.tex
bibtex Main
pdflatex -interaction=nonstopmode Main.tex
pdflatex -interaction=nonstopmode Main.tex
```

> **Warning:** Running `bibtex` on an outdated `Main.aux` file will cause references to fail and render literally (e.g., `[ref21]`). Always run `pdflatex` once *before* running `bibtex` when new citations are added.

## Important AI Context & Editing Guidelines

When making modifications to this project, adhere strictly to the following rules:

### 1. Table Formatting
- **Do NOT use `\resizebox`** to force tables to fit the `\textwidth`. It causes unpredictable margin overflows, font distortion, and vertical misalignment.
- **Instead**, strictly define exact column widths using `p{...cm}` in the tabular environment (e.g., `\begin{tabular}{|p{2.5cm}|p{4cm}|...}`). Use standard `\centering` within the `table` environment to center the table within the margins.

### 2. Handling Citations
- Citations are written as `\cite{ref1,ref2}`.
- If using Python scripts or automated tools to inject citations, be extremely careful with backslash escaping (`\c` is not a valid escape sequence in Python). Ensure the literal `\cite` is printed to the `.tex` file without double-escaping.

### 3. Blank Pages & Glossaries
- Empty `\printglossary` or `\printglossaries` commands in `Main.tex` will generate unwanted blank pages in the final PDF. Keep these commented out unless a fully populated glossary is explicitly added to the document.

### 4. Code Blocks
- Code snippets in the Appendix should use the `lstlisting` environment. Make sure comments within the code are stripped or heavily minimized if they cause layout or overflow issues.

### 5. AI Generated Images
- All `WhatsApp Image...` files in the `Figures/` directory correspond to specific diagrams and dashboards. When editing `.tex` files, do not assign random images; refer strictly to the exact file names that correspond to the desired visual content.
