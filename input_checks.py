


def valid_length(input):
    return (len(input) >= 3 and len(input)<=20)

def match(password_1,password_2):
    return password_1 == password_2

def valid_email(email):
    if not valid_length(email):
        return False
    periods = 0
    at_symbols = 0
    for i in email:
        if i == " ":
            return False
        elif i == ".":
            periods += 1
        elif i == "@":
            at_symbols += 1
    return periods == 1 and at_symbols == 1





def main():
    # print(valid_length("a"))
    # print(valid_length("as"))
    # print(valid_length("ass"))
    # print(valid_length("asdf"))
    # print(valid_length("aaaaaaaaaaaaaaaaaaaa"))
    # print(valid_length("zzzzzzzzzzzzzzzzzzzzz"))

    # print(match("ass","ass"))
    # print(match("asdfg","ass"))


    print(valid_email("abc@gmail.com"))
    print(valid_email("aaaaaaaaaa@aaaaaaaaaaaaaa.com"))
    print(valid_email("@."))
    print(valid_email("abc aaaa@aaa.com"))
    print(valid_email("abc"))
    print(valid_email("aa@@.com"))
    print(valid_email("aaa@...com"))



if __name__=="__main__":
    main()