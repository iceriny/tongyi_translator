# 使用 通义千问 API 进行翻译的 Python 实现

# 使用

1. 在阿里云获取相关权限并获取模型的`API_KEY`
2. Git clone 本仓库
3. 使用 `pipenv` 安装依赖
4. 在根目录创建`.env.private`文件，写入`API_KEY`
    - 像这样: `DASHSCOPE_API_KEY="sk-***********************"`
5. 请参考`src/dnd_translator.py`文件编写针对某类文件的翻译逻辑
    - 该类继承于`src/base_plugin.py`中的`BasePlugin`类

# 对于 BG3 的翻译

如果你是从 3DM 站来的，那你大概率是为了翻译 BG3 的 Mod，对于 BG3Mod 的解包与翻译教程请自行搜索
本工具需要简单的 Python 基础。

1. 请参考上述的`使用`部分的 1~4 步
2. 将需要翻译的`*.xml`文件放入`input`文件夹中，可以是多个`*.xml`文件
3. 使用:

    ```Bash
    pipenv run python __init__.py
    ```

    程序会自动将翻译结果输出到`output`文件夹中

    - 如果你使用 VSCode，请开启虚拟环境，并使用`F5`键运行程序

> 因为本工具目前只是自己使用，所以针对用户没有进行什么优化，日后如果有需要，我可能考虑将程序进行构建为可执行程序
