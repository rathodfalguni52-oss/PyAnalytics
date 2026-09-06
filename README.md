# PyAnalytics
PyAnalytics is a modular Python-based data ingestion tool that supports reading and 
validating CSV and JSON files through a command-line interface.

# Features
-CSV file parsing
-JSON file parsing
-File validation
-Error handling
-Command-line interface
-Modular project structure
-Basic automated testing

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
python main.py --file sample_data/students.csv

### Read a JSON file
```
python main.py --file sample_data/students.json

# Testing
PyAnalytics uses `pytest` for automated testing.
### Install pytest
```bash
pip install pytest
```

