from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

app = FastAPI(debug=True)
# app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.route("/hello")
def read_item(request: Request):
    # テンプレートに渡すデータ
    data = {'title': 'My Page', 'name': 'Rena'}
    
    # テンプレートのレンダリング
    return templates.TemplateResponse("hello.html", {"request": request, "data": data})


@app.get("/Hello-Word")
def read_root():
    return {"body": "Hello World"}