FROM python:3.12-slim
WORKDIR /app
COPY simple_scanner/ /app/simple_scanner/
RUN python -m compileall -q /app/simple_scanner && python -m unittest discover -s simple_scanner -p 'test_*.py' -v
CMD ["python","-m","simple_scanner.execute_once","cron"]
