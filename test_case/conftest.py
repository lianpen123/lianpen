import pytest

from tools.api import request_tool


@pytest.fixture(scope='session')                            
def pub_data():
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
    data = {'token':r.json()["data"]["token"]}
    return data                                             


@pytest.fixture(scope='session')                            
def pub_list():                                             
    data = ['张三','zhangsan',30,'男','aaa123']             
    return data                                             


@pytest.fixture(scope='session')                            
def pub_var():                                              
    token = 'xxxxsdfsdfjkllwklewe'                          
    return token                                            

@pytest.fixture(scope='session',autouse=True)
def aaa(pytestconfig):
    print(pytestconfig.invocation_dir)