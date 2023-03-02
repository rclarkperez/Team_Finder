import zmq

context = zmq.Context()
#  Socket to talk to server
print("Connecting to spike server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(2):
    if request == 0:
        region_input = input("Please enter team city/region: ")
        print(f"Sending request {region_input} …")
        socket.send_string(region_input)

        #  Get the reply.
        message = socket.recv()
        print(f"Received reply {region_input} [ {message} ]")
    if request == 1:
        team_name_input = input("Please enter team name: ")
        print(f"Sending request {team_name_input} …")
        socket.send_string(team_name_input)

        #  Get the reply.
        message = socket.recv()
        print(f"Here is the link to the {region_input} {team_name_input} logo [ {message} ]")

