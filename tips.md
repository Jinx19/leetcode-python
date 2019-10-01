# 最大值最小值

# list
列表反转可以用`reverse()`，改变原有列表顺序。

也可以用切片进行反转，l[::-1],对于字符串，只能用切片返回一个反转后的字符串。

列表删除元素：`list.remove(值)`，删除匹配到的第一个元素或者`list.pop(索引)`

# dict
和c++中的map类似，key-value方式。dict.has_key(key)判断有无元素,dict[key] = value插入或赋值。字典

排序：列表有自带的sort函数，直接对原列表进行更改。
对于字典，字符串等数据结构，必须用sorted函数。
sorted(iterable[, cmp[, key[, reverse]]])

cmp和key都是函数，key的输出是cmp的输入

比如

```python
dic = {‘a’:2,’b’:1}
sorted(dic.items(),key=lambda d:d[0])
```
是按照key排序，
返回[(‘a’,2),(‘b’,1)]

把d[0]换成d[1]是按照value排序，cmp函数默认是升序

sorted(“123321”)返回[‘1’, ‘1’, ‘2’, ‘2’, ‘3’, ‘3’]

# string
循环输入的字符串做处理
```python
while True:
    try:
        x = raw_input()
        if not x:
            break
    except:
        break
```
`str()` 数字转字符串
`int()` 浮点数转int或整数字符串转int，`int(‘1’) = int(1.2) = 1`
同样可以做进制转换，`int(‘0xA1’,16) = 161`

`isalpha()`：判断字符串是否全是字母

`isdigit()`：判断字符串是否全是数字

`is_integer()`：判断浮点数是否为整数

`join()`：”分隔符”.join(字符串序列)

`str.count(substr,start,end)`：计数substr在范围内出现的次数

`str.upper()`：转大写

`str.lower()`：转小写
# 标准库
## collections
这个模块实现了特定目标的容器，以提供Python标准内建容器 dict , list , set , 和 tuple 的替代选择。
### deque
### Counter
### OrderedDict
### defaultdict


# 数据结构
## 列表
```python
list.append(x)
在列表的末尾添加一个元素。相当于 a[len(a):] = [x] 。

list.extend(iterable)
使用可迭代对象中的所有元素来扩展列表。相当于 a[len(a):] = iterable 。

list.insert(i, x)
在给定的位置插入一个元素。第一个参数是要插入的元素的索引，所以 a.insert(0, x) 插入列表头部， a.insert(len(a), x) 等同于 a.append(x) 。

list.remove(x)
移除列表中第一个值为 x 的元素。如果没有这样的元素，则抛出 ValueError 异常。

list.pop([i])
删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop() 将会删除并返回列表中的最后一个元素。（ 方法签名中 i 两边的方括号表示这个参数是可选的，而不是要你输入方括号。你会在 Python 参考库中经常看到这种表示方法)。

list.clear()
删除列表中所有的元素。相当于 del a[:] 。

list.index(x[, start[, end]])
返回列表中第一个值为 x 的元素的从零开始的索引。如果没有这样的元素将会抛出 ValueError 异常。

可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。

list.count(x)
返回元素 x 在列表中出现的次数。

list.sort(key=None, reverse=False)
对列表中的元素进行排序（参数可用于自定义排序，解释请参见 sorted()）。

list.reverse()
反转列表中的元素。

list.copy()
返回列表的一个浅拷贝。相当于 a[:] 。
```
### 列表作为栈
```python
stack = [3,4,5]
stack.append(6)
stack.append(7)
stack.pop()
```
### 列表作为队列使用
列表也可以用作队列，其中先添加的元素被最先取出 (“先进先出”)；然而列表用作这个目的相当低效。因为在列表的末尾添加和弹出元素非常快，但是在列表的开头插入或弹出元素却很慢 (因为所有的其他元素都必须移动一位)。

若要实现一个队列， collections.deque 被设计用于快
速地从两端操作。例如

```python
from collections import deque
queue = deque([1, 2, 3])
queue.append(43)
print(queue.popleft())
```
### 列表推导式
```python
squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
```

