#Print the no.of tiles required to  fill the n x m matrix using K squares of a tile.
# l,b,T = map(int,input().split())
l = int(input())
b = int(input())
T = int(input())
import math
rows = math.ceil(l/T)
cols = math.ceil(b/T)
print("AREA - ", rows*cols)
#parliamentry square
