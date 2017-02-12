# Selenium Shoe Bot

*NOTE: This program is made for Python 2.7.X and will not work with Python 3.X.X!*

This is a simple Python bot which uses Selenium to navigate the website [http://www.nakedcph.com/](http://www.nakedcph.com/)  and quickly checkout shoe orders. Although the script was written with the specific intention of making shoe orders, there is nothing stopping users from checking out other items on the site through the script. Users can configure how many orders they want to make, including the credit card info to use and various items to checkout within each order by editing the included checkout.conf JSON file. The script is configured to use the PhantomJS headless webdriver, which is included as a NodeJS dependency. Chromedriver is also included as a dependency in the case that you don't want to use a headless webdriver.

## Installation Instructions (Linux/Mac)

1. Make sure that you have Python 2.7.X installed, along with Pip.

2. Install Node.JS and NPM.

3. Download or clone this repository to a directory on your machine.

4. Open the terminal, navigate to the project directory, and type the command `pip install -r requirements.txt`. This should install the Python dependencies Selenium and Chromedriver. *NOTE: On Mac, the dependency chromedriver-installer may not download. If this is the case, you will have to install chromedriver manually.*

5. From the terminal, type the command `npm install`. This should install PhantomJS.

6. Edit the checkout.conf JSON file to your liking, but make sure that it still contains valid JSON syntax.

7. You may edit autocheckout.py to use Chromedriver instead of PhantomJS if you wish to view the browser navigation performed by the script. 

8. Run the program from the terminal with `python autocheckout.py`.

## Installation Instructions (Windows)

This script has not been tested for Windows, but it should still work if a similar procedure is followed as the one for Linux/Mac.
