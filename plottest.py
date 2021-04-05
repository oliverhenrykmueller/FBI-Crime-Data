# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def dataplotfunction(y):
    # y = alterliste
    ### data graph age
    dic = {}
    for yy in y:
        try:
            dic[yy] = dic[yy] + 1
        except:
            dic[yy] = 1

    list1 = []
    list2 = []

    for x in dic.keys():
        list1.append(x)
        list2.append(dic[x])

    plt.plot(list1, list2)
    plt.ylabel("Anzahl Personen")
    plt.xlabel("Alter")

    plt.axis([0, sorted(list1)[-1], 0, sorted(list2)[-1] + 200])
    plt.savefig('agedemographicAGEDATASET.png')

    return


if __name__ == '__main__':


    print "Plot"
    x = [2006,2007,2008,2009,2010]
    y = [1,2,2,4,10]

    # Numpy: arange, arrangiert zahlen von min zu max in einem abstandsmuster (start,bis,)
    # Bsp: Von 1 bis 10 in 0.5 abständen arange(1,10,0.5) -> [1.0 1.5 2.0 ... 9.5 ]
    x2 = np.arange(2006, 2010, 1)
    xx = np.arange (1,10,0.5)
    y2 = [12,3,4,1]
    print xx**2

    t = np.arange(0., 5., 1)
    xy = np.array([2,3,0,10,5])

    print xy

    # red dashes, blue squares and green triangles
    #plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
    #plt.plot(t,xy,"r--",t,t **2,"ro")

    #Erzeuge mit plot Punkte,(die zu Linien verbunden werden können) modifiziere Label mit label="Bennenung",
    # oder Art der Punkte
    #plt.plot(x2,y2,'ro')
    #Bennene Achsen direkt selber: [x min, x max, y min, y max]
    #plt.axis([2000,2012,0,20])

    #plt.plot(x,y,label="erste")
    #plt.xlabel("Zeit")
    #plt.ylabel("Anzahl")
    #plt.legend()

    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50), #randint: (kleinste zufällige Zahl, höchste zufällige Zahl, Grösse des Arrays)
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100


    #plt.scatter([1,2,3,1],[8,8,8,8],c=np.random.randint(0,10, 4),s=np.arange(80,84))
    #Scatter: (x,y,c=Farbe der Punkte,s=Grösse der Punkte)
    #plt.scatter('a', 'b', c='c', s='d', data=data)
    #plt.xlabel('entry a')
    #plt.ylabel('entry b')
    #plt.title("Diagramm oder sowas")

    names = ['group_a', 'group_b', 'group_c']
    values = [20, 10, 100]

    #plt.figure(1, figsize=(9, 3))

    #plt.subplot(131)
    #plt.bar(names, values)
    #plt.subplot(132)
    #plt.scatter(names, values)
    #plt.subplot(133)
    #plt.plot(names, values)
    #plt.suptitle('Categorical Plotting')

    #plt.figure("Figure Name",figsize=(10,5))
    #plt.subplot(132)
    #plt.bar(names,values)

    #plt.subplot(131)
    plt.figure(u"Meine Interesse an Datascience",figsize=(10,7))
    #plt.plot(np.arange(0,3,1),label="Linienplot")
    #plt.plot((np.arange(0,4,1)),[129,1,1,1])
    #plt.plot(sorted(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]),[292, 1, 3, 15, 4,  5, 358, 3, 1, 350])
    #plt.plot(np.arange(0,100,1),np.arange(0,200,2))
    #plt.axis([0, 4, 0, 100])
    #plt.scatter(["aasd","aasd" ,"bdasd","bdasd","bdasd" ,"csadas","csadas","csadas", "dasd","dasd"],[10,0,0,15,0,0,9,0,0,20])
    #plt.plot(["aasd", "aasd", "bdasd", "bdasd", "bdasd", "csadas", "csadas", "csadas", "dasd", "dasd"],
    #         [12, 0, 0, 9, 0, 0, 20, 0, 0, 13])
    #print np.arange(1,7,1)
    #print "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

    #plt.xticks([1,2,3,4],["aa","asd","asdgg","kjk","asdasd","asda"])
    #plt.plot([1,2,3,4],[7,2,16,5])
    #
    # ind = [1,2]
    # l1 = [5,2]
    # l1_2 = [2,2]
    #
    # l2 = [1, 7]
    # l2_2 = [4, 6]
    #
    # l3 = [5, 2]
    # l3_2 = [2, 4]
    #
    #
    # p1 = plt.bar(ind, l1, 0.2, color='#d62728', yerr=l1_2)
    # p2 = plt.bar(ind, l2, 0.2 , bottom=l1, yerr=l2_2)
    # p3 = plt.bar(ind, l3, 0.2, bottom=l2, yerr=l3_2)

    plt.xlabel("Time in years")
    plt.ylabel("Interest")

    plt.bar(["2012","2013","2014","2015","2016","2017"],[0,5,30,60,57,85])


    plt.legend()

    #plt.subplot(133)
    #plt.scatter(names,np.random.randint(0,10,3),c=[1,2,3])

    plt.show()



