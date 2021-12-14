import re

if __name__ == "__main__":
    final_answer = 0
    points = {}
    folds_list = []
    with open("13input.txt") as f:
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
    print("x list before",points.keys())
    # for fold in folds_list:
    fold = folds_list[0]
    new_points = {}
    for x_coord,y_coord_set in points.items():
        # if it's an x fold
        if fold[0] == "x":
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

    for x_coord,y_coord_set in new_points.items():
        final_answer += len(y_coord_set)
    
    print("x list AFTER",new_points.keys())
    print(final_answer)
