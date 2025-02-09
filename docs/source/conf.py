# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../../.'))


project = 'T-COMMENTER'
copyright = '2025, ArtemXYZ (https://github.com/ArtemXYZ)'
author = 'ArtemXYZ (https://github.com/ArtemXYZ)'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Path to piccolo-theme
sys.path.append(os.path.abspath('D:/02_Работа/03_Работа_в_Python/01_Проекты/t-commenter/.venv/Lib/site-packages'))

html_theme = 'piccolo_theme'
html_static_path = ['_static']
