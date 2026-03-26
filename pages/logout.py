class LogoutPage:
    def __init__ (self, page):
        self.page = page
        page.pause()
        self.myaccount_button = page.get_by_role("button", name="Account Circle icon My Account")
        self.logout_button = page.get_by_role("button", name="Logout")
        
        
    def logout(self):
        self.myaccount_button.click()
        self.myaccount_button.click()
        self.logout_button.click()
        
        
        