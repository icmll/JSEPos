# 源码自动生成模板 empty

### 概述

* 模板: empty
* 模板使用时间: 2018-08-14 11:57:59

### Docker
* Image: registry.cn-beijing.aliyuncs.com/rdc-template/repo
* Tag: 0817
* SHA256: 5556cb0b0d1605f84cca2b4118fe3d65e50314e905b66b8d926f4b1de90c432d

### 用户输入参数
* repoUrl: "git@code.aliyun.com:28656-private/jsepos.git" 
* needDockerfile: "N" 
* appName: "jsepos" 
* operator: "aliyun_815058" 
* appReleaseContent: "# 
* 请参考: 请参考 
* https://help.aliyun.com/document_detail/59293.html: https://help.aliyun.com/document_detail/59293.html 
* 了解更多关于release文件的编写方式: 了解更多关于release文件的编写方式 
* [NEWLINE][NEWLINE]#: [NEWLINE][NEWLINE]# 
* 构建源码语言类型[NEWLINE]code.language: python3.5" 

### 上下文参数
* appName: jsepos
* operator: aliyun_815058
* gitUrl: git@code.aliyun.com:28656-private/jsepos.git
* branch: master


### 命令行
	sudo docker run --rm -v `pwd`:/workspace -e repoUrl="git@code.aliyun.com:28656-private/jsepos.git" -e needDockerfile="N" -e appName="jsepos" -e operator="aliyun_815058" -e appReleaseContent="# 请参考 https://help.aliyun.com/document_detail/59293.html 了解更多关于release文件的编写方式 [NEWLINE][NEWLINE]# 构建源码语言类型[NEWLINE]code.language=python3.5"  registry.cn-beijing.aliyuncs.com/rdc-template/repo:0817

