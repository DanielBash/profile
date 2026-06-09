"""- Gunicorn settings"""

bind = "0.0.0.0:5000"
workers = 1
worker_class = "eventlet"
worker_connections = 1000
timeout = 30
keepalive = 2
spew = False

accesslog = None
errorlog = None
loglevel = "info"

proc_name = "profile_gunicorn"
