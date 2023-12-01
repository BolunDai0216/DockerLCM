# DockerLCM
Test LCM Communication for Docker Containers

## Steps (Ubuntu 20.04)

1. Build the Docker image

```bash
sudo docker build -t dockerlcm .
```

2. Run the Docker image

```bash
sudo docker run -it --net host --name lcm_container dockerlcm:latest
```

3. Run the LCM publisher (in the Docker container)

```bash
python3 publisher.py
```

4. Run the LCM subscriber (on the host machine)

```bash
python3 listener.py
```

You should see the following messages being published in the host terminal

```bash
Received message on channel "EXAMPLE"
   timestamp   = 1701439070
   position    = (1.0, 2.0, 3.0)
   orientation = (1.0, 0.0, 0.0, 0.0)
   ranges: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
   name        = 'example string'
   enabled     = True
```


