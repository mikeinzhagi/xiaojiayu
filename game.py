
score = 10
level = ("D" if 0 <= score <60 else
"c" if 60 <= score <80 else
"b" if 80 <= score <90 else
"a" if 90 <= score <100 else
"s" if score == 100 else
         "wrong input")
print(level)