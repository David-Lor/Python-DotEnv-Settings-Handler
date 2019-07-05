#!/usr/bin/env python

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="dotenv-settings-handler",
    version="0.0.3",
    description="Settings handler to load settings from a DotEnv file or system env variables, "
                "using python-dotenv and pydantic.",
    author="David Lorenzo",
    url="https://github.com/David-Lor/Python-DotEnv-Settings-Handler",
    packages=("dotenv_settings_handler",),
    install_requires=("pydantic",),
    setup_requires=("pytest-runner",),
    tests_require=("pytest",),
    test_suite="pytest",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    long_description_content_type="text/markdown",
    long_description=long_description,
)
