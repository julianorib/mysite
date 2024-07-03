FROM cgr.dev/chainguard/python
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./mysite.python
