# import string
# def rotate(text, key):

#     alpha = string.ascii_lowercase
#     print(alpha)
#     alpha_shift = alpha[key:] + alpha[:key]
#     table = str.maketrans(alpha + alpha.upper(), alpha_shift + alpha_shift.upper())
#     print(table)
#     return text.translate(table)
# rotate("abc",-2)


alpha=['a','b',"c",'d','e',"f",'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def rotational_cipher(text="exmple",key=5):
    input_str=text.lower()
    result_str=""
    for char in input_str:
        if char in alpha:
            pos=(alpha.index(char)+key)%26
            result_str+=alpha[pos]
        else:
            result_str+=char
    # final out put
    return result_str
	
if __name__  == '__main__' :
    text_1='omg'
    text_2=" Vaishnavi@gmail.com "
    print(rotational_cipher(text_1,5))