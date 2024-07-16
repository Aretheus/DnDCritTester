# import numpy
import random
#setup generator
# gen = numpy.random.default_rng()


def roll_rng(dice_count: int, dice_type: int):
    # return [gen.integers(low=1, high=dice_type+1) for i in range(dice_count)]
    return [random.randint(a=1, b=dice_type) for i in range(dice_count)]


def default_dice_randomiser(dice_sets: list, total_runs: int):
    # the last entry is alway expected to be a stat modification otherwise none
    if len(dice_sets[-1]) < 2:
        mod = dice_sets[-1]
        temp = [[roll_rng(dice_count=d[0]*2, dice_type=d[-1]) for d in dice_sets if len(d) > 1] + [mod] for _ in range(total_runs)]
    else:
        temp = [[roll_rng(dice_count=d[0]*2, dice_type=d[-1]) for d in dice_sets] for _ in range(total_runs)]

    default_res = [[v for l in t for v in l] for t in temp]
    
    [print(p) for p in default_res]
    return [sum(d) for d in default_res]


def maximised_dice_randomiser(dice_sets: list, total_runs: int):
    # the last entry is alway expected to be a stat modification otherwise none
    if len(dice_sets[-1]) < 2:
        mod = dice_sets.pop(-1)
        temp = [[[d[-1] for i in range(d[0])] + roll_rng(dice_count=d[0], dice_type=d[-1]) for d in dice_sets if len(d) > 1] + [mod] for _ in range(total_runs)]
    else:
        temp = [[[d[-1] for i in range(d[0])] + roll_rng(dice_count=d[0], dice_type=d[-1]) for d in dice_sets] for _ in range(total_runs)]
    
    max_res = [[v for l in t for v in l] for t in temp]

    [print(p) for p in max_res]
    return [sum(d) for d in max_res]


def maximise_one_dice_randomiser(dice_sets: list, total_runs: int):
    # the last entry is alway expected to be a stat modification otherwise none
    if len(dice_sets[-1]) < 2:
        mod = dice_sets.pop(-1)
        temp = [[[d[-1]] + roll_rng(dice_count=(d[0]*2)-1, dice_type=d[-1]) for d in dice_sets if len(d) > 1] + [mod] for _ in range(total_runs)]
    else:
        temp = [[[d[-1]] + roll_rng(dice_count=(d[0]*2)-1, dice_type=d[-1]) for d in dice_sets] for _ in range(total_runs)]

    max_one_res = [[v for l in t for v in l] for t in temp]

    [print(p) for p in max_one_res]
    return [sum(d) for d in max_one_res]


def dice_separator(input_dice: str):
    dice_list = input_dice.split("+")
    print(dice_list)

    dice_col: list[list[int]] = []

    for d in dice_list:
        if "d" in d:
            dice_col.append([eval(s) for s in d.split("d")])
        else:
            dice_col.append([eval(d)])

    print(dice_col)

    return dice_col


if __name__ in "__main__":
    # setup 
    default_results: list[int] = []

    # input dice combinations
    dice_str: str = "1d8+2d6+3"
    print(dice_str)

    runs = 100000

    try:
        # check for valid str
        dice_set_count = dice_str.count("d")
        sep_count = dice_str.count("+")

        if dice_set_count > sep_count:
            raise ValueError()
        
        # breakdown dice sets
        dice_list = dice_separator(dice_str)
        
        total_default = default_dice_randomiser(dice_sets=dice_list, total_runs=runs)
        total_max = maximised_dice_randomiser(dice_sets=dice_list, total_runs=runs)
        total_max_one = maximise_one_dice_randomiser(dice_sets=dice_list, total_runs=runs)
        
        # print(total_crit)
        print(f"default: {sum(total_default)/len(total_default)}")
        
        # print(total_crit)
        print(f"maximised: {sum(total_max)/len(total_max)}")
        
        # print(total_crit)
        print(f"max 1: {sum(total_max_one)/len(total_max_one)}")


    except ValueError():
        print("program close")