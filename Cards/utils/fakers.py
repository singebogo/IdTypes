from faker import Faker

locals = {"ar_EG": "Arabic(Egypt)",
          "ar_PS": "Arabic(Palestine)",
          "ar_SA": "Arabic(Saudi Arabia)",
          "bg_BG": "Bulgarian",
          "bs_BA": "Bosnian",
          "cs_CZ": "Czech",
          "de_DE": "German",
          "dk_DK": "Danish",
          "el_GR": "Greek",
          "en_AU": "English(Australia)",
          "en_CA": "English(Canada)",
          "en_GB": "English(Great Britain)",
          "en_NZ": "English(NeW Zealand)",
          "en_US": "English(United States)",
          "es_ES": "Spanish(Spain)",
          "es_MX": "Spanish(Mexico)",
          "et_EE": "Estonian",
          "fa_IR": "Persian(Iran)",
          "fi_FI": "Finnish",
          "fr_FR": "French",
          "hi_IN": "Hindi",
          "hr_HR": "Croatian",
          "hu_HU": "Hungarian",
          "hy_AM": "Armenian",
          "it_IT": "Italian",
          "ja_JP": "Japanese",
          "ka_GE": "Georgian(Georgia)",
          "ko_KR": "Korean",
          "lt_LT": "Lithuanian",
          "lv_LV": "Latvian",
          "ne_NP": "Nepali",
          "nl_NL": "Dutch(Netherlands)",
          "no_NO": "Norwegian",
          "pl_PL": "Polish",
          "pt_BR": "Portuguese(Brazil)",
          "pt_PT": "Portuguese(Portugal)",
          "ro_RO": "Romanian",
          "ru_RU": "Russian",
          "sl_SI": "Slovene",
          "sv_SE": "Swedish",
          "tr_TR": "Turkish",
          "uk_UA": "Ukrainian",
          "zh_CN": "Chinese(China Mainland)",
          "zh_TW": "Chinese(China Taiwan)"}

fake = Faker('zh_CN')
# 生成虚拟电子邮件

# 地址相关字段
print(fake.address())  # 地址
print(fake.building_number())  # 楼名
print(fake.city())  # 完整城市名
print(fake.city_name())  # 城市名字(不带市县)
print(fake.city_suffix())  # 城市后缀名
print(fake.country())  # 国家名称
print(fake.country_code(representation="alpha-2"))  # 国家编号
print(fake.district())  # 地区
print(fake.postcode())  # 邮编
print(fake.province())  # 省
print(fake.street_address())  # 街道地址
print(fake.street_name())  # 街道名称
print(fake.street_suffix())  # 街道后缀名
# 时间相关
print(fake.am_pm())  # AM或PM
print(fake.century())  # 世纪
print(fake.date(pattern="%Y-%m-%d", end_datetime=None))  # 日期字符串(可设置格式和最大日期)
print(fake.date_between(start_date="-30y", end_date="today"))  # 日期(可设置限定范围)
print(fake.date_between_dates(date_start=None, date_end=None))  # 同上
print(fake.date_object(end_datetime=None))  # 日期(可设置最大日期)
print(fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115))  # 出生日期
print(fake.date_this_century(before_today=True, after_today=False))  # 本世纪日期
print(fake.date_this_decade(before_today=True, after_today=False))  # 本年代中的日期
print(fake.date_this_month(before_today=True, after_today=False))  # 本月中的日期
print(fake.date_this_year(before_today=True, after_today=False))  # 本年中的日期
print(fake.date_time(tzinfo=None, end_datetime=None))  # 日期和时间
print(fake.date_time_ad(tzinfo=None, end_datetime=None, start_datetime=None))  # 日期和时间(从001年1月1日到现在)
print(fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None))  # 日期时间(可设置限定范围)
print(fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None))  # 同上
print(fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None))  # 本世纪中的日期和时间
print(fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None))  # 本年代中的日期和时间
print(fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None))  # 本月中的日期和时间
print(fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None))  # 本年中的日期和时间
print(fake.day_of_month())  # 几号
print(fake.day_of_week())  # 星期几
print(fake.future_date(end_date="+30d", tzinfo=None))  # 未来日期
print(fake.future_datetime(end_date="+30d", tzinfo=None))  # 未来日期和时间
print(fake.iso8601(tzinfo=None, end_datetime=None))  # iso8601格式日期和时间
print(fake.month())  # 第几月
print(fake.month_name())  # 月份名称
print(fake.past_date(start_date="-30d", tzinfo=None))  # 过去日期
print(fake.past_datetime(start_date="-30d", tzinfo=None))  # 过去日期和时间
print(fake.time(pattern="%H:%M:%S", end_datetime=None))  # 时间(可设置格式和最大日期时间)
print(fake.time_delta(end_datetime=None))  # 时间间隔
print(fake.time_object(end_datetime=None))  # 时间(可设置最大日期时间)
print(fake.timezone())  # 时区
print(fake.unix_time(end_datetime=None, start_datetime=None))  # UNIX时间戳
print(fake.year())  # 某年
# 文件相关
print(fake.file_extension(category=None))  # 文件扩展名
print(fake.file_name(category=None, extension=None))  # 文件名
print(fake.file_path(depth=1, category=None, extension=None))  # 文件路径
print(fake.mime_type(category=None))  # MIME类型
print(fake.unix_device(prefix=None))  # UNIX设备
print(fake.unix_partition(prefix=None))  # UNIX分区
# 坐标相关
print(fake.coordinate(center=None, radius=0.001))  # 坐标
print(fake.latitude())  # 纬度
print(fake.latlng())  # 经纬度
print(fake.local_latlng(country_code="US", coords_only=False))  # 返回某个国家某地的经纬度
print(fake.location_on_land(coords_only=False))  # 返回地球上某个位置的经纬度
print(fake.longitude())  # 经度

