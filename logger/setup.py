import setuptools


with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setuptools.setup(
    name="logger_utils",
    version="0.0.1",
    author="YegorKhodak",
    author_email="yegorkhodak@gmail.com",
    packages=["elastic_utils"],
    install_requires=requirements,
)