FROM python:3.12-slim
WORKDIR /app
COPY engineering_agent/ /app/
RUN python -m unittest discover -s /app -p 'test_*.py' -v
EXPOSE 8080
CMD ["python", "/app/service.py"]
