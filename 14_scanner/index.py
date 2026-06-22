import requests
from bs4 import BeautifulSoup

bad_chars = ["'", "<", ">", "(", ")", ";"]

def spider_inputs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find('form')
    if not form:
        print("no form was found")
        return[]
    
    return form.find_all('input')

def test_inputs(url, inputs):
    results = {}
    for input_field in inputs:
        name = input_field.get('name')
        if name:
            for i in bad_chars:
                payload = {name: bad_chars}
                response = requests.post(url, data=payload)
                key = f"{url} input field: {name} payload {bad_chars}"
                results[key] = response.status_code

def main():
    url = input("Enter URL to scan: ")
    inputs = spider_inputs(url)
    if not inputs:
        return
    
    results = test_inputs(url, inputs)
    for key, value in results.items():
        print(f"{key} and Status code {value}")

if __name__ == "__main__":
    main()
