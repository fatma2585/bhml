# bhml  (black hole mass-luminosity)
[![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)
[![Made with NumPy](https://img.shields.io/badge/Made%20with-NumPy-blue.svg)](https://numpy.org/)
[![Uses SciPy](https://img.shields.io/badge/Uses-SciPy-blue.svg)](https://www.scipy.org/)
[![PyPI version](https://badge.fury.io/py/bhml.svg)](https://pypi.org/project/bhml/)
[![image](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![image alt](https://github.com/fatma2585/bhml/blob/c070588a1d1c3b5a28d328fec10297dbd04f10ab/6-astronomersr.jpg)

## Introduction

This package is used to constrain huge Astronomical catalogs/surveys to subsets based on redshift ranges to study the evolution of objects and make subsets based on their masses or any parameter we want to study. Furthermore, we visualize these subsets with their mean points.


## Motivation

The mass_luminosity_function is a Python package for calculating the mass-luminosity function of quasars. The mass-luminosity function is an important statistical relationship between the masses of supermassive black holes (SMBHs) at galaxies' centers and the quasars' luminosities.


## Installation

The package is installable on Python 3.x and can be installed using:

```pip install bhml```

## Use Example and Description of Function

The mass_luminosity_function (SMBH) package includes some functions, to load the data and then calculate and plot the mass-luminosity function for quasars to know its evolution over cosmic time.
Here's an example of how to use it:

```
from bhml import entry
from bhml import classify
from bhml import submean
from bhml import visual

# from bhml import entry
# Load observational data. Add all the parameters you may need from the catalog
Usage:
data = entry(RA,DEC,Z,M,LB, Me,Le)   


# from bhml import classify
#classify the quasars into subsets with specific redshift bins, in each redshift bin you could make subsets of any parameter you want in our example we made it for masses
Z_ranges = [(0.0, 1.0), (1.0, 2.0), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
M_ranges = [(3, 7.5), (7.5, 8.5), (8.5, 9.5), (9.5, 11.5)]
Usage:
subsets = classify(data, Z_ranges, M_ranges) 

# from bhml import submean
Used in getting the mean point of all the parameters in each subset. This function gives an abstract vision of these subsets and enables us to study the relations between the parameters of the catalog abstractly. This function assumes a normal distribution for the subsets. parameter: is the index of the parameter in the data, we want to get its mean values (M, paramter=3).
Usage:
MZ = def submean(subsets,Z_ranges,M_ranges,parameter=4)


# from bhml import visual
This Function is used to visualize the evolution of any two parameters with the cosmic time. (MZ, BZ, MZe, BZe): the parameters we got their means from the previous function. grading: the smoothing factor.
Usage:
evolution = visual(Z_ranges, MZ, BZ, MZe, BZe, Zlimit=2.0, grading=300, kernal=3)

