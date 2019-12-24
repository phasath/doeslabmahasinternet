export ENV=production
export AIO_HOST=0.0.0.0
export AIO_PORT=5000
export AIO_ROOT=$(pwd)/app
export PYTHONPATH=$(pwd)/app
gunicorn autoapp:web_app -b ${AIO_HOST}:${AIO_PORT} --chdir app --worker-class aiohttp.worker.GunicornWebWorker