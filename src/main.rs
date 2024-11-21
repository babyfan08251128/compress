use tonic::{transport::Server, Request, Response, Status};
use std::fs::{self, File};
use std::path::Path;
use tracing::{debug, error, info, Level};
use tracing_subscriber::FmtSubscriber;
use compress_tools::*;

pub mod myservice {
    tonic::include_proto!("filedecompress");
}

use myservice::file_decompress_server::{FileDecompress, FileDecompressServer};
use myservice::{MyRequest, MyResponse};

#[derive(Debug, Default)]
pub struct FileDecompressImpl {}

fn is_7z_file(path: &str) -> bool {
    path.to_lowercase().ends_with(".7z")
}

fn clean_directory(path: &str) -> std::io::Result<()> {
    info!("Cleaning directory: {}", path);
    if Path::new(path).exists() {
        fs::remove_dir_all(path)?;
    }
    fs::create_dir_all(path)?;
    Ok(())
}

#[tonic::async_trait]
impl FileDecompress for FileDecompressImpl {
    async fn my_method(
        &self,
        request: Request<MyRequest>,
    ) -> std::result::Result<Response<MyResponse>, Status> {
        let req = request.into_inner();
        info!("Received decompress request for file: {}", req.compress_file_path);
        
        // Check if input file exists
        if !Path::new(&req.compress_file_path).exists() {
            error!("Input file does not exist: {}", req.compress_file_path);
            return Err(Status::not_found(format!("Input file not found: {}", req.compress_file_path)));
        }

        // Clean target directory
        if let Err(e) = clean_directory(&req.decompress_file_path) {
            error!("Failed to clean directory: {}", e);
            return Err(Status::internal(format!("Failed to clean directory: {}", e)));
        }

        // Check file type and decompress accordingly
        let result = if is_7z_file(&req.compress_file_path) {
            info!("Detected 7z format by extension, using sevenz-rust");
            sevenz_rust::decompress_file(&req.compress_file_path, &req.decompress_file_path)
                .map_err(|e| std::io::Error::new(std::io::ErrorKind::Other, e.to_string()))
        } else {
            info!("Using compress-tools for non-7z format");
            let source = File::open(&req.compress_file_path)
                .map_err(|e| std::io::Error::new(std::io::ErrorKind::Other, e.to_string()))?;
            let dest = Path::new(&req.decompress_file_path);
            uncompress_archive(&source, &dest, Ownership::Preserve)
                .map_err(|e| std::io::Error::new(std::io::ErrorKind::Other, e.to_string()))
        };

        match result {
            Ok(_) => {
                info!("Successfully decompressed file to: {}", req.decompress_file_path);
                Ok(Response::new(MyResponse {
                    status: 200,
                    message: format!("Successfully decompressed file to: {}", req.decompress_file_path),
                }))
            }
            Err(e) => {
                error!("Failed to decompress file: {}", e);
                Err(Status::internal(format!("Failed to decompress file: {}", e)))
            }
        }
    }
}

#[tokio::main]
async fn main() -> std::result::Result<(), Box<dyn std::error::Error>> {
    // 设置日志订阅器
    let subscriber = FmtSubscriber::builder()
        .with_max_level(Level::INFO)
        .finish();
    tracing::subscriber::set_global_default(subscriber).expect("设置日志订阅器失败");
    let addr = "[::1]:50052".parse()?;
    let service = FileDecompressImpl::default();

    info!("Server listening on {}", addr);

    Server::builder()
        .add_service(FileDecompressServer::new(service))
        .serve(addr)
        .await?;

    Ok(())
}
