> I am sorry that due to time, there is no English version of this document. If you have any question, Welcome to contact me using the contact details below. By the way, Life is short, I use Python  :D



# 安装及快速开始

## 1. 安装第三方依赖：

别跑！听我说，第三方依赖均不涉及实现部分，仅仅是单元测试需要到的

```shell
python3 -m venv venv # 帮你建立虚拟环境，不弄脏你的环境，可爱~
source ./venv/Scripts/activate
pip install -r requirements.txt # 速度慢，你就那啥，你懂得
```


## 2. 跑测试

```shell
python3 -m pytest
```

不出意外应该都是绿色的，如果有意外，手动run一下，还有意外？！拜托，尽力看看我refactor多次只为卖弄风骚的优雅代码 :D

## 3. 敲黑板

请把你的测试数据，放进根目录的`data.txt`文件里，像这样：

```
# data.txt

3 3 
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1
```

我几经很贴心的为你在`main.py`里选择了最稳的模式（“production”）

之后你就可以继续测试啦

PS：为了方便你测试，你可以在`data.txt`中以如上格式，以此粘贴过去多份数据，有没有换行都无所谓，让你测个饱~


# 特性

- 使用包装函数校验输入错误：流程更可控，扩展性高
- 我也不知道自己使用了什么设计模式，该拆的模块都拆了，该可配置的尽量设置成可配置的了
- 自定义异常，方便扩展，类似的过早优化坑了自己呀，不然早写完了

# 实现思路

## 处理流程

1. 建立笛卡尔直线坐标系，定位Python中的二维list：
    
    `道路网格`坐标体系与`渲染网格`并初始化占位符

2. 寻找出`道路网格`与`渲染网格`的坐标映射关系：

    ```
    渲染网格_X = 2 * 道路网格_X + 1
    渲染网格_Y = 2 * 道路网格_Y + 1
    ```
3. 利用一组数据的两点，得到该点的运动趋势，无非就是X或Y加减1的关系，这里注意异常，因为我用了包装函数，所以能走到这一步的参数值都是可以信赖的。

4. 组织一份数据：`[{(start_point):"UP"}...]`, 我在代码中有定义常量解释`UP,DOWN,LEFT,RIGHT`

5. 有了上部组织的数据，一切看似走到了尾声，以消费者的姿态从list中取一个数据在`渲染网格`渲染一下，取完也就渲染完了。
> Talking is cheap. Please see my code. 瑟瑟发抖~~ Thanks Bro~~~!


# 测试报告

![](https://ws1.sinaimg.cn/large/641eb5d8ly1ftrmlz92y2j212w0dldgz.jpg)

`html`文件在根目录的`report`文件夹内。
---

# 联系

Mail: luke.bei.2015@gmail.com

