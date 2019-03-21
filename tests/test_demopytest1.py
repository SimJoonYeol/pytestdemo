#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""터미널에서 파일 전체 테스트 실행을 보기위해 넣은 Pytest 파일"""

import pytest

from click.testing import CliRunner

from demopytest import demopytest
from demopytest import cli


def test_demo_method():
    assert True


