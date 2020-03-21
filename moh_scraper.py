import requests
from bs4 import BeautifulSoup


def send_request(url='https://www.mohfw.gov.in/'):
    return requests.get(url=url)


def create_soup_object(data=None):
    if data is not None and data.text is not None:
        return BeautifulSoup(data.text, 'html.parser')
    return None


def scrape_covid_data(url='https://www.mohfw.gov.in/'):
    moh_page_html = send_request(url=url)
    soup = create_soup_object(data=moh_page_html)
    table_data_html = soup.find('table', attrs={'class': 'table table-striped table-dark'})
    inner_data_html = table_data_html.findAll('td', attrs={'align': "'centre"})
    state_data = {}
    '''
    {'State' : [Total Confirmed (Indian), Total Confirmed (Foreign), Cured, Death]
    '''
    for posn in range(1, len(inner_data_html)-5, 6):
        state_data[inner_data_html[posn].text] = [inner_data_html[posn + 1].text,
                                                  inner_data_html[posn + 2].text,
                                                  inner_data_html[posn + 3].text,
                                                  inner_data_html[posn + 4].text,
                                                  ]
    return state_data


if __name__ == '__main__':
    data = scrape_covid_data()
    for idx, d in enumerate(data):
        print(idx, d, data[d])
