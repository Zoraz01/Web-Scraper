import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")

results = soup.find(id = "ResultsContainer")
#print(results.prettify())

job_elements = results.find_all("div", class_="card-content")
#for jobelement in job_elements:
    #print(jobelement, end="\n"*2)

#for jobelement in job_elements:
    #title = jobelement.find("h2", class_="title")
    #company = jobelement.find("h3", class_="company")
   # location = jobelement.find("p",class_="location")
   # print(title.text.strip())
   # print(company.text.strip())
    #print(location.text.strip())
   # print()

python_jobs = results.find_all("h2",string =lambda text: "python" in text.lower())
#print(python_jobs)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element in python_job_elements:
    title = job_element.find("h2", class_="title")
    company = job_element.find("h3", class_="company")
    location = job_element.find("p",class_="location")
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()
