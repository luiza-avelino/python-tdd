from selenium.webdriver.firefox.options import Options
from selenium import webdriver

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser = webdriver.Firefox(
    executable_path=r'C:\dev\cursos\python-tdd-book\geckodriver.exe', options=options)
browser.get("http://localhost:8000")

assert 'Django' in browser.title
