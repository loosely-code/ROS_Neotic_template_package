# ROS Noetic Package Template

ROS 软件包模板

## 包名

在CMakeLists.txt 与 package.xml 中修改包名

## cpp开发

/include 文件夹中添加cpp头文件
/src 文件夹中添加cpp库文件
/bin 文件夹中添加可执行cpp程序
软件包根目录下 CMakeLists.txt 文件中配置上述库和可执行文件

## python开发

/bin 文件夹中添加可执行python程序
/src 文件夹中新建文件夹,新建 __init__.py 文件,初始化python库
软件包根目录下 setup.py 文件中添加python库
软件包根目录下 CMakeLists.txt 文件中配置python可执行文件

## 自定义msg

/msg 文件夹中自定义ros message
