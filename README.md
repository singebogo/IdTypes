# IdTypes
    自动生成各种证件类型包含（身份证 护照  军人证 台胞证  港澳通行证，统一社会信用代码，组织机构代码，纳税人识别号，工商注册号，税务登记号等）

## 项目目录


    │  Cards.json
    │  Cards.py  # 主程序
    │  nba.db   # sqllite数据库
    │
    ├─assers
    │      证件.png
    │
    ├─gui  界面逻辑处理
    │  │  __init__.py
    │  │
    │  ├─controlFrame
    │  │  │  controlFrame.py
    │  │  │  __init__.py
    │  │
    │  ├─converterFrame  
    │  │  │  commonFrame.py
    │  │  │  groupConverterFrame.py
    │  │  │  IDConverterFrame.py
    │  │  │  OtherConverterFrame.py
    │  │  │  personConverterFrame.py
    │  │  │  settingConverterFrame.py
    │  │  │  __init__.py
    │  │  │
    │
    ├─output
    │      Cards.exe
    │
    └─utils    # 规则工具包
        │  aesUtil.py
        │  Calendar.py
        │  contains.py
        │  frameTypes.py
        │  IDCards.py
        │  iIndustrial.py
        │  nba.db
        │  organization.py
        │  other.py
        │  region.py
        │  socialCreditCode.py
        │  taxpayerIdentificationNumber.py
        │  taxRegistration.py
        │  temperatureConverter.py
        │  __init__.py
        │
        ├─threading
        │  │  stopped_able_threading.py
        │  │  __init__.py

## 运行
    python Cards.py
                

## 可执行程序
    IdTypes\Cards\output\Cards.exe

## 打包
### 打包程序
    auto-py-to-exe  导入文件Cards.json


## 效果图
### 个人
	身份证 护照  军人证 台胞证  港澳通行证
	![个人](https://img2024.cnblogs.com/blog/2007173/202403/2007173-20240313175534870-1373482197.png)
	
### 团体
	统一社会信用代码，组织机构代码，纳税人识别号，工商注册号，税务登记号
       ![团体](https://img2024.cnblogs.com/blog/2007173/202403/2007173-20240313175704510-591203619.png)
	
