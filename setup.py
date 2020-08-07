import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymat", # Replace with your own username
    version="0.0.1",
    author="baely",
    author_email="me@baely.dev",
    description="A mathematics matrix module for Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/baely/matrix",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)