sodoku = [['*' for x in range(9)] for y in range(9)]
flag = True
printkon = True

for i in range(9):
    arg = input()
    nums = []
    for j in range(9):
        sodoku[i][j] = arg[0]
        if not sodoku[i][j] == '*':
            sodoku[i][j] = int(arg[0])
            if sodoku[i][j] < 1 or sodoku[i][j] > 9:
                flag = False
            nums.append(sodoku[i][j])
        arg = arg[1:]

    if not arg == "":
        flag = False
        
    prv_nums = nums
    new_nums = list(set(nums))
    if not len(new_nums) == len(prv_nums):
        flag = False
        
if flag == False:
    if printkon == True:
        print("No")
        printkon = False


else:
    for i in range(9):
        nums = []
        for j in range(9):
            if not sodoku[j][i] == '*':
                nums.append(sodoku[j][i])
        
        prv_nums = nums
        new_nums = list(set(nums))
        if not len(new_nums) == len(prv_nums):
            flag = False

    if flag == False:
        if printkon == True:
            print("No")
            printkon = False

    else:
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                temp_sodoku = [['*' for x in range(3)] for y in range(3)]
                temp_sodoku[0][0] = sodoku[i][j]
                temp_sodoku[0][1] = sodoku[i][j + 1]
                temp_sodoku[0][2] = sodoku[i][j + 2]
                temp_sodoku[1][0] = sodoku[i + 1][j]
                temp_sodoku[1][1] = sodoku[i + 1][j + 1]
                temp_sodoku[1][2] = sodoku[i + 1][j + 2]
                temp_sodoku[2][0] = sodoku[i + 2][j]
                temp_sodoku[2][1] = sodoku[i + 2][j + 1]
                temp_sodoku[2][2] = sodoku[i + 2][j + 2]

            nums = []
            for i in range(3):
                for j in range(3):
                    if not temp_sodoku[j][i] == '*':
                        nums.append(sodoku[j][i])
            
            prv_nums = nums
            new_nums = list(set(nums))
            if not len(new_nums) == len(prv_nums):
                flag = False

            if flag == False:
                if printkon == True:
                    print("No")
                    printkon = False

            

if flag == True:
    if printkon == True:
        print("Yes")
        printkon = False
