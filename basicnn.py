import numpy as np
import random



class nn(object):

    def __init__(self, inp, output, pop_s, mutation_r ):
        self.weights=[]
        self.weight_count = 0
        self.input = inp
        self.output = output
        self.layers = 0
        self.completed = 0
        self.nodes = []
        self.pop=[]
        self.pop_size = pop_s
        self.percentile = .3
        self.mutation_rate = mutation_r


    def sigmoid(self,x):
       return 1 / ( 1 + np.exp(-x))


    def tanh(self,x):
        return np.tanh(x)       #(ex – e-x) / (ex + e-x)


    def newlayer(self, nodes):
        self.nodes.append([nodes])
        self.layers += 1


    def int_weight(self,w):
        self.weights=w


    def get_pop(self,i):
        return self.pop[i]


    def finish(self):
        inputs = self.input
        for i in range(len(self.nodes)):
            x = self.nodes[i][0]
            if i == 0:
                self.weight_count += x * inputs + x
            else:
                self.weight_count += x * prev_x + x
            prev_x = x
        self.weight_count += self.output * prev_x
        #print(self.weight_count)


    def exc(self,inputs):
        prevnodes = np.array(inputs)
        n=0
        fin=[]
        for i in range(self.layers):

            fin=[]
            temp_array = []
            nu_nodes=self.nodes[i][0]
            x=0
            for j in range(len(prevnodes)):
                w_array = np.array(self.weights[n:n+nu_nodes])
                n += nu_nodes
                #print(len(prevnodes),len(w_array),j,i)
                x += np.dot(prevnodes[j],w_array)
                #print(x)
            x += self.weights[n:n+nu_nodes]
            n += nu_nodes
            #print(x)
            x = self.sigmoid(x)
            #print(x)
            prevnodes = np.array(x)
        #print(n,self.weight_count)
        nu_nodes = self.output
        x=0
        for p in range(0,len(prevnodes)):
            w_array = np.array(self.weights[n:n + nu_nodes])
            n += nu_nodes
            #print(len(prevnodes), len(w_array), i)
            x += np.dot(prevnodes[p], w_array)
        #print(x)
        x = self.tanh(x)
        #print(n,self.weight_count)
        fin = x
        return fin

    def gen_population(self):
        popx = []
        while len(popx) < self.pop_size:
            w = np.random.uniform(-1,1,self.weight_count)
            popx.append(w)
        self.pop=popx

    def crossover(self):
        popx= []
        cut = int(self.percentile * len(self.pop))
        #print(self.pop[1])
        for i in range(cut):
            popx.append(self.pop[i])

        for i in range(cut,self.pop_size):
            z= random.randint(0,cut-2)
            x= popx[z]
            y= popx[z+1]
            #print(x)
            r= random.randint(0,25)
            a = []
            if r<5 :
                for j in range(len(x)):
                    a.append((x[j]+y[j])/2)
                popx.append(a)
            elif r>5 and r<10 :
                for j in range(len(x)):
                    a.append((x[j]-y[j])/2)
                popx.append(a)
            elif r>10 and r<15:
                for j in range(len(x)):
                    p = random.uniform(0,1)
                    a.append(x[j]*p)
                popx.append(a)
            elif r>15 and r<20 :
                for j in range(len(x)):
                    t=random.randint(0,10)
                    if t<5 :
                        a.append(x[j])
                    else:
                        a.append(y[j])
                popx.append(a)
            else:
                for j in range(len(x)):
                    a.append(-1 * x[j])
                popx.append(a)
        self.pop = popx



    def mutation(self):
        for i in range(len(self.pop)):
            for j in range(len(self.pop[i])):
                if self.mutation_rate > random.randint(0,100):
                    self.pop[i][j]= np.random.uniform(-1,1)
