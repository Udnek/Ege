# import math
# def dist(xy0, xy1):
#     return math.sqrt((xy0[0]-xy1[0])**2 + (xy0[1]-xy1[1])**2)

starts = []
with open("27A_18678.txt") as f:
    lines = f.readlines()
    for i in lines:
        sp = i.strip().replace(",", ".").split("	")
        starts.append((float(sp[0]), float(sp[1])))

print(float(123.5).__mul__(4))

if __name__ == "__main__":
    print("kek")

# bestAnomalies = starts[:]
# bestDistance = float("inf")
#
# for center in starts:
#     anomalies = []
#     distance = 0
#     for star in starts:
#         d = dist(center, star)
#         if d > 1: anomalies.append(star)
#         else: distance += d
#
#     fl










