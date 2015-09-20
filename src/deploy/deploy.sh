ps -ef | grep redis-server | grep -v grep | awk '{print $2}' | xargs kill
ps -ef | grep "python server_main.py"  | grep -v grep | awk '{print $2}' | xargs sudo kill
rm -rf "$1"/cirno > /dev/null 2>&1
mkdir "$1"/cirno
mkdir "$1"/cirno/conf
sed -e 's/SAMPLEPASSWORD/'$2'/g' sample_redis.conf > "$1"/cirno/conf/redis.conf
rm nohup.out > /dev/null 2>&1
nohup redis-server "$1"/cirno/conf/redis.conf &
sleep 2
python set_db_for_release.py $2 $3
cd ..
sudo rm nohup.out > /dev/null 2>&1
sudo nohup python server_main.py $3 &
