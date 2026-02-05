"""
Kinetic Monte Carlo Simulation Package
=====================================

A package for performing Kinetic Monte Carlo simulations of atomic hopping
on lattice structures.

Functions:
    KMC1: 2D lattice hopping simulation
    KMC2: 2D lattice hopping simulation with complex transitions
"""

from .KMC import KMC1, KMC2

__version__ = "1.0.0"
__author__ = "Luca Berruezo and Hadrien Yim"
__email__ = "your.email@example.com"

__all__ = ["KMC1", "KMC2"]