#### 一、OVS简介
Openvswitch是一个优秀的开源软件交换机，支持主流的交换机功能，比如二层交换、网络隔离、QoS、流量监控等，而其最大的特点就是支持openflow，openflow定义了灵活的数据包处理规范。为用户提供L2-L7包处理能力。OVS支持多种Linux虚拟化技术，包括Xen、KVM以及VirtualBox。此外，OVS支持硬件交换机。OVS支持丰富的特性，如下：

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-9-28/29504104.jpg)
本教程主要就如下几个特性展开介绍：

    1、802.1Q VLAN

    2、流量监控sFlow

    3、QoS

    4、GRE、VXLAN、STT隧道

    5、LACP

    6、OpenFlow1.0/1.3

#### 二、OVS架构

1、OVS在SDN架构中所处位置

OvS 通过openflow流表可以实现各种网络功能，并且通过openflow protocol可以方便的实现控制+转发分离的SDN方案；基于虚拟化的OVS，可以为数据中心提供非常灵活的网络配置能力。

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-9-28/40575247.jpg)
2、OVS内部架构（各组件关系）

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-9-28/74254852.jpg)

+ ovs-vswitchd：主要模块，实现内核datapath upcall 处理以及ofproto 查表，同时是dpdk datapath处理程序。
+ ovsdb-server：数据库服务程序, 使用目前普遍认可的ovsdb 协议。
+ ovs-vsctl：网桥、接口等的创建、删除、设置、查询等。
+ ovs-dpctl：配置vswitch内核模块
+ ovs-appctl：发送命令消息到ovs-vswithchd, 查看不同模块状态
+ ovs-ofctl：下发流表信息。该命令可以配置其他openflow 交换机（采用openflow 协议）

接下来实验中主要涉及的模块为ovs-vsctl以及ovs-ofctl。

#### 三、安装OVS

1、环境：

  ubuntu18.04 LTS
  
  Open vSwitch2.9.0
  
2、采用二进制安装的方法，用ubuntu安装OVS极其简单
```
sudo apt-get update
sudo apt-get install openvswitch-switch openvswitch-common
```

#### 四、试试水

创建一个网桥并查看： sudo ovs-vsctl add-br s1

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-9-28/60795836.jpg)
#### 五、参考

https://media.readthedocs.org/pdf/openvswitch/latest/openvswitch.pdf
https://www.sdnlab.com/19448.html