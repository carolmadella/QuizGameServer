import socket
import json

HOST = "127.0.0.1"
PORT = 65432

# Load the quiz questions and answers from the JSON file.
# Only the server ever sees this file, the client never has access to the answers.
with open("questions.json", "r") as file:
    quiz_data = json.load(file)


def check_answer(user_answer, correct_answer):
    """Compares the player's answer to the correct one, ignoring capitalization."""
    return user_answer.strip().lower() == correct_answer.strip().lower()


# Set up the server socket: IPv4 (AF_INET) over TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((HOST, PORT))
except OSError:
    print("Could not start the server: port", PORT, "is already in use.")
    print("Make sure no other copy of server.py is already running, then try again.")
    exit()
server_socket.listen()

print("Quiz server is running and waiting for a player on port", PORT, "...")

# Wait for a client to connect
connection, client_address = server_socket.accept()
print("Player connected from", client_address)

score = 0
total_questions = len(quiz_data)

# Go through each question one at a time
for item in quiz_data:
    # Send the question text to the client
    connection.sendall(item["question"].encode())

    # Wait for the client's answer
    data = connection.recv(1024)

    # An empty response means the client disconnected
    if not data:
            
            print("Player disconnected before finishing the quiz.")
            connection.close()
            server_socket.close()
            exit()

    player_answer = data.decode()

    # Check the answer and prepare a response message
    if check_answer(player_answer, item["answer"]):
        score = score + 1
        result_message = "Correct!"
    else:
        result_message = "Wrong. The correct answer was: " + item["answer"]

    # Send the result back to the client
    connection.sendall(result_message.encode())

# After all questions are done, send a final message starting with "FINAL:"
# so the client knows the quiz is over and can display the final score.
final_message = "FINAL:You scored " + str(score) + " out of " + str(total_questions)
connection.sendall(final_message.encode())

connection.close()
server_socket.close()
print("Quiz finished. Player scored", score, "out of", total_questions)
print("Server closed.")