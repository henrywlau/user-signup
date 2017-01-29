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
import cgi

def escape_html(s):
    return cgi.escape(s, quote=True)

signup_header = "<h1>Signup</h1>"

signup_form = """
<form method="post">
    <label>Username
    <input type="text" name="username">
    </label>
    <br>

    <label>Password
    <input type="password" name="password1 value="">
    </label>
    <br>

    <label>Verify Password
    <input type="password" name="password2 value="">
    </label>
    <br>

    <label>Email (optional)
    <input type="text" name="email">
    </label>
    <br>

    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):

        content = signup_header + signup_form
        self.response.write(content)

    def post(self):

        self.response.write("post")


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
