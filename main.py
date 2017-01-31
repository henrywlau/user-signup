#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

# valid Username
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

# valid password
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

# valid email
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)

# create entry form
signup_form = """
<form method="post">
    <h1>Signup</h1>

    <label> Username
        <input type="text" name="username" value={username}>
    </label>
    <div style="color:red">{userNameError}</div>
    <br>

    <label> Password
        <input type="password" name="password" value="">
    </label>
    <div style="color:red">{passwordError}</div>
    <br>

    <label> Verify Password
        <input type="password" name="verify" value="">
    </label>
    <div style="color:red">{verifyError}</div>
    <br>

    <label> Email (optional)
        <input type="text" name="email" value={email}>
    </label>
    <div style="color:red">{emailError}</div>
    <br>

    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(signup_form.format(username='',email='',userNameError='', passwordError='', verifyError='', emailError=''))

    def post(self):
        have_error = False

        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username, email = email, error_username='',error_password='',error_verify='',error_email='')

        if not valid_username(username):
            params["error_username"] = "That is not a valid username!"
            have_error = True

        if not valid_password(password):
            params["error_password"] = "That is not a valid password!"
            have_error = True
        elif password != verify:
            params["error_verify"] = "Your passwords did not match!"
            have_error = True

        if not valid_email(email):
            params["error_email"] = "That is not a valid email!"
            have_error = True

        # render form again if error
        if have_error:
            self.response.out.write(signup_form.format(username=params["username"], email=params["email"], userNameError=params["error_username"], passwordError=params["error_password"], verifyError=params["error_verify"], emailError=params["error_email"]))
        # redirect to welcome message if data is good
        else:
            self.redirect("/welcome?username=" + username)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            welcome_message = "Welcome, " + username + "!"
            self.response.write(welcome_message)
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
