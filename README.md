# Implementing gRPC In Python

### Create venv (Optional)
```bash
python -m venv grpc-env
```

### Activate the virtual environnement 
```bash
grpc-enc\Scripts\Activate
```

### Install Requirements
```bash
pip install -r requirements.txt
```

### Generating the Grpc files 
```bash
python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ order.proto
```

### Run server
```bash
python server.py
```

### Run client
```bash
python client.py
```






