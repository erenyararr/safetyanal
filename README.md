# Safety Report Analyzer

Analyze aviation safety PDF reports with GPT, classify per TC/SMS, and save/search in a local SQLite DB. Export reports as PDF or Excel.

## Features
- Analysis methods: Five Whys, Fishbone, Bowtie, Fault Tree
- Auto-Classify: occurrence + risk severity/probability
- Local DB with latest-only versioning and similarity search
- Export: PDF (ReportLab) and Excel/CSV (pandas/openpyxl or xlsxwriter)
- English and Français output

## Quick Start (Windows)
1. Create a virtual environment and install deps:
   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\activate
   pip install -U pip
   pip install pymupdf openai numpy reportlab pandas openpyxl xlsxwriter
   ```
2. Add your OpenAI API key in `config.py`:
   ```python
   API_KEY = "sk-..."
   ```
3. Run the app:
   ```powershell
   python gui.py
   ```
   Or use `run.bat` for console-less start.

## Privacy
- `.gitignore` excludes `config.py`, `.env`, and `safety_reports.db` to keep secrets and local data private.

## License
MIT
