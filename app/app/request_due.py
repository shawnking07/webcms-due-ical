import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .due_model import DueModel

url = "https://webcms3.cse.unsw.edu.au"

payload = {}
headers = {
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.102 Safari/537.36',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Cookie': '',
}


def request_webcms(session: str):
    headers['Cookie'] = 'session=' + session
    response = requests.request("GET", url, headers=headers, data=payload)
    html_txt = response.text.encode('utf8')
    return resolve_html(html_txt)


def resolve_html(html_txt: bytes):
    bs = BeautifulSoup(html_txt, 'html.parser')
    due_panel = bs.select('#webcms3top > div > div.row.row-offcanvas.row-offcanvas-left > div > div.row > div.col-sm-4 '
                          '> div:nth-child(1) > ul > li')
    ans = list()
    for i in due_panel:
        info = DueModel(i.a['href'].split('/')[1],
                        i.a.get_text().strip(),
                        datetime.fromisoformat(i.abbr['title']),
                        url + (i.a['href'].strip()))
        ans.append(info)
    return ans

