FROM python:3.9-slim

# Create and activate a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy your application code
COPY . /app/

# Set working directory
WORKDIR /app

# Install dependencies inside the virtual environment
RUN apt-get update &&\
 apt-get install -y libstdc++6 libgl1-mesa-glx libglib2.0-0 &&\
 pip install --default-timeout=1000 -r requirements.txt && rm requirements.txt

# Expose port
EXPOSE 8000

# Set the command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
