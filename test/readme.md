1. 进入poetry环境
```shell
poetry shell
```
2. 安装依赖
```shell
poetry install
```
3. 生成python文件
```shell
poetry run python -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/service.proto
```
4. 运行测试
```shell
# 指定压缩文件和解压文件的路径
poetry run pytest test.py -v --compress-path=/path/to/compressed/file --decompress-path=/path/to/decompressed/file
```

参数说明：
- `--compress-path`: 压缩文件的路径（必需）
- `--decompress-path`: 解压后文件的保存路径（必需）
