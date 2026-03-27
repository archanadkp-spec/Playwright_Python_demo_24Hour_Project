from playwright.sync_api import Page
from pages.login import LoginPage
from pages.logout import LogoutPage

def test_login_Logout(page: Page) -> None:
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)
    login_page.login("archanabkp@gmail.com", "Nish*2010")
    logout_page = LogoutPage(page)
    logout_page.logout()
    print ("Made some changes to check git actions")
    print ("Made some changes to check git actions")
    
    





# def test_example(page: Page) -> None:
#     page.goto("https://www.24hourfitness.com/login.html#/")
#     page.pause()  # Opens Playwright Inspector - click Resume to continue
#     page.get_by_role("button", name="Account Circle icon Sign In").click()
#     page.get_by_role("button", name="Account Circle icon Sign In").click()
#     page.locator("#nav-login-username").click()
#     page.locator("#nav-login-username").fill("archanabkp@gmail.com")
#     page.locator("#nav-login-username").press("Tab")
#     page.locator("#nav-login-password").fill("Nish*2010")
#     page.get_by_role("button", name="SIGN IN", exact=True).click()
#     page.get_by_role("button", name="Account Circle icon My Account").click()
#     page.get_by_role("button", name="Account Circle icon My Account").click()
#     page.get_by_role("button", name="Logout").click()
#     page.pause()
#     expect(page.get_by_role("heading", name="My24 Account")).to_be_visible()
#     expect(page.locator("#login")).to_contain_text("Manage your membership online. Edit your profile, make payments, see your club visits and add services like personal training.")
#     page.get_by_role("button", name="Account Circle icon Sign In").click()
