from selenium import webdriver
from time import sleep
from matplotlib import pyplot as plt
options = webdriver.ChromeOptions()
options.add_argument("headless")

user     = ""
password = ""
url      = ""


browser = webdriver.Chrome('/Users/Alex/Desktop/chromedriver',chrome_options=options)
browser.get("https://www.instagram.com")
sleep(2)
browser.find_element_by_xpath("//input[@name=\"username\"]").send_keys(user)
browser.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
browser.find_element_by_xpath("//button[@type=\"submit\"]").click()
sleep(4)
# browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

browser.get(url)
sleep(3)

browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a").click()

arrow = browser.find_element_by_xpath("//a[contains(text(), 'Next')]")

sleep(1)
likes = []
counter = 0
while counter < 200:
  counter += 1
  sleep(2)
  try:
    like = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button/span").text
  except:
    pass
  likes.append(like)
  arrow.click()
  try:
    arrow = browser.find_element_by_xpath("//a[contains(text(), 'Next')]")
  except:
    break
print(likes)
likes.reverse()
print(likes)
plt.plot(likes,'.r-')
plt.show()
