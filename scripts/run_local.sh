export ENV=development
export AIO_HOST=0.0.0.0
export AIO_PORT=5000
export AIO_LIVERELOAD=True
export AIO_ROOT=$(pwd)/app
export PYTHONPATH=$(pwd)/app
adev runserver --host ${AIO_HOST} --port ${AIO_PORT} --root ${AIO_ROOT} --livereload --verbose app/autoapp.py
