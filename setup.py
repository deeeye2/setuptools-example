from setuptools import setup, find_packages

setup(
    name="setuptools_example",
    version="1.0.0",
    description="A simple example package using setuptools",
    author="Your Name",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'setuptools-example=my_package.main:main'
        ]
    },
    install_requires=[],
)
