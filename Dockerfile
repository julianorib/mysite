FROM python:3-alpine3.22
WORKDIR /app
COPY src/requirements.txt .
RUN python -m pip install --upgrade pip --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org
RUN pip install -r requirements.txt --user --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org
RUN pip install opentelemetry-distro opentelemetry-instrumentation-flask opentelemetry-exporter-otlp --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org
COPY src/ .
EXPOSE 8080
ENTRYPOINT [ "opentelemetry-instrument", "python", "/app/mysite.py"]

