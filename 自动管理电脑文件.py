import os
# print(os.getcwd())
# # os.path.join()
# files = os.listdir()
# for file in files:
#     print(file, os.path.isdir(file))
# specify_str = "python"
# for file in os.scandir():
#     if not file.is_dir():
#         print(file.name)


ls = ["python","PYTHoN","pYThON","PYTHON","hHAHA"]
list_lower = []
for item in ls:
    item = item.lower()
    list_lower.append(item)
print(list_lower)
