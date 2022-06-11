import requests
from bs4 import BeautifulSoup
import time

def company_searcher(cls, file, file2, cmp):
    for companies in soup.find_all(class_=cls):
        email = companies.find(class_='ajax-modal-link icon-envelope cursor-pointer addax addax-cs_hl_email_submit_click')
        company_name = companies.find(class_="company-name addax addax-cs_hl_hit_company_name_click")
        www = companies.find(class_='icon-website addax addax-cs_hl_hit_homepagelink_click')
        if email:
            print(company_name.get_text())
            print(email['data-company-email'])
            if www:
                file.write(company_name.get_text() + ',' + email['data-company-email'] + ',' + www['href'] + '\n')
                print(www['href'])
            else:
                file2.write(company_name.get_text() + ',' + email['data-company-email'] + cmp + '\n')
                print('Nie posiada strony')
        else:
            print('brak maila')

def get_pages():
    count_pages = soup.find(class_='text-dark py-1')
    pages = count_pages['data-paginatorpage']
    return int(pages)

company = input('Podaj nazwe firmy: ')
company = company.replace(' ','_')
city = input("Podaj miasto: ")
url = f'XXXXXX/{company}/{city}/firmy,1.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
fname = input('Podaj nazwe pliku: ')
f = open(fname+'.txt', 'w')
f2 = open(fname+"_without-www.txt", 'w')
pages = get_pages()
for i in range(0, pages):
    url = f'XXXXXX/{company}/{city}/firmy,{i}.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    company_searcher('card top-link company-item py-2 container my-2', f, f2, company)
    company_searcher('card company-item py-2 container my-2', f, f2, company)
    print(url)
    time.sleep(2)
f.close()
f2.close()
