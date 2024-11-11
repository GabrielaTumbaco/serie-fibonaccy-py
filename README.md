# Fibonacci-PY 🐍

This repository contains a Python program that generates and prints the Fibonacci sequence up to a specified number of terms. Useful for learning about Fibonacci numbers or practicing Python programming.

## Description ✍️

TThe program generates the Fibonacci sequence starting from 0 and 1, and continues up to the specified limit.

## Requirements

- **Python 3.x** or higher
- **Git** to clone the repository
  
## How to Clone and Run

To clone this repository to your local machine, use the following commands:

```bash
git clone https://github.com/GabrielaTumbaco/serie-fibonaccy-py.git
cd serie-fibonaccy-py
```
## To run the program:

python fibonacci

## Dockerization 🐋
<ol>
  Step 1: Build the Docker Image

```bash

docker build -t fibonacci-py .
```
  Step 2: Tag the Image

```bash

docker tag fibonacci-py gltumbaco/fibonacci-py:latest
```

  Step 3: Push Image to Docker Hub
```bash
docker push gltumbaco/fibonacci-py:latest
```
</ol>

## Link to Docker Hub 👩‍💻

Fibonacci-PY on Docker Hub: https://hub.docker.com/repository/docker/gltumbaco/fibonacci-py/general
