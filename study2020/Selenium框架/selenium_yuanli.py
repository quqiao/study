

"""
selenium1.0: JavaScript注入
selenium2.0: selenium1.0 + webdriver。 与浏览器通讯
WebDriver:通过原生浏览器支持或者浏览器扩展直接控制浏览器
          针对各个浏览器而开发，取代了嵌入到被测Web应用中的JavaScript
原理：1.C/S模式
     2.Client端脚本，driver启动。创建session,通过http请求向RemoteServer发送restful请求
     3.RemoteServer(browser）端通过解析client的http请求，执行相应的操作

RemoteWebDriver(类）:FireFoxDriver
                     ChromeDriver
                     InternetExplorerDriver
                     SafariDriver
                     OperaDriver

Driver常用方法（浏览器相关操作）：get, getTitle,maximize_window,minimize_window,quit,close等

基本控件的调用方法：1. 输入框input：sendkeys, clear, click
                  2. 超链接a: click, getAttribute("xxx")
                  3. 下拉菜单select: select_by_index, select_by_value, select_by_visible_text
                  4. 单选radioBox: click, isSelected
                  5. 多选框checkBox: click, isSelected
                  6. 按钮Button: click, isEnabled

获取对象属性或文本值： 1. getAttribute(attribute)
                     2. getText()

高级应用： 1.事件操作：ActionChains类,鼠标操作：1.move_to_element
                                            2.click_and_hold
                                            3.double_click
                                            4.drag_and_drop
                                            5.perform
                                            6.release
                              键盘操作：1.KeyUp
                                       2.KeyDown
                                       3.sendKeys
          2.跳转：核心方法，driver.switch_to(),1.switch_to.alert()
                                             2.switch_to.frame()
                                             3.switch_to.window()
          3.执行JS,javascriptExecutor(接口）,excuteScript,1.移除input只读属性（document.getElementById(\"text"\).readOnly=false)
                                                         2.页面下滑到底部(windows.scrollTo(0,3000))
                                                         3.显示(document.getElementById(\"img_good"\).style.display=\"block"\)
          4.Cookie类
          5.截图，TakesScreenshot(接口)
          6.页面等待：1.等待固定时长（time.sleep)
                     2.隐式等待方式（implicityWait): 设置脚本在查找元素时的最大等待时间
          7.文件上传与下载：1.上传
                          2.下载
          8.PageFactory:1.PageObject设计模式：将测试对象及单个的测试步骤封装在每个Page对象中，以page为单位进行管理
"""
