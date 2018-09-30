# -*- coding: utf-8 -*-
import json

from api.models.helpers import modelHelper as helper


def getMediaById(fid):
    return helper.getFileById(fid)
