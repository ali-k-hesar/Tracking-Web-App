# Tracking Web-App - Computer Vision Web Application

<!-- <div align="center">
  <p>
    <img width="100%" src="https://github.com/ali-k-hesar/pixel-shuffle-using-hand-tracking/assets/85279433/273d59f3-2fa8-47c1-a951-2af9251345e8"></a>
  </p>
</div>
 -->

This project is a web application that utilizes computer vision techniques to perform various tasks using AI models. The application allows users to easily track faces, hands, body poses, and perform background removal on images. Users can access these features with a click of a button inside the web app. The AI models are implemented in Python using mediapipe, open-cv, and PyTorch. The models are served through an API built with FastAPI and run using uvicorn. The frontend is created using HTML, CSS, and JavaScript to interact with the web app. The project is also dockerized for easy deployment.

If you want to run the app outside docker environment in your local machine, change to branch **"no-docker"**.

## Features

- **Face Tracking**: This feature utilizes AI models to track face landmarks in real-time.
- **Hand Tracking**: The application employs AI models to track hand movements and gestures.
- **Body Pose Tracking**: Users can track body poses and movements using the AI model provided.
- **Background Removal**: The application can perform background removal from images, isolating the subject.

## Languages and Modules

- **Python**: The AI models are coded using Python programming language.
- **Mediapipe**: Mediapipe library is used for its pre-trained AI models for various tracking tasks.
- **OpenCV**: OpenCV is used for handling video input, image processing, and visualization.
- **PyTorch**: PyTorch is used for any deep learning-related tasks.
- **FastAPI**: FastAPI is used to create the API for serving the AI models.
- **uvicorn**: Uvicorn is used as the ASGI server to host the FastAPI application.
- **HTML, CSS, JavaScript**: The frontend of the web application is built using HTML, CSS, and JavaScript.
- **Docker**: The application is containerized using Docker for easy deployment and reproducibility.

## Running the Application

#### 1. Clone this repository:

```shell
git clone https://github.com/ali-k-hesar/Tracking-Web-App.git

```

#### 2. Navigate to the project directory:

```shell
cd Tracking-Web-App
```

#### 3. Build the Docker image

```shell
docker build -t tracking-web-app .
```

#### 4. Run the Docker container:

```shell
docker run -p 8000:8000 your-app-name
```

#### 5. Access the application in your browser at http://localhost:8000.

## Usage

- Upon accessing the application, you will be presented with a user-friendly interface.
- Click on the buttons to select the desired tracking task: face-tracking, hand-tracking, pose-tracking, or background removal.
- The live video feed will display the tracking results in real-time.

## Directory Structure

- **main.py**: The FastAPI application code, including API endpoints and startup events.
- **templates**: Contains the HTML template used for rendering the frontend.
- **fonts**: Contains font files used in the frontend.
- **camera.py**: Contains the Camera class used to capture video frames.
- **model.py**: Contains the TrackModel class for handling AI model predictions.
- **Dockerfile**: The Dockerfile used to create the Docker image.
- **requirements.txt**: List of Python dependencies for the project.
- **bg_models**: Contains the yolov8n-segmentation model for background removal.

## License

This project is licensed under the MIT License. See the LICENSE file for details.