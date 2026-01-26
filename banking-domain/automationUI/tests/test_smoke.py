import pytest


@pytest.mark.skip
def test_open_parabank_homepage(setup):
    driver = setup
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    assert "ParaBank" in driver.title
