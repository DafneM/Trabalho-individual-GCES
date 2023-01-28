# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

project = 'Metabase - Trabalho Individual GCES'
copyright = '2023, Dafne Moretti Moreira'
author = 'Dafne Moretti Moreira'
release = '1.0.0'

sys.path.insert(0, os.path.abspath('../src'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'breathe']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

breathe_projects = { "MyProject": "./xml/" }
breathe_default_project = "MyProject"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'piccolo_theme'
html_static_path = ['_static']
