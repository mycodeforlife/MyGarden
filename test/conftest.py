import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--testevn", action="store", default="Test", help="my option: Dev or Test or Staging"
    )


@pytest.fixture
def testevn(request):
    print("inside cmdopt")
    return request.config.getoption("--testevn")


@pytest.fixture
def readcsv(file):
    print("inside reading csv file")
    dataset=[]
    return dataset
