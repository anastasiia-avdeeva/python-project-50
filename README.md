# Diff generator

### Hexlet tests and linter status:
[![Actions Status](https://github.com/anastasiia-avdeeva/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/anastasiia-avdeeva/python-project-50/actions)

___

## About the project

___

### Demo

Example of CLI usage:
[![asciicast](https://asciinema.org/a/qh6hHZkU4DRdcWHq.svg)](https://asciinema.org/a/qh6hHZkU4DRdcWHq)

___

### Links

This project was built using these tools:

| Tool                                                                   | Description                                             |
|------------------------------------------------------------------------|---------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                       | "An extremely fast Python package and project manager, written in Rust" |
| [Pytest](https://pytest.org)                                           | "A mature full-featured Python testing tool"            |
| [ruff](https://docs.astral.sh/ruff/)                                   | "An extremely fast Python linter and code formatter, written in Rust" |

___

### Requirements

* Python ≥ 3.14
* uv package manager

### Installation and Setup

1. Clone repository

    ```bash
    git clone git@github.com:anastasiia-avdeeva/python-project-49.git
    ```

2. Install dependencies

    ```bash
    make install
    ```

3. Build the package

    ```bash
    make build
    ```

4. Install the package locally

    ```bash
    make package-install
    ```

    to update the package:

    ```bash
    make package-reinstall
    ```

5. Run command

    ```bash
    gendiff <path_to_file1> <path_to_file2>
    ````
