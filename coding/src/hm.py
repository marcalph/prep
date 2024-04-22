"""
HashMap can be beneficial:

if both these conditions are fulfilled:
    1. When we require repeated fast access to data during the execution of the algorithm.
    2. We need to store the relationship between two sets of data in order to compute the required result. 

but is not if no useful relation can be established between two sets of data.
"""


class MyHashMap():
    # Use the constructor below to initialize the 
    # hash map based on the keyspace
    def __init__(self):
        # Write your code here
        self.size=1007
        self.arr = [-1] * self.size

    def put(self, key, value):
        # Write your code here
        keyhash = key%self.size
        self.arr[keyhash]=value

    def get(self, key):
        # Replace this placeholder return statement with your code
        return self.arr[key%self.size]

    def remove(self, key):
        # Write your code here
        self.arr[key%self.size]=-1




class RequestLogger:
    def __init__(self, time_limit):
        # Initialize your data structure here
        self.hm = {}
        self.limit = time_limit

    # This function decides whether the message request should be accepted or rejected
    def message_request_decision(self, timestamp, request):
        # Replace this placeholder return statement with your code
        if request not in self.hm:
            self.hm[request] = timestamp
            return True
        if timestamp-self.hm[request]>=self.limit:
            self.hm[request]=timestamp
            return True
        return False
    
  
def fraction_to_decimal(numerator, denominator):
    string_result = ""
    if numerator == 0:
        return "0"
    if bool(numerator) ^ bool(denominator):
        string_result += "-"
        numerator*=-1
    
    hm  = {}
    remainder = numerator % denominator   
    string_result += str(numerator//denominator)

    if remainder==0:
        return string_result
    else:
        string_result+="."

    while remainder !=0:
        hm[str(remainder)] = len(string_result)
        numerator = 10*remainder
        string_result+=str(numerator//denominator)
        remainder = numerator%denominator
        print(hm)
        if str(remainder) in hm:
            append = ")"
            string_result += append
            return string_result[:hm[str(remainder)]]+"("+string_result[hm[str(remainder)]:]

    
    # Replace this placeholder return statement with your code
    return string_result