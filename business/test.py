import yaml
with open('D:/test_case/dfappiumtest/data/data_element/fundaccountlogin.yml', 'r') as f:  # 打开文件
    data = yaml.load(f)
    print(data)