# PDF Toolkit
### A small Python CLI tool for working with PDF files.

## Features

* Merge PDFs
* Split PDFs
* Extract specific pages
* Convert PDF pages to images
* Extract text from PDFs
* Interactive CLI
* `--help` and `--version`

## Reqirements

* Python 3.10+
* PyMuPDF
* Questionary

## Installation

git clone https://github.com/travletothefurureprogramming/PDF-Toolkit.git 
cd PDF-Toolkit 

python -m venv .venv 
.venv\Scripts\activate 

pip install -r requirements.txt

## Usage

* Run the toolkit:

python cli.py

* Show help:

python cli.py --help

* Show version:

python cli.py --version

## Status

### 🚧 Beta / Development

The core PDF operations are implemented. The next step is packaging the project as a standalone Windows executable and preparing the v1.0.0 release.

License

MIT License
