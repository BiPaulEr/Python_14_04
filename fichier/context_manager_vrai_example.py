import requests

class SessionManager():
    def __enter__(self):
        self.session = requests.Session()
        return self.session
    def __exit__(self, exc_type, exc, tb):
        self.session.close()
        return True

with requests.Session() as session:
    headers = {"Accept" : "text/plain"}
    response = session.get("https://icanhazdadjoke.com/", headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print("erreur")
    

