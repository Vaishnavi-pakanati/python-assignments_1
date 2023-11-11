#Checking Given Number Is Amstrong OR not
def is_amstrong(number):
	str_num = str(number)
	length_= len(str_num)
	sum = 0
	for dig in str_num:
		sum += int(dig)**length_
	if sum == num:
		return f"{str_num} is Amstrong Number"
	else:
		return f"{str_num} is  not Amstrong Number"
	
if __name__  == '__main__' :
    num=8977
    print(is_amstrong(num))



