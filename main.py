import uvicorn 
from fastapi import FastAPI, Request, HTTPException
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
def scanner_ip(request: Request):
    try:
        return {"IP": request.client.host}
    except Exception:
            raise HTTPException(status_code=404, detail="Not found iP")

@app.get("/scanner/wifi")
def scanner_wifi(request: Request):
    try:
        return scanner.wifi(request.client.host)
    except Exception:
        raise HTTPException(status_code=404, detail="Not found devices")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info",  server_header=False , reload=True)