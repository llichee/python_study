def main(all_num):

    """当函数中出现yield时，该函数就是一个生成器模板"""

    a, b = 0, 1
    num = 0
    while num < all_num:
        yield a
        a, b = b, a+b
        num += 1

obj = main(10)     #由上述的生成器模板生成的一个可遍历的对象


for temp in obj:
    """通过for来遍历obj对象"""
    print(temp)