import sqlite3
import json
import requests
from pathlib import Path
from appdirs import *

from utils.aesUtil import dectry
from utils.contains import key as key1, provinces


from .dbLites.comLite import local_db

def dele():
        """删除数据"""
        Conn = sqlite3.connect(local_db())
        try:
                with Conn:
                        Conn.execute('delete from districts where adcode != "100000"')
                        print('数据删除成功')
        except Exception as e:
                print("districts删除失败")
                dro_tb()
                conn()
        finally:
                pass

def dro_tb():
        """删除表"""
        """注意这个需要先创建成功后，才能执行"""
        Conn = sqlite3.connect(local_db())
        Cur = Conn.cursor()
        try:
                Cur.execute('drop table districts')
                Conn.commit()
                print('删除表成功')
        except Exception as e:
                pass
        finally:
                Cur.close()
                Conn.close()


def conn():
        """创建数据库库"""
        
        Conn=sqlite3.connect(local_db()) # 连接数据库
        try:
                Conn.execute("""
                        CREATE TABLE `districts` (
                          `districtId` INTEGER PRIMARY KEY AUTOINCREMENT,
                          `districtPid` INTEGER DEFAULT NULL,
                          `name` varchar(200) DEFAULT NULL,
                          `citycode` varchar(200) DEFAULT NULL,
                          `adcode` varchar(200) DEFAULT NULL,
                          `lng` float(13,10) DEFAULT NULL,
                          `lat` float(13,10) DEFAULT NULL,
                          `level` varchar(200) DEFAULT NULL,
                          `createTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                          `updateTime` timestamp NULL DEFAULT NULL
                        )  
                """)
                print("districts表创建成功")
                insert_sql((0, '中华人民共和国', '100000', '116.3683244', '39.915085', 'country'))
        except Exception as e:
                print("districts表已经被创建")
                dele()
        finally:
                Conn.close()

def insert_sql(*args):
        """添加数据"""
        Conn = sqlite3.connect(local_db())
        try:
                with Conn:
                        Conn.execute("""INSERT INTO `districts` ( `districtpid`,`name`, `adcode`, `lng`, `lat`, 
                        `level`) VALUES (?,?,?,?,?,?)""", *args) # 插入数据，使用了占位符？
        except sqlite3.IntegrityError:
                print("districts表已经被创建")
        finally:
                pass

def insert_city_sql(*args):
        """添加数据"""
        Conn = sqlite3.connect(local_db())
        try:
                with Conn:
                        Conn.execute("""INSERT INTO `districts` (`districtpid`,`name`, `citycode`,`adcode`, `lng`, 
                        `lat`, `level`) VALUES (?, ?, ?, ?, ?, ?, ?)""", *args)
        except sqlite3.IntegrityError:
                print("districts表已经被创建")
        finally:
                pass

def executemany_sql(data_list):
        # example:
        # sql = 'insert into filelist (pkgKey, dirname, filenames, filetypes) values (?, ?, ?, ?);'
        # data_list = [(1, '/etc/sysconfig', 'openshift_option', 'f'), (1, '/usr/share/doc', 'adb-utils-1.6', 'd')]
        """添加数据"""
        Conn = sqlite3.connect(local_db())
        try:
                with Conn:
                        sql = """INSERT INTO `districts` (`districtpid`,`name`, `citycode`,`adcode`, `lng`, 
                                `lat`, `level`) VALUES (?, ?, ?, ?, ?, ?, ?)"""
                        Conn.executemany(sql, data_list)
                        Conn.commit()
        except Exception as e:
                print("executemany failed")

def select_districtId_sql(adcode):
        """添加数据"""
        Conn = sqlite3.connect(local_db())
        cur = Conn.cursor()
        row = []
        try:
                sql = 'select districtId from districts where adcode = {}'.format(adcode)
                cur.execute(sql)
                row = cur.fetchone()
        except sqlite3.IntegrityError:
                print("districts表已经被创建")
        finally:
                cur.close()
                Conn.close()
                return row

def select_districtId_Rand_sql():
    """添加数据"""
    Conn = sqlite3.connect('nba.db')
    cur = Conn.cursor()
    row = []
    try:
        sql = 'SELECT adcode FROM districts ORDER BY RANDOM() LIMIT 1'
        cur.execute(sql)
        row = cur.fetchone()
    except sqlite3.IntegrityError:
        print("districts表数据查询失败")
    finally:
        cur.close()
        Conn.close()
        return row[0]

