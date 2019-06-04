echo $1
source /root/.bash_profile
if [[ ! -d "/home/deploy/app/jsepos" ]];
then
    echo "/home/deploy/app/jsepos is not exists!"
    exit 1
fi

cd /home/deploy/app/jsepos
if [[ $1 = "start" ]];
then
    echo "start"
    pyenv activate py365
    nohup daphne -b 0.0.0.0 -p 8888 jsepos.asgi:application --access-log ./logs/daphne_access.log > ./logs/nohup.out & echo $! > ./logs/daphne.pid
elif [[ $1 = "stop" ]];
then
    echo "stop"
    pid=$(ps -ef | grep "py365/bin/daphne -b 0.0.0.0 -p 8888" | grep -v "grep " | awk '{print $2}')
    if [[ -n $pid ]];then
        echo $pid | xargs kill -9 $pid
    fi
    echo "app is not running"
elif [[ $1 = "restart" ]];
then
    echo "restart"
    pid=$(ps -ef | grep "py365/bin/daphne -b 0.0.0.0 -p 8888" | grep -v "grep " | awk '{print $2}')
    if [[ -n $pid ]];then
        echo $pid | xargs kill -9
    fi
    echo "app is not running"
    pyenv activate py365
    nohup daphne -b 0.0.0.0 -p 8888 jsepos.asgi:application --access-log ./logs/daphne_access.log > ./logs/nohup.out & echo $! > ./logs/daphne.pid
else
    echo "need a command line parament start or stop or  restart!"
fi