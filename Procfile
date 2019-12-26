release: chmod u+x mongo-setup/mongodb.sh && ./mongo-setup/mongodb.sh
web: gunicorn autoapp:web_app -b ${HOST}:${PORT} --chdir app --workers 4 --worker-class aiohttp.worker.GunicornWebWorker