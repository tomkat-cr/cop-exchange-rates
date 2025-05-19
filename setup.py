from setuptools import setup

setup(
    name="cop-exchange-rates",
    version="1.1.0",
    author="Carlos J. Ramirez",
    author_email="cramirez@mediabros.com",
    description="Mediabros Currency Exchange API series / Colombian Pesos",
    packages=["cop-exchange-rates"],
    install_requires=["requests", "beautifulsoup4"],
    zip_safe=False
)
