# Static site generator

## a markdown to html static website generator, bundled with a simple web-server that allows us to publish the content.

<br>

### Requirements

- python3
- docker/podman (optional)

## running using python.
Running this with python.

```bash
python3 src/main.py
cd public && python3 -m http.server 8888
```


## running the test suite

```bash
python3 -m unittest discover -s src -vvv

# or you can use the ./test.sh script which uses the same command wrapped in a bash script..

./test.sh
```

## run using docker or podman

```bash
docker build -t static-site-generator .
docker run -p 8888:8888 static-site-generator


# or using podman

podman build -t static-site-generator . 
podman run -p 8888:8888 static-site-generator
```