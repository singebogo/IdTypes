import sqlite3
import ijson
import requests
from pathlib import Path
from appdirs import *

from utils.dbLites.comLite import local_db, local_banks


def conn():
    """创建数据库库"""

    Conn = sqlite3.connect(local_db())  # 连接数据库
    try:
        Conn.execute("""
                    CREATE TABLE `banks` (
                      `city_id` varchar(100) DEFAULT NULL,
                      `city` varchar(100) DEFAULT NULL,
                      `province_id` INTEGER DEFAULT NULL,
                      `province` varchar(100) DEFAULT NULL,
                      `bank_id` varchar(100) DEFAULT NULL,
                      `bank_name` varchar(100) DEFAULT NULL,
                      `sub_branch_id` varchar(100) DEFAULT NULL,
                      `sub_branch_name` varchar(200) DEFAULT NULL,
                      `createTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                      `updateTime` timestamp NULL DEFAULT NULL
                    )  
            """)
        print("banks表创建成功")
        Conn.execute("""
            CREATE TABLE `cards`(
                `issuing_bank_code` varchar(100) DEFAULT NULL,
                `issuing_bank` varchar(100) DEFAULT NULL,
                `card_name` varchar(100) DEFAULT NULL,
                `len` varchar(100) DEFAULT NULL,
                `BIN` varchar(100) DEFAULT NULL,
                `BIN_len` varchar(100) DEFAULT NULL,
                `card_type` varchar(100) DEFAULT NULL,
                `range_of_application` varchar(100) DEFAULT NULL,
                `createTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                `updateTime` timestamp NULL DEFAULT NULL
            )  
            """)
        print("cards表创建成功")
    except Exception as e:
        print("banks表已经被创建")
        print("cards表已经被创建")
        dele()
    finally:
        Conn.close()


def dele():
    """删除数据"""
    Conn = sqlite3.connect(local_db())
    try:
        with Conn:
            Conn.execute('delete from banks')
            Conn.execute('delete from cards')
            print('数据删除成功')
    except Exception as e:
        print("banks删除失败")
        print("cards删除失败")
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
        Cur.execute('drop table banks')
        Cur.execute('drop table cards')
        Conn.commit()
        print('删除表成功')
    except Exception as e:
        pass
    finally:
        Cur.close()
        Conn.close()


def insert_sql(*args):
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    try:
        with Conn:
            Conn.execute("""INSERT INTO `banks` (`city_id`,`city`, `province_id`, `province`, `bank_id`, 
                    `bank_name`, 'sub_branch_id', 'sub_branch_name') VALUES (?,?,?,?,?,?,?,?)""", *args)  # 插入数据，使用了占位符？
    except sqlite3.IntegrityError:
        print("banks表已经被创建")
    finally:
        pass


def select_province_sql():
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    cur = Conn.cursor()
    row = []
    try:
        sql = """SELECT province_id, province FROM banks where province_id is not null GROUP BY province_id"""
        cur.execute(sql)
        row = cur.fetchall()
    except sqlite3.IntegrityError:
        print("banks表province查询失败...")
    finally:
        cur.close()
        Conn.close()
        return row


def select_city_sql(province_id):
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    cur = Conn.cursor()
    row = []
    try:
        sql = """SELECT city_id, city FROM banks where province_id = {} GROUP BY city_id""".format(province_id)
        cur.execute(sql)
        row = cur.fetchall()
    except sqlite3.IntegrityError:
        print("banks表city查询失败...")
    finally:
        cur.close()
        Conn.close()
        return row


def select_banks_sql(city_id):
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    cur = Conn.cursor()
    row = []
    try:
        sql = """select bank_id, bank_name from banks where city_id={} group by bank_name""".format(city_id)
        cur.execute(sql)
        row = cur.fetchall()
    except sqlite3.IntegrityError:
        print("banks表bank查询失败...")
    finally:
        cur.close()
        Conn.close()
        return row


