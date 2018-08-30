### 基本数据类型
***
#### 字符串
1.　多行字符串

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCE0d86f9866bda6f57c380ba8b62901cdc/3752)
2.　原始字符串

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCE5206a01b32b63f756ad9515bd80bfdea/3758)
***
#### 序列共同特征
1. 字符串
+ index访问

+ 切片
+ 拼接
+ 数乘

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCEf3ab454c31ae60dec9f9ab555c8e4d41/3771)
2. 列表
+ index访问

+ 切片
+ 拼接
+ 数乘

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCE11453d9edb86f2aa75a3df5d30467716/3778)
3. 元组

+ index访问

+ 切片
+ 拼接
+ 数乘

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCEe7a2f35a70e2b0d262e43565c49afec6/3782)

注意：序列中不存在减运算

4. 序列的in/len/min/max()

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCEe838c72243697a65bb8de782f701e8a7/3790)

注意：min/mx遵循ａｓｃｌｌ码，方法如下：

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCE955bd6b87fd8a30d5de73cefbdfd2410/3798)

***
#### 集合
+ 无序，不能使用index以及切片
+ 不重复
+ 可以使用in/len/min/max
+ 特有运算符：差集、交集、并集

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCE3a1e8ed04358e2bc578f874a2e9fefe6/3809)

注意：序列与集合为空时的表示：

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCEaf8a71d5507819ddec6735e8650f2a7f/3814)

***
#### python基本数据类型归纳

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCE194e358e21a642ddba090cc86ed5ba20/3822)

分类：
+ 值类型：不可改变,包括ｓｔｒ,int,float,tuple

> 值类型的数据不可改变表现在：数据只可读不可该，对变量重新赋值是析构原变量后生成新变量，所以从这个意义上来说，值类型数据不允许改变（简单判断方法：内存地址没变就是不可改变）

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCE550b1ab1e6081d78a9e82da909557856/3837)

复杂情况：

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCE1a173f5b550183387c5319adb1de7cce/3863)

可以看出：ａ[3]是引用类型，可以改变，改变后a[3]内存地址未变，相当于未对元组元素进行改变，如果试图给a[3]赋值，即改变ａ[3]内存地址，则报错。所以可证整个元组不可改变
> 因此：元组的不可改变指：元祖起始内存ＩＤ不变，各个元素的起始ＩＤ也不可改变！！！

+ 引用类型：可改变,包括list,set,dict

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/D28FA0A63AB642E6BF04A8CC91EE6C4D/3885)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/B0B352C8620344D1B425071A5FAEE43D/3887)

可以看出，元素的内存地址改变了，所以可以改变。
***
### python运算符


![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/41F2494F799747BA8766A1EBA328B8A8/3894)
+ 算数运算符中的Bool值

int str list tuple

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/C74788D3ED214988B4B042DF219CAAD4/3901)

set dict
![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/67A012D125394EBC9E6D1E1D2CE6E8F9/3905)

报错总结：
![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/3393AF8A78D34407BCAA3C54ACBF5F3D/3918)

+ 广义的比较运算符

str

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/2AD376A5877745EABF9E4E755FB509B0/3923)
> 按ascll码比较，从左往右比，字符与字符间采用与逻辑

list tuple

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/342E53A0E2404B4EAC1761B0C103EC78/3934)
> 序列数据类型军类似

注意：其他未提到的数据类型如字典等，一般不进行关系运算

+ 逻辑运算符及其扩展
> 特征：运算符两端为bool类型的数值或变量

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/00659C5A21EB4B4CB31DE9BE5517C881/3946)

对于数值，true/false会自动转变为数值

+ 成员运算符

特殊地：字典

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/AD7B7E444BAD4F5DBC155C47717076B8/3955)

+ 身份运算符

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/B7A3FFDA7B954028A202A59D859A288B/3965)
> is 判断依据为内存id

+ 位运算符

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/5850341CC17E44B7969A9E3FB14A7045/3987)

#### 运算优先级

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/D6739300C15243888FCB854C31ECED2F/3973)
#### 对象三要素：id、value、type
对应三个运算符和方法： is  ==  isinstance
***
### sublime快捷键
+ package control ： Ctrl+shift+P
+ 运行python命令行：ctrl + ~
+ build:ctrl +B 
+ 注释：Ctrl+ /
+ 缩进：Ctrl+]  撤销缩进：Ctrl+[

***
#### 几个特殊用法
+ print(str,'字符')
+ 循环+else

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/8515BCDE86E244FD9BE3306BC679E6B4/4012)
+ 带步长的切片

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/4289462713E24E02A719C3470F63194A/4019)

    注意：左闭又开
    
