import os
import sys

# Add the directory containing KMC.py to the path
kmc_dir = os.path.abspath(os.path.join('..', '..'))
sys.path.insert(0, kmc_dir)

print(f"Added to sys.path: {kmc_dir}")
print(f"Files in KMC directory: {os.listdir(kmc_dir)}")

# Test import for debugging
try:
    import KMC
    print("✅ KMC module imported successfully during doc build")
except ImportError as e:
    print(f"❌ KMC import failed during doc build: {e}")

# -- Project information -----------------------------------------------------
project = 'Kinetic Monte Carlo Simulation'
copyright = '2025, Luca Berruezo and Hadrien Yim'
author = 'Luca Berruezo and Hadrien Yim'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Napoleon settings -------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = True

# -- Autodoc settings -------------------------------------------------------
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# Mock imports for problematic modules
autodoc_mock_imports = ['numba']

# Set master document
master_doc = 'index'