def select_subbanks_sql(bank_id, city_id):
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    cur = Conn.cursor()
    row = []
    try:
        sql = """select sub_branch_id, sub_branch_name  from banks where bank_id={} and city_id={}""".format(bank_id,
                                                                                                             city_id)
        cur.execute(sql)
        row = cur.fetchall()
    except sqlite3.IntegrityError:
        print("banks表sub_bank查询失败...")
    finally:
        cur.close()
        Conn.close()
        return row


def select_random_bank_sql(bank_id):
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    cur = Conn.cursor()
    row = []
    try:
        sql = """select sub_branch_id from banks where bank_id ={} order by random()  LIMIT 1""".format(bank_id)
        cur.execute(sql)
        row = cur.fetchall()
    except sqlite3.IntegrityError:
        print("banks表bank随机一条数据查询失败...")
    finally:
        cur.close()
        Conn.close()
        return row


def select_random_card_sql(issuing_bank, card_type):
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    cur = Conn.cursor()
    row = []
    try:
        sql = """select issuing_bank, len, Bin, BIN_len, card_type, card_name from cards where 
        issuing_bank not in ({}) and card_type in ({}) group by issuing_bank_code order by random()  LIMIT 1""".format(
            issuing_bank, card_type)
        cur.execute(sql)
        row = cur.fetchall()
    except sqlite3.IntegrityError:
        print("cards表card随机一条数据查询失败...")
    finally:
        cur.close()
        Conn.close()
        return row


def select_all_banks_sql():
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    cur = Conn.cursor()
    row = []
    try:
        sql = """select bank_id, bank_name from banks group by bank_id"""
        cur.execute(sql)
        row = cur.fetchall()
    except sqlite3.IntegrityError:
        print("banks表bank分类查询失败...")
    finally:
        cur.close()
        Conn.close()
        return row


def select_card_type_sql():
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    cur = Conn.cursor()
    row = []
    try:
        sql = """select distinct card_type from cards"""
        cur.execute(sql)
        row = cur.fetchall()
    except sqlite3.IntegrityError:
        print("cards表card_type分类查询失败...")
    finally:
        cur.close()
        Conn.close()
        return row


def select_card_sql(bank_name):
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    cur = Conn.cursor()
    row = []
    try:
        sql = """select issuing_bank, len, Bin, BIN_len, card_type, card_name from cards where issuing_bank like '%{}%' 
         group by issuing_bank_code order by random()  LIMIT 1""".format(bank_name)
        cur.execute(sql)
        row = cur.fetchall()
    except sqlite3.IntegrityError:
        print("cards表card_info查询失败...")
    finally:
        cur.close()
        Conn.close()
        return row


def select_card_bytype_sql(bank_name, type):
    """添加数据"""
    Conn = sqlite3.connect(local_db())
    cur = Conn.cursor()
    row = []
    try:
        sql = """select issuing_bank, len, Bin, BIN_len, card_type, card_name from cards where issuing_bank like '%{}%' 
        and card_type='{}' group by issuing_bank_code order by random() LIMIT 1""".format(bank_name, type)
        cur.execute(sql)
        row = cur.fetchall()
    except sqlite3.IntegrityError:
        print("cards表card_info查询失败...")
    finally:
        cur.close()
        Conn.close()
        return row


def get(log_label):
    # 1、下载json
    # 2、解析
    file = local_banks()
    process_large_json(file, log_label)


def process_large_json(file_path, log_label):
    with open(file_path, 'r', encoding='utf-8') as f:
        objects = ijson.items(f, 'item')
        # 这个objects在这里就是相当于一个生成器，可以调用next函数取它的下一个值
        while True:
            try:
                item = objects.__next__()
                insert_sql((item['city_id'], item['city'], item['province_id'], item['province'],
                            item['bank_id'], item['bank_name'], item['sub_branch_id'], item['sub_branch_name']))
                log_label.config(text=item)
            except StopIteration as e:
                log_label.config(text="数据读取完成")
                break
