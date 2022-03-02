"""
autouse - is like setUp in unittest
just set things for every test.
and by using scope, we can define in what scope this autouse will be work :)
default = function

scopes:
- function: if we define fixure IN test file (default) this will work. or if we define fixture in conftest.py
- class: 
- module: 
- package: 
- session: 

Basicly the simplest way is to use autouse with default value (with no defining scope :)
"""

import os
import pytest


def test_env_variable_one():
    env_variable = os.getenv('AAA_VARIABLE')
    assert env_variable == 'aaa_variable_name_dude'
