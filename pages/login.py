class LoginPage:
    def __init__(self, page):
        self.page = page
        self.page.goto("https://www.24hourfitness.com/login.html#/")
        page.pause()
        self.signin_button = page.get_by_role("button", name="Account Circle icon Sign In")
        self.username_box = page.locator("#nav-login-username")
        self.password_box = page.locator("#nav-login-password")
        self.signin_button_exact = page.get_by_role("button", name="SIGN IN", exact=True)

    def login(self, username, password):
        self.signin_button.click()
        self.signin_button.click()
        self.username_box.click()
        self.username_box.fill(username)
        self.password_box.click()
        self.password_box.fill(password)
        self.signin_button_exact.click()
