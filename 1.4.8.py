from plotting import plot
S = {1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j, 2+2j, 3+2j}
plot({s*1j/2 for s in S}, 4, browser='firefox')
