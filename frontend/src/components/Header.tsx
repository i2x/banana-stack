import { useState } from "react";
import { Link } from "react-router-dom";

export default function Header() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="bg-slate-800 shadow-md">
      <nav className="container mx-auto flex justify-between items-center py-4 px-6">
        {/* Logo */}
        <div className="flex items-center space-x-2">
          <img
            src="/dookluay-icon.svg"   // ✅ แนะนำให้ใส่รูปไว้ใน public แล้วเรียกแบบนี้
            alt="Doo Kluay Logo"
            className="w-12 h-12 object-contain"
          />
          <span className="text-white font-bold text-2xl">Doo Kluay</span>
        </div>

        {/* Hamburger Button (มือถือ) */}
        <button
          className="md:hidden text-white focus:outline-none"
          onClick={() => setIsOpen(!isOpen)}
        >
          {/* icon แบบ 3 ขีด */}
          <svg
            className="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            {isOpen ? (
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M6 18L18 6M6 6l12 12"
              />
            ) : (
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M4 6h16M4 12h16M4 18h16"
              />
            )}
          </svg>
        </button>

        {/* Menu Links */}
        <ul
          className={`flex-col md:flex md:flex-row md:space-x-6 text-white font-medium absolute md:static left-0 w-full md:w-auto bg-slate-800 md:bg-transparent transition-all duration-300 ease-in-out ${
            isOpen ? "top-16 flex" : "top-[-500px] hidden"
          }`}
        >
          <li className="px-6 py-2 md:p-0">
            <Link to="/" className="hover:text-gray-200 transition" onClick={() => setIsOpen(false)}>
              Home
            </Link>
          </li>
          <li className="px-6 py-2 md:p-0">
            <Link to="/about" className="hover:text-gray-200 transition" onClick={() => setIsOpen(false)}>
              About
            </Link>
          </li>
          <li className="px-6 py-2 md:p-0">
            <Link to="/articles" className="hover:text-gray-200 transition" onClick={() => setIsOpen(false)}>
              Articles
            </Link>
          </li>
          <li className="px-6 py-2 md:p-0">
            <Link to="/models" className="hover:text-gray-200 transition" onClick={() => setIsOpen(false)}>
              Models
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}
