# 第一章 容器技术的发展

## 为什么需要容器

宿主机和容器之间为容器引擎，容器并不包含操作系统，应用程序运行在容器中。

容器主要的特性之一就是 **进程隔离**，容器非常适合在当前云环境快速迁移和部署应用程序。

## 容器的优缺点

1. 优点
   1. 敏捷度高
   2. 提高生产力
   3. 版本控制
   4. 运行环境可移植
   5. 标准化
   6. 安全
2. 缺点
   1. 复杂性增加
   2. 原生Linux支持
   3. 不成熟



## docker容器是如何工作的

> Docker容器：使用Docker引擎进行调度和隔离，提高了资源利用率，在相同硬件能力下可以运行更多的容器实例；每个容器拥有自己的隔离化用户空间

| 对比内容     | Docker容器                                                   | VM                                                           |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 隔离性       | 较弱的隔离                                                   | 强隔离                                                       |
| 启动速度     | 秒级                                                         | 分钟级                                                       |
| 镜像大小     | 最小几兆字节                                                 | 几百兆字节到几吉字节                                         |
| 运行性能     | 损耗小于2%                                                   | 损耗15%左右                                                  |
| 镜像可移植性 | 平台无关                                                     | 平台相关                                                     |
| 密度         | 单机上支持100到1000个                                        | 单机上支持10到100个                                          |
| 安全性       | 权限提升：容器内用户可具备宿主机root权限<br />硬件不隔离：容器容易受到攻击 | 权限分离：虚拟机租户root权限和主机root权限分离<br />硬件隔离：防止虚拟机彼此交互 |

Docker使用客户端/服务器（C/S）架构模式，Docker守护进程（Docker Daemon）作为服务器端接收Docker客户端的请求，并负责创建、运行和分发Docker容器。Docker守护进程一般在Docker主机后台运行，用户使用Docker客户端直接跟Docker守护进程进行信息交互。

## Docker体系结构重点部分组成

1. Docker客户端：用于与Docker守护进程建立通信的客户端。Docker客户端只需要向Docker服务器或者守护进程发出请求指令（Docker构建、Docker拉取和Docker启动等指令），服务器或者守护进程将完成所有工作并返回结果。
2. Docker主机：一个物理或者虚拟的机器，用于执行Docker守护进程和容器。
3. Docker守护进程：接收并处理Docker客户端发送的请求，监测Docker API的请求和管理Docker对象，比如镜像、容器、网络和数据卷。



# 第二章 Docker简介

## 什么是Docker

基于go开发并遵从Apache 2.0开源协议，完全使用沙箱机制，容器之间不会有任何的接口。

## Docker的由来与发展历程

dotCloud公司做的后来改名为Docker公司

## Docker的架构与组成

1. 采用C/S架构
   1. 管理员通过Docker客户端与Docker服务器进行交互。
   2. Docker服务器负责构建、运行和分发Docker镜像

### 镜像

镜像就是**容器的模板**。对于普通用户来说，镜像文件通常都是只读的。

镜像的作用是用来创建容器，镜像和容器之间的关系就是模板和具体实例的关系，用户可以使用一个镜像创建多个容器。

### 容器

容器是独立运行的一个或者一组应用，是从镜像创建的运行实例

### 仓库

仓库（repository）是集中存放镜像文件的地方，同时Docker的仓库还提供镜像文件的版本控制功能。

1. 公有仓库 Docker Hub，存放了数据庞大的镜像供用户下载
2. 私有仓库

## Docker容器生态环境

### 容器核心技术

容器核心技术是指能够让容器在主机上运行起来的那些技术

1. 容器规范
   1. OCI(Open Container Initiative)的组织已发布了两个规范：runtime spec和image format spec，保证了不同的开发商的容器能够在不同的runtime上运行，保证了容器的可移植性和互操作性
2. 容器runtime
   1. runtime是容器真正运行的地方且需要与操作系统kernel紧密合作，为容器提供运行环境。类似于JVM和java。目前主流的三个容器lxc、runc和rkt
3. 容器管理工具
   1. 容器管理工具对内与runtime交互，对外为用户提供接口，如CLI等。目前主流的三个runtime对应的管理工具：lxd-lxc，Docker Engine-runc，rkt cli-rkt
4. 容器定义工具
   1. 容器定义工具允许用户定义容器的内容和属性，可用于保存、共享和重建容器。Docker image是Docker容器的模板，runtime依据Docker image创建容器。Dockerfile是包含若干条命令的文本文件，可以通过这些命令创建Docker image。ACI（App Container Image）与Docker image类似，只不过它是由CoreOS开发的rkt容器的镜像格式。
5. Registry仓库
   1. 用于统一存放镜像，这个仓库称为Registry
6. 容器OS
   1. 专门运行容器的操作系统，通常体积更小，启动更快。且因为是容器定制的OS，所以通常它们运行容器的效率会很高。目前如CoreOS、Atomic和Ubuntu Core

### 容器平台技术

让容器作为集群在分布式环境中运行

#### 容器编排引擎

编排（orchestration），通常包含容器管理、调度、集群定义和服务发现等。通过容器编排引擎，容器被有机地组合成微服务应用

容器的编排引擎有：

​	Docker Swarm（Docker开发的）

​	Kubernetes（Google领导开发的也支持Docker和CoreOS容器）

​	Mesos（通用的集群资源调度平台。Mesos和Marathon一起提供容器编排引擎功能）

#### 容器管理平台

是架构在容器编排引擎之上的一个更为通用的平台，通常其可以支持多种编排引擎，抽象了编排引擎的底层实现细节。Rancher和ContainerShip是容器管理平台的典型代表

#### 基于容器的PaaS

为微服务应用开发人员和公司提供了开发、部署和管理应用的平台，使用户不必关心底层基础设施而专注于应用的开发。Deis、Flynn和Dokku都是开源容器PaaS的代表。

## 容器支持技术

1. 容器网络
2. 服务发现
3. 监控
4. 数据管理
5. 日志管理
6. 安全性

# 第三章 Docker的安装与使用

## 将当前用户添加到docker组中

```shell
sudo usermod -aG docker testuesr
```

## 使用docker镜像

```shell
docker run hello-world
docker search ubuntu
docker pull hello-world
docker run -it hello-world
docker images
```

 # 第四章

## 容器的生命周期

1. Created
2. Running
3. Paused
4. Stopped
5. Deleted