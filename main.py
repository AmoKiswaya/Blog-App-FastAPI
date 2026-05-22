from fastapi import FastAPI, Request 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") 

templates = Jinja2Templates(directory="templates") 

posts: list[dict] = [
    {
        "id": 1,
        "author": "Amo Kline",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and fast.",
        "date_posted": "May 20 2026",
    },
    {
        "id": 2,
        "author": "John Doe",
        "title": "Python is Awesome",
        "content": "Python is a great language.",
        "date_posted": "May 21 2026",
    },
]

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request, 
        "home.html", 
        {"posts": posts, "title": "Home"},
    ) 


@app.get("/api/posts")
def get_posts():
    return posts 