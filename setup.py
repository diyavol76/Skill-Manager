"""Setup configuration for skill-manager."""

from setuptools import find_packages, setup

setup(
    name="skill-manager",
    version="0.1.0",
    description="A lightweight framework for building agents with pluggable skills.",
    author="diyavol76",
    python_requires=">=3.9",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[],
    extras_require={
        "dev": ["pytest>=7.0"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
