# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('_extensions'))


# -- Project information -----------------------------------------------------

project = 'GDAL'
copyright = '1998-2019'
author = 'Frank Warmerdam, Even Rouault, and others'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'breathe',
    'configoptions',
    'redirects'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme_path = ['.']
html_theme = 'gdal_rtd'

html_context = {
  'display_github': True,
  'github_user': 'hobu',
  'github_repo': 'GDAL',
  'github_version': '/doc-sprint/gdal/doc/source/'
}

html_theme_options = {
        'canonical_url': 'https://gdal.dev',
    'analytics_id': '',  #  Provided by Google in your dashboard
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    #'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    #'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

html_logo = '../images/gdalicon.png'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).

author_frankw = 'Frank Warmerdam <warmerdam@pobox.com>'
author_silker = 'Silke Reimer <silke@intevation.de>'
author_mikhailg = 'Mikhail Gusev <gusevmihs@gmail.com>'
author_dmitryb = 'Dmitry Baryshnikov <polimax@mail.ru>'
author_evenr = 'Even Rouault <even.rouault@spatialys.com>'

man_pages = [
    (
        'programs/gdalinfo',
        'gdalinfo',
        u'Lists various information about a GDAL supported raster dataset',
        [author_frankw],
        1
    ),
    (
        'programs/gdal_translate',
        'gdal_translate',
        u'Converts raster data between different formats.',
        [author_frankw, author_silker],
        1
    ),
    (
        'programs/gdaladdo',
        'gdaladdo',
        u'Builds or rebuilds overview images.',
        [author_frankw, author_silker],
        1
    ),
    (
        'programs/gdalwarp',
        'gdalwarp',
        u'Image reprojection and warping utility.',
        [author_frankw, author_silker],
        1
    ),
    (
        'programs/gdaltindex',
        'gdaltindex',
        u'Builds a shapefile as a raster tileindex.',
        [author_frankw],
        1
    ),
    (
        'programs/gdalbuildvrt',
        'gdalbuildvrt',
        u'Builds a VRT from a list of datasets.',
        [author_evenr],
        1
    ),
    (
        'programs/gdal_contour',
        'gdal_contour',
        u'Builds vector contour lines from a raster elevation model.',
        [author_frankw, author_silker],
        1
    ),
    (
        'programs/gdaldem',
        'gdaldem',
        u'Tools to analyze and visualize DEMs.',
        ['Matthew Perry <perrygeo@gmail.com>', author_evenr, 'Howard Butler <hobu.inc@gmail.com>', 'Chris Yesson <chris.yesson@ioz.ac.uk>'],
        1
    ),
    (
        'programs/rgb2pct',
        'rgb2pct',
        u'Convert a 24bit RGB image to 8bit paletted.',
        [author_frankw],
        1
    ),
    (
        'programs/pct2rgb',
        'pct2rgb',
        u'Convert an 8bit paletted image to 24bit RGB.',
        [author_frankw, author_silker],
        1
    ),
    (
        'programs/gdal_merge',
        'gdal_merge',
        u'Mosaics a set of images.',
        [author_frankw, author_silker],
        1
    ),
    (
        'programs/gdal2tiles',
        'gdal2tiles',
        u'Generates directory with TMS tiles, KMLs and simple web viewers.',
        ['Klokan Petr Pridal <klokan@klokan.cz>'],
        1
    ),
    (
        'programs/gdal_rasterize',
        'gdal_rasterize',
        u'Burns vector geometries into a raster.',
        [author_frankw],
        1
    ),
    (
        'programs/gdaltransform',
        'gdaltransform',
        u'Transforms coordinates.',
        [author_frankw, "Jan Hartmann <j.l.h.hartmann@uva.nl>"],
        1
    ),
    (
        'programs/nearblack',
        'nearblack',
        u'Convert nearly black/white borders to black.',
        [author_frankw],
        1
    ),
    (
        'programs/gdal_retile',
        'gdal_retile',
        u'Retiles a set of tiles and/or build tiled pyramid levels.',
        ['Christian Mueller <christian.mueller@nvoe.at>'],
        1
    ),
    (
        'programs/gdal_grid',
        'gdal_grid',
        u'Creates regular grid from the scattered data.',
        ['Andrey Kiselev <dron@ak4719.spb.edu>'],
        1
    ),
    (
        'programs/gdal_proximity',
        'gdal_proximity',
        u'Produces a raster proximity map.',
        [author_evenr],
        1
    ),
    (
        'programs/gnmmanage',
        'gnmmanage',
        u'Manages networks',
        [author_mikhailg, author_dmitryb],
        1
    ),
    (
        'programs/gnmanalyse',
        'gnmanalyse',
        u'Analyses networks',
        [author_mikhailg, author_dmitryb],
        1
    ),
]

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Breathe -------------------------------------------------

# Setup the breathe extension
breathe_projects = {
    "api": "../build/xml"
}
breathe_default_project = "api"

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'

import redirects
redirect_files = redirects.gather_redirects()

