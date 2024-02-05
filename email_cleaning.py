import os
from transformers import pipeline

pipe = pipeline("text-generation", model="/Users/sarthakkapila/.ollama/models/manifests/registry.ollama.ai/library")

prompt = """
    You are an expert of convert raw email thread into original message / reply pairs. 
    You are given a raw email thread that Jason reply to others, your goal is to convert it into original message / reply pairs. 
    - orignal_message: the last message sent to Jason, if it is a long email thread, only take the last message
    - jason_reply: Jason's reply to the original message

    if there is only one message in the thread, that should be jason_reply

    The exported format should look something like 
    {
        "original_message": "xxxx",
        "jason_reply": "xxxx"
    }
    """
    
inputs = tokenizer(prompt, return_tensors="pt")


generate_ids = model.generate(inputs.input_ids, max_length=1024)
tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
