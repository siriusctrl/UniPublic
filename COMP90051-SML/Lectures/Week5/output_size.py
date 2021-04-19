import math

def op_size(ip_size, kernel_size, stride, padding=0):
    return math.ceil((ip_size - kernel_size+1)/stride) + 2*padding 

if __name__ == "__main__":
    print(op_size(5, 3, 1))
