MASTER_IP=
PORT=$1

ssh -i ~/.ssh/penguin2017.pem -NL $PORT:localhost:$PORT ubuntu@$MASTER_IP
