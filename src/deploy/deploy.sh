rm -rf "$1"/cirno > /dev/null 2>&1
mkdir "$1"/cirno
mkdir "$1"/cirno/conf
sed -e 's/SAMPLEPASSWORD/'$2'/g' sample_redis.conf > "$1"/cirno/conf/redis.conf
nohup redis-server "$1"/conf/redis.conf &
cd ..
nohup python server_main.py &
