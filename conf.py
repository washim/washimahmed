import sphinx_typo3_theme
project = 'My Technical Blog'
copyright = '2021, Washim Ahmed'
author = 'Washim Ahmed'
extensions = [
    'sphinx_typo3_theme'
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'sphinx_typo3_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_show_sourcelink = False
html_theme_options = {
    'logo': 'logo.png',
    'logo_width': '319',
    'logo_height': '45',
    'github_repository': False
}