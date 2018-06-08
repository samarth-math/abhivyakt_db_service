from api import ROOT
import os

# Errors
END_OF_CONTENT = "Oops, looks like we are out of content"


# Limits
API_LIMIT = 50


# File paths
CONFIG_FOLDER = os.path.join(ROOT, 'configurations')
FEATURED_FILE_PATH = os.path.join(CONFIG_FOLDER, 'featuredContent')
