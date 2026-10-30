
# tests/e2e/conftest.py

import time

import pytest
import requests
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def fastapi_server():
    """
    Check that the FastAPI server running in Docker is available.
    """
    server_url = 'http://127.0.0.1:8000/'

    timeout = 30
    start_time = time.time()

    print("Checking FastAPI server...")

    while time.time() - start_time < timeout:
        try:
            response = requests.get(server_url, timeout=5)

            if response.status_code == 200:
                print("FastAPI server is up and running.")
                yield
                return

        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.Timeout:
            pass

        time.sleep(1)

    raise RuntimeError(
        "FastAPI server failed to respond within timeout period."
    )


@pytest.fixture(scope="session")
def playwright_instance_fixture():
    """
    Manage Playwright's lifecycle.
    """
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance_fixture):
    """
    Launch a headless Chromium browser.
    """
    browser = playwright_instance_fixture.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """
    Create a new browser page for each test.
    """
    page = browser.new_page()
    yield page
    page.close()
