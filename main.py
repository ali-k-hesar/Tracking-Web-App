from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from camera import Camera
from model import TrackModel


templates = Jinja2Templates(directory="templates")
model_list = None


app = FastAPI(title='AI as an API',
              description='Web-App created by ali-k-hesar as an example for serving AI model through API',
              version='1.0.0')

app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")

@app.on_event('startup')
def start_app() -> None:
    global model_list
    model_list = {'hand': TrackModel('hand'),
                  'face': TrackModel('face'),
                  'pose': TrackModel('pose'),
                  'bg': TrackModel('bg')}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {
        "request": request,
        "app_title": app.title,
        "app_description": app.description
    }
    return templates.TemplateResponse('index.html', context)


def predict_on_image(camera, track_type):
    """Video streaming generator function."""
    try:
        model = model_list[track_type]
    except:
        raise HTTPException(status_code=400,
                            detail='Wrong track_type! Choose between ["hand", "pose", "face", "bg"].')

    while True:
        frame = camera.get_frame()
        output_image = model.predict(frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + output_image + b'\r\n')


@app.get('/video_feed', response_class=HTMLResponse)
async def video_feed(track_type: str = 'face'):
    """Video streaming route."""
    return StreamingResponse(predict_on_image(Camera(), track_type=track_type),
                             media_type='multipart/x-mixed-replace; boundary=frame')
