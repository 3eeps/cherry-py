# cherry-🥧

consoldating llama.cpp scripts and quantize.exe for easy conversions

should be trivial to add more arguments if needed

keep all files in same dir as 'convert_pipeline.py' then run convert_pipeline.py and follow prompts.

thanks to https://github.com/ggerganov for his amazing work on llama.cpp

ggml_to_gguf help

```
arguements:		defaults/choice:		help/info:   
--input							Input GGMLv3 filename
--output 		 				Output GGUF filename
--name							Set model name
--desc 							Set model description
--gqa 			default = 1, 			grouped-query attention factor (use 8 for LLaMA2 70B)
--eps 			default = '5.0e-06',		RMS norm eps: Use 1e-6 for LLaMA1 and OpenLLaMA, use 1e-5 for LLaMA2
--context-length	default = 2048, 		Default max context length: LLaMA1 is typically 2048, LLaMA2 is typically 4096

--model-metadata-dir 	 				Load HuggingFace/.pth vocab and metadata from the specified directory
--vocab-dir 						directory containing tokenizer.model, if separate from model file - only meaningful with --model-metadata-dir
--vocabtype		choices=["spm", "bpe"]  	vocab format - only meaningful with --model-metadata-dir and/or --vocab-dir (default: spm)", default="spm"
```

hf-to-gguf help:

```
Usage: convert_hf_to_gguf.py dir-model ftype

  ftype == 0 -> float32
  ftype == 1 -> float16
```

quantize help:

```
usage: quantize.exe [--help] [--allow-requantize] [--leave-output-tensor] model-f32.gguf [model-quant.gguf] type [nthreads]

  --allow-requantize: Allows requantizing tensors that have already been quantized. Warning: This can severely reduce quality compared to quantizing from 16bit or 32bit
  --leave-output-tensor: Will leave output.weight un(re)quantized. Increases model size but may also increase quality, especially when requantizing

Allowed quantization types:
   2  or  Q4_0   :  3.56G, +0.2166 ppl @ LLaMA-v1-7B
   3  or  Q4_1   :  3.90G, +0.1585 ppl @ LLaMA-v1-7B
   8  or  Q5_0   :  4.33G, +0.0683 ppl @ LLaMA-v1-7B
   9  or  Q5_1   :  4.70G, +0.0349 ppl @ LLaMA-v1-7B
  10  or  Q2_K   :  2.63G, +0.6717 ppl @ LLaMA-v1-7B
  12  or  Q3_K   : alias for Q3_K_M
  11  or  Q3_K_S :  2.75G, +0.5551 ppl @ LLaMA-v1-7B
  12  or  Q3_K_M :  3.07G, +0.2496 ppl @ LLaMA-v1-7B
  13  or  Q3_K_L :  3.35G, +0.1764 ppl @ LLaMA-v1-7B
  15  or  Q4_K   : alias for Q4_K_M
  14  or  Q4_K_S :  3.59G, +0.0992 ppl @ LLaMA-v1-7B
  15  or  Q4_K_M :  3.80G, +0.0532 ppl @ LLaMA-v1-7B
  17  or  Q5_K   : alias for Q5_K_M
  16  or  Q5_K_S :  4.33G, +0.0400 ppl @ LLaMA-v1-7B
  17  or  Q5_K_M :  4.45G, +0.0122 ppl @ LLaMA-v1-7B
  18  or  Q6_K   :  5.15G, -0.0008 ppl @ LLaMA-v1-7B
   7  or  Q8_0   :  6.70G, +0.0004 ppl @ LLaMA-v1-7B
   1  or  F16    : 13.00G              @ 7B
   0  or  F32    : 26.00G              @ 7B
   ```
