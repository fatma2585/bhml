from setuptools import setup, find_packages, Extension
import pathlib

# The text of the README file
with open('README.md', 'r', encoding='utf-8') as f:
    README = f.read()

setup(
    name='bhml',
    version="1.1.0",
    packages=find_packages(),
    install_requires=["numpy>=1.24.4", "scipy>=1.11.1", "astropy>=5.3.3", "matplotlib>=3.6.1"],
    description="This package is used to constrain huge Astronomical catalogs/surveys to subsets based on redshift ranges to study the evolution of celestial objects.",
    author='Fatma Shaban',
    author_email='fatmashaban0@gmail.com',
    url='https://github.com/fatma2585/bhml',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT",  # Changed from "LICENSE"
    include_package_data=True,  # Fixed typo
    long_description=README,
    long_description_content_type='text/markdown'
)
