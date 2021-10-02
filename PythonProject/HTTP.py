# import requests
# payload = {'username':'admin','password':'password'}
# r = requests.post('http://httpbin.org/post',data=payload)
# print(r.url)
# print(r.text)
# print(r.json()['origin'])
# print(r.text.index('origin',449))
# r = requests.get('https://httpbin.org/get',params=payload)
# print(r.headers['Content-type'])
# print(r.headers['Date'])
# print(r.headers['Server'])
# print(r.json())
# r = requests.post('http://github.com')
# print(r.history)
#-------------------------
# import webbrowser

# chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# print(webbrowser.get(chrome_path).open(url='google.com'))
