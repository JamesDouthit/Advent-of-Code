import matplotlib.pyplot as plt
import numpy as np
import re

def enumeratePoints(point_dict):
    x = []; y = []
    for x_val, y_vals_set in point_dict.items():
        for y_val in y_vals_set:
            x.append(int(x_val))
            y.append(-y_val)
    return x, y

if __name__ == "__main__":
    final_answer = 0
    points = {}
    folds_list = []
    # with open("13input.txt") as f:
    with open("13test.txt") as f:
        lines = f.readlines()
    mode = 0
    for line in lines:
        if line == "\n":
            mode = 1
            continue
        if mode == 0:
            coords=line.rstrip("\n").split(",")
            if(not points.get(coords[0],None)):
                points[coords[0]] = {int(coords[1])}
            else:
                points[coords[0]].add(int(coords[1]))
        if mode == 1:
            r = re.search("^fold along ([xy])=([0-9]*)$", line)
            folds_list.append([r[1],int(r[2])])
    area = (15 * np.ones(len(x)))**2
    for i in range(len(folds_list)):
        plt.figure(i)
        plt.subplot(121)
        x_tmp, y_tmp = enumeratePoints(points)
        plt.scatter(x_tmp,y_tmp,s=area)
        fold = folds_list[i]
        new_points = dict()
        for x_coord,y_coord_set in points.items():
            # if it's an x fold
            if fold[0] == "x":
                plt.axvline(x = fold[1])
                if int(x_coord) > fold[1]:
                    # new_points[str(fold[1]-(int(x_coord)-fold[1]))] = y_coord_set
                    if(not new_points.get(str(fold[1]-(int(x_coord)-fold[1])),None)):
                        new_points[str(fold[1]-(int(x_coord)-fold[1]))] = y_coord_set
                    else:
                        new_points[str(fold[1]-(int(x_coord)-fold[1]))].update(y_coord_set)
                else:
                    if(not new_points.get(x_coord,None)):
                        new_points[x_coord] = y_coord_set
                    else:
                        new_points[x_coord].update(y_coord_set)
            # it's a y fold
            elif fold[0] == "y":
                ypoints = np.array([0, -fold[1], max(list(points.keys())), -fold[1]])
                plt.plot(ypoints, linestyle = 'dashed')
                for y_coord in y_coord_set:
                    if y_coord > fold[1]:
                        if(not new_points.get(x_coord,None)):
                            new_points[x_coord] = {fold[1]-(y_coord-fold[1])}
                        else:
                            new_points[x_coord].add(fold[1]-(y_coord-fold[1]))
                    else:
                        if(not new_points.get(x_coord,None)):
                            new_points[x_coord] = {y_coord}
                        else:
                            new_points[x_coord].add(y_coord)
        # print("before fold",fold[0],fold[1],":",points,"\n")
        points = new_points
        plt.subplot(122)
        plt.scatter(enumeratePoints(new_points),s=area)
        plt.show()

    
    x = []; y = []
    for x_val, y_vals_set in new_points.items():
        for y_val in y_vals_set:
            x.append(int(x_val))
            y.append(-y_val)
    print("x:",x,"\n")
    print("y:",y,"\n")
    plt.rcParams["figure.autolayout"] = True
    plt.scatter(x,y,s=area)
    plt.show()

    for x_coord,y_coord_set in new_points.items():
        final_answer += len(y_coord_set)
    
    print(final_answer)


# if __name__ == "__main__":
#     final_answer = 0
#     points = {}
#     folds_list = []
#     # with open("13input.txt") as f:
#     with open("13test.txt") as f:
#         lines = f.readlines()
#     mode = 0
#     for line in lines:
#         if line == "\n":
#             mode = 1
#             continue
#         if mode == 0:
#             coords=line.rstrip("\n").split(",")
#             if(not points.get(coords[0],None)):
#                 points[coords[0]] = {int(coords[1])}
#             else:
#                 points[coords[0]].add(int(coords[1]))
#         if mode == 1:
#             r = re.search("^fold along ([xy])=([0-9]*)$", line)
#             folds_list.append([r[1],int(r[2])])
#     for i in range(len(folds_list)):
#         fold = folds_list[i]
#         new_points = dict()
#         for x_coord,y_coord_set in points.items():
#             # if it's an x fold
#             if fold[0] == "x":
#                 if int(x_coord) > fold[1]:
#                     # new_points[str(fold[1]-(int(x_coord)-fold[1]))] = y_coord_set
#                     if(not new_points.get(str(fold[1]-(int(x_coord)-fold[1])),None)):
#                         new_points[str(fold[1]-(int(x_coord)-fold[1]))] = y_coord_set
#                     else:
#                         new_points[str(fold[1]-(int(x_coord)-fold[1]))].update(y_coord_set)
#                 else:
#                     if(not new_points.get(x_coord,None)):
#                         new_points[x_coord] = y_coord_set
#                     else:
#                         new_points[x_coord].update(y_coord_set)
#             # it's a y fold
#             elif fold[0] == "y":
#                 for y_coord in y_coord_set:
#                     if y_coord > fold[1]:
#                         if(not new_points.get(x_coord,None)):
#                             new_points[x_coord] = {fold[1]-(y_coord-fold[1])}
#                         else:
#                             new_points[x_coord].add(fold[1]-(y_coord-fold[1]))
#                     else:
#                         if(not new_points.get(x_coord,None)):
#                             new_points[x_coord] = {y_coord}
#                         else:
#                             new_points[x_coord].add(y_coord)
#         # print("before fold",fold[0],fold[1],":",points,"\n")
#         points = new_points
#         print("after fold",fold[0],fold[1],":",new_points,"\n\n")
    
#     x = []; y = []
#     for x_val, y_vals_set in new_points.items():
#         for y_val in y_vals_set:
#             x.append(int(x_val))
#             y.append(-y_val)
#     print("x:",x,"\n")
#     print("y:",y,"\n")
#     plt.rcParams["figure.autolayout"] = True
#     area = (15 * np.ones(len(x)))**2
#     plt.scatter(x,y,s=area)
#     plt.show()

#     for x_coord,y_coord_set in new_points.items():
#         final_answer += len(y_coord_set)
    
#     print(final_answer)
