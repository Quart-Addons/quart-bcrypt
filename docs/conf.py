# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Quart Bcrypt'
copyright = '2022, Chris Rood'
author = 'Chris Rood'
release = '0.0.6'
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', 'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

master_doc = 'index'
source_suffix = '.rst'

autodoc_preserve_defaults = True

autodoc_default_options = {
    'member-order': 'bysource',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
htmlhelp_basename = 'QuartBcryptdoc'

html_logo = "_static/logo_short.png"

html_sidebars = {
    "index": [],
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "external_links": [
        {"name": "Source code", "url": "https://github.com/Quart-Addons/quart-bcrypt"},
        {"name": "Issues", "url": "https://github.com/Quart-Addons/quart-bcrypt/issues"},
    ],
    "icon_links": [
        {
            "name": "Quart Add-Ons",
            "url": "https://github.com/Quart-Addons",
            "icon": "fab fa-github",
        },
        {
            "name": "Quart",
            "url": "https://quart.palletsprojects.com/",
            "icon": "_static/quart.png",
            "type": "local",
        },
    ],
}

latex_documents = [
  ('index', 'Quart-Uploads.tex', 'Quart-Uploads Documentation',
   'Chris Rood', 'manual'),
]

latex_documents = [
  ('index', 'Quart-Uploads.tex', 'Quart-Uploads Documentation',
   'Chris Rood', 'manual'),
]