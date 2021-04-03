# 【教程】莉沫酱教你学继承！

众所周知，类的继承就是说当一个类死亡的时候，它的子类会获得它拥有的资源。

根据类的继承法不同，各个子类能获得的资源也不同。


## 继承法的类型

在解释继承法之前，我们先定义三个类，一个父类`A`，和它的子类`B`、`C`。

它们都拥有`x`、`y`、`z`三个属性。

```python
class A:
    x = 100
    y = 200
    z = 300
class B(A):
    x = y = z = 9
class C(A):
    x = y = z = 0
```


### 长子继承制

假如父类`A`采用了`长子继承制`，那么在继承中，所有资源都会被交给其最年长的子类，其他子类什么也得不到。

```python
@长子继承制
class A:
    x = 100
    y = 200
    z = 300
```

在使用了`长子继承制`之后，我们杀掉父类，看看子类的资源有什么变化——

```python
print(f'{A.x=}, {A.y=}, {A.z=}')
print(f'{B.x=}, {B.y=}, {B.z=}')
print(f'{C.x=}, {C.y=}, {C.z=}')
print('====继承====')
A.__del__()
print(f'{B.x=}, {B.y=}, {B.z=}')
print(f'{C.x=}, {C.y=}, {C.z=}')
```

可以看到，这个时候父类的所有属性都被第一个子类——也就是`B`——继承了。

```text
A.x=100, A.y=200, A.z=300
B.x=9, B.y=9, B.z=9
C.x=0, C.y=0, C.z=0
====继承====
B.x=100, B.y=200, B.z=300
C.x=0, C.y=0, C.z=0
```


### 分割继承制

但是在软件开发的早期，我们无法`import 长子继承制`，因此我们得考虑一些其他的继承法，比如`分割继承制`。

在`分割继承制`中，父类的所有资源都会被划分给其子类。

```python
@分割继承制
class A:
    x = 100
    y = 200
    z = 300
```

在继承之后，子类`B`获得了属性`x`和`z`，而子类`C`获得了属性`y`。

```
A.x=100, A.y=200, A.z=300
B.x=9, B.y=9, B.z=9
C.x=0, C.y=0, C.z=0
====继承====
B.x=100, B.y=9, B.z=300
C.x=0, C.y=200, C.z=0
```


### 斯堪的纳维亚选举制

斯堪的纳维亚选举制是北欧的维京程序员喜欢的继承法。

在这种制度下，程序中所有没有被回收的类都可以在该类的亲戚中提名一位继承人，最终由投票得分最高的类继承所有资源。

```python
@斯堪的纳维亚选举制
class A:
    x = 100
    y = 200
    z = 300
```

在类`A`死亡时，所有的类都会在类`B`和类`C`中投票。尽管在这个例子里`B`和`C`都是`A`的子类，实际上其他类也能投给`A`的兄弟等能DFS到的类。

通常，其他类会倾向于投给名字和自己长得比较像的类，一次典型的选举过程如下: 


```text
====继承====
_OrderedDictKeysView 投给 C
_OrderedDictItemsView 投给 C
_OrderedDictValuesView 投给 C
_Link 投给 C
Counter 投给 C
ChainMap 投给 C
UserDict 投给 C
UserList 投给 C
UserString 投给 C
partialmethod 投给 C
CacheInfo 投给 C
_HashedSeq 投给 B
singledispatchmethod 投给 C
cached_property 投给 B
AbstractContextManager 投给 C
AbstractAsyncContextManager 投给 C
ContextDecorator 投给 C

...

C: 142票
B: 133票
B.x=9, B.y=9, B.z=9
C.x=100, C.y=200, C.z=300
```

最终类`C`在选举中胜出，并继承了其父类`A`的所有属性。


## 使用方法

首先你需要1个3.6以上版本的Python，然后使用pip安装——

```sh
pip install git+https://github.com/RimoChan/inherit.git
```

然后你就可以在你的代码里使用继承法了，耶！

```python
from 继承法 import 长子继承制, 分割继承制, 斯堪的纳维亚选举制
```
