import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import { BrowserRouter } from "react-router-dom"

import App from "./App"

import "./styles/styles.css"
import Header from "./components/Header"

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter>
      <Header />
      <App />
    </BrowserRouter>
  </StrictMode>
)
