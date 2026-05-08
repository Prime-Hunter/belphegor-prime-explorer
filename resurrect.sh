pkill python
echo "Amanda" > amanda_input.txt
nohup python -u src/name_hunter.py < amanda_input.txt >> name_primes.txt 2>&1 &
nohup python -u src/twin_giant_hunter.py >> twin_discovery.txt 2>&1 &
nohup python -u src/limit_pusher.py >> limit_pusher_log.txt 2>&1 &
echo "🚀 All Hunters Resurrected!"
