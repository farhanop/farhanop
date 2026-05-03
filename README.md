"use client";
import { useState, useEffect } from "react";
import ThemeToggle from "./ThemeToggle";
import Logo from "./Logo";
import {
  FiUser,
  FiBriefcase,
  FiTerminal,
  FiMail,
  FiMenu,
  FiX,
} from "react-icons/fi";
import { motion, AnimatePresence } from "framer-motion";

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [activeLink, setActiveLink] = useState<string>("");

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const handleLinkClick = (id: string) => {
    setActiveLink(id);
    setIsMobileMenuOpen(false);
  };

  const navLinks = [
    { id: "about", label: "About", icon: <FiUser size={18} /> },
    { id: "experience", label: "Experience", icon: <FiBriefcase size={18} /> },
    { id: "projects", label: "Projects", icon: <FiTerminal size={18} /> },
    { id: "contact", label: "Contact", icon: <FiMail size={18} /> },
  ];

  return (
    <nav className="fixed top-0 left-0 w-full z-50 px-4 py-4 pointer-events-none">
      <motion.div
        initial={{ y: -100, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.5, type: "spring", stiffness: 80 }}
        className={`max-w-7xl mx-auto pointer-events-auto transition-all duration-300 ${
          isScrolled
            ? "bg-white/80 dark:bg-[#0a0a0a]/80 backdrop-blur-xl border border-slate-200/50 dark:border-white/10 shadow-[0_8px_30px_rgb(0,0,0,0.04)] dark:shadow-[0_8px_30px_rgba(0,0,0,0.4)] rounded-2xl py-3 px-6"
            : "bg-transparent border-transparent py-4 px-6"
        }`}
      >
        <div className="flex justify-between items-center">
          {/* Bagian Kiri: Logo */}
          <div className="flex items-center gap-3 group cursor-pointer w-1/3">
            <div className="relative p-2 bg-slate-100 dark:bg-slate-800 rounded-lg group-hover:bg-blue-100 dark:group-hover:bg-blue-900/30 transition-colors">
              <Logo />
              <span className="absolute top-1.5 right-1.5 w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></span>
            </div>
            <div className="font-mono font-bold text-lg tracking-widest text-slate-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-cyan-400 transition-colors hidden sm:block">
              &lt;Parhan /&gt;
            </div>
          </div>

          {/* Bagian Tengah: Menu Navigasi (Centered) */}
          <div className="flex-1 flex justify-center w-1/3">
            <ul className="flex items-center gap-1 bg-slate-100/50 dark:bg-slate-900/50 p-1.5 rounded-full border border-slate-200/50 dark:border-white/5">
              {navLinks.map((link) => (
                <li key={link.id}>
                  <a
                    href={`#${link.id}`}
                    onClick={() => handleLinkClick(link.id)}
                    className={`relative px-4 py-2 rounded-full flex items-center gap-2 text-sm font-medium transition-colors ${
                      activeLink === link.id
                        ? "text-blue-600 dark:text-cyan-400 bg-white dark:bg-slate-800 shadow-sm"
                        : "text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-white/50 dark:hover:bg-slate-800/50"
                    }`}
                  >
                    <span className="group-hover:scale-110 transition-transform">
                      {link.icon}
                    </span>
                    <span className="hidden lg:inline">{link.label}</span>
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Bagian Kanan: Theme Toggle & Mobile Menu Button */}
          <div className="flex items-center justify-end w-1/3 gap-3">
            <ThemeToggle />
            <button
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className="md:hidden p-2 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-lg transition-colors"
            >
              {isMobileMenuOpen ? <FiX size={24} /> : <FiMenu size={24} />}
            </button>
          </div>
        </div>
      </motion.div>

      {/* Mobile Menu Dropdown */}
      <AnimatePresence mode="wait">
        {isMobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0, y: -20 }}
            animate={{ opacity: 1, height: "auto", y: 0 }}
            exit={{ opacity: 0, height: 0, y: -20 }}
            transition={{ duration: 0.3, ease: "easeInOut" }}
            className="mt-4 md:hidden bg-white/90 dark:bg-[#0a0a0a]/95 backdrop-blur-xl border border-slate-200 dark:border-white/10 rounded-2xl shadow-2xl overflow-hidden"
          >
            <ul className="flex flex-col p-4 space-y-2">
              {navLinks.map((link) => (
                <li key={link.id}>
                  <a
                    href={`#${link.id}`}
                    onClick={() => handleLinkClick(link.id)}
                    className={`flex items-center gap-4 p-3 rounded-xl transition-all font-medium ${
                      activeLink === link.id
                        ? "text-blue-600 dark:text-cyan-400 bg-blue-50 dark:bg-blue-900/20"
                        : "text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800/50 hover:text-blue-600 dark:hover:text-cyan-400"
                    }`}
                  >
                    {link.icon}
                    <span>{link.label}</span>
                  </a>
                </li>
              ))}
            </ul>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
}
