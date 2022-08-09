# USAGE

run app

```
podman run --rm -it -p 5080:5080 quay.io/aizquier/fake-app
```

Endpoints:

- /health: check status
- /down: simulate an outage
- /up: fix the outage
