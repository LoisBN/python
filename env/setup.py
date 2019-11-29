from setuptools import setup, find_packages

setup(
    name="Python stuff",
    version="1.1",
    description="this is a simple place where i store my pythons stuff",
    long_description="this is essentially now mathematical function that i have to write for school but more useful stuff are coming soon",
    author="Lois Bibehe",
    author_email="lois@pixelogi.com",
    packages=find_packages(exclude=["tests"]),
    install_requires=['numpy'],
    test_require=["pytest"]
)