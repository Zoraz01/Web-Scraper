import requests
from bs4 import BeautifulSoup
import xlsxwriter

# initialize file
workbook = xlsxwriter.Workbook('webScrapeData.xlsx')
# add a sheet
worksheet = workbook.add_worksheet()
row = 1
column = 0
# headers are written before the data is inserted
worksheet.write(0, 0, "Title")
worksheet.write(0, 1, "Location")
worksheet.write(0, 2, "Date")
worksheet.write(0, 3, "status")
worksheet.write(0, 4, "company")
worksheet.write(0, 5, "details")
worksheet.write(0, 6, "link")

# url of website we are scraping
url = "https://pythonjobs.github.io/"

# Use requests to get data from website
page = requests.get(url)
# BS is used to format data
soup = BeautifulSoup(page.content, "html.parser")
# Finding data that concerns the list of jobs
results = soup.find(class_="job_list")
# All the different job elements are put in a list
job_elements = results.find_all("div", class_="job")
# for each loop for the info in each element
for jobelement in job_elements:
    title = jobelement.find("h1")
    # Many different variables are stored under the same tag and class so all of them for each element are placed in
    # a list
    infos = jobelement.findAll("span", {"class": "info"})
    detail = jobelement.find("p", class_="detail")
    links = jobelement.find_all("a", class_="go_button")
    # list of info is looped to extract correct data
    for info in infos:
        location = infos[0]
        date = infos[1]
        status = infos[2]
        company = infos[3]
    # links are found 
    for link in links:
        link_url = link["href"]
    # Information is printed
    print("Job Title: " + title.text.strip())
    print(location.text.strip())
    print(date.text.strip())
    print(status.text.strip())
    print(company.text.strip())
    print(detail.text.strip())
    print("Apply here: " + url + link_url)
    print()

    # Information is added to file
    worksheet.write(row, column, title.text.strip())
    worksheet.write(row, column + 1, location.text.strip())
    worksheet.write(row, column + 2, date.text.strip())
    worksheet.write(row, column + 3, status.text.strip())
    worksheet.write(row, column + 4, company.text.strip())
    worksheet.write(row, column + 5, detail.text.strip())
    worksheet.write(row, column + 6, url + link_url)
    row += 1

workbook.close()
