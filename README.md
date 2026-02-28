<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Cyberpunk Dark README</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script>
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        primary: "#06b6d4", // Cyan
                        secondary: "#d946ef", // Magenta
                        background: {
                            light: "#1e293b", 
                            dark: "#0f172a", // Deep charcoal
                        },
                        surface: {
                            light: "#334155",
                            dark: "#1e293b",
                        },
                        accent: "#22d3ee",
                    },
                    fontFamily: {
                        display: ["Space Grotesk", "sans-serif"],
                        mono: ["Courier New", "monospace"], // For terminal feel
                    },
                },
            },
        }
    </script>
<style>
        /* Custom scrollbar for terminal feel */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0f172a; 
        }
        ::-webkit-scrollbar-thumb {
            background: #334155; 
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #475569; 
        }
        
        .neon-text {
            text-shadow: 0 0 5px rgba(6, 182, 212, 0.5), 0 0 10px rgba(6, 182, 212, 0.3);
        }
        .neon-border {
            box-shadow: 0 0 5px rgba(6, 182, 212, 0.2), inset 0 0 5px rgba(6, 182, 212, 0.1);
        }
        .glitch-effect {
            position: relative;
        }
        .glitch-effect::before,
        .glitch-effect::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        .glitch-effect::before {
            left: 2px;
            text-shadow: -1px 0 #d946ef;
            clip: rect(44px, 450px, 56px, 0);
            animation: glitch-anim 5s infinite linear alternate-reverse;
        }
        .glitch-effect::after {
            left: -2px;
            text-shadow: -1px 0 #06b6d4;
            clip: rect(44px, 450px, 56px, 0);
            animation: glitch-anim2 5s infinite linear alternate-reverse;
        }
        @keyframes glitch-anim {
            0% { clip: rect(31px, 9999px, 91px, 0); }
            20% { clip: rect(72px, 9999px, 14px, 0); }
            40% { clip: rect(5px, 9999px, 86px, 0); }
            60% { clip: rect(65px, 9999px, 33px, 0); }
            80% { clip: rect(98px, 9999px, 4px, 0); }
            100% { clip: rect(18px, 9999px, 52px, 0); }
        }
        @keyframes glitch-anim2 {
            0% { clip: rect(62px, 9999px, 11px, 0); }
            20% { clip: rect(14px, 9999px, 78px, 0); }
            40% { clip: rect(95px, 9999px, 2px, 0); }
            60% { clip: rect(5px, 9999px, 48px, 0); }
            80% { clip: rect(32px, 9999px, 99px, 0); }
            100% { clip: rect(81px, 9999px, 63px, 0); }
        }
    </style>
</head>
<body class="bg-background-dark text-slate-200 font-display min-h-screen selection:bg-primary selection:text-white">
<div class="relative flex min-h-screen w-full flex-col overflow-x-hidden">
<!-- Background Grid Pattern -->
<div class="absolute inset-0 bg-[linear-gradient(to_right,#1e293b_1px,transparent_1px),linear-gradient(to_bottom,#1e293b_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] pointer-events-none opacity-20"></div>
<div class="layout-container flex h-full grow flex-col relative z-10">
<div class="px-4 md:px-10 lg:px-40 flex flex-1 justify-center py-10">
<div class="layout-content-container flex flex-col max-w-[960px] flex-1 gap-8">
<!-- Profile Header Section -->
<div class="flex flex-wrap justify-between items-end gap-6 p-6 rounded-xl border border-primary/20 bg-surface-dark/50 backdrop-blur-sm neon-border">
<div class="flex flex-col gap-2">
<div class="flex items-center gap-3 mb-2">
<div class="h-2 w-2 rounded-full bg-secondary animate-pulse"></div>
<span class="text-secondary text-xs font-mono tracking-widest">SYSTEM_READY</span>
</div>
<h1 class="text-white text-5xl md:text-6xl font-black leading-tight tracking-tighter glitch-effect uppercase" data-text="ALEXANDER_NEO">
                                ALEXANDER_NEO
                            </h1>
