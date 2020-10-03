from seleniumwire import webdriver
import time
from fastapi import FastAPI
import uvicorn

app = FastAPI()

response = "Failed to grab cookies"
startTime = time.time()
firstTime = True

@app.get("/")
async def grab_headers():
    global firstTime, startTime, response
    if time.time() - startTime >= 120 or firstTime is True:
        firstTime = False
        while True:
            try:
                del driver.requests
                driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[2]/div/div/div/form/div[4]/button').click()
                time.sleep(2)
                for request in driver.requests:
                    if str(request) == "https://rango.id.peacocktv.com/signin/service/international":
                        get_headers = request.headers
                        response = {
                            'q5VwYrl1FT-a': get_headers['q5VwYrl1FT-a'],
                            'q5VwYrl1FT-b': get_headers['q5VwYrl1FT-b'],
                            'q5VwYrl1FT-c': get_headers['q5VwYrl1FT-c'],
                            'q5VwYrl1FT-d': get_headers['q5VwYrl1FT-d'],
                            'q5VwYrl1FT-f': get_headers['q5VwYrl1FT-f'],
                            'q5VwYrl1FT-z': get_headers['q5VwYrl1FT-z']
                        }
                        #print(response)
                        break
                startTime = time.time()
                break
            except:
                send_data()
                continue
    return response

def send_data():
    driver.get("https://www.peacocktv.com/signin")
    email = driver.find_element_by_xpath('//*[@id="userIdentifier"]')
    text = 'test@mail.com'
    for character in text:
        email.send_keys(character)
        time.sleep(0.3)
    time.sleep(1)
    password = driver.find_element_by_xpath('//*[@id="password"]')
    text = 'password'
    for character in text:
        password.send_keys(character)
        time.sleep(0.3)
    time.sleep(1)
driver = webdriver.Chrome()
send_data()

uvicorn.run(app, host="127.0.0.1", port=8000)
