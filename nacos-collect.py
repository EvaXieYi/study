'''import nacos



def init(data_id, group):
    server_address="192.168.198.5"
    server_port="8847"
    Namespace="public"
    client = nacos.NacosClient(f'{server_address}:{server_port}', namespace=Namespace)
    config = client.get_config(data_id, group)
   
    return config
    # 配置数据解析（YAML）
   

    # 通过键路径，解析出数据

group ="DEFAULT_GROUP"
data_id="1122222"
init(group,data_id)'''

from nacos import NacosClient
import yaml

rules_config = {}

def nacos_init():
    # 服务地址
    server_address = "192.168.198.6:8847"
    # 命名空间
    namespace = "public"

    client = NacosClient(server_addresses=server_address, namespace=namespace)
    # 组
    group = "DEFAULT_GROUP"
    # data_id
    data_id = "1122222"
    # 返回结果为字符串
    conf = client.get_config(data_id, group)
    # print(conf)
    read_config(conf)

    # add watch
    client.add_config_watcher(data_id, group, test_cb)
    # instances = client.list_naming_instance('my_service')

def test_cb(args):
    content = args['content']
    read_config(content)
    print(content)

def read_config(content):
    rules_config.update(yaml.load(content, yaml.FullLoader))

if __name__ == '__main__':
    # 单文件测试时，要加上time.sleep()。在flask或其他项目中调用只需要nacos_init()即可
    nacos_init()
    # time.sleep(3000)