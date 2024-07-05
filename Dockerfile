FROM cgr.dev/chainguard/python:latest-dev as builder
WORKDIR /app
COPY src/requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --user --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org

FROM cgr.dev/chainguard/python
WORKDIR /app
COPY --from=builder /home/nonroot/.local/lib/python3.12/site-packages /home/nonroot/.local/lib/python3.12/site-packages
COPY src/ .
EXPOSE 8080
ENTRYPOINT [ "python", "/app/mysite.py"]