<p class="text-primary text-lg md:text-xl font-medium leading-normal font-mono mt-2">
<span class="text-slate-500">&lt;</span> FULL_STACK_DEVELOPER <span class="text-slate-500">/&gt;</span>
<span class="text-slate-600 mx-2">|</span>
<span class="text-secondary">WAKE_UP_SAMURAI</span>
</p>
</div>
<div class="flex flex-col items-end gap-2 text-right">
<div class="h-16 w-16 md:h-20 md:w-20 rounded-full border-2 border-primary/50 overflow-hidden relative shadow-[0_0_15px_rgba(6,182,212,0.4)]">
<img alt="Cyberpunk avatar profile picture" class="object-cover w-full h-full filter saturate-0 contrast-125 hover:saturate-100 transition-all duration-300" data-alt="Cyberpunk avatar profile picture" src="https://lh3.googleusercontent.com/aida-public/AB6AXuArF3lGMXAcoIQ-ZKd48sRNeP84rfEVl_6fMGVvNyHTHzC1P10dBfJNCeay3lDpQUoGqyu7mCb3E5wP-9yRUrJY8mmTpwpHbZ8pObMY4g96OxRiL3i5kxINRZj0ZmEfNx2wuWgCwZwf2e3L5BvEfzAgtrdqfxjCxDyS19AsT-EGTaZ5GtiBrEyRV1Qi_xXZX0vdtoM0fha4V1K_BWxl143fJaQGZ_lCF4IUNbA4WzHygFp5hHspzuTdhMyXWTZgm1k1RrmN_e7oL9Yi"/>
</div>
</div>
</div>
<!-- Status Bar -->
<div class="flex flex-wrap gap-4 p-4 bg-black/40 border-y border-slate-800 font-mono text-xs md:text-sm text-slate-400 justify-between items-center">
<div class="flex gap-6">
<span class="flex items-center gap-2"><span class="material-symbols-outlined text-green-500 text-[16px]">wifi</span> STATUS: ONLINE</span>
<span class="flex items-center gap-2"><span class="material-symbols-outlined text-primary text-[16px]">memory</span> MEMORY: 64GB</span>
<span class="hidden md:flex items-center gap-2"><span class="material-symbols-outlined text-secondary text-[16px]">location_on</span> LOCATION: NIGHT_CITY</span>
</div>
<div class="text-slate-600">UPTIME: 99.9%</div>
</div>
<!-- Tech Stack Section -->
<div>
<div class="flex items-center gap-2 px-4 pb-4 pt-4">
<span class="material-symbols-outlined text-primary">terminal</span>
<h3 class="text-white text-xl font-bold leading-tight tracking-tight font-mono text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary">
                                &gt; INITIALIZE_TECH_STACK.EXE
                            </h3>
