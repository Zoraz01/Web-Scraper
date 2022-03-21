import requests
from bs4 import BeautifulSoup
import xlsxwriter


workbook = xlsxwriter.Workbook("imdbData.xlsx")
worksheet = workbook.add_worksheet()
row = 1
column = 0

worksheet.write(0,0,"Rank:")
worksheet.write(0,1,"Title:")
worksheet.write(0,2,"Rating:")


url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(class_ = "lister-list")
movie_elements = results.find_all("tr")
print("Most Popular Movies: ")
for movie_element in movie_elements:
    titleColumn = movie_element.find("td", class_= "titleColumn")
    rank = titleColumn.find("div", class_= "velocity")
    textRank = rank.text
    splitrank = textRank.split('\n',1)[0]
    title = titleColumn.find("a")
    releaseYear = titleColumn.find("span", class_="secondaryInfo")
    rating = movie_element.find("td", class_="imdbRating")



    print("Rank: " + splitrank)
    print( title.text.strip() + " " + releaseYear.text.strip())
    print("Rating: " + rating.text.strip())

    print()

    worksheet.write(row,column,splitrank)
    worksheet.write(row,column+1,title.text.strip())
    worksheet.write(row,column+2,rating.text.strip())
    row += 1


workbook.close()