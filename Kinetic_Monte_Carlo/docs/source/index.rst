.. filepath: d:\python cpde\Kinetic_Monte_Carlo\docs\index.rst
Kinetic Monte Carlo Simulation Documentation
===========================================

Welcome to the Kinetic Monte Carlo (KMC) simulation documentation. This package
provides efficient implementations for simulating hydrogen atom hopping on lattice
structures using the kinetic Monte Carlo method.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   examples
   theory

Features
--------

* **Fast Numba-accelerated simulations** - Up to 100x speedup over pure Python
* **2D and 3D lattice hopping** - Support for various lattice geometries
* **Multiple transition types** - Simple and complex hopping mechanisms
* **Well-documented API** - Comprehensive docstrings and examples

Quick Start
-----------

.. code-block:: python

   import numpy as np
   from KMC import KMC1, KMC2
   
   # Simple 2D simulation
   initial_position = [0, 0]
   trajectory = KMC1(initial_position, gamma_1=0.5, gamma_2=0.3, N=1000)
   
   # Plot trajectory
   import matplotlib.pyplot as plt
   plt.plot(trajectory[:, 0], trajectory[:, 1])
   plt.xlabel('X Position')
   plt.ylabel('Y Position')
   plt.title('2D Random Walk Trajectory')
   plt.show()

API Reference
=============

.. automodule:: 
   :members:
   :undoc-members:
   :show-inheritance:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`