# 网络相关
print(fake.ascii_company_email())  # 企业邮箱(ascii编码)
print(fake.ascii_email())  # 企业邮箱+免费邮箱(ascii编码)
print(fake.ascii_free_email())  # 免费邮箱(ascii编码)
print(fake.ascii_safe_email())  # 安全邮箱(ascii编码)
print(fake.company_email())  # 企业邮箱
print(fake.domain_name(levels=1))  # 域名
print(fake.domain_word())  # 二级域名
print(fake.email())  # 企业邮箱+免费邮箱
print(fake.free_email())  # 免费邮箱
print(fake.free_email_domain())  # 免费邮箱域名
print(fake.hostname())  # 主机名
print(fake.image_url(width=None, height=None))  # 图片URL
print(fake.ipv4(network=False, address_class=None, private=None))  # ipv4
print(fake.ipv4_network_class())  # ipv4网络等级
print(fake.ipv4_private(network=False, address_class=None))  # 私有ipv4
print(fake.ipv4_public(network=False, address_class=None))  # 公共ipv4
print(fake.ipv6(network=False))  # ipv6
print(fake.mac_address())  # MAC地址
print(fake.safe_email())  # 安全邮箱
print(fake.slug())  # URL中的slug
print(fake.tld())  # 顶级域名
print(fake.uri())  # URI
print(fake.uri_extension())  # URI扩展
print(fake.uri_page())  # URI页
print(fake.uri_path(deep=None))  # URI路径
print(fake.url(schemes=None))  # URL
print(fake.user_name())  # 用户名

# 人物相关
print(fake.first_name())  # 名字
print(fake.first_name_female())  # 名字(女)
print(fake.first_name_male())  # 名字(男)
print(fake.first_romanized_name())  # 名字(罗马文)
print(fake.last_name())  # 姓
print(fake.last_name_female())  # 姓(女)
print(fake.last_name_male())  # 姓(男)
print(fake.last_romanized_name())  # 姓(罗马文)
print(fake.name())  # 姓名
print(fake.name_female())  # 姓名(女)
print(fake.name_male())  # 姓名(男)
print(fake.prefix())  # 称谓
print(fake.prefix_female())  # 称谓(女)
print(fake.prefix_male())  # 称谓(男)
print(fake.romanized_name())  # 称谓(罗马文)
print(fake.suffix())  # 姓名后缀(中文不适用)
print(fake.suffix_female())  # 姓名男后缀(中文不适用)
print(fake.suffix_male())  # 姓名女后缀(中文不适用)

# 电话相关
print(fake.msisdn())  # 完整手机号码(加了国家和国内区号)
print(fake.phone_number())  # 手机号
print(fake.phonenumber_prefix())  # 区号
print(fake.ssn(min_age=18, max_age=90))  # 身份证
print(fake.job())

# 公司相关
print(fake.bs())  # 商业用词
print(fake.catch_phrase())  # 妙句(口号)
print(fake.company())  # 公司名称
print(fake.company_prefix())  # 公司名称前缀
print(fake.company_suffix())  # 公司名称后缀

# 文本相关
print(fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None))  # 单个段落
print(fake.paragraphs(nb=3, ext_word_list=None))  # 多个段落
print(fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))  # 单个句子
print(fake.sentences(nb=3, ext_word_list=None))  # 多个句子
print(fake.text(max_nb_chars=200, ext_word_list=None))  # 单个文本
print(fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None))  # 多个文本
print(fake.word(ext_word_list=None))  # 单个词语
print(fake.words(nb=3, ext_word_list=None, unique=False))  # 多个词语
