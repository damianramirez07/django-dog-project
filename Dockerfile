FROM python:3.13-slim 

# Setting working directory 
WORKDIR /app 

# Stops python from creating .pyc fiels
ENV PYTHONDONTWRITEBYTECODE=1

# Sends output to terminal
ENV PYTHONUNBUFFERED=1

# Copy dependecy list into container and . represents the current working directory which was defined as /app above
COPY requirements.txt .

# Install required py packages
RUN pip install --no-cache-dir -r requirements.txt

# Django port - listening port for app
EXPOSE 8000

# Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



