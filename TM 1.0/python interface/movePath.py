# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:15:19 2019

@author: seb
"""

SAFETY = 40  # the higher it is the less the algorithm will go through intersections

class Node(object):
    def __init__(self, _x, _y, _parent, _c = 0, _h = 0):
        self.x = _x
        self.y = _y
        self.c = _c  # cost
        self.h = _h  # heuristic
        self.parent = _parent
        
    def print(self):
        print((self.x, self.y))
        print("cost :", self.c)
        print("heur :", self.h)
        
    def __lt__(self, n):
        return self.h < n.h
    
    def __eq__(self, n):
        return (self.x == n.x and self.y == n.y)
    
def print_graph(g):
    for y in g:
        for x in y:
            print(x, end=" ")
        print("")
        
def get_path(g, end):
    current = end
    path = []
    while current.c != 0:
        path.append((current.x, current.y))
        current = current.parent
    return path

def print_path(graph, path, start):
    graph[start[1]][start[0]] = "S"
    for i in path:
        graph[i[1]][i[0]] = "*"
    graph[path[0][1]][path[0][0]] = "E"
    print_graph(graph)
    
def evaluate_child(graph, shift, parent):
    if parent.x + shift[0] > -1 and parent.x + shift[0] < len(graph[0]) and parent.y + shift[1] > -1 and parent.y + shift[1] < len(graph):
        child = Node(parent.x + shift[0], parent.y + shift[1], parent)
        if graph[child.y][child.x] == 1:  # if there's a wall
            return None
        else:
            child.c = parent.c + 1
            return child
    else:
        return None
        
def Astar(graph, start, end):
    open_list = []  # list of nodes visited but not expanded (TODO list)
    closed_list = []  # list of nodes visited and expanded
    open_list.append(Node(start[0], start[1], None))
    
    while len(open_list) > 0:  # while not empty
        
        open_list.sort(key=lambda z : z.h)  # get lowest element
        
        current_n = open_list[0]
        del open_list[0]
        closed_list.append(current_n)
        
        if current_n.x == end[0] and current_n.y == end[1]:
            return current_n
        
        # generate children
        for shift in [(0,1), (1,0), (0,-1), (-1,0)]:  # no diagonals
            child = evaluate_child(graph, shift, current_n)
            if not child:
                continue
            
            if child in closed_list:
                continue
            
            elif child in open_list and open_list[open_list.index(child)].c < child.c:
                continue
            
            else:
                child.c += SAFETY if graph[child.y][child.x] == 2 else 0  # you don't want to go through an intersection unless it's necessary
                child.h = child.c + (end[0] - child.x)**2 + (end[1] - child.y)**2
                open_list.append(child)
        
    return None

def generate_graph(all_pieces, captured_pieces):
    graph =[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,2,0,2,0,2,0,2,0,2,0,2,0,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

    nb_counter = 1
    let_counter = 0
    all_pieces_str = bin(all_pieces)[2:]
    all_pieces_str = all_pieces_str[::-1]
    for i in all_pieces_str:
        graph[nb_counter][let_counter] = int(i)
        let_counter += 2
        if let_counter > 14:
            let_counter = 0
            nb_counter += 2

    if captured_pieces > 15:
        print("[-] There cannot be more than 15 captured pieces, there's :", captured_pieces)
        return None
    
    ci = 14
    while ci > (14 - captured_pieces):
        graph[0][ci] = 1
        ci -=1
    
    return graph

def transform_coo_to_index(coo, captured_pieces):
    let_to_i = {"a":14, "b":12, "c":10, "d":8, "e":6, "f":4, "g":2, "h":0}
    cfrom = coo[:2]
    cto = coo[2:]
    
    end = (0,0)
    begin = (0,0)

    begin = (let_to_i[cfrom[0]], (int(cfrom[1]) -1)*2 + 1)
    if cto == "CA":
        end = (captured_pieces, 16)
        print("Going to CAPTURED :", end)
        captured_pieces += 1
    else:
        end = (let_to_i[cto[0]], (int(cto[1]) -1)*2 + 1)

    return begin, end, captured_pieces
