"""Area of interest shared by all pipeline steps (Genoa, ported from stared/warsaw-vibe-voxel).

World coords: EPSG:32632 (UTM 32N), x = easting, y = northing.
Grid coords: (i, j) continuous, i = column (east), j = row (south); cell (c, r) spans [c, c+1) x [r, r+1).
"""
import math

import numpy as np

CX, CY = 494736.87, 4917103.39  # Piazza De Ferrari, EPSG:32632 (UTM 32N, ETRS89); approximate, refine against OSM
THETA = math.radians(0.0)  # Genoa has no single street grid; axis-aligned
# 5600 x 3500 m: the Lanterna and the port in the west, Porto Antico, the old town, De Ferrari, Brignole in the east,
# Castelletto and the Righi funicular hills in the north.
W, D = 5600, 3500
I0, J0 = 2900, 1750  # grid position of the anchor
