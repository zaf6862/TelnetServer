# TelnetServer
This repo contains a python application that acts as a telnet server. Users can use a command line telnet client to connect to this server and experience a very basic telnet service. You need python3 to run this application. 

To run the server follow these steps:

1) Clone the repository to a local folder on your machine.

```
  git clone https://github.com/zaf6862/TelnetServer.git
```
2) Change current directory to the repository on your local machine and run the following command.
```
  python3 TelnetServer.py <portNumber>
```
   
Here \<portNumber\> is the port you want the server to listen on. It can be any positive integer.
To connect a telnet client to this server use the following command:

```
  telnet localhost <portNumber>
```
Where \<portNumber\> is the same as the one you specified for the server. Once you are connected ot the server, you can start issuing commands to it. Please type "help" as the command and hit enter to see a list of all the supported commands.

To run the unit tests for the server, run the following command. 
```
  python3 -m unittest test_CommandParser.py
```

## What I could have done with more time:
While I implemented all of the requirements listed in the assessment, there are a few things that I would have liked to add to the application but couldn't due to time constraints. These include the following. 

1) Unit tests for the network I/O part of the server code. 
2) Support for assignment expressions of the form x = y = z = 2 and x = y. Right now the only supported assignment expressions are of the form x = 1 or y = 2 (as specified in the requirements document). 
3) Right now the server only reads 4096 bytes from the client socket and those too only once. This is unstable because if some packets get delayed or if the command is longer than 4096 characters, the server will not be able to read the entire command and either miscalculate (if the command is a mathematical expression) or throw invalid command error (since it couldn't read the entire command). Both of these cases are extremely rare and unlikely in the scope of this assignment because both the server and the client are running on localhost and also, the user is not really expected to input an expression longer than 4096 bytes. However, in any real-case version of this application, this issue would need to be dealt with upfront. 
4) Make "eval()" in CommandParser.py safe. eval() is a system-level utility that can evaluate mathematical expressions but at the same time can execute compiled code. What that means is that a malicious user of this application can inject malware code as a command which can compromise the entire host machine. This, again, is not a concern in the scope of this assignment but in a real-worl version of this application, the eval() method would need to made much more secure essentially through input sanitization. 
5) Make an executable version of the application so that it is easier to interact with for users not familiar with computer programming. 