def select_province_sql():
        """添加数据"""
        Conn = sqlite3.connect(local_db())
        cur = Conn.cursor()
        row = []
        try:
                sql = """select * from districts where level = 'province'"""
                cur.execute(sql)
                row = cur.fetchall()
        except sqlite3.IntegrityError:
                print("districts表province查询失败...")
        finally:
                cur.close()
                Conn.close()
                return row

def select_city_sql(districtPid):
        """添加数据"""
        Conn = sqlite3.connect(local_db())
        cur = Conn.cursor()
        row = []
        try:
                sql = """select * from districts where level = 'city' and districtPid = {}""".format(districtPid)
                cur.execute(sql)
                row = cur.fetchall()
        except sqlite3.IntegrityError:
                print("districts表city查询失败...")
        finally:
                cur.close()
                Conn.close()
                return row

def select_district_sql(districtPid):
        """添加数据"""
        Conn = sqlite3.connect(local_db())
        cur = Conn.cursor()
        row = []
        try:
                sql = """select * from districts where level in ('district')  and districtPid = {}""".format(districtPid)
                cur.execute(sql)
                row = cur.fetchall()
        except sqlite3.IntegrityError:
                print("districts表district查询失败...")
        finally:
                cur.close()
                Conn.close()
                return row

def select_street_sql(districtPid):
        """添加数据"""
        Conn = sqlite3.connect(local_db())
        cur = Conn.cursor()
        row = []
        try:
                sql = """select * from districts where level = 'street' and districtPid = {}""".format(districtPid)
                cur.execute(sql)
                row = cur.fetchall()
        except sqlite3.IntegrityError:
                print("districts表district查询失败...")
        finally:
                cur.close()
                Conn.close()
                return row

def get(log_label):
        key = dectry(key1)

        header = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36'
        }

        for i in provinces:
                code_url = 'https://restapi.amap.com/v3/config/district?key={}&keywords={}&subdistrict=3'.format(key, i)
                res = requests.get(code_url, headers=header)
                log_label.config(text=code_url)
                log_label.config(text=res.text)
                if json.loads(res.text)['status'] == "0":
                        log_label.config(text=json.loads(res.text)["info"])
                        return
                data = json.loads(res.text)
                province = data['districts']
                province_adcode = province[0]['adcode']
                pname = province[0]['name']
                print(pname)
                center = province[0]['center']
                pcitycode = province[0]['citycode']
                level = province[0]['level']
                lng = province[0]['center'].split(',')[0]
                lat = province[0]['center'].split(',')[1]
                city_list = province[0]['districts']
                insert_sql((1, pname, province_adcode, lng, lat, level))

                districtpid = select_districtId_sql(province_adcode)[0]
                log_label.config(text=city_list)
                for city in city_list:
                        citycode = city['citycode']
                        city_adcode = city['adcode']
                        name = city['name']
                        level = city['level']
                        lng = city['center'].split(',')[0]
                        lat = city['center'].split(',')[1]
                        district_list = city['districts']
                        log_label.config(text=(name, citycode, city_adcode, lng, lat, level))
                        insert_city_sql((districtpid, name, citycode, city_adcode, lng, lat, level))
                        citypid = select_districtId_sql(city_adcode)[0]
                        print(city['name'], city_adcode,'-----', citypid,'-----', districtpid,'-----', province_adcode)
                        for district in district_list:
                                citycode = district['citycode'] if district['citycode'] else ""
                                district_adcode = district['adcode']
                                name = district['name']
                                level = district['level']
                                lng = district['center'].split(',')[0]
                                lat = district['center'].split(',')[1]
                                street_list = district['districts']
                                log_label.config(text=(name, citycode, district_adcode, lng, lat, level))
                                insert_city_sql((citypid, name, citycode, district_adcode, lng, lat, level))
                                district_districtpid = select_districtId_sql(district_adcode)[0]
                                streets = []
                                for street in street_list:
                                        streetcitycode = street['citycode'] if district['citycode'] else ""
                                        adcode = street['adcode']
                                        name = street['name']
                                        level = street['level']
                                        lng = street['center'].split(',')[0]
                                        lat = street['center'].split(',')[1]
                                        streets.append((district_districtpid, name, streetcitycode, adcode, lng, lat, level))
                                        log_label.config(text=(name, streetcitycode, adcode, lng, lat, level))
                                executemany_sql(streets)
