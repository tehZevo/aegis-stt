import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

def create_pipeline(model_id):
  device = "cuda:0" if torch.cuda.is_available() else "cpu"
  print("Pipeline created on", device)
  torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

  model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
  )
  model.to(device)

  processor = AutoProcessor.from_pretrained(model_id)

  pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    torch_dtype=torch_dtype,
    device=device,
  )

  return pipe
