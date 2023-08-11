from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "List Methods"
sheet.append(["No","Method", "Decreption"])
try:
    source = requests.get("https://www.geeksforgeeks.org/list-methods-in-python/")
#     source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    movie = soup.find('figure', class_='table').find_all('tr')
    movie= soup.find_all("tbody")

    for movies in movie:
        print(movies)

        movies = soup.find_all('th')
        No = movies[0].get_text(strip=True).split('.')[0]
        Method = movies[1].get_text(strip=True).split('.')[0]
        Decreption = movies[2].get_text(strip=True).split('.')[0]
        print(No,Method, Decreption)
        

#         name = movies.find('td', class_='titleColumn').a.text

#         rank = movies.find('td', class_='titleColumn').get_text(
#             strip=True).split('.')[0]

#         year = movies.find('td', class_='titleColumn').span.text.strip('()')

#         rating = movies.find(
#             'td', class_='ratingColumn imdbRating').strong.text

#         # print(rank, name, year, rating)

        sheet.append([No,Method, Decreption])

except Exception as e:
    print(e)
# finally:
#     print("This program is excuted")

# excel.save('list.xlsx')
