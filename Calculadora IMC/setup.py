from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="calculadora_IMC",
    version="0.0.1",
    author="Ytalo Hanieri Brito",
    author_email="hanieri21@gmail.com",
    description="Calculadora de IMC simples",
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements
)