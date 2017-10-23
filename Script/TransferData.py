
import json
if __name__ == '__main__':
    content = ''
    with open("D:\\MyConfiguration\\ywl48338\\Desktop\\新建文件夹\\今日头条1.txt", "r") as jsonFile:
       content = jsonFile.readline();
       #content = content.replace("\\\\", "\\")


    myjson = json.loads(content)
    result = json.dumps(myjson, ensure_ascii=False)
    print(result)
