# -*- coding: utf_8 -*-
# @Create   : 2021/7/15 10:06
# @Author   : yh
# @Remark   : 日志配置
import datetime
import logging
import os
from logging.handlers import RotatingFileHandler


def setup_log():
    """配置日志"""

    # 设置日志的记录等级
    logging.basicConfig(level=logging.INFO)  # 调试等级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    log_path = os.path.join(__file__.split('webexpress')[0], 'middle', 'Pymod', datetime.date.today().strftime('%Y%m%d') + '.log')
    file_log_handler = RotatingFileHandler(log_path, maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(pathname)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
