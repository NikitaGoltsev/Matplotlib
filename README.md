# Matplotlib
Matplot_lib
#...
#### CONFIGURATION BEGINS HERE
# The default backend; one of GTK GTKAgg GTKCairo GTK3Agg GTK3Cairo
# MacOSX Qt4Agg Qt5Agg TkAgg WX WXAgg Agg Cairo GDK PS PDF SVG
# Template.
# You can also deploy your own backend outside of matplotlib by
# referring to the module name (which must be in the PYTHONPATH) as
# 'module://my_backend'.
#backend
: TkAgg
# If you are using the Qt4Agg backend, you can choose here
# to use the PyQt4 bindings or the newer PySide bindings to
# the underlying Qt4 toolkit.
#backend.qt4 : PyQt4
# PyQt4 | PySide
# Note that this can be overridden by the environment variable
# QT_API used by Enthought Tool Suite (ETS); valid values are
# "pyqt" and "pyside". The "pyqt" setting has the side effect of
# forcing the use of Version 2 API for QString and QVariant.
# The port to use for the web server in the WebAgg backend.
# webagg.port : 8888
# If webagg.port is unavailable, a number of other random ports will
# be tried until one that is available is found.
# webagg.port_retries : 50
# When True, open the webbrowser to the plot that is shown
# webagg.open_in_browser : True
# When True, the figures rendered in the nbagg backend are created with
# a transparent background.
# nbagg.transparent : False
# if you are running pyplot inside a GUI and your backend choice
# conflicts, we will automatically try to find a compatible one for
# you if backend_fallback is True
#backend_fallback: True

#toolbar
#timezone
: toolbar2
: UTC
# None | toolbar2 ("classic" is deprecated)
# a pytz timezone string, e.g., US/Central or Europe/Paris
# Where your matplotlib data lives if you installed to a non-default
# location. This is where the matplotlib fonts, bitmaps, etc reside
#datapath : /home/jdhunter/mpldata
### LINES
# See http://matplotlib.org/api/artist_api.html#module-matplotlib.lines for more
# information on line properties.
#lines.linewidth
: 1.5
# line width in points
#lines.linestyle
: -
# solid line
#lines.color
: C0
# has no affect on plot(); see axes.prop_cycle
#lines.marker
: None
# the default marker
#lines.markeredgewidth : 1.0
# the line width around the marker symbol
#lines.markersize : 6
# markersize, in points
#lines.dash_joinstyle : miter
# miter|round|bevel
#lines.dash_capstyle : butt
# butt|round|projecting
#lines.solid_joinstyle : miter
# miter|round|bevel
#lines.solid_capstyle : projecting
# butt|round|projecting
#lines.antialiased : True
# render lines in antialiased (no jaggies)
# The three standard dash patterns. These are scaled by the linewidth.
#lines.dashed_pattern : 2.8, 1.2
#lines.dashdot_pattern : 4.8, 1.2, 0.8, 1.2
#lines.dotted_pattern : 1.1, 1.1
#lines.scale_dashes : True
#markers.fillstyle: full # full|left|right|bottom|top|none
### PATCHES
# Patches are graphical objects that fill 2D space, like polygons or
# circles. See
# http://matplotlib.org/api/artist_api.html#module-matplotlib.patches
# information on patch properties
#patch.linewidth
: 1
# edge width in points.
#patch.facecolor
: C0
#patch.edgecolor
: black
# if forced, or patch is not filled
#patch.force_edgecolor : False
# True to always use edgecolor
#patch.antialiased
: True
# render patches in antialiased (no jaggies)
### HATCHES
#hatch.color
: k
#hatch.linewidth : 1.0
### Boxplot
#boxplot.notch
: False
#boxplot.vertical
: True
#boxplot.whiskers
: 1.5
#boxplot.bootstrap
: None
#boxplot.patchartist : False
#boxplot.showmeans
: False
#boxplot.showcaps
: True
#boxplot.showbox
: True
#boxplot.showfliers : True
#boxplot.meanline