# def test_backs_pace_for(self):
#     self.chrome.get("https://the-internet.herokuapp.com/login")
#     user = self.chrome.find_element(*self.USER)
#     user.send_keys('QWERTYUIOP')
#     for i in range(0, 10):
#         user.send_keys(Keys.BACKSPACE)
#         sleep(0.5)
#         i += 1
#     sleep(3)
#  assert Text area == empty


"""
GIVEN when I am on heroku login page (ex: https://the-internet.herokuapp.com/login)
WHEN the input to username is 10 character
AND after deleting 10 characters from username
THEN I verify that the text area is empty
"""