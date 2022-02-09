####Mohamed khaled Ahmed
####Group:3
####ITI AI Alex

##from selenium import webdriver
##import csv
##driver=webdriver.Chrome(r"C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
##
##driver.get(r"https://www.amazon.in/gp/bestsellers/books/")
##products=driver.find_elements_by_xpath("//div[@class='p13n-sc-truncate-desktop-type2 p13n-sc-truncated']")
##prices=driver.find_elements_by_xpath("//span[@class='p13n-sc-price']")
##for i in products:
##    print(i.text)
##for i in prices:
##    print(i.text)
##with open('D:\Amazon_Products.csv', 'w',encoding='utf-8') as csvfile:
##    csvwriter = csv.writer(csvfile, delimiter=',')
##    csvwriter.writerow(['Product Name','Price'])
##    for i in range(1,len(products)):
##        csvwriter.writerow([products[i].text,prices[i].text])
