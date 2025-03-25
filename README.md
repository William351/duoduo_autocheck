# 朵朵校友圈自动签到

## 食用方式：

### 打开朵朵
### **Fork**本仓库



### 添加**secret**

1. 跳转至自己的仓库的`Settings`->`Secrets and variables`->`Action`

2. 添加1个`repository secret`，命名为``，其值对应账号的Ddtk值中的有效部分（获取方式如下）

- 在朵朵校友圈网页端的按下'F12'

- 切换到`Network`页面下，点击签到,出现名称为api的请求

- 点击后在`Request Headers`下找到`Ddtk`，右键复制Ddtk的值即可

  > 参考格式：********************************************************（ps:不需要bearer前缀，直接第二行开始


- 多账号请在 `DDTK_TOKEN` 中 添加多个 `Ddtk` 中间使用 `&`连
