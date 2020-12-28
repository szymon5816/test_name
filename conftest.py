import pytest

@pytest.yield_fixture()
def setUp():
    print("Wykonane przed każdą funkcją")
    yield
    print("Wykonane po każdej funkcji")


@pytest.yield_fixture(scope="module")
def setOnece(browser,osType):
    if browser == "chrome":
        print("Test on chrome")
    elif browser == "firefox":
        print("test on firefox")
    else:
        "invalid value"

    if osType == "windows":
        print("Test on widnows")
    elif osType == "macos":
        print("test on macos")
    else:
        "invalid value"
    print("Executed before method")
    yield
    print("Executed After method")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")