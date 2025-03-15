import os
import sys

# For files
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)
    
    
# For Notebooks
# Get the notebook directory
notebook_path = os.path.abspath(".")

# Define the project path relative to the notebook's location
project_path = os.path.abspath(os.path.join(notebook_path, "..", ".."))

# Add to sys.path if not already present
if project_path not in sys.path:
    sys.path.append(project_path)
