MASTER_IP=52.33.166.70
PORT=$1

ssh -i ~/.ssh/penguin2017.pem -NL $PORT:localhost:$PORT ubuntu@$MASTER_IP
