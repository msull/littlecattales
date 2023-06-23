source prod.env.sh
echo $DOMAIN
git pull && docker build . -t littlecattales:latest && docker stack deploy -c docker-compose.prod.yaml littlecattales && docker service update littlecattales_littlecattales --force

docker ps
