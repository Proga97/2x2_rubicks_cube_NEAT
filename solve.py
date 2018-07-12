from basicnn import *
from cube2 import *

nn = nn(24,12,100,2)
nn.newlayer(18)
nn.newlayer(14)
nn.finish()
nn.gen_population()

cube= thecube()
cube.newcube()

consec = 5
shuffle=1
gen = 0
cube.randomize(shuffle)
print('\na random cube after shuffling '+str(shuffle)+' times :' )
print(cube.get_cube(),'\n')
print('fitness of a cube after '+str(shuffle)+' shuffes:  ',cube.fitnes(),'\n')
nn.int_weight(nn.get_pop(1))
print('    Best fit        Average fit      shuffle    generation')
best_fit = 0
avg_gen = 0
best_fit = 0
while True:
        gen += 1
        winner=[]
        winnerflag=False
        temp_pop=[]
        avg_gen = 0
        best_fit = 0
        for i in range(nn.pop_size):
            player=nn.get_pop(i)
            nn.int_weight(player)
            avg=0
            best_cube = []
            best_cube_fit = 0
            for j in range(consec):
                cube.newcube()
                cube.randomize(shuffle)
                moves = 0
                temp_bestc=[]
                temp_bestf=0
                while moves <= 30:
                    a = cube.get_input()
                    o = nn.exc(a)
                    # print(o)
                    t = np.argmax(o)
                    #print(t)
                    cube.move(t)
                    k = cube.fitnes()
                    moves += 1
                    if k > temp_bestf:
                        temp_bestf= k
                        temp_bestc = cube.get_cube()
                    if k == 100:
                        #print(k,'d',cube.cube)
                        break
                avg += k
            avg = avg / consec
            if avg > best_cube_fit:
                best_cube_fit = avg
                best_cube = temp_bestc
            temp_pop.append([player,avg])
            if avg == 100:
                shuffle += 1
                print('\nsolved cube: ',best_cube)
                cube.randomize(shuffle)
                print('\na random cube after shuffling ' + str(shuffle) + ' times :')
                print(cube.get_cube())
                print('fitness of a cube after ' + str(shuffle) + ' shuffes:  ', cube.fitnes(), '\n')
                print('    Best fit        Average fit      shuffle    generation')
        temp_pop = sorted(temp_pop, key=lambda x: x[1])
        temp_pop = temp_pop[::-1]
        if best_fit < temp_pop[0][1]:
            best_fit=temp_pop[0][1]
        for i in range(len(temp_pop)):
            avg_gen += temp_pop[i][1]
        avg_gen = avg_gen / float(nn.pop_size)
        print(best_fit,avg_gen,'     ',shuffle,'      ',gen)
        nn.crossover()
        nn.mutation()





