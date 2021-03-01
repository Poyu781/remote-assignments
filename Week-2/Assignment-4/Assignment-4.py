def count(input): 
    output_dict = dict()
    for i in input:
        if i not in output_dict :
            output_dict[i] = 1
        else:
            output_dict[i] += 1
    return output_dict



def group_by_key(input):
    output_dict = dict()
    for i in range(len(input)):
        key_data = input[i]["key"]
        if key_data not in output_dict:
            output_dict[key_data] = input[i]["value"]
        else:
            output_dict[key_data] += input[i]["value"]
    return output_dict
