# TCP-Chat-Room

This simple terminal-based and GUI-enabled chat room utilizes Python's built-in socket and threading libraries to create a local connection between two clients using the Transmission Control Protocol (TCP). 

The server listens for client connections on 127.0.0.1:9090, and each connected client is prompted to enter a nickname. Messages from clients are broadcast to all other users in real time. The GUI client features a chat window, message entry box, and buttons for sending messages or exiting the chat. Background threading ensures the UI remains responsive while messages are being received.

**Run Through**

First, we want to get the server up and running. To do this, simply type the following command in the terminal:

![Image](https://github.com/user-attachments/assets/8923987d-9619-4101-9b89-0edae909b990)

The following confirmation message should appear in the terminal:

![Image](https://github.com/user-attachments/assets/740ce44d-2c47-4afc-8dee-46923a99fcc4)

Next, run the client file from your IDE or from terminal. This should make the box below appear:


