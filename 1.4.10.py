from plotting import plot
from image import file2image

data = file2image('img01.png')
data = [[sum(pixel)/len(pixel) for pixel in row] for row in data]
s = {x + (len(data) - y)*1j for y in range(len(data)) for x in range(len(data[0])) if data[y][x] < 120}
plot(s, len(data), browser='firefox')



