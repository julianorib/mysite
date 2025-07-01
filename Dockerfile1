FROM python:3-alpine3.22
WORKDIR /app
COPY src/requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --user --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org
COPY src/ .
EXPOSE 8080
ENTRYPOINT [ "python", "/app/mysite.py"]

