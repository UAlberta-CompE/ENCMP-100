# ENCMP-100 – Programming for Engineers Labs

Hands-on lab solutions and reference material for the University of Alberta's ENCMP 100 course. Each lab folder contains incremental versions (V0 starter through V2 feature-complete) plus supporting datasets or plots that illustrate the required engineering concept.

## Repository map

| Folder | Focus | Highlights & Key Files |
| --- | --- | --- |
| `LAB 1` | Quantum chemistry | `Version 2/hSpectrumV2_misbahah.py` compares Bohr-model wavelengths against NIST data and plots the hydrogen emission series. |
| `LAB 2` | Logic & conditionals | `V2FullDecoder/lab2V2_misbahah.py` validates and decodes a nine-digit rescue cipher with exhaustive guard clauses. |
| `LAB 3` | Data structures & plotting | `V2Optimization/lab3V2_misbahah.py` models RESP savings versus tuition inflation, produces Matplotlib plots, and searches for the optimal monthly contribution. |
| `LAB 4` | File I/O & menu-driven design | `V2LimitDimension/lab4V2_misbahah.py` loads TSPLIB data, filters records by dimension, and renders EUC_2D tours. |
| `LAB 5` | Scientific data pipelines | `V2SaveRefine/lab5V2_misbahah.py` parses NASA Horizons perihelion logs, extracts key epochs, produces regression plots, and exports cleaned CSV output. |
| `LAB 6` | Signal processing & simulation | `V2OccultationPlot/lab6V2_misbahah.py` simulates a coronagraph with FFTs and the Gerchberg–Saxton algorithm, saving each iteration as PNG frames. |
| `Hortsmann/bookcode-py-3` | Textbook companion code | Supplemental scripts from Cay Horstmann’s *Python for Everyone* used for practice and reference. |
| `Hortsmann/ezgraphics-supp` | Graphics utilities | The EzGraphics support library needed by several Horstmann examples. |

## Getting started

1. Install Python 3.10+ plus the course libraries:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install numpy matplotlib scipy
   ```
2. Navigate to a lab version (e.g., `LAB 5/V2SaveRefine`) and run the target script with `python lab5V2_misbahah.py`.
3. Refer to the included PDFs (`Lab#Instructions.pdf`) for background, grading rubrics, and prompts.

Many labs generate figures (`*.png`) or CSV exports alongside their source. Keep those artifacts—they document the simulation outputs that labs are graded on.

## Course themes covered

- Modeling physical systems (hydrogen spectra, tuition compounding, orbital mechanics, optical systems).
- Defensive programming techniques in input validation and menu-driven workflows.
- Working with structured data: text parsing, NumPy arrays, SciPy statistics, and Matplotlib visualization.
- Reusable utility development (file readers, FFT helpers, Gerchberg–Saxton iterations, TSP tooling).

## Contributing or re-running labs

These submissions reflect completed coursework; please keep academic integrity policies in mind before reusing code. If you revisit a lab:

1. Copy the latest `V2` folder.
2. Re-run the script to regenerate outputs so that plots and CSV files match your Python version.
3. Document any deviations from the original algorithms to maintain provenance.
