# TCP-Chat-Room

This simple terminal-based and GUI-enabled chat room utilizes Python's built-in socket and threading libraries to create a local connection between two clients using the Transmission Control Protocol (TCP). 

The server listens for client connections on 127.0.0.1:9090, and each connected client is prompted to enter a nickname. Messages from clients are broadcast to all other users in real time. The GUI client features a chat window, message entry box, and buttons for sending messages or exiting the chat. Background threading ensures the UI remains responsive while messages are being received.

**Run Through**

First, we want to get the server up and running. To do this, simply type the following command in the terminal:

![Image](https://github.com/user-attachments/assets/8923987d-9619-4101-9b89-0edae909b990)

The following confirmation message should appear in the terminal:

![Image](https://github.com/user-attachments/assets/740ce44d-2c47-4afc-8dee-46923a99fcc4)

Next, run the client file from your IDE or from terminal. This should make the box below appear:

![Image](https://github.com/user-attachments/assets/0cbe7276-bcda-4226-8fd2-847a448959b2)

Enter a nickname and select the OK button. This will closeout the nickname window, and make the Chat Client appear:

![Image](https://github.com/user-attachments/assets/784da74c-42c2-48ea-8e36-82f4b23a8104)

Run another iteration of the client via terminal: 

![Image](https://github.com/user-attachments/assets/8558ff2e-0100-4d45-81d3-c02492f75e02)

Enter another nickname and select the OK button. Another Chat Client window should appear with the second nickname listed: 

<img width="615" alt="Image" src="https://github.com/user-attachments/assets/5e603232-ef09-48e0-afb7-486cdfb37989" />

The two clients will now be able to share messages with each other:

![Image](https://github.com/user-attachments/assets/df846cd3-5cf6-4705-96ea-640ee235a165)

The server will also notify you when users have exited the Chat Client:
![Image](https://github.com/user-attachments/assets/68b99d35-ebb4-436e-9592-916677dc4d04)


The server will keep a log of the conversation:

![Image](https://github.com/user-attachments/assets/49440b2a-2e73-4be3-9ecf-4a3e861f05ac)


