# uni-ml-project

## Dev env setup

1. Clone the repository on local machine.
2. Create a virtual enviroment.
3. Install dependencies.

```bash
python -m venv venv

Set-ExecutionPolicy Unrestricted -Scope Process # Scope based, must be run each time cause windows is trash.

.\venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

## Structure

```
uni-ml-project/
├── .venv/
├── data/                  # Datasets
│   ├── raw/               # Original datasets
│   └── processed/         # Cleaned datasets
├── notebooks/             # Jupyter notebooks
├── outputs/               # Model outputs
│   ├── models/            # Model saves
│   ├── plots/             # Plots for visualisation
│   └── reports/           # Metrics
├── project_requirements   # Requirements handed by the professor.
├── requirements.txt       # All installed packages
├── README.md              # Project overview and instructions
└── .gitignore             # Files to ignore in git (if you use git)
```
