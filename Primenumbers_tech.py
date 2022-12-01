'''
Input: [ {“Dg set”: “Diesel generator”}, {“Organization”: “Organisation”}, 
            {“Group”: “Organization”}, {“Orange”: “Kinnu”}, {“Orange”: “narangi”} ]
Output: [[“Organization”, “Organisation”, “Group”], [“Dg set”, “Diesel generator”], [“Orange”, “Kinnu”, “narangi”]]
'''  
def solution(input):
    output = [[list(input[0].keys())[0], list(input[0].values())[0]]]
    for i in range(1, len(input)):
        group = []
        key = list(input[i].keys())[0]
        value = list(input[i].values())[0]
        flag = 0
        for j in range(len(output)):
            if key in output[j]:
                output[j].append(value)
                flag = 1
                break
            elif value in output[j]:
                output[j].append(key)
                flag = 1
                break
        if flag == 0:
            group.append(key)
            group.append(value)
            output.append(group)
    return output

if __name__ == '__main__':
    input = [{"Dg set": "Diesel generator"}, {"Organization": "Organisation"}, 
             {"Group": "Organization"}, {"Orange": "Kinnu"}, {"Orange": "narangi"}]
    print(solution(input))
