THORLORD=90
LOGFILE=/var/log/disk-logfile.log
USAGE=$(df / | tail -1 | awk {'print $5'} | tr -d '%')
if [ "$USAGE" -gt "$THORLORD" ]; then
    echo "WARNING, your disk "$USAGE"%  - $(data '+%Y-%m-%d  %H:%M:%S' )" >> "$LOGFILE"
else
    echo "OK usage="$USAGE"%"
fi