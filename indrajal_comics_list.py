from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_list_of_pages():
    for count in range(12):
        yield f"https://comicvine.gamespot.com/indrajal-comics/4050-40270/?page={count}"
    for count in range(10):
        yield f"https://comicvine.gamespot.com/indrajal-comics/4050-40373//?page={count}"
    # return ["https://comicvine.gamespot.com/indrajal-comics/4050-40373/?page=9"]

def get_data(element):
    image_url=element.find("div",{'class':'imgboxart'}).find('img')["src"]
    issue_number=element.find("p",{'class':'issue-number'}).text
    issue_name=element.find("p",{'class':'issue-name'}).text
    issue_date=element.find("p",{'class':'issue-date'}).text
    return [image_url,issue_number,issue_name,issue_date]

if __name__ == '__main__':
    comic_list = []
    for url in get_list_of_pages():
        page = urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        list_comic_elements=comic_list.extend(soup.find_all('ul', class_='editorial grid issue-grid js-simple-paginator-container'))
        list_comic_elements = soup.find_all('ul', class_ = 'editorial grid issue-grid js-simple-paginator-container')[0]
        # interate through all the elements in the list
        for element in list_comic_elements.find_all('li'):
            block=get_data(element)
            comic_list.append(block)
            print(block)
        # print(list_comic_elements.find_all('li')[0])
        # comic_list()

    # page = urlopen("https://comicvine.gamespot.com/indrajal-comics/4050-40270/?page=1").read().decode('utf-8')
    # soup = BeautifulSoup(page, 'html.parser')
    # list_comic_elements=soup.find_all('ul', class_='editorial grid issue-grid js-simple-paginator-container')[0]
    # print(list_comic_elements.find_all('li')[0])
    # print(get_data(list_comic_elements.find_all('li')[0]))

