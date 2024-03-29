# Difference calculator

[![hexlet-check](https://github.com/Mr-Freewan/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Mr-Freewan/python-project-50/actions/workflows/hexlet-check.yml)
[![CI check](https://github.com/Mr-Freewan/python-project-50/actions/workflows/pyci.yaml/badge.svg)](https://github.com/Mr-Freewan/python-project-50/actions/workflows/pyci.yaml)
[![Maintainability](https://api.codeclimate.com/v1/badges/2d7b759fc7462a88dc10/maintainability)](https://codeclimate.com/github/Mr-Freewan/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2d7b759fc7462a88dc10/test_coverage)](https://codeclimate.com/github/Mr-Freewan/python-project-50/test_coverage)

### Description

CLI-based Python script for finding differences between two versions of JSON or YAML files.

The output type depends on the selected format:
- **stylish** - default
- **plain**
- **json**

### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://python-poetry.org/)                                        | "Python dependency management and packaging made easy"  |
| [flake8](https://flake8.pycqa.org/)                                         | "Your tool for style guide enforcement"                 |
| [pytest](https://docs.pytest.org/)                                          | "Easy to write small, readable tests"                   | 

---

### Installation with pip

    pip install git+https://github.com/Mr-Freewan/gendiff.git
    
Test running after installation:

    gendiff -h

    usage: gendiff [-h] [-f {stylish,json,plain}] first_file second_file

    Compares two configuration files and shows a difference.

    positional arguments:
    first_file            the path of the first file to compare
    second_file           the path of the second file to compare

    options:
    -h, --help            show this help message and exit
    -f {stylish,json,plain}, --format {stylish,json,plain}
                            set format of output. Default is stylish

### Building from repo and test running
Steps (see video below):

    git clone https://github.com/Mr-Freewan/python-project-50.git

    cd python-project-50/

    poetry install

    poetry build

Test running with poetry:

    poetry run gendiff

Test running without poetry:

    make package-install

    gendiff

[![asciicast](https://asciinema.org/a/AIGAJEtM2oUwNuhc7Mqj6dfax.svg)](https://asciinema.org/a/AIGAJEtM2oUwNuhc7Mqj6dfax)

---

### Demonstration:

---

Launch gendiff in stylish format:

    gendiff file1_.json file2_.json

or

    gendiff file1_.json file2_.json -f stylish    

Launch gendiff in json format:

    poetry run gendiff file1_.json file2_.json -f json

Launch gendiff in plain format:

    poetry run gendiff file1_.json file2_.json -f plain

### Flat JSON or YAML files

[![asciicast](https://asciinema.org/a/nHA0Wdog6Jh6gMAHvla62a96K.svg)](https://asciinema.org/a/nHA0Wdog6Jh6gMAHvla62a96K)

### Nested JSON or YAML files

[![asciicast](https://asciinema.org/a/NJT00vWpB4OlTUmbIX2ILYptV.svg)](https://asciinema.org/a/NJT00vWpB4OlTUmbIX2ILYptV)