# Diff generator

## Hexlet tests and linter status

[![Actions Status](https://github.com/anastasiia-avdeeva/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/anastasiia-avdeeva/python-project-50/actions)
[![check code](https://github.com/anastasiia-avdeeva/python-project-50/actions/workflows/check_code.yml/badge.svg)](https://github.com/anastasiia-avdeeva/python-project-50/actions/workflows/check_code.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-50)

___

## About the project

___

### Demo

Example of CLI usage:
[![asciicast](https://asciinema.org/a/qh6hHZkU4DRdcWHq.svg)](https://asciinema.org/a/qh6hHZkU4DRdcWHq)
[![asciicast](https://asciinema.org/a/PgkbQxqF1zWqcU5Y.svg)](https://asciinema.org/a/PgkbQxqF1zWqcU5Y)
[![asciicast](https://asciinema.org/a/n5TVzifyzsH12iKJsvg)](https://asciinema.org/a/n5TVzifyzsH12iKJ)

___

### Links

This project was built using these tools:

| Tool                                                                   | Description                                                             |
|------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                       | "An extremely fast Python package and project manager, written in Rust" |
| [Pytest](https://pytest.org)                                           | "A mature full-featured Python testing tool"                            |
| [ruff](https://docs.astral.sh/ruff/)                                   | "An extremely fast Python linter and code formatter, written in Rust"   |

___

### Requirements

* Python ≥ 3.14
* uv package manager

### Installation and Setup

1. Clone repository

    ```bash
    git clone git@github.com:anastasiia-avdeeva/python-project-50.git
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
