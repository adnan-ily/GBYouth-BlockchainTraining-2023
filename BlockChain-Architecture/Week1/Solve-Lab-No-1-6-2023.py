import hashlib,bcrypt

my_str = "Adnan Ali"
my_str_as_bytes = str.encode(my_str)
type(my_str_as_bytes) # ensure it is byte representation
print(my_str_as_bytes)
salt = bcrypt.gensalt()
bcrypt_hash = bcrypt.hashpw(my_str_as_bytes, salt)
print("bcrypt Hash", bcrypt_hash)

# m = hashlib.md5()
# m.update((my_str_as_bytes))
# md5string=m.digest()
# print(md5string)
# Python 3 code to demonstrate
# SHA hash algorithms.

# initializing string
str = "Adnan Ali"

# encoding GeeksforGeeks using encode()
# then sending to SHA256()
result = hashlib.sha256(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

print ("\r")

str = "Adnan Ali"
result = hashlib.sha384(str.encode())
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())

print ("\r")


str = "Adnan Ali"
result = hashlib.sha224(str.encode())
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())

print ("\r")


str = "Adnan Ali"
result = hashlib.sha512(str.encode())
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())

print ("\r")


str = "Adnan Ali"
result = hashlib.sha1(str.encode())
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())