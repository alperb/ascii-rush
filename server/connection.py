import os
from socket import socket
import json

from errors.exceptions import WrongAnswerError

game_config = open("game/config.json", "r")
game_config = json.load(game_config)

WELCOME_MESSAGE = "Welcome player!\nNow you will be challenged with some labyrinth puzzles.\nYou will be given a map of the labyrinth and you will have to find the exit.\nYou will answer with the number of steps you have to take to reach the exit.\nType \"START\" to start. Good luck!\n"

flag_indexes = game_config['indexes']
        

class Connection:
    def __init__(self, conn: socket, addr: tuple):
        self.conn = conn
        self.addr = addr
        self.current_step = 0
        self.total_steps = len(game_config["schema"])

    def run(self):
        with self.conn:
            print('Connected by', self.addr)
            self.conn.sendall(bytes(WELCOME_MESSAGE, "utf-8"))
            while True:
                try:
                    data = self.conn.recv(1024)
                except ConnectionError as e:
                    print(f'Connection with {self.addr} has been reset.')
                    self.close()
                    break
                try:
                    splitted = data.decode().split(" ")
                    splitted = [s.strip() for s in splitted]
                    print(splitted)
                    if splitted[0] == "START":
                        self.send_game(self.current_step)
                    elif splitted[0] == "ANS":
                        self.send_game(self.current_step, int(splitted[1]))
                    else:
                        raise Exception("Invalid command")
                except WrongAnswerError as e:
                    print(e, 1)
                    self.conn.sendall(b'Wrong answer, try again.')
                    self.close()
                    break
                except Exception as e:
                    print(e, 2)
                    self.conn.sendall(b'Bruh, what was that?')
                    self.close()
                    break

                if not data:
                    self.close()
                    break

            

    def send_game(self, step: int, answer: int = None):
        if step >= self.total_steps:
            self.conn.sendall(b'\nCongratulations, you have completed the game!')
            self.close()
            return

        s = game_config["schema"][step]
        print(s)
        
        if 'answer' in s and answer != s['answer']:
            raise WrongAnswerError("Wrong answer was given")

        schema = s['schema']

        flag = 'SUCTF{' + os.getenv("FLAG") + '}'
        joined = "\n".join(schema)
        if '%' in joined:
            joined = joined.replace("%", flag[flag_indexes.index(step)])
        self.conn.sendall(bytes(f"\nSTEP {self.current_step}\n" + joined + '\n\n', "utf-8"))
        self.current_step += 1

    def close(self):
        print(f'Connection with {self.addr} has been closed.')
        self.conn.close()

    def replace_with_flag(self, s: str, flag_bit: str):
        return s.replace("%", flag_bit)