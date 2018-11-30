# -*- coding: utf-8 -*-
import json
import base64
from api.models.helpers import modelHelper as helper


def getMediaById(fid):
    fileAsHexString = base64.encodebytes(helper.getFileById(fid))
    return fileAsHexString
