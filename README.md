# NIELIT Python

A public teaching repository for the Python language and five complete programs. The notebooks state the idea, then run it. The documents in [docs/](docs) explain the same material more slowly: the claim each section is making, the sample result, the mistake that section is meant to prevent, and the exercise that follows it.

The repository is open source under the [MIT Licence](LICENSE). You may use, copy, modify, and redistribute the notebooks and the documentation, including in a course, provided the copyright notice and the permission notice travel with any substantial copy. Attribution beyond that notice is appreciated and not required. A citation form is in [CITATION.cff](CITATION.cff).

**Author:** Er. Rishabh Aryan  
**Repository:** https://github.com/Rishabh-bgp/NIELIT-PYTHON-  
**Python:** 3.10 or newer  
**Dependencies:** none

## Contents

| Path | What it is |
| --- | --- |
| [notebooks/python_mastery.ipynb](notebooks/python_mastery.ipynb) | Language reference with theory, examples, and captured output |
| [notebooks/capstones/](notebooks/capstones) | Calculator, tic-tac-toe, Hangman, quiz, expense ledger |
| [src/nielit_python/](src/nielit_python) | The same five programs as importable Python modules |
| [tests/test_modules.py](tests/test_modules.py) | Standard-library tests for the published samples |
| [docs/python-modules.md](docs/python-modules.md) | How to run and import the modules |
| [docs/language-reference.md](docs/language-reference.md) | Section notes, claims, and the mistake each section prevents |
| [docs/capstones/](docs/capstones) | Design note, trace, and limits for each program |
| [docs/getting-started.md](docs/getting-started.md) | Interpreter, Jupyter, and the usual failures |
| [docs/learning-path.md](docs/learning-path.md) | Eight sittings with outcomes |
| [docs/exercises.md](docs/exercises.md) | Practice that is not already solved in a cell |
| [docs/glossary.md](docs/glossary.md) | Terms used in the notebooks |
| [docs/faq.md](docs/faq.md) | Licence, version, coursework, and output questions |
| [docs/further-reading.md](docs/further-reading.md) | Official Python documentation, mapped to each section |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose a correction |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Expected behaviour in issues and reviews |

## Run the notebooks

```bash
git clone https://github.com/Rishabh-bgp/NIELIT-PYTHON-.git
cd NIELIT-PYTHON-
python3 -m pip install notebook
python3 -m notebook
```

Open a file under `notebooks/`. Use **Restart kernel and run all** after a clone if you want the output replaced by a run on your machine. Stored output is already in the file, so the notebooks can be read on GitHub without a kernel. `id()` values and timestamps will differ on a local run. Other printed results should match the notes.

Each notebook is independent. A capstone does not import the language reference. The same programs can be run without Jupyter:

```bash
PYTHONPATH=src python3 -m nielit_python.calculator
PYTHONPATH=src python3 -m unittest tests/test_modules.py
```

No notebook, and no module, imports a third-party package. Jupyter is only the program that opens the notebooks. The module guide is [docs/python-modules.md](docs/python-modules.md).

The full setup, including a virtual environment and a table of common failures, is in [docs/getting-started.md](docs/getting-started.md).

## Suggested reading order

1. [Getting started](docs/getting-started.md), then the [glossary](docs/glossary.md) if a term is unfamiliar.
2. [python_mastery.ipynb](notebooks/python_mastery.ipynb), with [the section guide](docs/language-reference.md) open beside it.
3. The capstones in order. The calculator practises parsing and errors. The two games practise state. The quiz practises records. The ledger practises dates and exact decimal money.
4. [Exercises](docs/exercises.md) after the matching section, not before.
5. [Learning path](docs/learning-path.md) if you are teaching the set as a short course.

## Capstones

| Notebook | Subject | Detailed note |
| --- | --- | --- |
| [Calculator](notebooks/capstones/Project_01_Safe_Expression_Calculator.ipynb) | Recursive-descent arithmetic, memory, history | [note](docs/capstones/01-calculator.md) |
| [Tic-tac-toe](notebooks/capstones/Project_02_Tic_Tac_Toe.ipynb) | Immutable board, minimax opponent | [note](docs/capstones/02-tic-tac-toe.md) |
| [Hangman](notebooks/capstones/Project_03_Hangman.ipynb) | State machine, repeated-guess rule | [note](docs/capstones/03-hangman.md) |
| [Quiz master](notebooks/capstones/Project_04_Quiz_Master.ipynb) | Frozen paper, recomputed score | [note](docs/capstones/04-quiz-master.md) |
| [Expense tracker](notebooks/capstones/Project_05_Expense_Tracker.ipynb) | `Decimal` ledger, monthly totals, budgets | [note](docs/capstones/05-expense-tracker.md) |

