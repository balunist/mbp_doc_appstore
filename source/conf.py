# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MapBoards Pro'
copyright = '2025, Icarus Soft Landings, LLC'
author = 'Icarus'
release = '2.815'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "classic"
# html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_with_keys": "true",
    "body_max_width": "none",
}
html_sidebars = {
    "**": ["globaltoc.html", "sourcelink.html", "searchbox.html"],
    "using/windows": ["windows-sidebar.html", "searchbox.html"],
}
html_copy_source = False
html_use_index = False

html_static_path = ['_static']
html_css_files = ["custom.css"]
html_show_sphinx = False
