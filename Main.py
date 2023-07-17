import numpy as np #Use numpy for a suitable output.

#Main:
def floyd(graph):
    n = len(graph)

    for k in range(n): #k use for test all possible paths 
        for i in range(n):
            for j in range(n):
                if i!=j: #To avoid unnecessary re-processing(indexes of the main diametr are always is 0)
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) #Find the shortest path 

    return graph

#Define paths here 
my_graph = [[0, 5, float('inf'), float('inf')],
     [50, 0, 15, 5],
     [30, float('inf'), 0, 15],
     [15, float('inf'), 5, 0]]

print(np.array(floyd(my_graph))) #Show the output()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                             #
# Telegram : @iliyafaramarzi , @iliya_faramarzi                                                               #
# Instagram : faramarziiliya                                                                                  #
# Github : iiyafaramarzi                                                                                      #
# Linkedin : iliyafaramarzi                                                                                   #
#                                                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #