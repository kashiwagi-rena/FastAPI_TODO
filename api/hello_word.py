# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# templates = Jinja2Templates(directory="templates")

# @app.get("/hello", response_class=HTMLResponse)
# def read_item(request: Request):
#     # テンプレートに渡すデータ
#     data = {'title': 'My Page', 'name': 'John'}
    
#     # テンプレートのレンダリング
#     return templates.TemplateResponse("template.html", {"request": request, "data": data})
