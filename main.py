import requests
from bs4 import BeautifulSoup


def get_content():

    url = 'https://www.hhs.gov/about/agencies/dab/decisions/alj-decisions/2021/alj-cr5975/index.html'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    parties = soup.find('div', attrs={'class':'field field--name-field-legal-d-party-citation field--type-text-long field--label-hidden field--item'}).text
    #print(parties)

    judge = soup.find('span', attrs={'class':'judge-name'}).text
    #print(judge)

    contents = soup.find('div', attrs={'class':'field field--name-field-uswds-body field--type-text-long field--label-hidden field--item'})
    contents = contents.findChildren('p')
    decision = contents[0]

    html = soup.find('h3')
    html.time.clear()
    #print(html.prettify())
    no = str(html)
    no = no.split('<br/>')
    no = no[0]
    no = no.split('<h3>')
    no = no[1]
    print(no)


    number =html.text.split('No. ')
    number = number[1]

    data_dict = {
        'case number': number,
        'judge': judge,
        'parties': parties,
        'decision text': decision
    }
    #print(data_dict)


def get_link():
    url ='https://www.hhs.gov/about/agencies/dab/decisions/alj-decisions/2021/index.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }

    r = requests.get(url, headers=headers)
    s = BeautifulSoup(r.text, 'html.parser')
    judul = s.find('div', attrs={'class':'field field--name-field-uswds-body field--type-text-long field--label-hidden field--item'})
    judul = judul.find('p')
    #link = judul.find_all('a')['href']
    comp_name = [link['href'] for link in judul.find_all('a')]

    all_link = []
    for link in comp_name:
        all_link.append('https://www.hhs.gov'+link)

    return all_link


def run():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    link = get_link()

    i = 0
    hasil = []
    for i in range(len(link)):
        print('Case',i+1)
        print(link[i])
        url = str(link[i])

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        parties = soup.find('div', attrs={
            'class': 'field field--name-field-legal-d-party-citation field--type-text-long field--label-hidden field--item'}).text
        # print(parties)

        judge = soup.find('span', attrs={'class': 'judge-name'}).text
        # print(judge)

        contents = soup.find('div', attrs={
            'class': 'field field--name-field-uswds-body field--type-text-long field--label-hidden field--item'})
        contents = contents.findChildren('p')
        decision = contents[0]

        html = soup.find('h3')
        html.time.clear()
        no = str(html)
        no = no.split('<br/>')
        no = no[0]
        no = no.split('<h3>')
        no = no[1]


        data_dict = {
            'case number': no,
            'judge': judge,
            'parties': parties,
            'decision text': decision
        }
        hasil.append(data_dict)
        print(data_dict)
        i += 1

    #print(hasil)
    return hasil


if __name__ == '__main__':
    run()