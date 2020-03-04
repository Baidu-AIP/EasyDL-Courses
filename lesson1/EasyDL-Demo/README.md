## 简介

EasyDL 云端API调用demo。该demo适用于检测模型和分割模型的调用。


**安装Python依赖库：**

Python依赖库在[requirements.txt](./requirements.txt)中给出，可通过如下命令安装：

```
pip install -r requirements.txt
```
如果遇到 **No module named 'Cython'**的错误, 请先执行```pip install cython```，或者直接运行```install_requirement.sh```

## 使用教程
1、登陆EasyDL官网训练模型；
2、发布模型并获取API地址；
3、参照API文档申请token；
4、将获取的API地址和access_token参数填入demo相应位置；
5、运行demo。
