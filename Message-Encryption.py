import string

# Get the message to be encrypted
message = input('Enter the message to be encrypted: ')

# Generate a random key
key = ''.join(
    [random.choice(
        string.ascii_letters + string.digits + string.punctuation
    ) for i in range(len(message))]
)

# Encrypt the message
encrypted_message = ''.join(
    [chr(ord(char) ^ ord(key[index]))
     for index, char in enumerate(message)]
)

# Print the results
print('Original message:', message)
print('Encrypted message:', encrypted_message)
print('Key:', key)