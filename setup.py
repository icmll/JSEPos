
import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsepos",
    version="0.0.1",
    author="yanglin",
    author_email="421168852@qq.com",
    description="just so easy pos system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
