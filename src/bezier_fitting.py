# src/bezier_fitting.py

from scipy.interpolate import splprep, splev
import numpy as np

def fit_bezier_curves(paths_XYs):
    bezier_paths = []
    for XYs in paths_XYs:
        for XY in XYs:
            tck, u = splprep([XY[:, 0], XY[:, 1]], s=0)
            unew = np.linspace(0, 1, 100)
            out = splev(unew, tck)
            bezier_paths.append(np.vstack(out).T)
    return bezier_paths
