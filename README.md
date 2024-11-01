# IdTypes
## 主要功能
    1、自动生成各种证件类型包含（身份证 护照  军人证 台胞证  港澳通行证，统一社会信用代码，组织机构代码，纳税人识别号，工商注册号，税务登记号等）
	2、电话号码可生成移动电话号码和固定电话号码
	3、银行账户号码模拟生成
	3、设置
		可用功能：界面置顶功能

## 项目目录

	│  Cards.json
    │  Cards.py
    │  nba.db
    │  __init__.py
    │
    ├─assers
    │      证件.png
    │
    ├─gui
    │  │  __init__.py
    │  │
    │  ├─controlFrame
    │  │      controlFrame.py
    │  │      customNotebook.py
    │  │      phone_controlFrame.py
    │  │      __init__.py
    │  │
    │  └─converterFrame
    │          banksConverterFrame.py
    │          commonFrame.py
    │          fixedLineTelephoneConverterFrame.py
    │          groupConverterFrame.py
    │          IDConverterFrame.py
    │          OtherConverterFrame.py
    │          personConverterFrame.py
    │          phoneConverterFrame.py
    │          settingConverterFrame.py
    │          __init__.py
    │
    ├─output
    │      Cards.exe
    │
    └─utils
        │  aesUtil.py
        │  areaCode.py
        │  banks.py
        │  Calendar.py
        │  contains.py
        │  fakers.py
        │  frameTypes.py
        │  IDCards.py
        │  iIndustrial.py
        │  organization.py
        │  other.py
        │  phones.py
        │  socialCreditCode.py
        │  taxpayerIdentificationNumber.py
        │  taxRegistration.py
        │  temperatureConverter.py
        │  __init__.py
        │
        ├─dbLites
        │      bnkLite.py
        │      comLite.py
        │      region.py
        │      __init__.py
        │
        └─threading
                stopped_able_threading.py
                __init__.py

## 运行
    python Cards.py
                
## 数据库替换

    “因获取地区代码需计流量，付费行为，故停止服务，可以使用替换数据库目录”
    操作步骤：
	    1、界面切换notbook: 【设置】
	    2、点击【替换数据库】，打开系统目录界面
	    3、将Cards\nba.db文件复制到步骤2中打开的目录中
	    4、重启软件

## 可执行程序
    IdTypes\Cards\output\Cards.exe

## 打包
### 打包程序
    auto-py-to-exe  导入文件Cards.json


## 数据来源和整理
     [BankLists](https://github.com/singebogo/BankLists)
          内容有：
              1、json和excel数据： banks1.json 、banks.json、银行卡bin.xls
              2、本软件的数据库数据sql： cards.sql、districts.sql


## 效果图
### 证件
#### 个人
	身份证 护照  军人证 台胞证  港澳通行证
	
![个人](https://img2024.cnblogs.com/blog/2007173/202403/2007173-20240313175534870-1373482197.png)
	
#### 团体
	统一社会信用代码，组织机构代码，纳税人识别号，工商注册号，税务登记号
	
![团体](https://img2024.cnblogs.com/blog/2007173/202403/2007173-20240313175704510-591203619.png)

### 电话
### 电话号码
![电话号码](https://github.com/singebogo/IdTypes/blob/master/vx_images/%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81.bmp)

### 固定电话
![固定电话](https://github.com/singebogo/IdTypes/blob/master/vx_images/%E5%9B%BA%E5%AE%9A%E7%94%B5%E8%AF%9D.bmp)	

### 设置
![设置](https://github.com/singebogo/IdTypes/blob/master/vx_images/%E8%AE%BE%E7%BD%AE.bmp)

### 银行账号
![银行账号](https://github.com/singebogo/IdTypes/blob/master/vx_images/%E9%93%B6%E8%A1%8C%E5%8D%A1%E8%B4%A6%E5%8F%B7.bmp)

![银行卡归属地查询结果](https://github.com/singebogo/IdTypes/blob/master/vx_images/%E9%93%B6%E8%A1%8C%E5%8D%A1%E5%BD%92%E5%B1%9E%E5%9C%B0%E6%9F%A5%E8%AF%A2%E7%BB%93%E6%9E%9C.bmp)


# 免责说明

    本软件仅为技术交流，使用本软件任何违反法律行为与作者无关！
    This software is for technical communication only, and any violation of the law by using this software has nothing to do with the author！