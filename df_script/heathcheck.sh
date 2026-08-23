HOST_FILE="hosts.txt"

printf "%-20s %-10s %-10s\n" "HOST" "STATUS" "TIME(ms)"
printf "%-20s %-10s %-10s\n"  "----" "------" "-------"

while read -r host; do
    [ -z "$host" ] && continue
    result=$(ping -c 1 -W 2 "$host" 2>/dev/null)
    if [ $? -eq 0 ]; then
        time_ms=$(echo "$result" | grep -oP 'time=\K[0-9.]+')
        printf "%-20s %-10s %-10s\n" "$host" "OK" "$time_ms"
    else
        printf "%-20s %-10s %-10s\n" "$host" "Fail" "-"
    fi
done < "$HOST_FILE"