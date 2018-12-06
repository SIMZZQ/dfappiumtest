# coding:utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from PIL import Image
import os,time,random,datetime,pytesseract

class publicmethods:
    def __init__(self,driver):
        self.driver = driver
    # 判断定位类型选择定位方法
    def findelement(self,type,contents,num=None):
        if type == 'id':
            return self.driver.find_element_by_id(contents)
        elif type == 'ids':
            return self.driver.find_elements_by_id(contents)[num]
        elif type == 'xpath':
            return self.driver.find_element_by_xpath(contents)
        elif type == 'xpaths':
            return self.driver.find_elements_by_xpath(contents)[num]
        elif type == 'text':
            return self.driver.find_element_by_android_uiautomator(contents)
        elif type == 'texts':
            return self.driver.find_elements_by_android_uiautomator(contents)[num]
        elif type == 'class':
            return self.driver.find_element_by_class_name(contents)
        elif type == 'classes':
            return self.driver.find_elements_by_class_name(contents)[num]
        else:
            print('无此定位方法')
    #根据像素点击页面
    def tapPage(self,x,y):
        self.driver.tap([(x,y)])

    def quit(self):
        self.driver.quit()

    #获取当前页名称
    def currentPage(self):
        return self.driver.current_activity

    # 等待指定页面出现后进行操作
    def waitActivity(self,active,seconds):
        self.driver.wait_activity(active,seconds)

    # 模拟返回
    def backKey(self):
        self.driver.back()

    # 截图
    def getScreenShot(self,module,staus):
        # nowtime = int(time.time())
        nowtime = time.strftime("%Y-%m-%d_%H-%M-%S")
        nowdate = datetime.datetime.now().strftime('%Y-%m-%d')
        try:
            os.makedirs('D:/test_case/myyamltest/dfappiumtest/screenpicture/%s/%s/%s' % (module, staus, nowdate)) # 创建保存当天图片目录
        except:
            pass
        filename = 'D:/test_case/myyamltest/dfappiumtest/screenpicture/%s/%s/%s/%s.png' %(module,staus,nowdate,nowtime)
        # print('D:/test_case/mytest/screenpicture/%s/%s' %(module,staus))
        print(filename)
        return self.driver.get_screenshot_as_file(filename)

    # 显示等待
    def wait(self,type,waittime,address):
        if type == 'xpath':
            return WebDriverWait(self.driver,waittime,2).until(expected_conditions.presence_of_element_located((By.XPATH,address)))
        elif type == 'id':
            return WebDriverWait(self.driver,waittime,2).until(expected_conditions.presence_of_element_located((By.ID,address)))
        elif type == 'class':
            return WebDriverWait(self.driver, waittime, 2).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, address)))
        else:
            print('无此等待方法')

    # 隐式等待
    def hideWait(self,t):
        return self.driver.implicitly_wait(t)

    # 生成随机11位以1开头的数字（测试手机号）
    def creatPhone(self):
        suffix = random.randint(999999999, 10000000000)  # 生成后10位随机数
        return '1{}'.format(suffix)  # 拼接手机号

    # 生成随机6位验证码
    def creatCode(self):
        code = random.randint(99999, 1000000)  # 生成6位随机数
        return code

    # 页面上下滑动
    def swipeUpDown(self,xRate,ystartRate,yendRate):
        x = self.driver.get_window_size()['width'] # 获取屏幕宽度
        y = self.driver.get_window_size()['height'] # 获取屏幕高度
        x1 = int(x*xRate) # x坐标
        y1 = int(y*ystartRate) #y起始坐标
        y2 = int(y*yendRate) #y终点坐标
        self.driver.swipe(x1,y1,x1,y2)
    # 解绑资金账号滑动
    def swipeLeftRight(self,loc,size,x1rate,x2rate):
        x1 = int(loc['x']+size['width']/10*x1rate)
        x2 = int(loc['x']+size['width']/10*x2rate)
        y1 = int(loc['y']+size['height']/2)
        self.driver.swipe(x1,y1,x2,y1,200)

    # 九宫格控件定位
    # loc为九宫格左上角起始坐标，s为九宫格的宽和高
    def jiu(self,loc,s):
        gongge = {}
        # press与move_to里都有三个参数，第一个默认为None,故返回参数中默认第一个参数为None
        gongge[1] = (None,loc['x']+s['width']/6,loc['y']+s['height']/6)
        gongge[2] = (None,loc['x']+s['width']/6*3,loc['y']+s['height']/6)
        gongge[3] = (None,loc['x']+s['width']/6*5,loc['y']+s['height']/6)
        gongge[4] = (None,loc['x']+s['width']/6,loc['y']+s['height']/6*3)
        gongge[5] = (None,loc['x']+s['width']/6*3,loc['y']+s['height']/6*3)
        gongge[6] = (None,loc['x']+s['width']/6*5,loc['y']+s['height']/6*3)
        gongge[7] = (None,loc['x']+s['width']/6,loc['y']+s['height']/6*5)
        gongge[8] = (None,loc['x']+s['width']/6*3,loc['y']+s['height']/6*5)
        gongge[9] = (None,loc['x']+s['width']/6*5,loc['y']+s['height']/6*5)
        return gongge

    # 九宫格偏移量
    def pianyi(self,a,b,gongge):
        g1 = gongge[a]
        g2 = gongge[b]
        r = (None,g2[1]-g1[1],g2[2]-g1[2])
        return r

    # H5页面自定义软键盘控件定位
    def H5keyboard(self,x,y):
        numbutton = {}
        numbutton[1] = [x/6,y/384*255+y/384*129/8]
        numbutton[2] = [x/6*3,y/384*255+y/384*129/8]
        numbutton[3] = [x/6*5,y/384*255+y/384*129/8]
        numbutton[4] = [x/6,y/384*255+y/384*129/8*3]
        numbutton[5] = [x/6*3,y/384*255+y/384*129/8*3]
        numbutton[6] = [x/6*5,y/384*255+y/384*129/8*3]
        numbutton[7] = [x/6,y/384*255+y/384*129/8*5]
        numbutton[8] = [x/6*3,y/384*255+y/384*129/8*5]
        numbutton[9] = [x/6*5,y/384*255+y/384*129/8*5]
        numbutton[0] = [x/6*3,y/384*255+y/384*129/8*7]
        return numbutton

    # 验证码识别
    def identifyCode(self,beginpoint,codesize,threshold):
        # 获取验证码框起始与终点坐标
        startx = beginpoint['x']
        starty = beginpoint['y']
        endx = beginpoint['x'] + codesize['width']
        endy = beginpoint['y'] + codesize['height']
        # 设置需截取的验证码框范围
        box = [startx, starty, endx, endy]
        cp = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'codepic'))
        # 创建保存验证码相关截图文件夹
        try:
            os.makedirs(cp)
        except:
            pass
        # 保存登录页面截图
        self.driver.get_screenshot_as_file(cp + '/login.png')
        # 打开资金账号登录页面截图
        loginim = Image.open(cp + '/login.png')
        # 截取验证码框
        codeim = loginim.crop(box)
        # 保存验证码截图
        codeim.save(cp + '/code.png')
        codeim = Image.open(cp + '/code.png')
        # 将截取的验证码图片以L模式灰化
        gyimage = codeim.convert('L')
        # 给定一个阈(yu)值,小于该值给定灰度0(白色)，否则给定灰度1(黑色)，非黑即白
        # 灰度范围为0-255。0%的灰度RGB数值是255,255,255；1%灰度的RGB数值是253,253,253；
        table = []
        for i in range(256):
            # 0-222元素都为0，223-255为1
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        erzhiimage = gyimage.point(table, '1')
        erzhiimage.save(cp + '/code.png')
        # 获取验证码图片宽高
        imagesize = erzhiimage.size
        imagew = imagesize[0]
        imageh = imagesize[1]
        # 从图片左上角（1，1）开始，由左至右，由上至下遍历每一个像素点
        for x in range(1, imagew):
            for y in range(1, imageh):
                # xx.getpixel((x,y))获取目标像素点颜色。
                # xx.putpixel((x,y),255)更改像素点颜色，255代表颜色。
                if x <= 2 or x >= (imagew - 5):
                    erzhiimage.putpixel((x, y), 255)  # x=1，2，大于等于宽-5的列设置白色
                elif y <= 2 or y >= (imageh - 5):
                    erzhiimage.putpixel((x, y), 255)  # y=1,2,大于等于高-5的行设置白色
                elif erzhiimage.getpixel((x, y)) == 0:
                    # 以目标像素点为起始点，获取下方4个点的颜色
                    # 0为黑色，1为白色
                    down_color = erzhiimage.getpixel((x, y + 1))
                    down2_color = erzhiimage.getpixel((x, y + 2))
                    down3_color = erzhiimage.getpixel((x, y + 3))
                    down4_color = erzhiimage.getpixel((x, y + 4))
                    if down_color == 1:
                        erzhiimage.putpixel((x, y), 255)
                    elif down2_color == 1:
                        erzhiimage.putpixel((x, y), 255)
                    elif down3_color == 1:
                        erzhiimage.putpixel((x, y), 255)
                    elif down4_color == 1:
                        erzhiimage.putpixel((x, y), 255)
                    else:
                        pass
                else:
                    pass
        erzhiimage.save(cp + '/code.png')
        # 识别异常校正
        rep = {'O': '0',
               'I': '1',
               'L': '1',
               'Z': '2',
               'S': '8',
               'Q': '0',
               '}': '7',
               '*': '',
               'E': '6',
               ']': '0',
               '`': '',
               'B': '8',
               '\\': '',
               ' ': '',
               '\'': ''
               }
        result = pytesseract.image_to_string(erzhiimage,lang='eng')
        # 去除前后空格
        result.strip()
        # 如识别出字母，转变大写
        result.upper()
        # 识别内容中如出现校正库中字符，进行替换
        for r in rep:
            result = result.replace(r, rep[r])
        return result
