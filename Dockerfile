# 基于的基础镜像

FROM python:3.7.0

# 维护者信息

MAINTAINER y_wang shengguanglong01@sina.com

# 代码添加到code文件夹

ADD ./ /

# 设置code文件夹是工作目录

WORKDIR /

# 安装支持

RUN pip install -r requirements.txt

CMD ["python3", "/manage.py","runserver","0.0.0.0:12345"]

