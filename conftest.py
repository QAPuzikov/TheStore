import pytest

@pytest.fixture()
def pre_set():
    print("\n Start Test")
    yield
    print("\n Finish Test")