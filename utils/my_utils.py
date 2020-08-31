#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-

from PIL import Image
from PIL import ImageDraw
import os

def _highlight_element_appium_test( png_data, out_data_name):
    img = Image.open(png_data)
    draw = ImageDraw.Draw(img)
    # location = imgelement.location  # 获取元素x,y轴坐标
    # size = imgelement.size  # 获取元素的长宽
    blank_height = 150
    # rect = (0, blank_height, location.x, size.height)
    # canvas = Image.new('RGB', (10, 5), (0, 0, 255))
    # canvas.save(out_data_name, format('PNG'))

    x1, y1, x2, y2 = 195,1608,885,1666#
    draw.rectangle([x1, y1, x2, y2], outline=(255, 0, 0),width = 10) # x1,y1左上定点，x2，y2右下顶点
    img.save(out_data_name)
    print("标记高亮成功")
# _highlight_element_appium_test("jietu.png","jietu1.png")

def highlight_element_appium(imgelement, driver, original_name, target_name):
    """
    :param imgelement: 需要高亮的元素
    :param driver: webdriver对象
    :param original_name: 任意的一个图片名称
    :param target_name: 最后被高亮显示的图片名称
    :return:
    """
    # TODO：图片的路径及文件名称处理
    # original_name = "\screenpic\\"+original_name
    # target_name = "\screenpic\\" + target_name
    # 保存截图
    driver.get_screenshot_as_file(original_name)
    # 打开图片资源
    img = Image.open(original_name)
    draw = ImageDraw.Draw(img)
    location = imgelement.location  # 获取左上角起始坐标
    size = imgelement.size  # 获取元素的长宽
    # {'x': 195, 'y': 1608}
    # {'height': 58, 'width': 690}
    # # 253,2298----885,1666 -------X是横轴，Y是纵轴，起点为左上角顶点
    # x1, y1, x2, y2 = 195, 1608, 885, 1666  #
    # draw.rectangle([x1, y1, x2, y2], outline=(255, 0, 0), width=10)  # x1,y1左上定点，x2，y2右下顶点
    x1, y1 = location['x'],location['y']
    x2, y2 = location['x']+size['width'],location['y']+size['height']
    # 在空间区域画矩形
    draw.rectangle([x1, y1, x2, y2], outline=(255, 0, 0), width=10)
    # 重新保存标记高亮的图片
    img.save(target_name, format('PNG'))
    # 删除最开始保存的截图
    if os.path.exists(original_name):
        os.remove(original_name)
        print("删除未高亮截图成功"+original_name)
    else:
        print(original_name+"文件不存在")
    print("标记"+original_name+"高亮成功")



# 封装高亮显示页面元素的方法
# 使用javascript代码将传入的页面元素对象的背景颜色和边框颜色分别设置为绿色和红色
def highlight_element_selenium(driver, element):
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                          "background:green; border:2px solid red;")




