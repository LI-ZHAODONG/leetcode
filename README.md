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
Question:
我叫王大锤，是一名特工。我刚刚接到任务：在字节跳动大街进行埋伏，抓捕恐怖分子孔连顺。和我一起行动的还有另外2名特工，我提议
1. 我们在字节跳动大街的 N 个建筑中选定 3 个埋伏地点。
2. 为了相互照应，我们决定相距最远的2名特工间的距离不超过 D 。
   请听题：给定 N（可选作为埋伏点的建筑物数）、 D（相距最远的两名特工间的距离的最大值）以及可选建筑的坐标，计算在这次行动中，大锤的小队有多少种埋伏选择。
注意：
1. 两个特工不能埋伏在同一地点
2. 三个特工是等价的：即同样的位置组合( A , B , C ) 只算一种埋伏方法，不能因“特工之间互换位置”而重复使用
输入描述：
第一行包含空格分隔的两个数字 N和D(1 ≤ N ≤ 1000000; 1 ≤ D ≤ 1000000)
第二行包含N个建筑物的的位置，每个位置用一个整数（取值区间为[0, 1000000]）表示，从小到大排列（将字节跳动大街看做一条数轴）
输出描述:
一个数字，表示不同埋伏方案的数量。结果可能溢出，请对 99997867 取模!!!!!!

Learnt:
1. data = sys.stdin.read().split(): sys.stdin.read() whole stuff in one string -> .split() split through space, tabs, newline!!!
2. C(n, 2): n is the number of values and 2 is the (inner) window size. Formula: C(n,x)= n!/(x!(n-x)!)
3. Why上面的x是2, it is because 最大的i已经锁定，要在里面找另外两个数字的组合，所以最后还是3个特工。
4. k-i>=2因为等于2也是3个value，k和i只是index，要区分。
