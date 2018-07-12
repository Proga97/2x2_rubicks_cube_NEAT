import random
import numpy as np

#1 front, 2 right, 3 back, 4 left, 5 top, 6 bot
#m1 right cw, m2 right ccw, m3 left cw, m4 left ccw, m5 back cw, m6 back ccw,
# m7 front cw, m8 frnt ccw, m9 up cw, m10 up cw, m11 down cw, m12 down ccw
class thecube(object):
    def __init__(self):
        self.cube= { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[] }

    def newcube (self):
        for i in range(1,7):
            self.cube[i]=[[i],[i],[i],[i]]


    def get_cube(self):
        return self.cube


    def turncw(self,side):              #to turn the face cw
        x = self.cube
        temp = x[side][0]
        x[side][0] = x[side][2]
        x[side][2] = x[side][3]
        x[side][3] = x[side][1]
        x[side][1] = temp
        self.cube = x


    def turnccw(self, side):        #to turn the face ccw
        x = self.cube
        temp = x[side][0]
        x[side][0] = x[side][1]
        x[side][1] = x[side][3]
        x[side][3] = x[side][2]
        x[side][2] = temp
        self.cube = x


    def move1(self): #right cw
        x=self.cube
        temp1= x[6][1]
        temp2= x[6][3]
        x[6][1] = x[3][3]
        x[6][3] = x[3][1]
        x[3][1] = x[5][1]
        x[3][3] = x[5][3]
        x[5][1] = x[1][3]
        x[5][3] = x[1][1]
        x[1][1] = temp1
        x[1][3] = temp2
        self.cube = x
        self.turncw(2)


    def move2(self):  # right ccw
        x = self.cube
        temp1 = x[6][1]
        temp2 = x[6][3]
        x[6][1] = x[1][1]
        x[6][3] = x[1][3]
        x[1][1] = x[5][3]
        x[1][3] = x[5][1]
        x[5][1] = x[3][1]
        x[5][3] = x[3][3]
        x[3][3] = temp1
        x[3][1] = temp2
        self.cube = x
        self.turnccw(2)


    def move3(self): #left cw
        x=self.cube
        temp1= x[6][0]
        temp2= x[6][2]
        x[6][0] = x[3][2]
        x[6][2] = x[3][0]
        x[3][0] = x[5][0]
        x[3][2] = x[5][2]
        x[5][0] = x[1][2]
        x[5][2] = x[1][0]
        x[1][0] = temp1
        x[1][2] = temp2
        self.cube = x
        self.turncw(4)


    def move4(self):  # left ccw
        x = self.cube
        temp1 = x[6][0]
        temp2 = x[6][2]
        x[6][0] = x[1][0]
        x[6][2] = x[1][2]
        x[1][0] = x[5][2]
        x[1][2] = x[5][0]
        x[5][0] = x[3][0]
        x[5][2] = x[3][2]
        x[3][2] = temp1
        x[3][0] = temp2
        self.cube = x
        self.turnccw(4)


    def move5(self): #back cw
        x=self.cube
        temp1= x[6][2]
        temp2= x[6][3]
        x[6][2] = x[2][3]
        x[6][3] = x[2][1]
        x[2][3] = x[5][3]                               #1 front, 2 right, 3 back, 4 left, 5 top, 6 bot
        x[2][1] = x[5][2]
        x[5][3] = x[4][1]
        x[5][2] = x[4][3]
        x[4][1] = temp1
        x[4][3] = temp2
        self.cube = x
        self.turncw(3)


    def move6(self):  # bck ccw
        x = self.cube
        temp1 = x[6][2]
        temp2 = x[6][3]
        x[6][2] = x[4][1]
        x[6][3] = x[4][3]
        x[4][3] = x[5][2]  # 1 front, 2 right, 3 back, 4 left, 5 top, 6 bot
        x[4][1] = x[5][3]
        x[5][3] = x[2][3]
        x[5][2] = x[2][1]
        x[2][3] = temp1
        x[2][1] = temp2
        self.cube = x
        self.turnccw(3)


    def move7(self):  # front cw
        x = self.cube
        temp1 = x[6][0]
        temp2 = x[6][1]
        x[6][0] = x[2][2]
        x[6][1] = x[2][0]
        x[2][2] = x[5][1]  # 1 front, 2 right, 3 back, 4 left, 5 top, 6 bot
        x[2][0] = x[5][0]
        x[5][1] = x[4][0]
        x[5][0] = x[4][2]
        x[4][0] = temp1
        x[4][2] = temp2
        self.cube = x
        self.turncw(1)


    def move8(self):  # front ccw
        x = self.cube
        temp1 = x[6][0]
        temp2 = x[6][1]
        x[6][0] = x[4][0]
        x[6][1] = x[4][2]
        x[4][0] = x[5][1]  # 1 front, 2 right, 3 back, 4 left, 5 top, 6 bot
        x[4][2] = x[5][0]
        x[5][1] = x[2][2]
        x[5][0] = x[2][0]
        x[2][2] = temp1
        x[2][0] = temp2
        self.cube = x
        self.turnccw(1)


    def move9(self):  # up cw
        x = self.cube
        temp1 = x[1][0]
        temp2 = x[1][1]
        x[1][0] = x[2][0]
        x[1][1] = x[2][1]
        x[2][0] = x[3][1]  # 1 front, 2 right, 3 back, 4 left, 5 top, 6 bot
        x[2][1] = x[3][0]
        x[3][1] = x[4][1]
        x[3][0] = x[4][0]
        x[4][1] = temp1
        x[4][0] = temp2
        self.cube = x
        self.turncw(5)


    def move10(self):  # up ccw
        x = self.cube
        temp1 = x[1][0]
        temp2 = x[1][1]
        x[1][0] = x[4][1]
        x[1][1] = x[4][0]
        x[4][1] = x[3][1]  # 1 front, 2 right, 3 back, 4 left, 5 top, 6 bot
        x[4][0] = x[3][0]
        x[3][1] = x[2][0]
        x[3][0] = x[2][1]
        x[2][0] = temp1
        x[2][1] = temp2
        self.cube = x
        self.turnccw(5)


    def move11(self):  # down cw
        x = self.cube
        temp1 = x[1][2]
        temp2 = x[1][3]
        x[1][2] = x[2][2]
        x[1][3] = x[2][3]
        x[2][2] = x[3][3]  # 1 front, 2 right, 3 back, 4 left, 5 top, 6 bot
        x[2][3] = x[3][2]
        x[3][3] = x[4][3]
        x[3][2] = x[4][2]
        x[4][3] = temp1
        x[4][2] = temp2
        self.cube = x
        self.turncw(6)


    def move12(self):  # down ccw
        x = self.cube
        temp1 = x[1][3]
        temp2 = x[1][2]
        x[1][3] = x[4][2]
        x[1][2] = x[4][3]
        x[4][2] = x[3][2]  # 1 front, 2 right, 3 back, 4 left, 5 top, 6 bot
        x[4][3] = x[3][3]
        x[3][2] = x[2][3]
        x[3][3] = x[2][2]
        x[2][3] = temp1
        x[2][2] = temp2
        self.cube = x
        self.turnccw(6)


    def move(self,n):
        moves=[self.move1,self.move2,self.move3,self.move4,self.move5,self.move6,
               self.move7,self.move8,self.move9,self.move10,self.move11,self.move12]
        moves[n]()


    def randomize(self,n):
        for i in range(0,n):
            x = random.randint(0,11)
            #print(x)
            self.move(x)

    def fitnes(self):
        fit=0
        for i in range(1,7):
            x = self.cube[i]
            seen=[]
            for j in range(len(x)):
                #print(x[j])
                for k in range(len(x)):
                    if x[j] == x[k] and x[j] not in seen and j!= k :
                        fit += 1
                seen.append(x[j])
        #print(fit)
        fit = (fit/18)*100
        #print(fit)
        return fit



    def get_input(self):
        x=[]
        for i in range(1,7):
            for j in range(4):
                x.append(self.cube[i][j][0])
        std= np.std(x)
        mean= np.mean(x)
        #print(std,mean,x)
        for i in range(len(x)):
            x[i] = 0.5 * (np.tanh(0.01* ( x[i]- mean )/ std ) + 1 )         #normalising input
        #print(x)
        return x



