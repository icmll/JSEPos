
# 启动daphne服务，
SERVICE_NAME="daphne"

while [ -n "$1" ];
do
    case "$1" in
        "start")
            HANDLE="$1"
            echo 'do start!'
            shift 1
            ;;
        "stop")
            HANDLE="$1"
            echo 'do stop!'
            shift 1
            ;;
        "restart")
            HANDLE="$1"
            echo 'do restart!'
            shift 1
            ;;
        "status")
            HANDLE="$1"
            echo 'do status!'
            shift 1
            ;;
        "show")
            HANDLE="$1"
            echo 'do show!'
            shift 1
            ;;
        "-c"[1-3][0-9])
            CONCURRENCY="${1:2}"
            echo 'set worker num '${CONCURRENCY}
            shift 1
            ;;
        "-c"[1-9])
            CONCURRENCY="${1:2}"
            echo 'set worker num '${CONCURRENCY}
            shift 1
            ;;
        *)
            echo 'nothing to do!'
            shift 1
            ;;
    esac
done

if [ $HANDLE == "start" ];then
    PID=""
    if [ -f "../celery_worker.pid" ];then
        echo '../celery_worker.pid 已存在!'
        exit 1
    fi
    source /root/pyenv/grimlock/bin/activate
    COMMAND="python manage.py celery multi $HANDLE worker --autoscale=40,$CONCURRENCY -Ofair --pidfile=../celery_worker.pid --loglevel=debug  --logfile=logs/celery_worker.log"
    eval $COMMAND
elif [ $HANDLE == "restart" ];then
    PID=""
    if [ -f "../celery_worker.pid" ];then
        PID=`cat ../celery_worker.pid`
    else
        echo '../celery_worker.pid 不存在!'
        exit 1
    fi
    ps -ef | grep "${APP_NAME}" | grep "$PID" | grep -v "grep" | awk '{print $2}'
    # kill -s 9 `ps -ef | grep "${APP_NAME}" | grep "$PID" | grep -v "grep" | awk '{print $2}'`
    source /root/pyenv/grimlock/bin/activate
    COMMAND="python manage.py celery multi $HANDLE worker --autoscale=40,$CONCURRENCY -Ofair --pidfile=../celery_worker.pid --loglevel=debug  --logfile=logs/celery_worker.log"
    eval $COMMAND
elif [ $HANDLE == "stop" ];then
    PID=""
    if [ -f "../celery_worker.pid" ];then
        PID=`cat ../celery_worker.pid`
    else
        echo '../celery_worker.pid 不存在!'
        exit 1
    fi
    ps -ef | grep "${APP_NAME}" | grep "$PID" | grep -v "grep" | awk '{print $2}'
    # kill -s 9 `ps -ef | grep "${APP_NAME}" | grep "$PID" | grep -v "grep" | awk '{print $2}'`
    source /root/pyenv/grimlock/bin/activate
    COMMAND="python manage.py celery multi $HANDLE worker --pidfile=../celery_worker.pid"
    eval $COMMAND
elif [ $HANDLE == "kill" ];then
    PID=""
    if [ -f "../celery_worker.pid" ];then
        PID=`cat ../celery_worker.pid`
    else
        echo '../celery_worker.pid 不存在!'
        exit 1
    fi
    ps -ef | grep "${APP_NAME}" | grep "$PID" | grep -v "grep" | awk '{print $2}'
    # kill -s 9 `ps -ef | grep "${APP_NAME}" | grep "$PID" | grep -v "grep" | awk '{print $2}'`
    source /root/pyenv/grimlock/bin/activate
    COMMAND="python manage.py celery multi $HANDLE worker --pidfile=../celery_worker.pid"
    eval $COMMAND
elif [ $HANDLE == "status" ];then
    PID=""
    if [ -f "../celery_worker.pid" ];then
        PID=`cat ../celery_worker.pid`
    else
        echo '../celery_worker.pid 不存在!'
    fi
    ps -ef | grep "${APP_NAME}" | grep "$PID" | grep -v "grep" | awk '{print $2}'
else
    echo ""
fi