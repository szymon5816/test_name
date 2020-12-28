import pytest



@pytest.mark.run(order=2)
def test_B(setOnece, setUp):
    print("test B")

@pytest.mark.run(order=1)
def test_A(setOnece, setUp):
    print("Test A")


@pytest.mark.run(order=4)
def test_D(setOnece, setUp):
    print("Test D")


@pytest.mark.run(order=3)
def test_C(setOnece, setUp):
    print("test C")