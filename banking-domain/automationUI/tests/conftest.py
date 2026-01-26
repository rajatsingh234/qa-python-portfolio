import pytest
import allure
from automationUI.utils.browser_factory import get_driver

@pytest.fixture
def setup(request):
    driver = get_driver()
    yield driver

    #Take screenshot only if test failed
    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
    driver.quit()

#pytest hook to get test result status
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)