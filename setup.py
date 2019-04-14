import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hephaestus-Brewery-pkg",
    version="0.0.1",
    author="Oscar Hemken",
    author_email="oscar@bratdev.com",
    description="Hephaestus ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cervecerathesource/HephaestusBrewery",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
