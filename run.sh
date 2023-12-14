source ./venv/bin/activate
kill -9 `ps -ef|grep python3|awk '{print $2}'`
nohup python3 main.py &