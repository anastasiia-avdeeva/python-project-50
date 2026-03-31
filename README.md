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

This project is a CLI tool that compares two configuration files and shows the difference between them.

The tool supports two input formats - JSON and YAML, and provides output in different formats:

* stylish (tree-like structure, default)
* plain (human-readable text)
* json (structured data for further processing)

The application parses files, builds a difference tree, and formats the result depending on the selected output format.
___

## Features

* Supports JSON and YAML input formats
* Provides multiple output formats (stylish, plain, json)
* Handles nested structures
* Designed as a CLI tool

___

## Demo

Example of CLI usage:

**Get help:**

[![asciicast](https://asciinema.org/a/ECRwmnw5l65ngeVh.svg)](https://asciinema.org/a/ECRwmnw5l65ngeVh)

**JSON files with flat structure and stylish output:**

[![asciicast](https://asciinema.org/a/7LtGvqGNDXcu7NJ8.svg)](https://asciinema.org/a/ECRwmnw5l65ngeVh)

**YAML files with flat structure and stylish output:**

[![asciicast](https://asciinema.org/a/vLms1YAcKp82PRjN.svg)](https://asciinema.org/a/vLms1YAcKp82PRjN)

**Files with nested structure and stylish output:**

[![asciicast](https://asciinema.org/a/n5TVzifyzsH12iKJ.svg)](https://asciinema.org/a/n5TVzifyzsH12iKJ)

**Different output formats:**

[![asciicast](https://asciinema.org/a/I3RqAIgg8b4FjH20.svg)](https://asciinema.org/a/I3RqAIgg8b4FjH20)
[![asciicast](https://asciinema.org/a/2hCFyaogCuF4JdV0.svg)](https://asciinema.org/a/2hCFyaogCuF4JdV0)
___

## Tools

This project was built using these tools:

| Tool                                                                   | Description                                                             |
|------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                       | "An extremely fast Python package and project manager, written in Rust" |
| [Pytest](https://pytest.org)                                           | "A mature full-featured Python testing tool"                            |
| [ruff](https://docs.astral.sh/ruff/)                                   | "An extremely fast Python linter and code formatter, written in Rust"   |

___

## Requirements

* Python ≥ 3.10
* uv package manager

## Installation

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

to reinstall the package:

```bash
make package-reinstall
```

## Usage

Compare two files:

```bash
gendiff <file1> <file2>
```

Specify output format:

```bash
gendiff -f <format> <file1> <file2>
````

Available formats:

* stylish (default)
* plain
* json

Examples:

```bash
gendiff file1.json file2.json
gendiff -f plain file1.yml file2.yml
gendiff -f json file1.json file2.json
```