</div>
<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 p-4">
<!-- Tech Item 1 -->
<div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-primary/50 hover:shadow-[0_0_15px_rgba(6,182,212,0.15)] transition-all duration-300 relative overflow-hidden">
<div class="absolute inset-0 bg-gradient-to-br from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
<div class="text-primary group-hover:text-white transition-colors group-hover:scale-110 transform duration-300">
<span class="material-symbols-outlined text-[40px]">code_blocks</span>
</div>
<h2 class="text-slate-300 text-sm font-bold leading-tight font-mono group-hover:text-primary transition-colors">React</h2>
</div>
<!-- Tech Item 2 -->
<div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-green-500/50 hover:shadow-[0_0_15px_rgba(34,197,94,0.15)] transition-all duration-300 relative overflow-hidden">
<div class="absolute inset-0 bg-gradient-to-br from-green-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
<div class="text-green-500 group-hover:text-white transition-colors group-hover:scale-110 transform duration-300">
<span class="material-symbols-outlined text-[40px]">dns</span>
</div>
<h2 class="text-slate-300 text-sm font-bold leading-tight font-mono group-hover:text-green-500 transition-colors">Node.js</h2>
</div>
<!-- Tech Item 3 -->
<div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-yellow-400/50 hover:shadow-[0_0_15px_rgba(250,204,21,0.15)] transition-all duration-300 relative overflow-hidden">
<div class="absolute inset-0 bg-gradient-to-br from-yellow-400/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
<div class="text-yellow-400 group-hover:text-white transition-colors group-hover:scale-110 transform duration-300">
<span class="material-symbols-outlined text-[40px]">terminal</span>
</div>
<h2 class="text-slate-300 text-sm font-bold leading-tight font-mono group-hover:text-yellow-400 transition-colors">Python</h2>
</div>
<!-- Tech Item 4 -->
<div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-orange-500/50 hover:shadow-[0_0_15px_rgba(249,115,22,0.15)] transition-all duration-300 relative overflow-hidden">
<div class="absolute inset-0 bg-gradient-to-br from-orange-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
<div class="text-orange-500 group-hover:text-white transition-colors group-hover:scale-110 transform duration-300">
<span class="material-symbols-outlined text-[40px]">settings_suggest</span>
</div>
<h2 class="text-slate-300 text-sm font-bold leading-tight font-mono group-hover:text-orange-500 transition-colors">Rust</h2>
</div>
<!-- Tech Item 5 -->
<div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-blue-500/50 hover:shadow-[0_0_15px_rgba(59,130,246,0.15)] transition-all duration-300 relative overflow-hidden">
<div class="absolute inset-0 bg-gradient-to-br from-blue-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
<div class="text-blue-500 group-hover:text-white transition-colors group-hover:scale-110 transform duration-300">
<span class="material-symbols-outlined text-[40px]">inventory_2</span>
</div>
<h2 class="text-slate-300 text-sm font-bold leading-tight font-mono group-hover:text-blue-500 transition-colors">Docker</h2>
</div>
<!-- Tech Item 6 -->
<div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-secondary/50 hover:shadow-[0_0_15px_rgba(217,70,239,0.15)] transition-all duration-300 relative overflow-hidden">
<div class="absolute inset-0 bg-gradient-to-br from-secondary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
<div class="text-secondary group-hover:text-white transition-colors group-hover:scale-110 transform duration-300">
<span class="material-symbols-outlined text-[40px]">cloud_queue</span>
</div>
<h2 class="text-slate-300 text-sm font-bold leading-tight font-mono group-hover:text-secondary transition-colors">AWS</h2>
</div>
<!-- Tech Item 7 -->
<div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-red-500/50 hover:shadow-[0_0_15px_rgba(239,68,68,0.15)] transition-all duration-300 relative overflow-hidden">
<div class="absolute inset-0 bg-gradient-to-br from-red-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
<div class="text-red-500 group-hover:text-white transition-colors group-hover:scale-110 transform duration-300">
<span class="material-symbols-outlined text-[40px]">dataset</span>
</div>
<h2 class="text-slate-300 text-sm font-bold leading-tight font-mono group-hover:text-red-500 transition-colors">PostgreSQL</h2>
</div>
<!-- Tech Item 8 -->
<div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-purple-500/50 hover:shadow-[0_0_15px_rgba(168,85,247,0.15)] transition-all duration-300 relative overflow-hidden">
<div class="absolute inset-0 bg-gradient-to-br from-purple-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
<div class="text-purple-500 group-hover:text-white transition-colors group-hover:scale-110 transform duration-300">
<span class="material-symbols-outlined text-[40px]">deployed_code</span>
</div>
<h2 class="text-slate-300 text-sm font-bold leading-tight font-mono group-hover:text-purple-500 transition-colors">Kubernetes</h2>
</div>
</div>
</div>
<!-- System Metrics / GitHub Stats -->
<div>
<div class="flex items-center gap-2 px-4 pb-4 pt-4">
<span class="material-symbols-outlined text-secondary">monitoring</span>
<h3 class="text-white text-xl font-bold leading-tight tracking-tight font-mono text-transparent bg-clip-text bg-gradient-to-r from-secondary to-primary">
                                &gt; SYSTEM_METRICS_LOG
                            </h3>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 p-4">
