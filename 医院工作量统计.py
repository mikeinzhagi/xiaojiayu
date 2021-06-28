from numpy import empty


position = []
doctor_reporter = []
doctor_auditer = []

with open(r"C:\Users\milan\Desktop\123.txt", encoding='utf8') as f0:
    lines = f0.readlines()  # 读取文件
    for line in lines:
        if line.isspace() is False:
            line = line.strip('\n')  # 去除换行符
            position.append(line)


with open(r"C:\Users\milan\Desktop\报告医生.txt", encoding='utf8') as f1:
    lines = f1.readlines()  # 读取文件
    for line in lines:
        if line.isspace() is False:
            line = line.strip('\n')  # 去除换行符
            doctor_reporter.append(line)


with open(r"C:\Users\milan\Desktop\审核医生.txt", encoding='utf8') as f2:
    lines = f2.readlines()  # 读取文件
    for line in lines:
        if line.isspace() is False:
            line = line.strip('\n')  # 去除换行符
            doctor_auditer.append(line)

# print(doctor_reporter)
# print(doctor_auditer)
# print(position)

# for doctor in doctor_reporter:
#     if doctor in doctor_auditer:
#         print(doctor, end=" ")

with open(r"C:\Users\milan\Desktop\123456.txt", encoding='utf8') as f:
    lines = f.readlines()  # 读取文件
    i= 1
    for line in lines:
        if line.isspace() is False:
            for doctor in doctor_reporter:
                if doctor in line:
                    print(doctor,"有",i,"条记录")
                    i+=1
