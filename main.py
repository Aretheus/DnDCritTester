import random

# setup 
default_results: list[int] = []

# input dice combinations
dice_str: str = "1d8+2d6+3"

try:
    # check for valid str
    dice_set_count = dice_str.count("d")
    sep_count = dice_str.count("+")

    if dice_set_count > sep_count:
        raise ValueError()
    
    # breakdown dice sets
    dice_list = dice_str.split("+")
    print(dice_list)

    total_crit: list[int] = []

    for num in range(100000):
        crit_list: list[int] = []
        crit_sum = 0

        # start default calc
        for _ in dice_list:
            if "d" in _:
                die_split_int = [eval(s) for s in _.split("d")]
                crit_list += [random.randint(a=1, b=die_split_int[-1]) for i in range(die_split_int[0]*2)]

            else:
                # calc mod. mod must be final number
                crit_sum = sum(crit_list) + eval(_)
                # print(crit_sum)
                total_crit.append(crit_sum)
    
    # print(total_crit)
    print(f"default: {sum(total_crit)/len(total_crit)}")


    for num in range(100000):
        crit_list: list[int] = []
        crit_sum = 0
        
        # start maximised calc
        for _ in dice_list:
            if "d" in _:
                die_split_int = [eval(s) for s in _.split("d")]
                crit_list += [die_split_int[-1] for i in range(die_split_int[0])]
                crit_list += [random.randint(a=1, b=die_split_int[-1]) for i in range(die_split_int[0])]

            else:
                # calc mod. mod must be final number
                crit_sum = sum(crit_list) + eval(_)
                # print(crit_sum)
                total_crit.append(crit_sum)
    
    # print(total_crit)
    print(f"maximised: {sum(total_crit)/len(total_crit)}")


    for num in range(100000):
        crit_list: list[int] = []
        crit_sum = 0
        
        # start max 1 calc
        for _ in dice_list:
            if "d" in _:
                die_split_int = [eval(s) for s in _.split("d")]
                crit_list += [die_split_int[-1]]
                crit_list += [random.randint(a=1, b=die_split_int[-1]) for i in range((die_split_int[0]*2)-1)]

            else:
                # calc mod. mod must be final number
                crit_sum = sum(crit_list) + eval(_)
                # print(crit_sum)
                total_crit.append(crit_sum)
    
    # print(total_crit)
    print(f"max 1: {sum(total_crit)/len(total_crit)}")



except ValueError():
    print("program close")