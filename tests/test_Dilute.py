#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import
## batteries
import os
import sys
import shutil
import tempfile
import pytest
## 3rd party
import pandas as pd
## package
from pyTecanFluent import Dilute
from pyTecanFluent import Utils

# data dir
test_dir = os.path.join(os.path.dirname(__file__))
data_dir = os.path.join(test_dir, 'data')

# tests
def test_basic(script_runner, tmp_path):
    output_prefix = os.path.join(str(tmp_path), 'basic')
    conc_file = os.path.join(data_dir, 'conc_file1.txt')
    ret = script_runner.run('pyTecanFluent', 'dilute',
                            '--prefix', output_prefix, conc_file)
    assert ret.success

