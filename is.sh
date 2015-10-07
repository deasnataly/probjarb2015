kill -9 $(ps aux | grep '[p]ython' | awk '{print $2}')
clear
clear
python tcp_server.py
