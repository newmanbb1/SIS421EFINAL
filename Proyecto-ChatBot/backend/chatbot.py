from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = "Qwen/Qwen1.5-0.5B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

llm_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
    temperature=0.7,
    top_p=0.9,
    do_sample=True,
  

)

llm = HuggingFacePipeline(pipeline=llm_pipeline)

# ✅ Prompt personalizado en español
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
Responde siempre en español de forma clara y útil. Responde solo lo que el usuario pregunta, sin saludar si no se solicita y sin inventar preguntas o continuar el diálogo.

{history}
Usuario: {input}
Asistente:"""
)


memory = ConversationBufferMemory(memory_key="history", k=2)
chat_chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

# Función para obtener respuesta
def get_response(user_input):
    raw_output = chat_chain.run(user_input)
    answer = raw_output.split("Asistente:")[-1].strip()

    # Si el modelo genera un turno del usuario por error, lo cortamos
    if "Usuario:" in answer:
        answer = answer.split("Usuario:")[0].strip()

    # Si empieza con saludos innecesarios, los eliminamos
    for saludo in ["Hola", "hola", "Buenas", "buenas"]:
        if answer.lower().startswith(saludo.lower()):
            answer = answer.replace(saludo, "").strip(",. ")

    return answer
