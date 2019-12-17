'''

    Bresenhaim's Algorithm :

        y(i+1) = -> yi + 1
                 -> yi

    Batasan Masalah : Digunakan per 2 titik

    Program by prokoding
    
'''

class Bresenhaim :

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def start(self):
        point_x = []
        point_y = []
        pn = []
        
        #mencari delta x dan delta y
        d_x = abs(int(self.x2 - self.x1))
        d_y = abs(int(self.y2 - self.y1))

        d_x_norm = int(self.x2 - self.x1)
        d_y_norm = int(self.y2 - self.y1)
       

        #ploting p0, x0, y0
        point_x.append(self.x1)
        point_y.append(self.y1)

        if d_x > d_y :
            #mendapatkan p0
            po = (2 * d_y) - (d_x)
            pn.append(po)
            for i in range(1,d_x+1,1):
                if pn[i-1] < 0 :
                    if d_x_norm > 0:
                        point_x.append(point_x[i-1] + 1)
                    else :
                        point_x.append(point_x[i-1] - 1)
                    point_y.append(point_y[i-1])
                    pn.append(pn[i-1] + 2 * d_y)
                else:
                    if d_x_norm > 0 and d_y_norm > 0:
                        point_x.append(point_x[i-1] + 1)
                        point_y.append(point_y[i-1] + 1)
                    elif d_x_norm < 0 and d_y_norm < 0:
                        point_x.append(point_x[i-1] - 1)
                        point_y.append(point_y[i-1] - 1)
                    elif d_x_norm < 0 and d_y_norm > 0 :
                        point_x.append(point_x[i-1] - 1)
                        point_y.append(point_y[i-1] + 1)
                    elif d_x_norm > 0 and d_y_norm < 0:
                        point_x.append(point_x[i-1] + 1)
                        point_y.append(point_y[i-1] - 1)
                        pn.append(pn[i-1] + (2 * d_y) - (2 * d_x))
                    pn.append(pn[i-1] + (2 * d_y) - (2 * d_x))

                    
        elif d_x < d_y :
            po = (2 * d_x) - (d_y)
            pn.append(po)
            for i in range(1,d_y+1,1):
                if pn[i-1] < 0 :
                    if d_y_norm > 0:
                        point_y.append(point_y[i-1] + 1)
                    else :
                        point_y.append(point_y[i-1] - 1)
                    point_x.append(point_x[i-1])
                    pn.append(pn[i-1] + 2 * d_x)
                else:
                    if d_x_norm > 0 and d_y_norm > 0:
                        point_x.append(point_x[i-1] + 1)
                        point_y.append(point_y[i-1] + 1)
                    elif d_x_norm < 0 and d_y_norm < 0:
                        point_x.append(point_x[i-1] - 1)
                        point_y.append(point_y[i-1] - 1)
                    elif d_x_norm < 0 and d_y_norm > 0 :
                        point_x.append(point_x[i-1] - 1)
                        point_y.append(point_y[i-1] + 1)
                    elif d_x_norm > 0 and d_y_norm < 0:
                        point_x.append(point_x[i-1] + 1)
                        point_y.append(point_y[i-1] - 1)
                        
                    pn.append(pn[i-1] + (2 * d_x) - (2 * d_y))

        elif d_x == d_y :
            po = (2 * d_y) - (d_x)
            pn.append(po)
            for i in range(1,d_x+1,1):
                if pn[i-1] < 0 :
                    if d_x > 0:
                        point_x.append(point_x[i-1] + 1)
                    else :
                        point_x.append(point_x[i-1] - 1)
                    point_y.append(point_y[i-1])
                    pn.append(pn[i-1] + 2 * d_y)
                else:
                    if d_x_norm > 0 and d_y_norm > 0:
                        point_x.append(point_x[i-1] + 1)
                        point_y.append(point_y[i-1] + 1)
                    elif d_x_norm < 0 and d_y_norm < 0:
                        point_x.append(point_x[i-1] - 1)
                        point_y.append(point_y[i-1] - 1)
                    elif d_x_norm < 0 and d_y_norm > 0 :
                        point_x.append(point_x[i-1] - 1)
                        point_y.append(point_y[i-1] + 1)
                    elif d_x_norm > 0 and d_y_norm < 0:
                        point_x.append(point_x[i-1] + 1)
                        point_y.append(point_y[i-1] - 1)
                        pn.append(pn[i-1] + (2 * d_y) - (2 * d_x))
                    pn.append(pn[i-1] + (2 * d_y) - (2 * d_x))

        
        return point_x, point_y, pn

xs= []
ys= []
for i in range(2):
    xn = int(input('Masukan x'+str(i+1)+' : '))
    xs.append(xn)
    yn = int(input('Masukan y'+str(i+1)+' : '))
    ys.append(yn)

clf = Bresenhaim(xs[0], ys[0], xs[-1], ys[-1])
x, y, pn = clf.start()

print('p(k)\t x(k)\t y(k)\t ')
for i in range(len(x)):
    print(pn[i],'\t',x[i],'\t',y[i])



















