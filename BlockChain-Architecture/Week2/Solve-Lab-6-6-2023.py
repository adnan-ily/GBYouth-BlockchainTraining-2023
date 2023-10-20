import hashlib
 

file_path = "./Lab 6-6-2023.pdf"  
with open(file_path, "rb") as file:
    file_data = file.read()

block_size = len(file_data) // 8
blocks = [file_data[i:i + block_size] for i in range(0, len(file_data), block_size)]
block_hashes = []
for block in blocks:
    hash_object = hashlib.sha256(block)
    block_hashes.append(hash_object.hexdigest())
print(hash_object)
print(len(block_hashes),[block_hashes ])
while len(block_hashes) > 1:
    temp_hashes = []
    for i in range(len(block_hashes) - 1):
        combined_hash = block_hashes[i] + block_hashes[i + 1]
        hash_object = hashlib.sha256(combined_hash.encode())
        temp_hashes.append(hash_object.hexdigest())
    block_hashes = temp_hashes

merkle_root = block_hashes[0]

print("Merkle Root:", merkle_root)