<!-- Stats Card 1 -->
<div class="rounded-xl border border-slate-700 bg-[#0b1120] p-0 overflow-hidden relative group">
<div class="bg-slate-800/50 px-4 py-2 border-b border-slate-700 flex justify-between items-center">
<span class="text-xs font-mono text-slate-400">root@github:~/contributions</span>
<div class="flex gap-1.5">
<div class="w-2.5 h-2.5 rounded-full bg-red-500/50"></div>
<div class="w-2.5 h-2.5 rounded-full bg-yellow-500/50"></div>
<div class="w-2.5 h-2.5 rounded-full bg-green-500/50"></div>
</div>
</div>
<div class="p-6 relative">
<div class="absolute top-0 right-0 p-4 opacity-10">
<span class="material-symbols-outlined text-6xl">commit</span>
</div>
<div class="flex justify-between items-end mb-6">
<div>
<p class="text-slate-400 text-xs font-mono mb-1">TOTAL_CONTRIBUTIONS</p>
<h4 class="text-3xl font-black text-white tracking-tight">1,337</h4>
</div>
<div class="text-right">
<p class="text-green-400 text-xs font-mono mb-1 flex items-center justify-end gap-1">
<span class="material-symbols-outlined text-sm">arrow_upward</span> +12%
                                            </p>
