# 1.客户端连接
# mysql -u root -p
# 2.查看数据库
# show databases;


# 字符串数据类型 varchar(长度)
# 数值类型
# 加 unsighed无符号
# tinyint -128~127 一个字节
#     int
#     float
#     double
#     decimal(总长度,小数长度)
#    char(长度) 固定长度
#    varchar(长度)。自动计算存储长度





# sql语句以;号作为结尾
# SQL分类




# DML:数据操作语言
# create table if not exists t_student(
#     id int comment '主键',
#     name varchar(20) comment '姓名',
#     age int comment '年龄',
#     gender varchar(1) comment '性别',
#     class_id int comment '班级id',
#     create_time datetime comment '创建时间',
#     update_time datetime comment '更新时间'
# );

    # desc t_student;# 查看表结构
    # show create table t_student;# 查看建表语句
    # show tables;#查看所有表

# 表修改:
#     alter table 表名 add 字段名 字段类型;
#     alter table 表名 change 字段名 新字段名 字段类型;


# 删除字段:
#     alter table 表名 drop 字段名;


# 删除表:
#     drop table 表名;
#     truncate table 表名;表中信息全部被删除,但是表结构还在

#删除数据
         #delect不能删除某个字段的值
#     delete from 表名 where 条件;
#     delete from 表名;#删表跑路


# 修改表名:
#     alter table 表名 rename to 新表名;


#
# 表里面加数据:
#     insert into 表名(字段名1,字段名2) values(值1,值2);
        #指定字段|^
        # insert into 表名 values(值1,值2);



#全部字段加数据
    # insert into 表名(字段名1,字段名2) values(值1,值2),(值1,值2),(值1,值2);
    # insert into 表名 values(值1,值2),(值1,值2),(值1,值2);


#修改字段数据
    # update 表名 set 字段名=值 where 条件;
    #update 表名 set 字段名=值;#批量改
#批量加数据|^
    # select * from 表名;#查询所有数据
#
查询:
#     select 字段名 as 新名称 from 表名;
                   (as可以去掉)
    select distinct 字段名 from 表名;#去重
#条件查询
    # select * from 表名 where 条件;
    between 小and大
      #select * from 表名 where age in(1,2,3); #满足其一就可,可用or替换

      #模糊查询
        #select * ....... like '___'#(一个_表示一位) 按占位数查找
        #select * ........ like '%x'  #%代替前面所有的,字符最后是x

    #聚合函数:纵向计算

#       select count(*) from 表名;#查询表中数据的条数 NULL不计入
      # select count(字段名) from 表名;#查询表中字段不为空的数据的条数
      # select sum(字段名) from 表名;#求和
      # select avg(字段名) from 表名;#求平均值
      # select max(字段名) from 表名;#求最大值


    #分组查询
    #执行顺序from > where >聚合函数 >having>select > order by>limit
    select 字段名,聚合函数 from 表名 表替代名group by 字段名;


    #排序 默认升序ASC
    #select * from 表名 order by 字段名 desc;#降序
    #select * from 表名 order by 字段名 asc;#升序
# select * from 表名 order by 字段名 asc,字段名 asc;


   #分页(数据库方言)
   起始位置=(当前页-1)*每页显示条数
    #select * from 表名 limit 起始位置,查询记录数;
    
#   show databases;
#  select database(); 查询当前数据库
#  create database [if is exists]   [default charset utf8mb4];
# use database;开用哪个


#用户权限语句  管理员用的多
# 查看用户
use mysql;
select user,host from user;
create user 'root'@'localhost' identified by '123456';#创建用户
create user 'root'@'%' identified by '123456';#创建用户任意主机访问
alter user 'root'@'localhost' identified with mysql_native_password by '123456';#修改密码
drop user 'root'@'localhost';#删除用户



