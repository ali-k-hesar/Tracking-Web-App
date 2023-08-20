# Tracking Web-App - Computer Vision Web Application (No Docker Version)

<div align="center">
  <p>
    <img width="100%" src="https://github.com/ali-k-hesar/Tracking-Web-App/assets/85279433/8ba2b6f0-4dec-4e20-bc98-f05b49505d7e"></a>
  </p>
</div>

This branch of the project allows you to run the Computer Vision Web-App without using Docker. You can set up and run the application using Uvicorn and the required Python dependencies. The application utilizes computer vision techniques to perform various tasks using AI models. It allows users to track faces, hands, body poses, and perform background removal on images.

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

## Running the Application

#### 1. Clone this repository:

```shell
git clone -b no-docker https://github.com/ali-k-hesar/Tracking-Web-App.git
```

#### 2. Navigate to the project directory:

```shell
cd Tracking-Web-App
```

#### 3. Install the required Python dependencies:

```shell
pip install -r requirements.txt
```

#### 4. Run the application using Uvicorn:

```shell
uvicorn main:app --host 127.0.0.1 --port 8000
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
- **requirements.txt**: List of Python dependencies for the project.
- **bg_models**: Contains the yolov8n-segmentation model for background removal.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
