import time
import unittest
from setting import *
from BeautifulReport import BeautifulReport
#discover运行的路径
discover=unittest.defaultTestLoader.discover(CASE_PATH,'test_M*.py')
time_now=time.strftime('%Y%m%d%H%M%S')
#生成报告的名字
report_name="小白接口-{}.html".format(time_now)
runner=BeautifulReport(discover)
#生成报告的地方
runner.report("小M白接口测试",report_name,REPORT_PATH)