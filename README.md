# Leetcode
Not only have leetcode questions

## Q1.
Question:
1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC

Learnt:
1. pattern = r'^(\w)\1(\w)(?!\1)\2$';
   (\w) for receive a char, \1 for repeat and make groups, need to add (?!\1) if AABB need defferent things.
2. in a for loop, the start and end index won't change even you modify them in the loop itself.
3. index.sort(reverse=True)；
   Need to reverse before del it
4. re.match(pattern, (req_list[x] + req_list[x + 1] + req_list[x + 2] + req_list[x + 3])) is not None; import re and it is a boolean.
5. 扫过一次string之后还再扫一次就用counter跟temp；
   while True -> for扫 counter+= -> if counter大于temp就让temp相等 -> else自然而然counter没有增长就break
6. 三个字母连在一起就看几次删除，AABB就扫多几遍随5.思路.
7. 有个小窗口，三个或者两个空间的，“length-2or3”是遍历次数.

## Q2.
Question:<br>
我叫王大锤，是一名特工。我刚刚接到任务：在字节跳动大街进行埋伏，抓捕恐怖分子孔连顺。和我一起行动的还有另外2名特工，我提议
1. 我们在字节跳动大街的 N 个建筑中选定 3 个埋伏地点。
2. 为了相互照应，我们决定相距最远的2名特工间的距离不超过 D 。
   请听题：给定 N（可选作为埋伏点的建筑物数）、 D（相距最远的两名特工间的距离的最大值）以及可选建筑的坐标，计算在这次行动中，大锤的小队有多少种埋伏选择。
注意：
1. 两个特工不能埋伏在同一地点
2. 三个特工是等价的：即同样的位置组合( A , B , C ) 只算一种埋伏方法，不能因“特工之间互换位置”而重复使用
3. 输入描述：第一行包含空格分隔的两个数字 N和D(1 ≤ N ≤ 1000000; 1 ≤ D ≤ 1000000)； 第二行包含N个建筑物的的位置，每个位置用一个整数（取值区间为[0, 1000000]）表示，从小到大排列（将字节跳动大街看做一条数轴）
4. 输出描述: 一个数字，表示不同埋伏方案的数量。结果可能溢出，请对 99997867 取模!!!!!!

Learnt:
1. data = sys.stdin.read().split(): sys.stdin.read() whole stuff in one string -> .split() split through space, tabs, newline!!!
2. C(n, 2): n is the number of values and 2 is the (inner) window size. Formula: C(n,x)= n!/(x!(n-x)!)
3. Why上面的x是2, it is because 最大的i已经锁定，要在里面找另外两个数字的组合，所以最后还是3个特工。
4. k-i>=2因为等于2也是3个value，k和i只是index，要区分。

## Q3. Failed
Question:
1. 总共有36张牌，每张牌是1-9。每个数字4张牌。
2. 你手里有其中的14张牌，如果这14张牌满足如下条件，即算作和牌。
- 14张牌中有2张相同数字的牌，称为雀头。
- 除去上述2张牌，剩下12张牌可以组成4个顺子或刻子。顺子的意思是递增的连续3个数字牌（例如234,567等），刻子的意思是相同数字的3个数字牌（例如111,777）。
3. 例如：
1 1 1 2 2 2 6 6 6 7 7 7 9 9 可以组成1,2,6,7的4个刻子和9的雀头，可以和牌
1 1 1 1 2 2 3 3 5 6 7 7 8 9 用1做雀头，组123,123,567,789的四个顺子，可以和牌
1 1 1 2 2 2 3 3 3 5 6 7 7 9 无论用1 2 3 7哪个做雀头，都无法组成和牌的条件。
4. 输入描述：
输入只有一行，包含13个数字，用空格分隔，每个数字在1~9之间，数据保证同种数字最多出现4次。
5. 输出描述：
输出同样是一行，包含1个或以上的数字。代表他再取到哪些牌可以和牌。若满足条件的有多种牌，请按从小到大的顺序输出。若没有满足条件的牌，请输出一个数字0

## Q4. 5/8 - 62.5%
Question:
1. 一个猫咪特征是一个两维的vector<x, y>。如果x_1=x_2 and y_1=y_2，那么这俩是同一个特征。
2. 第一行包含一个正整数N，代表测试用例的个数。
3. 每个测试用例的第一行包含一个正整数M，代表视频的帧数。
4. 接下来的M行，每行代表一帧。其中，第一个数字是该帧的特征个数，接下来的数字是在特征的取值；比如样例输入第三行里，2代表该帧有两个猫咪特征，<1，1>和<2，2>
5. 输出描述：对每一个测试用例，输出特征运动的长度作为一行
3. 例如：
“<br>
1<br>
5<br>
3 0 0 1 1 3 3<br>
3 8 9 9 0 3 3<br>
2 1 5 3 4<br>
0<br>
1 0 0<br>
      ”
预期输出：2
5. 输入描述：
输入只有一行，包含13个数字，用空格分隔，每个数字在1~9之间，数据保证同种数字最多出现4次。
6. 输出描述：
输出同样是一行，包含1个或以上的数字。代表他再取到哪些牌可以和牌。若满足条件的有多种牌，请按从小到大的顺序输出。若没有满足条件的牌，请输出一个数字0

## Q5. Failed
Question:<br>
TSP, Brute Force & Dynamic Programming<br>
找路过所有城市不重复且回到原点的最短距离。<br>
输入例子：<br>
4<br>
0 2 6 5<br>
2 0 4 4<br>
6 4 0 2<br>
5 4 2 0<br>
输出例子：<br>
13

## Q6.
Question:
1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
2. You may assume that each input would have exactly one solution, and you may not use the same element twice.<br>
Example:<br>
Input: nums = [2,7,11,15], target = 9<br>
Output: [0,1]<br>
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Learnt:<br>
1. Hash Table: Store index as value in a Dictionary not and Array cuz please see the Example, key can be any value.
2. Dictionary can be give value by index like in an Array way!?!?!?!
3. Cuz we need index not value, so if the target - nums[i] is in numsToIndex, then just return the index.

## Q7.
Question:
1. Palindrome Number
2. If negative then False, "121" - True; "1221" - True; "10" - False.
   
Learnt:
1. "//" is as same as "int()"
2. "x //= 10" =》 12321 -> 1232 -> 123 -> 12 -> 1 -> 0!!!
3. Formula can be reversed!!!
4. divided by and the modulas: 10 * res + modulas = x
5. When return statement be given a condition signal e.g. reverse == xcopy. The "==" is a condition to judge T or F.
6. return in a "if" statement can return previously.
