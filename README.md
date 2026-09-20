# PyAnalytics
PyAnalytics is a modular Python-based data processing and analytics tool that supports
CSV and JSON data processing, data cleaning, statistical analysis, report generation, and
REST API integration.

# Features
-CSV file parsing
-JSON file parsing
-File validation
-Error handling
-Command-line interface
-Modular project structure
-Basic automated testing
-Data validation
-Missing value handling
-Duplicate removal
-Numeric type conversion
-Statistical analysis
-Group-by analysis
-Markdown report generation
-FastAPI REST API
-Swagger/OpenAPI documentation
-Interactive web dashboard
-CSV and JSON file upload


# Project Structure
PyAnalytics/
 |
 |---main.py
 |
 |---parsers/
 |   |
 |   |---__init__.py
 |   |---csv_parser.py
 |   |---json_parser.py
 |
 |---validators/
 |   |
 |   |---__init__.py
 |   |---input_validator.py
 |
 |---tests/
 |   |
 |   |---__init__.py
 |   |---test_parser.py
 |
 |---sample_data/
 |   |
 |   |---students.csv
 |   |---students.json
 |
 |---.gitignore
 |---README.md
 |---requirements.text


# Usage
PyAnalytics can be used from command line to read CSV and JSON files.

### Read a CSV file
```bash
python cli_main.py --file sample_data/students.csv
```
### Read a JSON file

python cli_main.py --file sample_data/students.json

### API Endpoints
-`GET /`-API welcome message
-`GET /health`-API health check
-`POST /analyze`-Analyze json data
-`POST /upload`-Upload and analyze CSV/JSON files

### API Documentation
After starting server
```bash
python -m uvicorn api_main:app --reload
```
# Testing
PyAnalytics uses `pytest` for automated testing.
### Install pytest
```bash
pip install pytest
```

