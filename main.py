import uvicorn 
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from command import scanner


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory="templates")


@app.get("/")
def controller(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.get("/scanner/ip")
def scanner_ip():
    return scanner.ip('127.0.0.1')

@app.get("/scanner/wifi")
def scanner_wifi():
    return scanner.wifi('127.0.0.1')

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)