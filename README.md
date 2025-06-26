# 🤖 Chatbot Inteligente con LangChain + Qwen + FastAPI + React

Este proyecto implementa un **chatbot conversacional inteligente** basado en el framework **LangChain** y el modelo open-source **Qwen** de Alibaba, con un backend desarrollado en **FastAPI** y una interfaz de usuario en **React**.

---

## 🧠 Tecnologías Utilizadas

### 🔧 Backend
- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [Transformers](https://huggingface.co/docs/transformers/index)
- Qwen1.5-0.5B (modelo LLM)

### 💻 Frontend
- ReactJS (Vite o Create React App)
- Axios (para peticiones al backend)
- TailwindCSS (opcional para estilos)


## 🚀 Instrucciones de Instalación y Ejecución

### 🔹 1. Clonar el Repositorio


git clone https://github.com/tu-usuario/langchain-qwen-chatbot.git
cd langchain-qwen-chatbot


🔧 Backend – FastAPI + LangChain
### 🔹2. Ir al directorio del backend


cd backend

### 🔹3. Crear entorno virtual (opcional pero recomendado)

python -m venv venv
source venv/bin/activate  # en Linux/macOS
venv\\Scripts\\activate    # en Windows

### 🔹4. Instalar dependencias
pip install -r requirements.txt

Si no tienes requirements.txt, instala manualmente:

pip install fastapi uvicorn langchain transformers accelerate torch


### 🔹5 Ejecutar el servidor FastAPI
uvicorn main:app --reload

### 🔹Frontend – ReactJS
### 🔹Ir al directorio del frontend
cd ../frontend
### 🔹Instalar dependencias
npm install
### 🔹Ejecutar la app React
npm run dev
