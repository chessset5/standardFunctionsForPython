import os
import sys

# For files
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_path not in sys.path:
    sys.path.append(project_path)
    
    
# For Notebooks
# Get the notebook directory
notebook_path = os.path.abspath(".")

# Define the project path relative to the notebook's location
project_path = os.path.abspath(os.path.join(notebook_path, "..", ".."))

# Add to sys.path if not already present
if project_path not in sys.path:
    sys.path.append(project_path)
