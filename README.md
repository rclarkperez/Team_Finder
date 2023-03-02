# NFL-Team_Finder

COMMUNICATION CONTRACT:
Microservice named 'Team Finder' was constructed for CS361 at Oregon State University. This microservice is going to be used in conjunction with my partner's NFL Fantasy Football application. The microservice works by taking a NFL team region and name as inputs in one file and uses ZeroMQ communication pipeline to send it to another file. When the parameters are sent to the second file, what is returned to the original file is the URL link to the logo for the given team. 

To Request Data: The ZeroMQ communication pipeline is used from the team_input.py file to send data in a message variable assigned to 'socket.send'. What is sent are two subsequent user inputs, each assigned to region_input and team_name_input variables respectively. 


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
for request in range(2):
    if request == 0:
        region_input = input("Please enter team city/region: ")
        print(f"Sending request {region_input} …")
        socket.send_string(region_input)

        message = socket.recv()
        print(f"Received reply {region_input} [ {message} ]")
    if request == 1:
        team_name_input = input("Please enter team name: ")
        print(f"Sending request {team_name_input} …")
        socket.send_string(team_name_input)

To Receive Data: The ZeroMQ communication pipeline is used from the Team_finder.py file, which is where microservice itself is located. The microservice receives the input variables from team_input.py through socket.recv(). This is then assigned to message. There will be two messages sent, one that is assigned to variable: 'team_name', the other assigned to variable 'region'. These two variables are then given to the main microservice function 'logo_finder' as parameters. What is returned is the team logo URL on wikipedia or an 'invalid input' error message set to variable 'result'. This is then sent as the result through socket.send_string(f'{result}'). 


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
count = 0
while True:

    message = socket.recv()
    if count == 0:
        region_input = str(message)[1:].replace("'", "")
        '_'.join([word.capitalize() for word in region_input])
        print(region_input)
        #  Do some 'work'
        time.sleep(1)

        socket.send(b"Please send team data")
        print(f"Received request: {message}")

        count += 1

    else:
        team_name_input = str(message)[1:].replace("'", "")
        '_'.join([word.capitalize() for word in team_name_input])
        print(team_name_input)
        #  Do some 'work'
        time.sleep(1)

        result = logo_finder(region_input, team_name_input)
        socket.send_string(f'{result}')
        print(f"Received request: {message}")


