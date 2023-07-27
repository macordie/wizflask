Summary: This app was written to control Phillips WIZ lightbulbs in locations without an Internet connect since the Phillips mobile app requires an active Internet connection for light control. This is an AJAX one page app that does not require reloading. The page uses AJAX to access flaskapp routes (URLS) and updates settings without submitting or reloading data.

You can use these app as a WSGI flask app or standalone with gunicorn.

This simple app supports the following:

* On / Off
* Brightness
* Color Temperature
* Custom R:G:B settings
* 32 Scenes

Quickstart: To start this app with gunicorn run:

gunicorn flaskapp:app --name flaskapp -b 0.0.0.0:8000

If you want to run this app as a wsgi app, you can change the root_path in the index.html file to match the path on your server. For gunicorn the root_path = "/" should be set as follows.

This simple app supports the following:

* On / Off
* Brightness
* Color Temperature
* Custom R:G:B settings
* 32 Scenes


This code is releases under the MIT Licenses

=============================================
Copyright 2023 Michael George

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
