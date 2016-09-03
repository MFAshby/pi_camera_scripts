#! /bin/sh
# /etc/init.d/camera_server.sh

### BEGIN INIT INFO
# Provides: camserver
# Required-Start: $remote_fs $syslog $camprovider
# Required-Stop: $remote_fs $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Start camera webserver
# Description: Start camera webserver
### END INIT INFO

USER=pi
HOME=/home/pi

export USER_HOME

case "$1" in
  start)
    echo "Starting camera and webserver"
    su - $USER -c "python3 ~/camera_scripts/python_webcam_server.py start"
    ;;
  stop)
    echo "Stopping camera server"
    python3 ~/camera_scripts/python_webcam_server.py stop 
    ;;
  *)
    echo "Usage: /etc/init.d/camera_server.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
