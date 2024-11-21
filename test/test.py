import os
import pytest
import grpc
import tempfile
import tomli
from datetime import datetime

# 导入生成的 gRPC 模块
# import service_pb2
import service_pb2_grpc


# def load_config():
#     with open("pyproject.toml", "rb") as f:
#         config = tomli.load(f)
#     return config["tool"]["compress"]
#
#

class TestFileDecompress:

    def test1(self):
        assert 1== 1
    # @pytest.fixture(scope="class")
    # def config(self):
    #     return load_config()
    #
    # @pytest.fixture(scope="class")
    # def grpc_channel(self):
    #     # 连接到您的 gRPC 服务器
    #     server_address = 'localhost:50052'
    #     channel = grpc.insecure_channel(server_address)
    #     try:
    #         grpc.channel_ready_future(channel).result(timeout=10)
    #     except grpc.FutureTimeoutError:
    #         raise Exception("无法连接到gRPC服务器")
    #     return channel
    #
    # @pytest.fixture(scope="class")
    # def stub(self, grpc_channel):
    #     return service_pb2_grpc.FileDecompressStub(grpc_channel)

# @pytest.fixture
# def temp_files(self, config):
#
#     # 获取压缩文件路径和解压缩目录路径
#     compressed_file_path = config["compressed_file_path"]
#     decompressed_path = config["decompressed_dir"]
#
#     # 确保解压缩目录存在
#     os.makedirs(decompressed_path, exist_ok=True)
#
#     yield compressed_file_path, decompressed_path
#
# def test_successful_decompression(self, stub, temp_files, config):
#     compressed_path, decompressed_path = temp_files
#
#     # 确保7z文件存在
#     assert os.path.exists(compressed_path), f"7z文件不存在: {compressed_path}"
#
#     # 构造请求
#     request = service_pb2.MyRequest(
#         compress_file_path=compressed_path,
#         decompress_file_path=os.path.join(decompressed_path, "output")
#     )
#
#     # 发送请求并检查响应
#     response = stub.MyMethod(request)
#     print(f"Response: status={response.status}, message={response.message}")
#
#     # 验证结果
#     assert response.status == 200, f"解压失败: {response.message}"
#     assert os.path.exists(decompressed_path), f"解压目录不存在: {decompressed_path}"
