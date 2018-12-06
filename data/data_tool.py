# coding:utf-8
import yaml
import os
import jinja2
# 当前脚本路径
basepath = os.path.dirname(os.path.realpath(__file__))
# yaml文件夹
yamlPagesPath = os.path.join(basepath, "data_element")

def parseyaml():
    '''

    遍历读取yaml文件
    '''
    dataElements = {}
    # 遍历读取yaml文件
    for fpath, dirname, fnames in os.walk(yamlPagesPath):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            # 排除一些非.yaml的文件
            if ".yml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f: #打开文件
                    data = yaml.load(f) # 读取yaml文件
                    dataElements.update(data) #更新字典
    return dataElements


def get_data_list(yamldata):
    '''
    function：把yaml对象转成需要的页面对象数据:页面对象-->定位list
    args:yaml解析的对象->dict类型
    return:
    eg:
      {"PhoneAccount":["实名纯手机号","资金号加手机号","有密码手机号"], "VerificationCode":["验证码"]
    '''
    data_object = {}
    for datatype, names in yamldata.items():
        data_names = []
        # 获取所有的Data信息方法
        dataes = names['Data']
        # 添加定位name到列表
        for dataname in dataes:
            data_names.append(dataname['name'])
        data_object[datatype] = data_names
    return data_object



def create_data_py(data_list):
    """
    function:用jinja2把templetdata模板生成dataes.py文件
    args:传get_data_list返回的内容：
       eg:
       {"PhoneAccount":["实名纯手机号","资金号加手机号","有密码手机号"], "VerificationCode":["验证码"]
    return:None
    """
    print(os.path.join(basepath, "templetdata"))
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)

    templateVars = {
               'data_list': data_list
                }
    template = template_env.get_template("templetdata")
    with open(os.path.join(basepath, "dataes.py"), 'w', encoding='utf-8') as f:
        f.write(template.render(templateVars))


if __name__ == "__main__":
    a = parseyaml()
    print(a)
    # print(a.items())
    b = get_data_list(a)
    # print(b.items())
    print(b)
    create_data_py(b)