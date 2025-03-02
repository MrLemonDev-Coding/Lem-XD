import requests

url = input("URL: ")
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
    with open("website.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("HTML grabbed and saved to website.html")
else:
    print(f"Failed to grab HTML. Status code: {response.status_code}")
