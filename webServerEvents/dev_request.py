import requests

if __name__ == "__main__":
    r = requests.post("http://127.0.0.1:8090/log-in",
                      data={"username": "Anton", "password": "12345"})
    print(r.text, r.status_code)

    r = requests.post("http://127.0.0.1:8090/log-in",
                  data={"username": "alison", "password": "gradprog2016@07"})

    print(r.text, r.status_code)
