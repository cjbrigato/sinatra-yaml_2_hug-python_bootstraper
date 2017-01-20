#!/usr/bin/env python3
import hug

import bootstrap
import config

# -*- coding: utf-8 -*-

API = hug.API(__name__)
bootstrap.bootstrap(config.models,API)

if __name__ == '__main__':
    API.http.serve()