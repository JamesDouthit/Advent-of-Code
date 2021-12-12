import re
import copy

def explorePaths(paths_list,allowed_dict,visited_dict,current_path,endcounter):
    # if visited_dict[current_path[-1]] == True:
    #     return(paths_list)
    new_paths_list = copy.deepcopy(paths_list)
    new_visited_dict = copy.deepcopy(visited_dict)
    new_endings = 0
    # print("---- current_path",current_path)
    if(current_path[-1][0].islower()):
        new_visited_dict[current_path[-1]] = True
    if current_path[-1] == "end":
        endcounter += 1
        return(new_paths_list.append(current_path),endcounter)
    for connecting_v in allowed_dict[current_path[-1]]:
        if not visited_dict[connecting_v]:
            new_current_path = copy.deepcopy(current_path)
            new_current_path.append(connecting_v)
            new_paths, new_ending = explorePaths(paths_list,allowed_dict,new_visited_dict,new_current_path,endcounter)
            new_paths_list.append(new_paths)
            new_endings += new_ending
    endcounter += new_endings
    return(new_paths_list,endcounter)

if __name__ == "__main__":
    final_answer = 0
    path_record = {}
    visited = {}
    with open("12input.txt") as f:
        lines = f.readlines()
    for line in lines:
        x = re.search("^(.*)-([a-zA-Z]*?)$", line)
        if (not path_record.get(x[1], None)):
            visited[x[1]] = False
            path_record[x[1]] = [x[2]]
        else:
            path_record[x[1]].append(x[2])
        if(not path_record.get(x[2], None)):
            visited[x[2]] = False
            path_record[x[2]] = [x[1]]
        else:
            path_record[x[2]].append(x[1])
    # print(path_record)
    # print("---- about to explorePaths",[],path_record,visited,["start"],0)
    visited["start"] = True
    paths,final_counter = explorePaths([],path_record,visited,["start"],0)
    print("111`-`-`------ THE ANSWER:",final_counter)
    print(paths)
    print(len(paths))
