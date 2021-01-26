# Last Soldier
The last soldier is a puzzle. You take one random pieced out, then you need to take pieces one by one only by jumping over it like you do in checkers.

The goal is to finish with only one piece left i.e. the last soldier.

![Last soldier puzzle](https://github.com/yarivgdidi/lastSoldier/blob/master/lastSoldier.jpg "Last soldier puzzle")
  
I got this puzzle as a gift in a Secret Santa (Giant/Dwarf) Purim game from some one who hates me.

First it seemed easy, then it seemed impossible, so I had to write some code that will solve this for me.

Just run the python script in thge command line and you get options like shown below
```

D:\Python\lastSoldier>python lastSoldier.py
4 - 1 > ur     3 - 3 > l      4 - 3 > l      1 - 1 > dr     4 - 4 > ul     1 - 0 > dr     2 - 2 > dl     3 - 0 > ur     4 - 1 > r      0 - 0 > dl     2 - 0 > dr     4 - 3 > l      4 - 0 > r
    1              1              1              1              1              1              1              1              1              1              0              0              0
   1  1           1  1           1  1           1  1           1  0           1  0           0  0           0  0           1  0           1  0           0  0           0  0           0  0
  1  0  1        1  1  1        1  1  1        1  1  1        1  1  0        1  1  1        1  0  1        1  0  0        0  0  0        0  0  0        1  0  0        0  0  0        0  0  0
 1  1  1  1     1  0  1  1     1  1  0  0     1  1  0  0     1  1  0  1     1  1  0  0     1  1  1  0     1  1  0  0     0  1  0  0     0  1  0  0     0  1  0  0     0  0  0  0     0  0  0  0
1  1  1  1  1  1  0  1  1  1  1  0  1  1  1  1  1  0  0  1  1  1  0  0  1  1  1  0  0  0  1  1  0  0  0  1  1  1  0  0  1  1  1  0  0  1  0  0  1  0  1  0  0  1  0  1  0  1  1  0  1  1  0  0  0


4 - 1 > ur     3 - 3 > l      4 - 3 > l      1 - 1 > dr     4 - 4 > ul     1 - 0 > dr     2 - 2 > dl     3 - 0 > ur     0 - 0 > dl     4 - 1 > r      2 - 0 > dr     4 - 3 > l      4 - 0 > r
    1              1              1              1              1              1              1              1              1              0              0              0              0
   1  1           1  1           1  1           1  1           1  0           1  0           0  0           0  0           1  0           0  0           0  0           0  0           0  0
  1  0  1        1  1  1        1  1  1        1  1  1        1  1  0        1  1  1        1  0  1        1  0  0        0  0  0        1  0  0        1  0  0        0  0  0        0  0  0
 1  1  1  1     1  0  1  1     1  1  0  0     1  1  0  0     1  1  0  1     1  1  0  0     1  1  1  0     1  1  0  0     0  1  0  0     0  1  0  0     0  1  0  0     0  0  0  0     0  0  0  0
1  1  1  1  1  1  0  1  1  1  1  0  1  1  1  1  1  0  0  1  1  1  0  0  1  1  1  0  0  0  1  1  0  0  0  1  1  1  0  0  1  1  1  0  0  1  1  1  0  0  1  0  0  1  0  1  0  1  1  0  1  1  0  0  0


4 - 1 > ur     3 - 3 > l      4 - 3 > l      1 - 1 > dr     4 - 4 > ul     1 - 0 > dr     2 - 2 > dl     4 - 1 > r      3 - 0 > ur     0 - 0 > dl     2 - 0 > dr     4 - 3 > l      4 - 0 > r
    1              1              1              1              1              1              1              1              1              1              0              0              0
   1  1           1  1           1  1           1  1           1  0           1  0           0  0           0  0           0  0           1  0           0  0           0  0           0  0
  1  0  1        1  1  1        1  1  1        1  1  1        1  1  0        1  1  1        1  0  1        1  0  0        1  0  0        0  0  0        1  0  0        0  0  0        0  0  0
 1  1  1  1     1  0  1  1     1  1  0  0     1  1  0  0     1  1  0  1     1  1  0  0     1  1  1  0     1  1  0  0     1  1  0  0     0  1  0  0     0  1  0  0     0  0  0  0     0  0  0  0
1  1  1  1  1  1  0  1  1  1  1  0  1  1  1  1  1  0  0  1  1  1  0  0  1  1  1  0  0  0  1  1  0  0  0  1  1  1  0  0  1  0  0  1  0  1  0  0  1  0  1  0  0  1  0  1  0  1  1  0  1  1  0  0  0


```