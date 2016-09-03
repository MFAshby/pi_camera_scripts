#! /bin/sh
# /etc/init.d/camera_provider.sh

### BEGIN INIT INFO
# Provides: camprovider
# Required-Start: $remote_fs $syslog
# Required-Stop: $remote_fs $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Start camera webprovider
# Description: Start camera provider
### END INIT INFO

USER=pi
HOME=/home/pi

export USER_HOME

case "$1" in
  start)
    echo "Starting camera provider"
    su - $USER -c "python3 ~/camera_scripts/python_camera_provider.py start"
    ;;
  stop)
    echo "Stopping camera provider"
    python3 ~/camera_scripts/python_camera_provider.py stop 
    ;;
  *)
    echo "Usage: /etc/init.d/camera_provider.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