<span class="text-slate-600 text-[10px] font-mono">VS LAST MONTH</span>
</div>
</div>
<!-- Fake Graph -->
<div class="h-16 flex items-end gap-1 justify-between">
<div class="w-full bg-slate-800 rounded-sm h-[40%] group-hover:bg-primary/40 transition-colors duration-500"></div>
<div class="w-full bg-slate-800 rounded-sm h-[60%] group-hover:bg-primary/60 transition-colors duration-500 delay-75"></div>
<div class="w-full bg-slate-800 rounded-sm h-[30%] group-hover:bg-primary/30 transition-colors duration-500 delay-100"></div>
<div class="w-full bg-slate-800 rounded-sm h-[80%] group-hover:bg-primary/80 transition-colors duration-500 delay-150"></div>
<div class="w-full bg-slate-800 rounded-sm h-[55%] group-hover:bg-primary/50 transition-colors duration-500 delay-200"></div>
<div class="w-full bg-slate-800 rounded-sm h-[90%] group-hover:bg-primary/90 transition-colors duration-500 delay-300"></div>
<div class="w-full bg-primary rounded-sm h-[75%] shadow-[0_0_10px_rgba(6,182,212,0.5)]"></div>
</div>
</div>
</div>
<!-- Stats Card 2 -->
<div class="rounded-xl border border-slate-700 bg-[#0b1120] p-0 overflow-hidden relative group">
<div class="bg-slate-800/50 px-4 py-2 border-b border-slate-700 flex justify-between items-center">
<span class="text-xs font-mono text-slate-400">root@github:~/repositories</span>
<span class="material-symbols-outlined text-slate-500 text-sm">more_horiz</span>
</div>
<div class="p-6 grid grid-cols-2 gap-4">
<div class="space-y-1">
<p class="text-slate-400 text-xs font-mono">STARS_EARNED</p>
<p class="text-2xl font-bold text-secondary neon-text">4.2k</p>
</div>
<div class="space-y-1">
<p class="text-slate-400 text-xs font-mono">PULL_REQUESTS</p>
<p class="text-2xl font-bold text-white">245</p>
</div>
<div class="space-y-1">
<p class="text-slate-400 text-xs font-mono">ISSUES_CLOSED</p>
<p class="text-2xl font-bold text-white">892</p>
</div>
<div class="space-y-1">
<p class="text-slate-400 text-xs font-mono">CURRENT_STREAK</p>
<p class="text-2xl font-bold text-primary">42 <span class="text-sm font-normal text-slate-500">DAYS</span></p>
</div>
</div>
<div class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-secondary via-primary to-transparent"></div>
</div>
</div>
<!-- Top Projects Terminal -->
<div class="mx-4 mt-2 rounded-xl border border-slate-700 bg-[#0b1120] overflow-hidden font-mono text-sm shadow-2xl">
<div class="bg-slate-900 px-4 py-2 border-b border-slate-700 flex gap-2 items-center">
<div class="w-3 h-3 rounded-full bg-red-500"></div>
<div class="w-3 h-3 rounded-full bg-yellow-500"></div>
<div class="w-3 h-3 rounded-full bg-green-500"></div>
<span class="ml-2 text-slate-400 text-xs">~/projects/featured</span>
</div>
<div class="p-4 space-y-3">
<div class="flex flex-col md:flex-row md:items-center gap-2 hover:bg-white/5 p-2 rounded transition-colors cursor-pointer group">
<span class="text-green-500 shrink-0">➜</span>
<span class="text-secondary font-bold shrink-0">cyber_dashboard</span>
<span class="hidden md:inline text-slate-600">-</span>
<span class="text-slate-400 truncate">NextJS admin template with real-time websocket data</span>
<div class="ml-auto flex items-center gap-4 text-xs">
<span class="flex items-center gap-1 text-yellow-400"><span class="w-2 h-2 rounded-full bg-yellow-400"></span>JS</span>
<span class="flex items-center gap-1 text-slate-500"><span class="material-symbols-outlined text-[14px]">star</span> 124</span>
</div>
</div>
<div class="flex flex-col md:flex-row md:items-center gap-2 hover:bg-white/5 p-2 rounded transition-colors cursor-pointer group">
<span class="text-green-500 shrink-0">➜</span>
<span class="text-primary font-bold shrink-0">neural_net_v2</span>
<span class="hidden md:inline text-slate-600">-</span>
<span class="text-slate-400 truncate">Python lightweight ML library for edge devices</span>
<div class="ml-auto flex items-center gap-4 text-xs">
<span class="flex items-center gap-1 text-blue-400"><span class="w-2 h-2 rounded-full bg-blue-400"></span>PY</span>
<span class="flex items-center gap-1 text-slate-500"><span class="material-symbols-outlined text-[14px]">star</span> 89</span>
</div>
</div>
<div class="flex flex-col md:flex-row md:items-center gap-2 hover:bg-white/5 p-2 rounded transition-colors cursor-pointer group">
<span class="text-green-500 shrink-0">➜</span>
<span class="text-purple-500 font-bold shrink-0">crypto_bot</span>
<span class="hidden md:inline text-slate-600">-</span>
<span class="text-slate-400 truncate">Automated trading bot using Rust and Binance API</span>
<div class="ml-auto flex items-center gap-4 text-xs">
<span class="flex items-center gap-1 text-orange-400"><span class="w-2 h-2 rounded-full bg-orange-400"></span>RS</span>
<span class="flex items-center gap-1 text-slate-500"><span class="material-symbols-outlined text-[14px]">star</span> 256</span>
</div>
</div>
<div class="pt-2 pl-6 animate-pulse text-primary">
<span class="inline-block w-2 h-4 bg-primary align-middle"></span>
</div>
</div>
</div>
</div>
<!-- Footer / Command Line -->
<div class="px-4 pb-8 pt-4 text-center">
<div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-slate-800/50 border border-slate-700 text-xs text-slate-400 font-mono">
<span>Type 'help' for more commands</span>
<span class="w-1.5 h-1.5 rounded-full bg-slate-500 animate-pulse"></span>
</div>
</div>
</div>
</div>
</div>
</div>
</body></html>
