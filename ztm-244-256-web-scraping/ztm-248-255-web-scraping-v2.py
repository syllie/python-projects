import requests
from bs4 import BeautifulSoup
import pprint


def scrape_page(webpage, page_number):
    query_string = f'?p={page_number}' if page_number > 1 else ''

    print('retrieving: ' + webpage + query_string)
    response = requests.get(webpage + query_string)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.titlelink')
    subtext = soup.select('.subtext')

    return create_custom_hn(links, subtext)


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return hn


def main():
    url = 'https://news.ycombinator.com/news'

    hn_list = []

    for page in range(1, 3):
        hn_list += scrape_page(url, page)

    hn_list_sorted_by_vote = sort_stories_by_votes(hn_list)

    pprint.pprint(hn_list_sorted_by_vote)


if __name__ == '__main__':
    main()
