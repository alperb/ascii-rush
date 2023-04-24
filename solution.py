import socket

def find_exit(lab: str):
    for char_idx in range(len(lab)):
        char = lab[char_idx]

        if char != "=" and char != "|":
            return {"idx": char_idx, "char": char}
        
def find_entrance(lab: str):
    for char_idx in range(len(lab)):
        char = lab[char_idx]

        if char != "=" and char != "|":
            return {"idx": char_idx}

HOST = "0.0.0.0"  # The server's hostname or IP address
PORT = 9900  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    
    # start the game
    s.sendall(b"START")
    flag = ""
    responses = ['Bruh, what was that?', 'Wrong answer, try again.', '\nCongratulations, you have completed the game!']
    
    while True:
        data = s.recv(1024)
        d = data.decode()
        if d in responses:
            break
        
        splitted = d.split("\n")

        labyrinth = splitted[2:-2]
        top_layer = labyrinth[0]
        bottom_layer = labyrinth[2]

        entrance = find_entrance(bottom_layer)
        exit = find_exit(top_layer)
        ans = exit["idx"] - entrance["idx"]
        if exit['char'] != ' ':
            flag += exit['char']
        s.sendall(bytes(f'ANS {ans}', "utf-8"))
        if not data:
            break
        
    print(flag)