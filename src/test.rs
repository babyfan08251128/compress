use compress_tools::*;
use std::fs::File;
use std::path::Path;

fn main() {
    let mut source = File::open("/Users/kpas/SynologyDrive/Github/M01-AnalyzeCoreProgram/compress/test/compressd/SysinternalsSuite.zip").unwrap();
    let dest = Path::new("/Users/kpas/SynologyDrive/Github/M01-AnalyzeCoreProgram/compress/test/decompress");
    uncompress_archive(&mut source, &dest, Ownership::Preserve).unwrap();
} 