from SshToServer import SshToServer


my_ssh = SshToServer("/Users/markofir/Downloads/key-pair.pem", "51.20.1.114", "ubuntu")


print("Insert your commands as 'ubuntu' user\n"
      "Use the /home/ubuntu/ directory on the EC2\n"
      "Or type 'exit' to quit")

while True:
    command = input("Type your command: ")
    if command == "exit":
        break
    stdout, stderr = my_ssh.runRemoteCommand(command) or ("", "Failed to run command")

    if len(stderr) != 0:
        print("ERROR: " + stderr)
    else:
        print(stdout)
