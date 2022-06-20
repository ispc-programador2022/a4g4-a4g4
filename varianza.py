import media as m
def varianza(vector):
    media = m.media(vector)
    acu = 0
    for i in range(0, len(vector)):
        acu += (vector[i] - media)**2
    return round(acu / (len(vector) - 1), 2)