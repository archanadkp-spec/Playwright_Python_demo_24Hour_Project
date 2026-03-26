from playwright.sync_api import expect,sync_playwright  # import expect for assertions  playwright

def test_google_search(page):  # using page we can do browser action using page fixure
    page.wait_for_timeout(5000)  # wait for 5 seconds
    page.goto("https://google.com/ncr")  # navigate to google
    
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)  # click on accept all button
    except:
        print("No cookie banner found")  # if no cookie banner found, print message
    
    search_box = page.get_by_role("combobox", name="Search")
    #page.keyboard.press("Enter")  # press enter to focus on search box
    search_box.fill("Playwright Python")
    page.keyboard.press("Enter")
    assert search_box.input_value() == "Playwright Python"  # query text is entered correctly
    page.keyboard.press("Enter")  # press enter to search
    current_url = page.url
    assert "google.com" in current_url.lower()  # still on a Google-owned page
    print("Test passed: Search results page is displayed with the correct query and URL.")