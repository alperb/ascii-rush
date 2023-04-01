import random
import json

class PuzzleGenerator:
    def __init__(self, flag: str):
        self.flag = flag
        self.step = 0

    def generate_steps(self, step_count: int):
        steps = []
        width = 10
        flag_bit = 0

        for i in range(0, step_count):
            if len(steps) == 0:
                entry = random.randint(0, width)
            else:
                entry = steps[-1]["exit"]

            should_write_flag = True if random.randint(0, 10) < 2 else False
            if should_write_flag:
                steps.append(self.generate_step(entry, width, self.flag[flag_bit]))
                flag_bit += 1
                if flag_bit == len(self.flag):
                    break
            else:
                steps.append(self.generate_step(entry, width))

            if (i != 0) and (i % 10 == 0):
                width += 2
        return steps

    def generate_step(self, entry: int, width: int, flag_bit: str = None) -> dict:
        step_schema = [
            "",
            "",
            "",
        ]

        random_answer = random.randint(0, width - 1)
        print(random_answer)

        # fill the middle of the step
        step_schema[1] += '|' + (' ' * (width)) + "|"  # -2 because of the borders

        # fill the bottom of the step
        step_schema[2] += '|'
        for i in range(0, width):
            if i == entry:
                step_schema[2] += ' '
            else:
                step_schema[2] += '='
        step_schema[2] += '|'

        # fill the top of the step
        step_schema[0] += '|'
        for i in range(0, width):
            if i == random_answer:
                if flag_bit is not None:
                    step_schema[0] += "%"
                else:
                    step_schema[0] += ' '
            else:
                step_schema[0] += '='
        step_schema[0] += '|'

        return {
            "schema": step_schema,
            "exit": random_answer,
            "entry": entry,
        }

g = PuzzleGenerator("SUCTF{TcP_1s_r34lly_Aw3s0m3}")
steps = g.generate_steps(1000)

new_steps = []

for i in range(len(steps)):
    if i == 0:
        new_steps.append({"schema": steps[i]['schema']})
    else:
        d = {
            "schema": steps[i]['schema'],
            "answer": steps[i-1]['exit'] - steps[i-1]['entry']
        }
        new_steps.append(d)
    
indexes = []
for i in range(len(new_steps)):
    if '%' in new_steps[i]['schema'][0]:
        indexes.append(i)

f = open("config.json", "w")
f.write(json.dumps({"indexes": indexes, "schema": new_steps}))

