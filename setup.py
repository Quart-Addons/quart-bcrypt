from setuptools import setup

from src.quart_bcrypt import Bcrypt

setup(
    name="Quart-Bcrypt",
    install_requires=["quart", "bcrypt"]
)
