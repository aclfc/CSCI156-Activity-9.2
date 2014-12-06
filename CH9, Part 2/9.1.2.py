__author__ = 'Aidan'
f = open('user.txt','w+', encoding = 'utf-8')
def store(s):
    while s != 'q' and s != 'Q':
        f.write(s+'\n')
        s=input("Next input: ")
    return (f)
def printup(st):
    st.seek(0)
    ns=""
    for st in st:
        ns+=st.readline()
        for j in range(len(ns)):
            ns[j].upper()
    print(ns)
def user(str):
    printup(store(str))
    print("Goodbye!")
user(input("First input: "))
f.close()