#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `demopytest` package."""

import pytest

from click.testing import CliRunner

from demopytest import demopytest
from demopytest import cli


# ---------- Default ---------- # 모든 테스트 메소드는 test_로 시작해야 함.
def test_demo_method():
    assert demopytest.demo_method(1) == 2


# ---------- Raise ---------- # ImportError가 발생할시 테스트 통과
def test_demo_raise():
    with pytest.raises(ImportError):
        demopytest.demo_raise()


# ---------- Fixture ---------- # get_status를 모듈화시켜 다른 테스트 메소드에서도 사용 가능하게 함.
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


# ---------- Multiple ---------- # 여러 테스트를 하나로 묶고 싶으면 Class 사용
class TestTest(object):

    @pytest.fixture()
    def get_instance(self):
        demo_instance = demopytest.demo_class()
        return demo_instance

    def test_demo_plus_10(self, get_instance):
        assert get_instance.demo_plus_10(1) == 11

    def test_demo_minus_10(self, get_instance):
        assert get_instance.demo_minus_10(1) == -9

# ---------- Mock ---------- # 웹 서버 또는 DB등 dependency가 필요할 때 Mock 사용
import requests
from demopytest import demomock
from unittest import mock

@mock.patch('requests.get') # requests.get 을 mocked_get으로 mocking patch함
def test_mock_method(mocked_get):
    mocked_get.return_value.status_code = 200 # requests.get의 return값의 status_code를 200으로 정의함.

    response = requests.get('http://www.yujinrobot.com')
    assert response.status_code == 200


@mock.patch('demopytest.demomock.get_mongodb')
@mock.patch.object(requests, 'get')
def test_mock_method(mocked_get, mock_get_mongodb): # 2개 이상의 mock을 할 때 정의 한 순서와 반대로 파라미터설정
    mocked_get.return_value.status_code = 200
    mock_get_mongodb.return_value = ['demo', 'test']

    response = requests.get('http://www.yujinrobot.com')
    # get_collections()를 실행하기 위한 조건으로 mongodb가 필요한데 위에 monkeypatch를 통해서
    # mongodb의 리턴값을 강제함으로 get_collections() 정상 작동함.
    value = demopytest.get_collections()

    assert response.status_code == 200
    assert value == 'demotest'

# ---------- Skip ---------- #
@pytest.mark.skip(reason="no way of currently testing this")
def test_skip_default():
    assert False


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