+ 带步长的range()
  
+ pass代码块的作用：可以代替正式代码，后想清楚再填充，并且不会报错

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/B588A66555FC4CB68C72CAE06C6EA461/4033)
***
#### 包、模块以及导入
+ 概念

包：文件夹（通俗）

模块：某个python文件，里面包含类与函数

+ 模块导入方法
1. import module_name [as new_name]
> import只能接module_name，后面不能接package_name或者module_name.variable_name...

> 所以通过import module_name导入模块后，要使用variable/function/class...必须是这样的形式：module_name.variable_name/function_name/class_name

2. from  module_name import value/function/class... [as new_name]
> 相比于import直接导入模块，from ... import 直接导入模块内元素
3. from package_name import module_name
> 从 某个包导入某个模块

> from package_name import *  :导入包的所有模块

4. import package
> import 直接导入包的方法不存在，此写法实际上会导入package的__init__模块，因为__init__.py本身是一个模块，他的模块名叫做package_name

+ 特殊情况举例
1. 导入子package下的module

正确方式：

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/0BD600C824A84C26934C39EFAF9A2FF0/4145)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/AE1C0D5649A94300A06277585A52569B/4141)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/AE1C0D5649A94300A06277585A52569B/4141)

错误方式：不能在单独的import语句后直接加变量等模块内元素

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/303D289C147945BEAE3F4656E48149D6/4158)

2. 导入某个package所有module

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/2FE44D6F7FE149C089C6589F835576FA/4164)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/0D9AACF006154970BA32140EE1642387/4167)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/47A5B4A7183A476EBFB952DFD10D1958/4169)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/9A8E9B0DD18F4D80A007F55E34866D81/4171)
> 要想利用*导入package下的modules，必须在package的__init__.py中用系统变量__all__标识。

3. 导入某个package特定module
> 类似上一个，在__all__中标识

4. 导入某个module

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/D43227F960794CD3ADCB6B674482B8B0/4190)

5. 导入某个module中特定元素

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/D43227F960794CD3ADCB6B674482B8B0/4190)

+ * 与__all__的搭配
1. 从包中导入多个模块时（上面已经举例）
2. 从模块中导入多个元素时

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/E21E8F9A98C845A38497187ED7223793/4205)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/FADB1B89DBBD42D6A88ECEEC1B53283F/4207)

注意：避免循环导入module，即module1导入module2，module2又导入module1；python有避免重复导入module的机制

+   \_\_init__.py的作用：可以添加某个package下所有module均需要导入的其他module

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/FE55129C13134EBBBD1225AF405F48DC/4223)


![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/F9F3F218BB714598AF2DB7C0227A2B98/4238)


> 上述总结的作用是：在init文件中写入大量公共import，其他文件或模块直接 import package_name即可引入所有公共import ，提高工作效率。

***
插入：round系统函数

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/7BC7E2A33F6F4BB0B30EC8B158633A61/4252)

3:小数点后三位
***
### 序列解包

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/409A8A060A894FBB83CC1064F7E2B356/4263)

在函数中的应用

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/A76BB4ABE308442CA984E47CD65FE9BA/4268)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/16F1B592E0714E018F047566DB3A065D/4270)

***
### 函数
#### 关键字参数与默认参数
1. 函数申明时，默认参数必须位于形参的最右边

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/22899509B6DB485585A0848D215A33AE/4282)

2. 对于函数调用时，位置参数与关键字参数不可混搭！关键字参数全部靠右！！

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/21DED540CBD44B329AEE94C8072BE0F9/4276)

未完待续。。。

***
### 类与对象

#### 一、概览

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/4BA4264BAFB348FAB8F714520597EC13/4296)
#### 二、类变量+实例变量+实例方法+构造函数
+ 含义：

> 类变量：不依附于某一个具体的对象，一般为类的多个实例所共有，比如,sum:对类的实例进行计数统计

> 实例变量：为对象所特有，如姓名等

> 优雅的类须严格区分二者！

> 实例方法：为实例服务的方法

> 构造函数：特殊的实例方法，为对象初始化

+ 具体区分
1.
![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/9F773BD98AAC4DF0BED7C46680E74CC1/4332)

> 可见，通过系统变量__dict__，可以查看类或对象的属性；对象student1不含有类变量sum!!

