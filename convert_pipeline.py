# ./codespace/convert_pipeline.py
import os

def quant_gguf():
    arg_list_quant = ['gguf_file', 'output_file', 'quant type']
    iter = -1
    for arg in arg_list_quant:
        iter = iter + 1
        arg_list_quant[iter] = input(f"{arg}: ")
    os.system(f"quantize.exe {arg_list_quant[0]} {arg_list_quant[1]} {arg_list_quant[2]}")

def hf_to_gguf():
    arg_list_hf = ['hf_dir']
    iter = -1
    for arg in arg_list_hf:
        iter = iter + 1
        arg_list_hf[iter] = input(f"{arg}: ")
    os.system(f"py convert_hf_to_gguf.py {arg_list_hf[0]} 1")

def ggml_to_gguf():
    arg_list_ggml = ['ggml_file', 'output_file', 'metadata-dir']
    iter = -1
    for arg in arg_list_ggml:
        iter = iter + 1
        arg_list_ggml[iter] = input(f"{arg}: ")
    os.system(f"py convert_ggml_to_gguf.py --input {arg_list_ggml[0]} --output {arg_list_ggml[1]} --model-metadata-dir {arg_list_ggml[2]}")

run_loop = True
print("'hf': hf-to-gguf")
print("'ggml': ggml-gguf")
print("'quant': quantize-gguf")
while run_loop:
    convert_type = input(">>> ")
    if convert_type == "hf":
        hf_to_gguf()
    elif convert_type == "ggml":
        ggml_to_gguf()
    elif convert_type == "quant":
        quant_gguf()
    run_loop = False
