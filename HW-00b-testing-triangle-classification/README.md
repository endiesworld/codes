# Triangle Classification Project

## Description

This project provides a Python implementation for classifying triangles based on the lengths of their sides. It includes a CLI for user interaction and automated tests using the pytest framework.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Testing](#testing)

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd HW-00b-testing-triangle-classification
   ```
2. **Install dependencies using [uv](https://github.com/astral-sh/uv):**
   ```sh
   uv install
   ```
   Alternatively, use pip:
   ```sh
   pip install -r requirements.txt
   ```
   *(Dependencies are listed in `pyproject.toml`)*

## Usage

To classify a triangle, run the main script:

```sh
python src/main.py
```

You will be prompted to enter the lengths of the three sides. The program will output the classification.

## Features

- Classifies triangles as Equilateral, Isosceles, Scalene, and detects Right triangles.
- Handles invalid inputs and non-triangles.
- CLI for interactive use.
- Automated tests with pytest.

## Configuration

- Python version: 3.12 or higher (see `.python-version`)
- Dependencies managed via `pyproject.toml`
- No additional configuration required for basic usage.

## Testing

Tests are written using the pytest framework. To run all tests:

```sh
pytest
```

Test files are located in the `test/` directory. Ensure all dependencies are installed before running tests.