2.
![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/7A0FEA93B21D4E7BAFC02FF5F49138F4/4344)

> 对象既可以访问实例变量，也可以向上查找类变量；类当然可以访问类变量，但不能访问实例变量

3.
![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/4D2C30D203964A1E960C270F95CF3B2F/4355)
> 实例方法访问类变量的两种方式

4. 实例方法访问实例变量：当然

5. 对象调用实例方法：当然；类调用实例方法也可以，但意义不大，很鸡肋，只不过python提供了这样一种灵活的使用方式

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/A41FCEABDEAE48CDBA1A90397E2A0C43/4372)

> 虽然比较鸡肋，但此处解释了参数self的含义：实例方法中的self指对象，self名称可以变！

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/0CCBE46F125C4B51840FB16C2D0EBED7/4380)

可以看到：无报错

#### 三、类方法与静态方法
1. 类方法

+ 类方法定义：@classmethod

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/680B9D5648A3471DA6EDE22353EDBFA2/4384)

> 对象可以调用类方法，不推荐；类可以调用类方法，推荐;
类方法当然能调用类变量：cls.variable,类方法不能调用实例变量；当然cls也可以换为其他符号，比如this

2.静态方法

+ 静态方法定义：@staticmethod
![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/D21D4530DCDA4416AE77A482FB73556B/4413)
> 静态方法本质上就是个普通函数，但放在类里，可以像方法一样使用。静态方法为类与实例提供无差别的方法。

> 静态方法不能访问实例变量，可以通过Student.sum来访问类变量

> 把它当普通函数对待

#### 四、成员可见性
１．隐藏变量

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/DD78FFB410A44E51891DB47F68F6F28D/4423)

> 隐藏的变量不可以通过类、对象直接访问；但实例、类方法可以在类内部访问隐藏变量，外部类、对象可以借助各自的方法实现对隐藏变量的访问。

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/WEBRESOURCEe95a87e1822525fe2bf0828722c5ce17/4436)

#### 五、继承性与多态性

+ 法1

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/036010A073DD4C94A0C61207FE1AF78A/4459)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/BA9C934F0D764DD6AAD4E3A03E857A03/4448)

+ 法2

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/5020608AC753436989C63FB99AF35331/4457)

> 可以看出，同名方法会被覆盖
***
### 正则表达式与JSON

#### 一、正则概述
+ 两种实现方法

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/F2A36A2B608B433398BC5D53173D760D/4470)

+ 思维导图

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/8F84C4DB8F684BEBA6B42E31EF38744B/4485)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/A8F6BD0B64E745389A056F1A138DF159/4477)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/5904C1E311D24DDA9F84E3B6DD831CBB/4476)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/D8B686BAFC98485EB3B770090380C9D8/4478)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/75CF02326A854CA091825A77D84916B0/4475)

+ 用法举例

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/456430E769A14F34B755013E8663FF43/4483)

+ re模块的方法

1. findall方法
 
    **re.findall(pattern, string, flags)**

> 第三个参数：标志位 re.I表示忽略大小写 re.S表示元字符'.'可以指代换行符

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/792328827CC8424EB7D2935B1BBDB841/4507)

2. sub方法

    **re.sub(pattern, repl, string, count, flags)**
    
> repl：replace替换值，可以是函数

> count:替换个数

> flages:re.I、re.S


![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/8F9E186FB920425C8EF4F89D9C336CBD/4516)

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/ED7450C441F340C08411D1F4BCA0B6E4/4524)

+ 参数为函数实现动态替换

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/45BEB81F66804222AE143C05D6C31137/4539)

> 注意：函数名convert1可以自定义；参数value1也可以自定义

> 唯一要求：自定义函数参数个数为1，函数必须返回某个替代字符串

> group 为match对象的一个方法，用来取出匹配值！！

3. match与search方法

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/E16FDE449B5841EEB58C55B5415F4BFC/4567)

> 可以说findall与sub是search函数的高级封装，封装了一个一个search的过程

> 注意group方法的使用；span方法会返回匹配值在字符串中的index!

+ group方法使用

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/9A1DB4DF620941C991A08125AF1CFFAC/4577)

> 直接使用findall更优

+ 坑：正则最好在字符串前加r

![](https://note.youdao.com/yws/public/resource/5eabae31d62fa288e7021d6f89d8468c/xmlnote/36AC7DC009C54962805E18D5F309D9BD/4585)

> findall（）正则中有分组就会只返回分组！！这种情况下使用search+group（）可能更灵活




