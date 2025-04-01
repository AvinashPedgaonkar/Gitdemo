import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # Specify the correct path to the chromedriver executable
        chrome_driver_path = "C:\\Python selenium\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe"

        # Create a Service object for chromedriver
        serv_obj = Service(chrome_driver_path)

        # Initialize the WebDriver using the service object
        driver = webdriver.Chrome(service=serv_obj)

        # Set an implicit wait
        driver.implicitly_wait(4)


    elif browser_name == "edge":
        edge_driver_path = "C:\\Python selenium\\edgedriver_win64 (1)\\msedgedriver.exe"
        serv_obj1 = Service(edge_driver_path)
        driver = webdriver.Edge(service=serv_obj1)

    # Open the desired webpage
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    # Maximize the browser window
    driver.maximize_window()

    # Assign the driver to the request object for use in the class
    request.cls.driver = driver

    # Yield allows teardown after tests complete
    yield

    # Teardown: Close the browser after tests
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


