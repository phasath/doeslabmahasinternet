export ENV=production
export HOST=0.0.0.0
export PORT=5000
export AIO_ROOT=$(pwd)/app
export PYTHONPATH=$(pwd)/app
gunicorn autoapp:web_app -b ${HOST}:${PORT} --chdir app --workers 4 --worker-class aiohttp.worker.GunicornWebWorker