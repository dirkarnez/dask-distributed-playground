from dask.distributed import Client
client = Client('127.0.0.1:8786')


def square(x):
        return x ** 2

def neg(x):
        return -x

# 
A = client.map(square, range(10))
B = client.map(neg, A)
total = client.submit(sum, B)

print(total.result())
