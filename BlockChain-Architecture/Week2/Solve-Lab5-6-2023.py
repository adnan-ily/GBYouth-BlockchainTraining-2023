import hashlib
 
filename = input("Enter the input file name: ")
with open(filename,"rb") as f:
    bytes = f.read() # read entire file as bytes
    readable_hash256 = hashlib.sha256(bytes).hexdigest()
    print(readable_hash256)


filename = input("Enter the input file name: ")
with open(filename,"rb") as f:
    bytes = f.read() # read entire file as bytes
    readable_hashmd5 = hashlib.md5(bytes).hexdigest()
    print(readable_hashmd5)