列表推导式的结构是由一对方括号所包含的以下内容：一个表达式，后面跟一个 for 子句，然后是零个或多个 for 或 if 子句。 其结果将是一个新列表，由对表达式依据后面的 for 和 if 子句的内容进行求值计算而得出。 举例来说，以下列表推导式会将两个列表中不相等的元素组合起来:
```python
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
### 嵌套的列表推导式

```python
[[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

# 排序

[排序指南](https://docs.python.org/zh-cn/3/howto/sorting.html#sortinghowto)

可以使用 `list.sort()` 方法，它会直接修改原列表（并返回 None 以避免混淆），通常来说它不如 `sorted()` 方便 ——— 但如果你不需要原列表，它会更有效率。
另外一个区别是， `list.sort()` 方法只是为列表定义的，而 `sorted()` 函数可以接受任何可迭代对象。

关键函数
key 形参的值应该是一个函数，它接受一个参数并并返回一个用于排序的键。这种技巧速度很快，因为对于每个输入记录只会调用一次 key 函数。

```python
a = "this is a test string from Andrew"
res = sorted(a.split(), key=str.lower)
```

Operator 模块函数
```python
from operator import itemgetter, attrgetter
sorted(student_tuples, key=itemgetter(2))
sorted(student_objects, key=attrgetter('age'))
```
# 刷题常用

进制转换：
```python
int("字符串",进制) 返回10进制数
bin(数字) 返回0b开头的2进制字符串
hex(数字) 返回0x开头的16进制字符串
oct(数字) 返回0o开头的8进制字符串
str(10进制数字) 返回10进制字符串
```

字符列表合并成str:
```python
"".join(char_list)  
```

长度：
```python
len(list)
len(str)
```

list操作:
```python
l1 = [] 创建list
排序，getkey函数用来获取key,默认是第一个元素(此时不要指明key)
False是从小到大，True是从大到小
list.sort(key=getkey,reverse=False/True) 
list.insert(index,val) 向index处插入val,原本的index后移
list.extend(list1) 将list1追加list之后
list.append(val) 在list末尾添加val
list.pop(index=-1) 删除指定index，默认是最后一个
list.reverse() 反向列表中元素
```

词典操作:
```python
d1 = {key:val} 创建dict
dict.items() 以列表返回可遍历的(键, 值) 元组数组
dict.keys() 以列表返回一个字典所有的键
dict.values() 以列表返回字典中的所有值
dict.update(dict2) 添加，把字典dict2的键/值对更新到dict里
pop(key[,default]) 删除，删除字典给定键 key 所对应的值
dict[key] =new_val 修改，修改key对应的value
```

集合：不包含重复元素
```python
s1 = set() 创建一个空集合必须用set()
s1 = {1,2,3} 创建集合
s.add(x) 添加元素
s.update(list) 添加元素
s.remove( x ) 移除元素，不存在发生错误
s.discard( x ) 移除元素，不存在不报错
s.clear() 清空集合
x in s x在集合中
set.intersection(set1, set2 ... etc) 返回交集
set.union(set1, set2...) 返回并集
set1.issubset(set2) s1是否为s2的子集
set1.difference(set2) 返回差集， 包含在s1，但是不在s2中

利用集合去除重复
new_list = list ( set(list) )
```

内置函数:
```python
abs(val) 绝对值
max(list) list的最大值
min(list) list的最小值
sum(list) 求和
ord(char) 返回值char的num
chr(num) 返回num对应的char
any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如
果有一个为 True，则返回 True。

all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，
如果是返回 True，否则返回 False。

map(func,迭代对象) 对迭代对象执行批量func，例如： list(map(int,["123","234"]))
```
深复制：
python3在函数参数中传递的对象是引用

利用copy对象进行深赋值
```python
import copy
new_obj = copy.copy(obj)
```

全排列：
例子：
```python
import itertools
result = list(itertools.permutations([1,2,3])) 
# 返回[1,2,3]所有全排列，并放入list中
```

牛客网格式：
```python
#定义全局变量，函数
while True:
    try：
        #读取case并处理
        #打印
    except:
        # 所有case结束后的处理
        break
```