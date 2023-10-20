import hashlib


def calculate_hash(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    return sha256.hexdigest()

sender_email = "my@gmail.com"
recipient_email = "nust_blockchain@nust.com"
email_subject = "task2"
email_body = "This is final results of lab task final."
nonce = 0

def taskffff(sender, recipient, subject, body, nonce):
    message = sender + recipient + subject + body + str(nonce)
    attempts = 0
    while True:
        attempts += 1
        hash_result = calculate_hash(message)
        if hash_result[:4] == "ffff":
            break
        nonce += 1
        message = sender + recipient + subject + body + str(nonce)

    return attempts, hash_result

attempts, hash_result = taskffff(sender_email, recipient_email, email_subject, email_body, nonce)
print("Attempts:", attempts)
print("Hash Result:", hash_result)