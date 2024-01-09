<div align="center">
<h1 align="center">🍭Lab_Cambridge_Gambling_Task **剑桥赌博任务** </h1>
Project Name Psychopy Experimental programming design(Psychopy 实验编程设计)
</div>

> ### Operating System: Windows(可兼容Linux/MacOS)

> ### Programming Language and Version: Python 3.8

The task is designed to evaluate decision-making and risk-taking behavior, reward and loss contexts are carried out separately

该任务旨在评估决策和冒险行为，奖励和损失背景分别进行

### Time Taking:

> 10 minutes 10分钟

### Task:

> 试次开始，呈现博弈块，其中一部分为蓝色，另一部分为橙色。
> 有5种不同的比例，从非常确定到非常不确定。被试必须对他们预期程序抽取的结果下注。然后显示旋转指针，指针落在其中一种颜色上，作为反馈。
>
> 有两个条件；允许奖惩分离的输赢条件。

> The trial starts and the game blocks are presented, one part is blue and the other part is orange.

1. There are 5 different scales, from very certain to very uncertain.
2. Participants had to place bets on the outcomes they expected the program to draw.
3. The spinning pointer is then shown, and the pointer lands on one of the colors as feedback.

### Materials:

> 无明确的数据材料，仅有蓝色红色相关图片材料

### Statistical Result(Output):

> 结果测量：在赢和输的情况下，分别计算每个概率级别上放置的筹码的平均值。只包括最可能结果的选择。这用于使用以下公式计算风险调整（RA）分数：风险调整=（2*90%的时候赌bet）+（1* 80%的概率时bet赌）+（0*70%的概率时赌bet）-（1*赌60%的概率时bet赌）-（2*50%的概率时bet下注）/Average bet平均下注.   RA分别针对赢和输的背景进行计算。

> Outcome measurement: Calculate the mean value of the chips placed on each probability level separately for win and loss cases. Only the most likely outcomes are included in the selection. This is used to calculate a risk-adjusted (RA) score using the following formula: Risk Adjustment = (2 * bet 90% of the time) + (1 * bet 80% of the time) + (0 * bet 70% of the time )-(1*bet bet with 60% probability)-(2*50% probability bet bet)/Average bet average bet. RA is calculated separately for the background of winning and losing.

### Experimental Procedure：

> 1. 呈现当前的红蓝卡片张数，
> 2. 被试推测可能命中的卡牌颜色并按键
> 3. 被试选择奖励的权重
> 4. 记录存储每次的数据情况，告知被试此次的trial赢or输，并循环回到下一个trial去

### **指导语部分 Instruction Part**

**中文版**

> **开始部分**
>
>> 您好！欢迎您参加我们的实验！
>>

>> 在测试开始之前，你会获得100枚代币，并在屏幕左侧显示；
>>
>> 随后屏幕会呈现蓝色或红色的卡片共计10张；
>>
>> 10张卡片中的一张中含有代币，请你猜测含有代币那张图片是什么颜色
>>
>> 如果选择红色，请按键盘上的左方向键；
>>
>> 如果选择蓝色，请按键盘上的右方向键。
>>
>> 当你确定选择的颜色后，屏幕右侧出现赌注；
>>
>> 赌注会从小变大或从大变小，同时在屏幕右下角会指示
>>
>> 当前的赌注呈现是升序或是降序；
>>
>> 如果你觉得出现的赌注较为合适，
>>
>> 请按下方向键锁定当前的赌注；
>>
>> 如果你赌对了，
>>
>> 你会赢得你赌注的代币数；
>>
>> 如果你赌输了，
>>
>> 你会失去你赌注的代币数；
>>
>> 你的任务是尽可能获得更多的代币。
>>

>> 请按任意键继续
>>

> **结束部分**
>
>> 您现在已经完成了上机部分的实验，
>>

>> 请您休息一会儿，谢谢您的参与！
>>

**English Version**

> **Start Part**
>
>> Hello! Welcome to our experiment!
>>

>> Welcome to this test!
>> Before the test starts, you will get 100 tokens, which will be displayed on the left side of the screen;
>>
>> Then the screen will show a total of 10 blue or red cards;
>>
>> One of the 10 cards contains tokens, please guess the color of the picture containing tokens
>>
>> If red is selected, press the left arrow key on the keyboard;
>>
>> If you choose blue, press the right arrow key on your keyboard.
>>
>> When you confirm the selected color, the bet appears on the right side of the screen;
>>
>> The bet will change from small to large or from large to small, and at the same time, the lower right corner of the screen will indicate whether the current bet is rising order or descending;
>>
>> If you think the bet appears more appropriate, please press the arrow key to lock the current bet;
>>
>> If you bet correctly, you win the number of tokens you staked;
>>
>> If you lose your bet, you will lose the number of tokens you bet;
>>
>> Your task is to get as many tokens as possible.
>>

>> If you ensure that you are in a state without interruption and interference (e.g., no emergency, no cell phone ringing),
>>

>> please press any key to continue.
>>

> **End Part**
>
>> You have now completed the on-computer part of the experiment.
>>

>> Please take a break. Thank you for your participation!
>>

# material requirements

> No clear data materials, only blue and red related picture materials

# About Data Processing

At the end of the experiment, relevant results should be presented to the subjects, and the data should be integrated and processed by experimenters in general, so as to screen the required information for the subjects to conduct a series of statistical analysis.

> At this time, we run the **post_process.py** file and input the number of the subjects, and generate the report of the subjects in the output directory. The overall information of the subjects will be presented in the **subjects_results.csv** format, and the subjects can also conduct further statistical analysis by processing **post_process.ipynb**

> 实验文件分为两个部分：练习部分和测试部分，分别对应运行**CGT_python._practice.py**和**CGT_python.py**文件。

> The experiment files are divided into two parts: the practice part and the test part, which correspond to running the **CGT_python._practice.py** and **CGT_python.py** files respectively.

> 实验结束后需要向被试展示相关结果，同时对数据进行总体的整合处理，筛选需要的信息以便于主试进行一系列统计学分析，这时我们运行**post_process.py**文件，输入被试编号即可，生成被试报告在output目录下，被试总体信息在**subjects_results.csv**格式文件中呈现，主试也可以通过处理post_process.ipynb展开进一步数据统计分析操作

### References

[https://www.cambridgecognition.com/cantab/cognitive-tests/executive-function/cambridge-gambling-task-cgt/](https://www.cambridgecognition.com/cantab/cognitive-tests/executive-function/cambridge-gambling-task-cgt/)

Ricardo J. Romeu, Nathaniel Haines, Woo-Young Ahn, Jerome R. Busemeyer, Jasmin Vassileva,
A computational model of the Cambridge gambling task with applications to substance use disorders,
Drug and Alcohol Dependence,
Volume 206,2020,107711,ISSN 0376-8716,
[https://doi.org/10.1016/j.drugalcdep.2019.107711.](https://doi.org/10.1016/j.drugalcdep.2019.107711.)
