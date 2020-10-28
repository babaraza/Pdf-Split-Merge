[![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/downloads/release/python-374/)

# PDF-Split-Merge

Utility script to extract pages from PDF files and then create  a new combined PDF file with the extracted pages.



### Workflow

- Script iterates over a given path and finds all pdfs
- Then it extracts a specific page from each pdf file
- Then creates a new file with all the extracted pages
- Optionally: Prints the final file
  - This code is currently commented out in the `py` file



### Usage

> Run script independently or import into other module

- Script will prompt user to put the path where the PDF files are located:
  - `Enter full path to folder with pdf files >`
- Script will then prompt user to indicate the page number to extract
  - `Enter the page number to extract >`
  - Example: Enter `1` to extract the first page from each PDF

