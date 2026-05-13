#!/usr/bin/env python3
"""Setup script for atexec-pro."""

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8").read()

setup(
    name="atexec-pro",
    version="1.0.0",
    author="",
    author_email="",
    description="Advanced ATExec implementation with TSCH/ATSVC support",
    long_description=read("README.MD"),
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=["libs"],
    package_data={
        "libs": ["powershells/*.ps1"],
    },
    scripts=["atexec-pro.py"],
    python_requires=">=3.6",
    install_requires=[
        "cmd2>=2.4.3",
        "impacket>=0.11.0",
        "pycryptodome>=3.20.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    keywords="atexec impacket tsch atsvc lateral-movement pentesting security",
)
