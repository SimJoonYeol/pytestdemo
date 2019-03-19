#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `demopytest` package."""

import pytest

from click.testing import CliRunner

from demopytest import demopytest
from demopytest import cli


# ---------- Default ---------- #
def test_demo_method():
    assert demopytest.demo_method(1) == 2


# ---------- Raise ---------- #
def test_demo_raise():
    with pytest.raises(ImportError):
        demopytest.demo_raise()


# ---------- Fixture ---------- #
@pytest.fixture(scope="module")
# module : Run once per module
# session :	Run once per session
def get_status():
    import requests
    response = requests.get('http://www.naver.com')
    return response.status_code


def test_check_status(get_status):
    assert get_status == 200


def test_check_status_1(get_status):
    assert get_status == 200


# ---------- Multiple ---------- #
class TestDemo(object):

    @pytest.fixture()
    def get_instance(self):
        demo_instance = demopytest.demo_class()
        return demo_instance

    def test_demo_plus_10(self, get_instance):
        assert get_instance.demo_plus_10(1) == 11

    def test_demo_minus_10(self, get_instance):
        assert get_instance.demo_minus_10(1) == -9

# ---------- Mock ---------- #
import requests
from unittest import mock

@mock.patch('requests.get')
def test_mock_method(mocked_get):
    mocked_get.return_value.status_code = 200

    response = requests.get('http://www.yujinrobot.com')
    assert response.status_code == 200


@mock.patch('demopytest.demomock.get_mongodb')
@mock.patch.object(requests, 'get')
def test_mock_method(mocked_get, mock_get_mongodb):
    mocked_get.return_value.status_code = 200
    mock_get_mongodb.return_value = ['demo', 'test']

    response = requests.get('http://www.yujinrobot.com')
    value = demopytest.get_collections()

    assert response.status_code == 200
    assert value == 'demotest'

# ---------- Skip ---------- #
@pytest.mark.skip(reason="no way of currently testing this")
def test_skip_default():
    assert True


def test_skip_method():
    Invalid = True
    if Invalid:
        pytest.skip("unsupported configuration")


@pytest.mark.skipif(1 < 2, reason="1 is too small")
def test_skipif():
    assert True


minnum = pytest.mark.skipif(1 < 2, reason="1 is too small")

@minnum
def test_skipif():
    assert True

# ---------- Fail ---------- #
@pytest.mark.xfail
def test_fail_default():
    assert True

def test_fail_method():
    Invalid_config = True
    if Invalid_config:
        pytest.xfail("failing configuration (but should work)")

@pytest.mark.xfail(1 < 2, reason="1 is too small")
def test_failif():
    assert True

@pytest.mark.xfail(raises=IndexError) #indexerror로 실패한거는 넘긴다.
def test_hello7():
    x = []
    x[1] = 1
