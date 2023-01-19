from setuptools import setup

setup(
    name="cop-exchange-rates",
    version="1.0.0",
    author="Carlos J. Ramirez",
    author_email="cramirez@mediabros.com",
    description="A Python module to get COP (Colombian Pesos) to USD exchange rates",
    packages=["cop-exchange-rates"],
    install_requires=["requests", "beautifulsoup4", "a2wsgi"],
    zip_safe=False
)
