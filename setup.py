#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup


def read_(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="tinyec",
    version="0.4.1",
    packages=["tinyec"],
    author="Alex Moneger",
    author_email="alexmgr+github@gmail.com",
    description=(
        "A tiny library to perform arithmetic operations on elliptic curves in pure python"),
    license="GPLv3",
    keywords=["elliptic", "curves", "crypto", "tls", "ssl", "ecdhe", "diffie-hellman"],
    url="https://github.com/alexmgr/tinyec",
    download_url="https://github.com/alxchk/tinyec/archive/v0.4.tar.gz",
    long_description=read_("README.md"),
    test_suite="nose.collector",
    tests_require=["nose"])
