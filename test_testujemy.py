import pytest


@pytest.yield_fixture()
def setUp():
    print("Setup ")
    yield
    print("After method")


def test_A(setOnece):

    print("Test A")

def test_B(setOnece):
    print("test B")