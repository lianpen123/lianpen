#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tools.api import request_tool
'''
文件名 和方法名要以test_
类名Test
'''


def test_post_json(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "pwd": "guoya129",
  "userName": "guoya129"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    print(r.headers)




def test_get_params(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/getCustomer"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"phone":'18103909786'}
    headers={"token":"eyJ0aW1lT3V0IjoxNTcxMzgyNTQ3MTI1LCJ1c2VySWQiOjQ4LCJ1c2VyTmFtZSI6Inh1ZXBsMTIzIn0="}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_get_file(pub_data):
    file_name = "e:\\sku.xlsx" # 下载文件地址
    method = "GET"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '下载库存信息'  # allure报告中二级分类
    title = "下载库存信息_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/downProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"pridCode":'4l300'}
    headers={"token":"eyJ0aW1lT3V0IjoxNTcxMzgyNTQ3MTI1LCJ1c2VySWQiOjQ4LCJ1c2VyTmFtZSI6Inh1ZXBsMTIzIn0="}
    status_code = 200  # 响应状态码
    expect = "9999"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
    with open(file_name,"rw") as f :
        f.write(r.content)

def test_post_file(pub_data):
    file_name = "e:\\sku.xls" # 下载文件地址
    method = "POST"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '盘点库存'  # allure报告中二级分类
    title = "盘点库存"  # allure报告中用例名字
    uri = "/product/uploaProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    files = {"file":open(file_name,'rb')}
    headers={"token":"eyJ0aW1lT3V0IjoxNTcxMzgyNTQ3MTI1LCJ1c2VySWQiOjQ4LCJ1c2VyTmFtZSI6Inh1ZXBsMTIzIn0="}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,files=files,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)




