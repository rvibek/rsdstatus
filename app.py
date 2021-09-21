from flask import Flask, render_template, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from process_result import process 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/rsdstatus", methods=['GET', 'POST'])
def fetch_result(*args):
    
    formdob = request.form['dob']
    formcaseno = request.form['caseno']

    if len(formdob) == 0:
        formdob = "01/01/1950"
    if len(formcaseno) == 0:
        formcaseno = "555-15C00001"

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    
    # uncomment for hero
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
    
    driver.close()

    # pass to process function 
    result = process(result)

    return jsonify(result)
   

@app.route("/rsdstatus_check")
def access_param():
    
    paramdob = request.args.get('dob')
    paramcaseno = request.args.get('caseno')

    # if len(paramdob) < 8:
    #     paramdob = "01/01/1950"
    # if len(paramcaseno) == 0:
    #     paramdob = "555-15C00001"
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.binary_location = "/app/.apt/usr/bin/google-chrome-stable"
    driver = webdriver.Chrome(options=options)
    driver.get("https://pritt.unhcregypt.org/RefugeeResult.aspx")

    dob = driver.find_element_by_id('ctl00_ContentPlaceHolder1_sDoB_dateInput')
    dob.send_keys(paramdob)

    caseno = driver.find_element_by_id('ctl00_ContentPlaceHolder1_sProGresID')
    caseno.click()
    caseno.send_keys(Keys.HOME)
    caseno.send_keys(paramcaseno)

    driver.find_element_by_id(
        'ContentPlaceHolder1_bSearch').send_keys(Keys.ENTER)

    try:
        driver.find_element_by_id('ui-accordion-accordion-header-1').click()
    except:
        0

    result = driver.find_element_by_id('ContentPlaceHolder1_lResult')

    result = result.text
    # return result

    driver.close()

    # pass to process function 
    result = process(result)

    return jsonify(result)
   




if __name__ == '__main__':
    app.run(debug=True)
