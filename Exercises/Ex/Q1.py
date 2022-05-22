

def timeAngale(h, m):

    if h > 0:
        angle = (h/12)*360 + (30/2)
        angle -= (m/60)*360

    return angle


print(timeAngale(1, 30))
