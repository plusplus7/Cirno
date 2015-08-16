rm -rf "$1"/cirno > /dev/null 2>&1
mkdir "$1"/cirno
mkdir "$1"/cirno/conf
sed -e 's/SAMPLEPASSWORD/'$2'/g' sample_redis.conf > "$1"/cirno/conf/redis.conf
rm nohup.out
nohup redis-server "$1"/conf/redis.conf &
python set_db_for_release.py $2 $3
cd ..
rm nohup.out
nohup python server_main.py &
