# src/regularization.py

import numpy as np
from scipy.signal import savgol_filter

def regularize_paths(bezier_paths):
    regularized_paths = []
    for path in bezier_paths:
        smoothed_path = smooth_path(path)
        regularized_paths.append(smoothed_path)
    return regularized_paths

def smooth_path(path, window_len=11, polyorder=2):
    x = path[:, 0]
    y = path[:, 1]
    x_smooth = savgol_filter(x, window_len, polyorder)
    y_smooth = savgol_filter(y, window_len, polyorder)
    return np.vstack((x_smooth, y_smooth)).T


# src/regularization.py

from scipy.spatial.distance import cdist

def detect_symmetry(bezier_paths):
    symmetrical_paths = []
    for path in bezier_paths:
        if is_symmetric(path):
            symmetrical_paths.append(path)
        else:
            # Handle non-symmetric paths
            pass
    return symmetrical_paths

def is_symmetric(path, tolerance=1e-5):
    mid_point = np.mean(path, axis=0)
    mirrored_path = np.copy(path)
    mirrored_path[:, 0] = 2 * mid_point[0] - mirrored_path[:, 0]
    distance = cdist(path, mirrored_path)
    return np.all(distance < tolerance)


# src/regularization.py

from scipy.interpolate import interp1d
import numpy as np

def complete_shapes(bezier_paths):
    completed_paths = []
    for path in bezier_paths:
        completed_path = fill_gaps(path)
        completed_paths.append(completed_path)
    return completed_paths

def fill_gaps(path):
    x = path[:, 0]
    y = path[:, 1]

    # Identify gaps (simple example: assume gaps are NaN or very large distances)
    valid = ~np.isnan(x) & ~np.isnan(y)
    x_valid = x[valid]
    y_valid = y[valid]

    # Interpolation
    if len(x_valid) > 1:
        interp_func = interp1d(x_valid, y_valid, kind='linear', fill_value='extrapolate')
        x_full = np.linspace(min(x_valid), max(x_valid), num=len(x))
        y_full = interp_func(x_full)
        return np.vstack((x_full, y_full)).T
    else:
        return path  # Return original if not enough data for interpolation
