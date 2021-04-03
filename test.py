from 继承法 import 长子继承制, 分割继承制, 斯堪的纳维亚选举制



for 制 in (长子继承制, 分割继承制, 斯堪的纳维亚选举制):
    @制
    class A:
        x = 100
        y = 200
        z = 300

    class B(A):
        x = y = z = 9

    class C(A):
        x = y = z = 0

    print('\n' + '='*50 + '\n' + 制.__name__ + '\n' + '='*50)

    print(f'{A.x=}, {A.y=}, {A.z=}')
    print(f'{B.x=}, {B.y=}, {B.z=}')
    print(f'{C.x=}, {C.y=}, {C.z=}')
    print('====继承====')
    A.__del__()
    print(f'{B.x=}, {B.y=}, {B.z=}')
    print(f'{C.x=}, {C.y=}, {C.z=}')


