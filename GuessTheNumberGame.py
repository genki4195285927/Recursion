import sys, random

sys.stdout.buffer.write(b"select min num : ")
sys.stdout.flush()
n = sys.stdin.buffer.readline()
n = int(n.decode())

sys.stdout.buffer.write(b"select max num : ")
sys.stdout.flush()
m = sys.stdin.buffer.readline()
m = int(m.decode())

ans = random.randint(n, m + 1)
user_ans = n - 1

while user_ans != ans:
    sys.stdout.buffer.write(b"guess the number : ")
    sys.stdout.flush()
    user_ans = sys.stdin.buffer.readline()
    user_ans = int(user_ans.decode())

sys.stdout.buffer.write(b"conglatulation!!!")
sys.stdout.flush()