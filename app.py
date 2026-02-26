from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

html_file = Path(__file__).parent / "templates" / "index.html"
with open(html_file, "r") as f:
    html_content = f.read()

@app.get("/", response_class=HTMLResponse)
def home():
    return html_content

@app.post("/submit")
def submit(name: str = Form(...)):
    name=name.upper()
    if name:
        return RedirectResponse(
            #url=f'https://erp.silicon.ac.in/estcampus/hostel/db_hostel_attendance.php?oper=CHECK_HOSTEL_ATTENDANCE&studentId={name}',
            url='https://www.google.com',
            status_code=302
        )
    return RedirectResponse(url="/", status_code=302)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
