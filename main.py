# main.py

import os
from src.data_processing import read_csv, read_svg
from src.bezier_fitting import fit_bezier_curves
from src.regularization import regularize_paths, detect_symmetry, complete_shapes
from src.visualization import save_as_svg, save_as_csv

def main():
    data_dir = 'data/testCases'
    output_dir = 'data/output'
    
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            csv_path = os.path.join(data_dir, filename)
            output_svg = os.path.join(output_dir, filename.replace('.csv', '.svg'))
            output_csv = os.path.join(output_dir, filename.replace('.csv', '_processed.csv'))
            
            paths_XYs = read_csv(csv_path)
            bezier_paths = fit_bezier_curves(paths_XYs)
            bezier_paths = regularize_paths(bezier_paths)
            bezier_paths = detect_symmetry(bezier_paths)
            bezier_paths = complete_shapes(bezier_paths)
            
            save_as_svg(bezier_paths, output_svg)
            save_as_csv(bezier_paths, output_csv)
            print(f"Processed {filename} and saved output to {output_svg} and {output_csv}")

if __name__ == '__main__':
    main()
