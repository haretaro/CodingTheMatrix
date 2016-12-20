from plotting import plot
from image import file2image
import math

def centerize(s):
    r = [c.real for c in s]
    i = [c.imag for c in s]
    centre = (min(r) + max(r))/2 + (min(i) + max(i))*1j/2
    return {a - centre for a in s}

data = file2image('img01.png')
data = [[sum(pixel)/len(pixel) for pixel in row] for row in data]
pts = {x + (len(data) - y)*1j for y in range(len(data)) for x in range(len(data[0])) if data[y][x] < 120}

pts = [p * (math.e ** (1j * math.pi/4)) /2 for p in pts]
pts = centerize(pts)
plot(pts, len(data), browser='firefox')

