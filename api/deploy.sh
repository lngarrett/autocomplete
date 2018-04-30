#/bin/bash
docker rm -f ac-api
docker build -t ac-api .
docker run \
  --name="ac-api" \
  --publish=8000 \
  --restart="always" \
  --detach=true \
  --net=ac-net \
  ac-api
