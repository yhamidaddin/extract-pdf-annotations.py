### README for `extract-pdf-annotations.py`

```markdown
# extract-pdf-annotations.py

A Python script designed to extract text annotations from a PDF file and save them
into a CSV file. The output CSV contains five columns: 
- **Page Number**: The page number where the annotation appears.
- **Annotation Text**: The content of the annotation.
- **Author**: The author or creator of the annotation.
- **Creation Date**: The date when the annotation was created.
- **Modification Date**: The date when the annotation was last modified.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [License](#license)
- [Contact](#contact)

## Overview

The `extract-pdf-annotations.py` script allows you to extract all annotations
(e.g., comments, highlights, notes) from a PDF file and export them into a CSV
file for further analysis. This is useful when you need to review or analyze
comments made on a document without having to open the PDF itself.

## Installation

### Prerequisites

To run this script, you will need the `PyMuPDF` library, which provides functionality for working with PDFs.

### Step 1: Install PyMuPDF

You can install PyMuPDF via pip:

```bash
pip install PyMuPDF
```

### Step 2: Download the Script

You can download the Python script directly or clone the repository:

```bash
git clone https://github.com/yourusername/extract-pdf-annotations.git
```

### Step 3: Ensure Python Environment

Ensure that you are running this script in an environment where `PyMuPDF` is installed (either 
in a virtual environment or globally).

## Usage

To use the script, follow these steps:

1. Run the Python script:
   ```bash
   python extract-pdf-annotations.py
   ```

2. The script will prompt you to enter the full path of the PDF file you want to extract annotations from.

   ```bash
   Enter the full path of the PDF file: /path/to/your/pdf-file.pdf
   ```

3. The script will process the PDF file, extract all annotations, and create a CSV file in the same directory as the input file.

   Example:
   - Input file: `/path/to/your/pdf-file.pdf`
   - Output CSV file: `/path/to/your/pdf-file.csv`

4. The output CSV file will contain the following columns:
   - **Page Number**
   - **Annotation Text**
   - **Author**
   - **Creation Date**
   - **Modification Date**

### Example

```bash
Enter the full path of the PDF file: /home/user/document.pdf
Annotations have been written to: /home/user/document.csv
```

## Features

- **Extracts PDF annotations**: Captures text annotations (like comments and highlights) from all pages in the PDF.
- **Date conversion**: Converts the PDF-specific date format into a more human-readable format (with timezone handling).
- **Customizable CSV output**: The extracted annotations are saved into a CSV file with a clear structure.
- **Automatic file naming**: The output CSV file is automatically named after the input PDF, with `.csv` as the extension.

## Dependencies

This script requires the following Python library:

- **PyMuPDF (fitz)**: For parsing the PDF and extracting annotations.

To install the required dependencies, run:

```bash
pip install PyMuPDF
```

## License

This script is licensed under the **MIT License**. Feel free to modify and redistribute it under the terms of the license.

## Contact

For questions, feedback, or suggestions, please reach out to the author:

- **Author**: Yahya Hamidaddin
- **Email**: [yhamidaddin@open-alt.com](mailto:yhamidaddin@open-alt.com)

```
