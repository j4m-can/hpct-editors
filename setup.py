#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

from setuptools import setup, find_packages


setup(
    name="hpcteditors",
    version="0.1.0",
    description="Configuration file editors for common applications in HPC.",
    license="Apache-2.0",
    packages=find_packages(where="lib", include=["hpcteditors*"]),
    package_dir={"": "lib"},
)
