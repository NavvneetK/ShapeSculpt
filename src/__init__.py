# src/__init__.py

# Import functions from submodules to make them available at the package level
from .data_processing import read_csv, read_svg
from .bezier_fitting import fit_bezier_curves
from .visualization import save_as_svg, save_as_csv

# Optionally, you can include initialization code here
print("Initializing the src package")

# Define the package's public API
__all__ = [
    'read_csv',
    'read_svg',
    'fit_bezier_curves',
    'save_as_svg',
    'save_as_csv'
]

# Optionally, you can add more initialization logic if needed
# For example, setting up logging or configuration
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("src package initialized")


