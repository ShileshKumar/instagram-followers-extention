FROM python:3.11-slim
WORKDIR /workspace
COPY . /workspace
RUN pip install brython
CMD ["brython-cli", "build"]
