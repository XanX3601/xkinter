from setuptools import setup, find_packages

setup(
    name="xkinter",
    version="0.0.0",
    description="python gui library built upon customtkinter",
    author="Thomas Petiteau",
    author_email="thomas.petiteau@outlook.com",
    url="https://github.com/XanX3601/xkinter",
    packages=find_packages(),
    install_requires = ['customtkinter==5.0.3']
)
