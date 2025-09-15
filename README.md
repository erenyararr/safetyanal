# Safety Report Analyzer

Analyze aviation safety PDF reports with GPT, classify per TC/SMS, and save/search in a local SQLite DB. Export reports as PDF or Excel.

## Features
- Analysis methods: Five Whys, Fishbone, Bowtie, Fault Tree
- Auto-Classify: occurrence + risk severity/probability
- Local DB with latest-only versioning and similarity search
- Export: PDF (ReportLab) and Excel/CSV (pandas/openpyxl or xlsxwriter)
- English and Français output

## Quick Start

### Option 1: Automated Setup (Recommended)
```bash
# Run the setup script (works on Windows, Mac, Linux)
python setup.py
```

### Option 2: Manual Setup

#### Windows:
1. Run `install.bat` or manually:
   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\activate
   pip install -U pip
   pip install -r requirements.txt
   ```

#### Linux/Mac:
1. Run `install.sh` or manually:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -U pip
   pip install -r requirements.txt
   ```

### Configuration:
2. Copy and configure your API key:
   ```bash
   cp config.example.py config.py
   # Edit config.py and add your OpenAI API key
   ```

### Running the Application:

#### Desktop GUI (Tkinter):
- **Windows:** Double-click `run.bat` or run `python gui.py`
- **Linux/Mac:** `python gui.py`

#### Web Interface (Flask):
- **All platforms:** `python start_web.py`
- Then open http://localhost:5000 in your browser

## Privacy
- `.gitignore` excludes `config.py`, `.env`, and `safety_reports.db` to keep secrets and local data private.

## License
MIT
