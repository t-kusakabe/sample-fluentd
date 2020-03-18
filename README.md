# sample-fluentd

## application server

```
docker run -it --rm --name my-app -v $(PWD)/test_app:/usr/src/myapp -w /usr/src/myapp/app -p 8080:8080 --log-driver=fluentd --log-opt fluentd-address=localhost:24220 --log-opt tag="docker.{{.Name}}" python:3 /bin/sh
```

```
cd /usr/src/myapp
pip install bottle
python main.py
```

## fluentd server

```
docker run -p 24220:24220 -p 24220:24220/udp -v $(PWD)/fluentd/config:/fluentd/etc -e FLUENTD_CONF=fluent.conf --name=fluentd --rm fluent/fluentd
```
