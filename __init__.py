# -*- coding: utf-8 -*-
"""
/***************************************************************************
 shapefileloader
                                 A QGIS plugin
 this plugin will display shapefile
                             -------------------
        begin                : 2020-01-26
        copyright            : (C) 2020 by KIPYEGON AMOS
        email                : kiptoamos@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load shapefileloader class from file shapefileloader.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .shapefile_loader import shapefileloader
    return shapefileloader(iface)
