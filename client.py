import socket

HOST = "127.0.0.1"
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("=" * 40)
print("Welcome to the Networking Quiz Game!")
print("Answer each question as it appears.")
print("=" * 40)
print()

while True:
    data = client_socket.recv(1024)
    message = data.decode()

    if message.startswith("FINAL:"):
        print(message[len("FINAL:"):])
        break
    else:
        print(message)

        # Keep asking until the player actually types something
        answer = input("Your answer: ").strip()
        while answer == "":
            print("Please type an answer before submitting.")
            answer = input("Your answer: ").strip()

        client_socket.sendall(answer.encode())

        result_data = client_socket.recv(1024)
        print(result_data.decode())
        print()

client_socket.close()
print("Thanks for playing!")