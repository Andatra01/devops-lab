LOG_DIR="/var/log/myapp"
DAYS=7
COUNT=$(find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS | wc -l)

if [ "$COUNT" -gt 0 ]; then
    find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS -delete
    echo "$(date): Удалено $COUNT файлов старше $DAYS дней"
else
    echo "$(date) - Нечего удалять"
fi