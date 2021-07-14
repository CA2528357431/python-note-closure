# 本质上来说，函数名本身也是一种变量，只不过指向了变量

def hk(a, b):
    c = a ** b
    print(c)


re = hk
re(3, 6)

print()

print(id(re))
print(id(hk))
# 二者指向了同一个地址



