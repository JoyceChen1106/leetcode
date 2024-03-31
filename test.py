digits ="23"
if len(digits)== 0:
    result = []

phone_map= {
    0:"0",
    1:"1",
    2:"abc",
    3:"def",
    4:"ghi",
    5:"jkl",
    6:"mno",
    7:"pqrs",
    8:"tuv",
    9:"wxyz"
}

result = [""]
for digit in digits:
    temp_list = []
    for ph in phone_map[int(digit)]:
        for str in result:
            temp_list.append(str+ph)
            result = temp_list
        




        