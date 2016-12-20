from plotting import plot
S = {1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j, 2+2j, 3+2j}

def centerize(s):
    r = [c.real for c in s]
    i = [c.imag for c in s]
    centre = (min(r) + max(r))/2 + (min(i) + max(i))*1j/2
    return {a - centre for a in s}

plot(centerize(S), 4, browser='firefox')
