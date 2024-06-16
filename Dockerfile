FROM python:3.8-slim

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install pyjwt 

# Copy project files
COPY . /code/

# Add wait-for-it script and set permissions
COPY wait-for-it.sh /code/wait-for-it.sh
RUN chmod +x /code/wait-for-it.sh

# Set default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