## Design rules in the code

- A name is a binding. Mutation and rebinding are kept distinct.
- Default arguments are immutable. A container is created inside the function.
- Exceptions are specific, and a translated error keeps its cause with `raise ... from`.
- Text files are opened with `with` and an explicit encoding.
- Money is `Decimal` constructed from a string.
- Public behaviour sits on a class. Sample data sits below the class.

## Licence

MIT. See [LICENSE](LICENSE). Questions that come up when reusing the material in a course are answered in [docs/faq.md](docs/faq.md).

## Official Python documentation

This repository is a selection, not the manual. Readers who want the full language and library description should use the official documentation:

- [Python documentation](https://docs.python.org/3/)
- [Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Language reference](https://docs.python.org/3/reference/index.html)
- [Standard library](https://docs.python.org/3/library/index.html)

[docs/further-reading.md](docs/further-reading.md) maps each section of this course to the matching official page.

## 🔗 Other repositories by Rishabh Aryan

| Repository | Description | Live |
|---|---|---|
| [100-days-of-python](https://github.com/Rishabh-bgp/100-days-of-python) | My original, offline, no-API-key solutions to all 100 projects of the 100 Days of Code Python bootcamp curriculum… | — |
| [Agentic-Engineering-Ebook](https://github.com/Rishabh-bgp/Agentic-Engineering-Ebook) | Agentic Engineering is a practical notebook-book on specifying, generating, verifying, and refining multi-tenant… | — |
| [beed-ml-study](https://github.com/Rishabh-bgp/beed-ml-study) | Provenance audit and leakage-aware benchmark of seizure-type classifiers on the Bangalore EEG Epilepsy Dataset — IIT… | — |
| [Brain-Computer-Interfaces-and-Cognitive-Computing-An-Introduction](https://github.com/Rishabh-bgp/Brain-Computer-Interfaces-and-Cognitive-Computing-An-Introduction) | Brain–computer interfaces (BCIs) link neural activity to external devices, translating brain signals via algorithms… | — |
| [building-a-virtual-cell-in-python](https://github.com/Rishabh-bgp/building-a-virtual-cell-in-python) | A cell has a normal gene-activity pattern. Knock out one gene and that pattern changes. This project trains a small… | — |
| [Chronic-Kidney-Disease-Stage-Identification-in-HIV-Infected-Patients-Using-Supervised-ML](https://github.com/Rishabh-bgp/Chronic-Kidney-Disease-Stage-Identification-in-HIV-Infected-Patients-Using-Supervised-ML) | ML is transforming Chronic Kidney Disease (CKD) detection in HIV patients, catching early asymptomatic stages to… | — |
| [cobratate](https://github.com/Rishabh-bgp/cobratate) | Cobratate, an esoteric imperative programming language. Tate-flavored syntax, ordinary semantics, and a Python… | [open](https://rishabh-bgp.github.io/cobratate/) |
| [coda-synth](https://github.com/Rishabh-bgp/coda-synth) | CoDA-Synth: stylometric detection of LLM-rewritten dark-web documents with sparse TF-IDF + LinearSVC. Research lab,… | [open](https://shale-ember-delta-kite.grok.me/) |
| [IIT-ROPAR-GENAI-FOUNDATIONS](https://github.com/Rishabh-bgp/IIT-ROPAR-GENAI-FOUNDATIONS) | Free open-source Generative AI foundations ebooks (2026) covering Claude, Grok, Gemini, Cursor, OpenAI and more —… | — |
| [iris-classification](https://github.com/Rishabh-bgp/iris-classification) | Iris flower classification in Python: scikit-learn model comparison, tuning and evaluation, FastAPI /predict API,… | [open](https://rishabh-bgp.github.io/iris-classification/) |
| [kbc-game](https://github.com/Rishabh-bgp/kbc-game) | Kaun Banega Crorepati (KBC) quiz game for the terminal in Python: 16-question prize ladder, safe levels and 4… | — |
| [knn-classifier](https://github.com/Rishabh-bgp/knn-classifier) | Simple K-Nearest Neighbors classifier on the classic Iris dataset using scikit-learn. Loads data, trains the model,… | — |
| [linear-regression-model-](https://github.com/Rishabh-bgp/linear-regression-model-) | Supervised linear regression on the scikit-learn diabetes dataset. A single feature (BMI) is used to predict… | — |
| [logistic-regression](https://github.com/Rishabh-bgp/logistic-regression) | This graduate capstone applies multi-class logistic regression to the Iris dataset. It includes EDA, stratified… | — |
| [logistics-website-capstone](https://github.com/Rishabh-bgp/logistics-website-capstone) | Logistics website capstone: Kargonaut Logistics, a premium freight site mixing claymorphism, glassmorphism and… | [open](https://rishabh-bgp.github.io/logistics-website-capstone/) |
| [lovelight-leap](https://github.com/Rishabh-bgp/lovelight-leap) | 💖 Lovelight Leap: a love-themed 2D platformer in vanilla JS canvas. 4 worlds, a boss you cheer up, original… | [open](https://rishabh-bgp.github.io/lovelight-leap/) |
| [machine-learning-part-1](https://github.com/Rishabh-bgp/machine-learning-part-1) | Machine learning in Python with scikit-learn: heart disease classification and medical insurance cost regression… | — |
| [Meeting-of-Machines-Consumer-Agents-Seller-Agents-and-Hidden-Fulfilment-Risk-in-Online-Retail](https://github.com/Rishabh-bgp/Meeting-of-Machines-Consumer-Agents-Seller-Agents-and-Hidden-Fulfilment-Risk-in-Online-Retail) | Agentic commerce lets shopping and seller agents place orders without showing operational truth. This IS case argues… | — |
| [morocco-city-aware-load-forecasting](https://github.com/Rishabh-bgp/morocco-city-aware-load-forecasting) | City-aware short-term load forecasting and peak detection on high-resolution Moroccan smart-meter data (5 zones).… | — |
| [NIELIT-DATA-SCIENCE](https://github.com/Rishabh-bgp/NIELIT-DATA-SCIENCE) | Hands-on NumPy, Pandas, and Matplotlib Jupyter notebooks for the NIELIT Data Science curriculum — practical,… | — |
| [NIELIT-MACHINE-LEARNING-PROJECTS](https://github.com/Rishabh-bgp/NIELIT-MACHINE-LEARNING-PROJECTS) | Nineteen end-to-end machine learning projects: classification, regression, clustering, and recommendation, with… | — |
| [pan-cancer-classification](https://github.com/Rishabh-bgp/pan-cancer-classification) | Leakage, equivalence, conformal reliability and data efficiency on the UCI TCGA Pan-Cancer RNA-Seq dataset — IIT… | — |
| [Predicting-Hot-Events-in-the-Early-Period-through-Bayesian-Model-for-Social-Networks](https://github.com/Rishabh-bgp/Predicting-Hot-Events-in-the-Early-Period-through-Bayesian-Model-for-Social-Networks) | This notebook details the implementation and evaluation of a Bayesian perspective Early stage Event Prediction… | — |
| [prediction-as-power](https://github.com/Rishabh-bgp/prediction-as-power) | Laboratory and working paper on prediction as power in European electricity markets. A DE-like hourly simulator… | — |
| [snakes-and-ladders](https://github.com/Rishabh-bgp/snakes-and-ladders) | 🐍🪜 Original Snakes & Ladders browser game: hand-drawn SVG snakes and ladders, 3D dice, 2-4 humans or bots, sound,… | [open](https://rishabh-bgp.github.io/snakes-and-ladders/) |
| [spam-scan](https://github.com/Rishabh-bgp/spam-scan) | Explainable spam, phishing & Indian-scam detector for SMS/email (English, Hindi, Hinglish): TF-IDF + Logistic… | [open](https://spam-scan.onrender.com) |
| [vedic-math-hybrid-kt](https://github.com/Rishabh-bgp/vedic-math-hybrid-kt) | Hybrid Vedic Math AI: rule-based sutras (Urdhva-Tiryagbhyam, Nikhilam, Yavadunam) plus RF classifier that cleans… | — |
| [wind-turbine-power-model](https://github.com/Rishabh-bgp/wind-turbine-power-model) | Single-turbine power curves + wind-farm simulation. Weibull wind stats, hourly NASA-style speed data, and… | — |
| [zoo-website-capstone](https://github.com/Rishabh-bgp/zoo-website-capstone) | Capstone project: a fictional zoo website built twice — a beginner-style simple version and a cinematic advanced… | [open](https://rishabh-bgp.github.io/zoo-website-capstone/) |
