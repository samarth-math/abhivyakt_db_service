from flask import Blueprint
routes = Blueprint('routes', __name__)

from .muhavare import *
from .kavita import *
from .kahani import *
from .dictionary import *
from .dohe import *
from .manualtest import *