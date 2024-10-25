# IdTypes
## 主要功能
    1、自动生成各种证件类型包含（身份证 护照  军人证 台胞证  港澳通行证，统一社会信用代码，组织机构代码，纳税人识别号，工商注册号，税务登记号等）
	2、电话号码可生成移动电话号码和固定电话号码
	3、设置
		可用功能：界面置顶功能

## 项目目录
├─Cards
│  │  Cards.json
│  │  Cards.py
│  │  nba.db
│  │
│  ├─.idea
│  │  │  .gitignore
│  │  │  dataSources.local.xml
│  │  │  dataSources.xml
│  │  │  it_tools.iml
│  │  │  misc.xml
│  │  │  modules.xml
│  │  │  vcs.xml
│  │  │  workspace.xml
│  │  │
│  │  ├─dataSources
│  │  │      e7bf2e6a-e9b0-4dd8-8bfa-999168e99bac.xml
│  │  │
│  │  └─inspectionProfiles
│  │          profiles_settings.xml
│  │
│  ├─assers
│  │      证件.png
│  │
│  ├─gui
│  │  │  __init__.py
│  │  │
│  │  ├─controlFrame
│  │  │      controlFrame.py
│  │  │      customNotebook.py
│  │  │      phone_controlFrame.py
│  │  │      __init__.py
│  │  │
│  │  └─converterFrame
│  │          commonFrame.py
│  │          fixedLineTelephoneConverterFrame.py
│  │          groupConverterFrame.py
│  │          IDConverterFrame.py
│  │          OtherConverterFrame.py
│  │          personConverterFrame.py
│  │          phoneConverterFrame.py
│  │          settingConverterFrame.py
│  │          __init__.py
│  │
│  ├─output
│  │      Cards.exe
│  │
│  └─utils
│      │  aesUtil.py
│      │  areaCode.py
│      │  Calendar.py
│      │  contains.py
│      │  fakers.py
│      │  frameTypes.py
│      │  IDCards.py
│      │  iIndustrial.py
│      │  organization.py
│      │  other.py
│      │  phones.py
│      │  region.py
│      │  socialCreditCode.py
│      │  taxpayerIdentificationNumber.py
│      │  taxRegistration.py
│      │  temperatureConverter.py
│      │  __init__.py
│      │
│      ├─dbLites
│      │      comLite.py
│      │      __init__.py
│      │
│      └─threading
│              stopped_able_threading.py
│              __init__.py

## 运行
    python Cards.py
                
## 数据库替换
   “因获取地区代码需计流量，付费行为，估停止服务，可以使用替换数据库目录”
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


