from playwright.sync_api import sync_playwright

# Note: Playwright does not have a Galaxy S4 device descriptor.
# Galaxy S5 is the closest available Samsung device with the same era and screen size.

def test_open_24hour_on_galaxy_s5():
    with sync_playwright() as p:
        galaxy_s5 = p.devices["Galaxy S5"]  # 360x640, deviceScaleFactor=3, mobile UA

        browser = p.chromium.launch(headless=False)
        context = browser.new_context(**galaxy_s5)
        page = context.new_page()

        page.goto("https://www.24hourfitness.com/login.html#/")
        page.wait_for_timeout(5000)  # pause so you can see the mobile layout

        print("Title:", page.title())
        print("Viewport:", page.viewport_size)

        browser.close()
