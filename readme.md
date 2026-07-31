概述
----------
想要让agent还原设计图，需要在`Saved\TextureExports\Dynamic`下准备两样东西：`UITextures`和`image_describe.txt`
* `UITextures`需要每个用户使用编辑器工具手动导出
* `image_describe.txt`是对所有图片的描述，我传了，但当UITextures有新增时就需要更新

导出所有要描述的图片
-----------
使用编辑器工具`TextureExport`导出所有资产为图片，会导出到`Saved\TextureExports\Dynamic\UITextures`目录

安装CodeBuddy CLI
-----------
执行`npm install -g @tencent-ai/codebuddy-code`

生成图片路径列表
-----------
1. 下载本仓库
2. 把导出的`UITextures`目录复制到本仓库目录下
3. 运行`generate_image_list.py`（会生成`images_list_full.txt`文件）

描述图片
-----------
### 全量描述
运行`describe_images.py`

### 增量描述
1. 要有先前描述好的结果。先前的结果在`Saved\TextureExports\Dynamic\image_describe.txt`，要把它复制到本目录下，改名为`result.txt`
2. 用`find_remaining_images.py`，获取新增的图片列表
3. …………

错误处理
----------
### 中断后继续
如果因某些原因必须中断`describe_images.py`重新运行（如一直在print**输出不符合要求**，需要切换模型），下次需要接着运行，按以下步骤操作：
1. 看`result.txt`最下面，目前最新处理完的图片
2. 在`images_list_full.txt`中搜索这个图片文件名，记录行号，把`describe_images.py`开头的`StartPos`值改为这个行号，然后重新运行

使用结果
----------
1. 运行`remove_empty_lines.py`删除空行。最好再人工看一下`result.txt`，里面一些无关的AI自白也删掉
2. 把`result.txt`改名，覆盖`Saved\TextureExports\Dynamic\image_describe.txt`
