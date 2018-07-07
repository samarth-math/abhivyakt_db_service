from api import ROOT
import os
from enum import Enum

# Errors
class Error(Enum):
    END_OF_CONTENT = 'Oops, looks like we are out of content'
    COLLECTION_NONE = 'Collection object must not be null'

# Limits
API_LIMIT = 50


# File paths
CONFIG_FOLDER = os.path.join(ROOT, 'configurations')
FEATURED_FILE_PATH = os.path.join(CONFIG_FOLDER, 'featuredContent')

# Enums

class Art(Enum):
    dohe = 'dohe'
    kavita = 'kavita'
    kahani = 'kahani'
    muhavare = 'muhavare'