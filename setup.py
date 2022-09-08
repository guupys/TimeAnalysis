""" Minimal setup file """

from setuptools import setup, find_packages

base_packages = [
    "numpy>=1.20.0",
    "pandas>=1.1.5",
    "tqdm>=4.41.1",
]

use_packages = [
    "tensorflow",
    "tensorflow_hub",
    "tensorflow_text"
]

packages = base_packages + use_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="time-analysis",
    packages=find_packages(exclude=["notebooks", "docs"]),
    version="0.1.0",
    author="guupys",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guupys/Time-Analysis/",
    keywords="time series",
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=base_packages,
    #extras_require={},
    python_requires='>=3.8',
)
