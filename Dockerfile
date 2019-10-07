FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

# Install python dependencies
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy application code
COPY ./app /app

# Set environment variables
ENV APP_BASE_DIR /data
ENV WEB_CONCURRENCY 4
ENV WORKERS_PER_CORE 3