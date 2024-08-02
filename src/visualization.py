# src/visualization.py

import svgwrite

def save_as_svg(bezier_paths, svg_path):
    dwg = svgwrite.Drawing(svg_path, profile='tiny')
    for path in bezier_paths:
        dwg.add(dwg.polyline(path, stroke=svgwrite.rgb(0, 0, 0, '%'), fill='none'))
    dwg.save()


# src/visualization.py

import numpy as np

def save_as_csv(bezier_paths, csv_path):
    with open(csv_path, 'w') as f:
        for path in bezier_paths:
            for point in path:
                f.write(f"{point[0]},{point[1]}\n")
            f.write('\n')  # Separate different paths
