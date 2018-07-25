#!/usr/bin/env bash
set -e

python setup.py sdist bdist_wheel --universal
twine upload -r test dist/*
