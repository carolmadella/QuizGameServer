import socket

HOST = "127.0.0.1"
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to the quiz server. Get ready!")
print()

# Keep receiving messages from the server until we get the final score message
while True:
    data = client_socket.recv(1024)
    message = data.decode()

    if message.startswith("FINAL:"):
        # This is the last message, the quiz is over
        print(message[len("FINAL:"):])
        break
    else:
        # This message is a question, show it and ask the player to answer
        print(message)
        answer = input("Your answer: ")

        client_socket.sendall(answer.encode())

        # Get the result of that answer and show it
        result_data = client_socket.recv(1024)
        print(result_data.decode())
        print()

client_socket.close()