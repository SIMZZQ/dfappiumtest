# coding:utf-8
import yaml
import os
import jinja2
# 当前脚本路径
basepath = os.path.dirname(os.path.realpath(__file__))
# yaml文件夹
yamlPagesPath = os.path.join(basepath, "page_element")

def parseyaml():
    '''

    遍历读取yaml文件
    '''
    pageElements = {}
    # 遍历读取yaml文件
    for fpath, dirname, fnames in os.walk(yamlPagesPath):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            # 排除一些非.yaml的文件
            if ".yml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f: #打开文件
                    page = yaml.load(f) # 读取yaml文件
                    pageElements.update(page) #更新字典
    return pageElements


def get_page_list(yamlpage):
    '''
    function：把yaml对象转成需要的页面对象数据:页面对象-->定位list
    args:yaml解析的对象->dict类型
    return:
    eg:
      {"MinePage":["我的","登录",...], "AlertPage":["确定"],...
    '''
    page_object = {}
    for page, names in yamlpage.items():
        loc_names = []
        # 获取所有的loctors定位方法
        locs = names['locators']
        # 添加定位name到列表
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page] = loc_names
    return page_object



def create_pages_py(page_list):
    """
    function:用jinja2把templetpage模板生成pages.py文件
    args:传get_page_list返回的内容：
       eg:
       {"MinePage":["我的","登录",...], "AlertPage":["确定"],...
    return:None
    """
    print(os.path.join(basepath, "templetpage"))
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)

    templateVars = {
               'page_list': page_list
                }
    template = template_env.get_template("templetpage")
    with open(os.path.join(basepath, "page.py"), 'w', encoding='utf-8') as f:
        f.write(template.render(templateVars))


if __name__ == "__main__":
    a = parseyaml()
    print(a)
    # print(a.items())
    b = get_page_list(a)
    # print(b.items())
    print(b)
    create_pages_py(b)