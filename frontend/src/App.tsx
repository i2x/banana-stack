import { useEffect } from "react";
import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import About from "./pages/About";
import Articles from "./pages/Articles";
import TreatmentsList from "./pages/TreatmentsList";
import Models from "./pages/Models";
import NotFound from "./pages/Notfound";

import { initCsrf } from "./services/api";  // ✅ เรียกใช้จาก services

export default function App() {
  useEffect(() => {
    initCsrf().catch((err) => console.error("CSRF init failed", err));
  }, []);

  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/articles" element={<Articles />} />
      <Route path="/treatments/list/:diseaseId" element={<TreatmentsList />} />
      <Route path="/models" element={<Models />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}