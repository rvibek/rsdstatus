# RSD Status Check

This application passes DOB and Case Number to [UNHCR Egypt RSD website](https://rsd.unhcregypt.org) and fetches the result as a JSON.

The application is deployed at [https://rsdstatus.herokuapp.com/](https://rsdstatus.herokuapp.com/)

It runs on [Flask](https://flask.palletsprojects.com/en/2.0.x/) using [Selenium](https://selenium-python.readthedocs.io/) along with [Chrome web driver](https://chromedriver.chromium.org/downloads). 

Because of the limitation in that one cannot use custom software or libraries, the following buildpacks need to be installed in Heroku to enable the web driver to work. 


```
$ heroku buildpacks:add --index 1 heroku/python
$ heroku buildpacks:add --index 2 https://github.com/heroku/heroku-buildpack-chromedriver
$ heroku buildpacks:add --index 3 https://github.com/heroku/heroku-buildpack-google-chrome
```

or 

**Config in Heroku dashboard**

Settings -> Add buildpacks -> heroku/python -> Save changes

Settings -> Add buildpacks -> https://github.com/heroku/heroku-buildpack-chromedriver -> Save changes

Settings -> Add buildpacks -> https://github.com/heroku/heroku-buildpack-google-chrome -> Save changes



The web driver is pointed in the following manner in app.py

```
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.binary_location = "/app/.apt/usr/bin/google-chrome-stable"
driver = webdriver.Chrome(options=options)
```

The result can also be fetched as a query argument (i.e. /rsdstatus_check?dob=01/01/1970&caseno=555-15C00001). DOB has to be dd/mm/yyyy format and followed by standard case number format.

