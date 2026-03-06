# Configuration file for the Sphinx documentation builder.

import os
import re
import shutil
import sys

sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'Machine Learning for Electrochemical Image Processing'
copyright = '2026, Amir Omidvarnia, Forschungszentrum Jülich GmbH'
author = 'Amir Omidvarnia'
release = '1.0'
version = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinxcontrib.bibtex',
    'nbsphinx',
]

bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'unsrt'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# -- nbsphinx options --------------------------------------------------------

nbsphinx_execute = 'never'
nbsphinx_allow_errors = True

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo_tutorial.png'
html_css_files = ['custom.css']
html_show_sphinx = False

html_theme_options = {
    'navigation_depth': 4,
    'titles_only': False,
    'logo_only': False,
}

# -- Options for LaTeX output ------------------------------------------------
# Use pdflatex as the LaTeX engine
latex_engine = 'pdflatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'figure_align': 'htbp',
    'extraclassoptions': 'openany,oneside',
    'preamble': r'''
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=blue,
}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\leftmark}
\fancyfoot[C]{\thepage}
% All figures live in docs/figures, which is two levels
% above the LaTeX build directory docs/_build/latex.
% Make LaTeX search that folder by default.
\graphicspath{{../../figures/}}
''',
}

latex_documents = [
    (
        'index',
        'ml_electrochemical_imaging.tex',
        'Machine Learning for Electrochemical Image Processing',
        r'Amir Omidvarnia',
        'manual',
    ),
]

latex_show_pagerefs = True
latex_show_urls = 'footnote'


def fix_latex_image_paths(app, exception):
    """After a LaTeX build, fix image paths and copy figures to docs/figures/.

    nbsphinx stores notebook output images in _build/doctrees/nbsphinx/ and
    generates relative image URIs that, when written into the LaTeX output,
    resolve incorrectly relative to the _build/latex/ directory.  This hook:

    1. Copies all PNG images from _build/doctrees/nbsphinx/ into docs/figures/.
    2. Rewrites every occurrence of the broken path prefix in the generated
       .tex file so that images are looked up in ../../figures/ (i.e. the
       docs/figures/ directory that lives two levels above _build/latex/).
    """
    if app.builder.name != 'latex' or exception:
        return

    srcdir = app.srcdir  # docs/
    outdir = app.outdir  # docs/_build/latex/
    nbsphinx_imgdir = os.path.join(app.doctreedir, 'nbsphinx')
    figures_dir = os.path.join(srcdir, 'figures')

    # Copy images to docs/figures/
    os.makedirs(figures_dir, exist_ok=True)
    if os.path.isdir(nbsphinx_imgdir):
        for fname in os.listdir(nbsphinx_imgdir):
            if fname.endswith('.png'):
                shutil.copy2(
                    os.path.join(nbsphinx_imgdir, fname),
                    os.path.join(figures_dir, fname),
                )

    # Fix paths in every generated .tex file
    broken_prefix = re.compile(r'\.\./[_]?build/doctrees/nbsphinx/')
    correct_prefix = '../../figures/'
    for fname in os.listdir(outdir):
        if not fname.endswith('.tex'):
            continue
        tex_path = os.path.join(outdir, fname)
        with open(tex_path, encoding='utf-8') as fh:
            content = fh.read()
        new_content = broken_prefix.sub(correct_prefix, content)
        if new_content != content:
            with open(tex_path, 'w', encoding='utf-8') as fh:
                fh.write(new_content)


def setup(app):
    app.connect('build-finished', fix_latex_image_paths)


latex_elements['maketitle'] = r'''
\begin{titlepage}
\centering
\vspace*{2cm}
{\Huge\bfseries Machine Learning for\\[0.5em] Electrochemical Image Processing\par}
\vspace{1.5cm}
{\Large A Hands-On Tutorial\par}
\vspace{2cm}
{\large\itshape Amir Omidvarnia\par}
\vspace{0.5cm}
{\normalsize Forschungszentrum Jülich\par}
\vfill
{\large DPG 2026 -- AKPIK Session\\Dresden, March 2026\par}
\vspace{1cm}
\end{titlepage}
'''
