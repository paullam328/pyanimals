FROM python:3.13.0-alpine3.20

WORKDIR /code

# Copy the project over
COPY ./backend /code

# Install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]