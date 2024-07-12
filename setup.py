from setuptools import setup, find_packages, Extension
import pathlib

# The text of the README file
README = ("README.md").read_text()


setup(
    name='bhml',
    version="1.0.0",
    packages=find_packages(),
    install_requires=["numpy>=1.24.4", "scipy>=1.11.1", "astropy>=5.3.3", "matplotlib>=3.6.1"],
,  # Add your dependencies here
    long_description=README,
    description="This package is used to constrain huge Astronomical catalogs/surveys to subsets based on redshift ranges to study the evolution of celestial objects.",      
    #Constrain the evolution of a complete catalog based on redshift ranges and other parameters ranges (e.g. mass, luminosity .....)",
    author='Fatma Shaban',
    author_email='fatmashaban0@gmail.com',
    url='https://github.com/fatma2585/bhml',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System:: OS Independent',
    ],
    python_requires='>=3.6',
    license="LICENSE",
    incluce_package_data=True,
    

)
