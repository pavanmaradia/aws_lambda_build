"""
Package setup file

"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='aws_lambda_build',
    version='0.1',
    scripts=['collect_all'],
    author="Pavan Maradia",
    author_email="pavan.maradia@yahoo.com",
    description="AWS lambda builder. This module will build lambda zip file "
                "from microservice repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pavanmaradia/aws_lambda_build",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
