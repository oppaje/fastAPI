from fastapi import FastAPI, Form
import uvicorn
from mega import Mega

mega = Mega()
app = FastAPI()

@app.post("/")
async def login(email: str = Form(...), password: str = Form(...)):
    try:
        m = mega.login(email, password)
        total_storage = int(m.get_storage_space(giga=True)["total"])
        storage_used = int(m.get_storage_space(giga=True)["used"])
        if total_storage < 400:
            user_type = 'FREE'
        else:
            user_type = 'PREMIUM'
        return {
            'user_type': user_type,
            'storage_used': f'{storage_used}/{total_storage} GB',
            'oppaje': 'NeThinGoez.com'
        }
    except Exception as e:
        return e

uvicorn.run(app, host="127.0.0.1", port=8000)
