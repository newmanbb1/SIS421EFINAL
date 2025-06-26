from  transformers import pipeline

generator = pipeline("text-generation", model="Qwen/Qwen1.5-0.5B")

print(generator("Hola mundo", max_new_tokens=10))
