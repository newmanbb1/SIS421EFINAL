import { useState } from 'react'
import "./styles/styles.css";
import './App.css'
 import ChatBot from './components/ChatBot'
function App() {

  return (
    <div className="app">
      <h1 className="title">🤖 Chatbot </h1>
      <ChatBot />
    </div>

  )
}

export default App
