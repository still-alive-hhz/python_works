import time

n = 0  # 将 n 定义为全局变量
print("这是说n段神话的生成器。")

def gene():
    global n, speed
    if n >= 0:
        n += 1
        print("说", n, "段神话，话说那么一家。")
    time.sleep(speed)

x = int(input("请输入最终神话段数："))
speed = float(input("请输入速度（每多少秒输出一段神话）："))

for i in range(0, x):
    gene()
print("神话说完了。")