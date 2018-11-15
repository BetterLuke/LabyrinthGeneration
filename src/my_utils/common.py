"""
filepath: 输入数据文件路径
data: 数据
"""
def loadInputFile(filepath):
    datatemp = []
    inputdatas = []
    with open(filepath, 'r') as f:
        for line in f:
            if not line.isspace():
                datatemp.append(line.strip())
    for i in range(0, len(datatemp), 2):
        inputdatas.append({datatemp[i]:datatemp[i+1]})
    return inputdatas