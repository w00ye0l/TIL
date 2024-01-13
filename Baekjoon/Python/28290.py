dic = {
    "fdsajkl;": "in-out",
    "jkl;fdsa": "in-out",
    "asdf;lkj": "out-in",
    ";lkjasdf": "out-in",
    "asdfjkl;": "stairs",
    ";lkjfdsa": "reverse",
}

S = input()
if S in dic:
    print(dic[S])
else:
    print("molu")
