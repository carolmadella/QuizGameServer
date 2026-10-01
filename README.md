

## Overview

As I'm continuing to grow as a software developer, I wanted to learn how programs communicate with each other over a network, since almost every modern application depends on this in some way. For this project, I built a simple quiz game using Python's socket library to practice client-server communication with real TCP connections.

The project has two separate programs: a server (`server.py`) that stores the quiz questions and answers and checks each response, and a client (`client.py`) that a player runs to connect to the server, see the questions, and submit answers. The quiz questions are stored in a separate file, `questions.json`, so they can be edited or expanded without changing the code itself.

**To run the software:**
1. Start the server first by running `python server.py`. It will wait for a player to connect.
2. In a separate terminal, run `python client.py` to connect as the player.
3. Answer each question as it's displayed. The server checks each answer and sends back whether it was correct, and shows the final score once all questions are complete.

My purpose in writing this software was to understand, hands-on, how two separate programs can exchange information over a network connection, including how to structure a simple request-response protocol, and how to handle real-world issues like a player disconnecting unexpectedly.

[Software Demo Video](http://youtube.link.goes.here)

## Network Communication

This project uses the **client-server** architecture. The server runs first and waits for a connection; the client connects to it, and all communication happens between those two programs.

Communication uses **TCP** (via Python's `socket.SOCK_STREAM`), since the quiz needs each message to arrive reliably and in the correct order. Both programs communicate over `localhost` (127.0.0.1) on **port 65432**.

Messages are sent as plain text, encoded into bytes before sending and decoded back into text after receiving. The exchange follows this pattern for each question: the server sends the question text (including its progress, like "Question 2 of 5"), the client sends back the player's typed answer, and the server replies with either "Correct!" or the correct answer if the response was wrong. After the last question, the server sends a final message prefixed with `FINAL:` containing the player's total score and a short reaction to their performance, which signals to the client that the quiz is complete.

## Development Environment

I used Visual Studio Code as my code editor, along with its Python extension, and ran the programs using Python 3.13 from the terminal. I used Git and GitHub for version control.

The project uses only Python's built-in libraries: `socket` for the network communication, and `json` for reading the quiz questions from the `questions.json` file.

## Useful Websites

* [Python socket — Low-level networking interface](https://docs.python.org/3/library/socket.html)
* [Python json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Client-Server model — Wikipedia](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
* [What's the Difference Between TCP and UDP? — How-To Geek](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)

## Future Work

* Add a graphical user interface (GUI) instead of the command-line interface
* Support more than one client/player connecting to the server at the same time
* Add more quiz questions and organize them by category or difficulty
* Add a way to randomize the order questions are asked in each time the quiz runs