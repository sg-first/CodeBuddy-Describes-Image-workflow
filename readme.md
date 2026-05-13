
导出所有要描述的图片
-----------
使用编辑器工具`TextureExport`导出所有资产为图片，会导出到`Saved\TextureExports\Dynamic\UITextures`目录

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
2. 现在diff功能还没支持。如果你知道新增的是哪些，可以把新增的图片列表写到`task.md`，然后让workBuddy读取`task.md`进行描述（模型选择Kimi-K2.5），把描述结果复制追加到`result.txt`

错误处理
----------
### 中断后继续
如果因某些原因必须中断`generate_image_list.py`重新运行（如一直在print**“未生成任何描述”**，需要切换模型），下次需要接着运行，按以下步骤操作：
1. 看`result.txt`最下面，目前最新处理完的图片
2. 在`images_list_full.txt`中搜索这个图片文件名，记录行号，把`describe_images.py`开头的`StartPos`值改为这个行号

### 选择模型
按价格排序：Kimi-K2.5 < Kimi-K2.6 ≈ GLM-5v-Turbo ≈ GPT-5.1

使用结果
----------
把`result.txt`改名，覆盖`Saved\TextureExports\Dynamic\image_describe.txt`
