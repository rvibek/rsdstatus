from flask import Flask, render_template, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/rsdstat", methods=['GET', 'POST'])
def fetch_result(*args):

    formdob = request.form['dob']
    formcaseno = request.form['caseno']

    if len(formdob) == 0:
        formdob = "01/01/1950"
    if len(formcaseno) == 0:
        formcaseno = "555-14C00000"

    options = webdriver.ChromeOptions()
    # options = ChromeOptions()
    options.add_argument('headless')
    # options.addArguments("--headless")
    # options.addArguments("--disable-gpu")
    # options.addArguments("--no-sandbox")
    options.binary_location = "/app/.apt/usr/bin/google-chrome-stable"
    driver = webdriver.Chrome(options=options)
    driver.get("https://pritt.unhcregypt.org/RefugeeResult.aspx")

    dob = driver.find_element_by_id('ctl00_ContentPlaceHolder1_sDoB_dateInput')
    dob.send_keys(formdob)

    caseno = driver.find_element_by_id('ctl00_ContentPlaceHolder1_sProGresID')
    caseno.click()
    caseno.send_keys(Keys.HOME)
    caseno.send_keys(formcaseno)

    driver.find_element_by_id('ContentPlaceHolder1_bSearch').send_keys(Keys.ENTER)

    try:
        driver.find_element_by_id('ui-accordion-accordion-header-1').click()
    except:
        0

    result = driver.find_element_by_id('ContentPlaceHolder1_lResult')

    result = result.text
    # return result
    driver.close()

    if result != "No Result":
        result = result.split('\nFor more details click here\n')
    else:
        result = ["No Result", "Retry with correct input"]

    data = {"result": result[0], "explain": result[1]}

    # print(result)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
