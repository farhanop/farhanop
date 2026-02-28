<!DOCTYPE html>
<html class="dark" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Farhan - Cyberpunk Portfolio</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
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
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: #0f172a; }
        ::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #475569; }
        
        .neon-text { text-shadow: 0 0 5px rgba(6, 182, 212, 0.5), 0 0 10px rgba(6, 182, 212, 0.3); }
        .neon-border { box-shadow: 0 0 5px rgba(6, 182, 212, 0.2), inset 0 0 5px rgba(6, 182, 212, 0.1); }
        .neon-border-secondary { box-shadow: 0 0 5px rgba(217, 70, 239, 0.2), inset 0 0 5px rgba(217, 70, 239, 0.1); border-color: rgba(217, 70, 239, 0.5); }
        
        .glitch-effect { position: relative; }
        .glitch-effect::before,
        .glitch-effect::after {
            content: attr(data-text);
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
        }
        .glitch-effect::before {
            left: 2px; text-shadow: -1px 0 #d946ef;
            clip: rect(44px, 450px, 56px, 0);
            animation: glitch-anim 5s infinite linear alternate-reverse;
        }
        .glitch-effect::after {
            left: -2px; text-shadow: -1px 0 #06b6d4;
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
                            <h1 class="text-white text-5xl md:text-6xl font-black leading-tight tracking-tighter glitch-effect uppercase" data-text="FARHAN_OP">
                                FARHAN_OP
                            </h1>
                            <p class="text-primary text-lg md:text-xl font-medium leading-normal font-mono mt-2">
                                <span class="text-slate-500">&lt;</span> PASSIONATE_DEVELOPER <span class="text-slate-500">/&gt;</span>
                                <span class="text-slate-600 mx-2">|</span>
                                <span class="text-secondary">CRAFTING_AWESOME_PROJECTS</span>
                            </p>
                            
                            <!-- Social Media Links (Adapted for Cyberpunk) -->
                            <div class="flex flex-wrap gap-3 mt-4">
                                <a href="https://www.facebook.com/farhanop/" target="_blank" class="px-3 py-1.5 border border-blue-500/50 text-blue-400 font-mono text-xs rounded hover:bg-blue-500/10 hover:shadow-[0_0_10px_rgba(59,130,246,0.3)] transition-all">FACEBOOK</a>
                                <a href="https://www.instagram.com/parhanop07/" target="_blank" class="px-3 py-1.5 border border-pink-500/50 text-pink-400 font-mono text-xs rounded hover:bg-pink-500/10 hover:shadow-[0_0_10px_rgba(236,72,153,0.3)] transition-all">INSTAGRAM</a>
                                <a href="https://www.linkedin.com/in/parhan-oktaria-putra-60b647247/" target="_blank" class="px-3 py-1.5 border border-cyan-500/50 text-cyan-400 font-mono text-xs rounded hover:bg-cyan-500/10 hover:shadow-[0_0_10px_rgba(6,182,212,0.3)] transition-all">LINKEDIN</a>
                                <a href="mailto:farhanop2@gmail.com" class="px-3 py-1.5 border border-red-500/50 text-red-400 font-mono text-xs rounded hover:bg-red-500/10 hover:shadow-[0_0_10px_rgba(239,68,68,0.3)] transition-all">EMAIL</a>
                            </div>
                        </div>
                        <div class="flex flex-col items-end gap-2 text-right">
                            <div class="h-16 w-16 md:h-24 md:w-24 rounded-full border-2 border-primary/50 overflow-hidden relative shadow-[0_0_15px_rgba(6,182,212,0.4)]">
                                <!-- Mengambil avatar langsung dari GitHub Anda -->
                                <img alt="Cyberpunk avatar profile picture" class="object-cover w-full h-full filter saturate-50 contrast-125 hover:saturate-100 transition-all duration-300" src="https://github.com/farhanop.png"/>
                            </div>
                            <!-- View Count SVG terintegrasi -->
                            <div class="mt-2">
                                <img src="https://visitcount.itsvg.in/api?id=farhanop&icon=0&color=6" alt="Profile Views" class="opacity-80">
                            </div>
                        </div>
                    </div>

                    <!-- Status Bar -->
                    <div class="flex flex-wrap gap-4 p-4 bg-black/40 border-y border-slate-800 font-mono text-xs md:text-sm text-slate-400 justify-between items-center">
                        <div class="flex gap-6">
                            <span class="flex items-center gap-2"><span class="material-symbols-outlined text-green-500 text-[16px]">wifi</span> STATUS: ONLINE</span>
                            <span class="flex items-center gap-2"><span class="material-symbols-outlined text-primary text-[16px]">terminal</span> STACK: FULLSTACK</span>
                            <span class="hidden md:flex items-center gap-2"><span class="material-symbols-outlined text-secondary text-[16px]">location_on</span> LOCATION: INDONESIA</span>
                        </div>
                        <div class="text-slate-600">UPTIME: 99.9%</div>
                    </div>

                    <!-- GitHub Stats Section -->
                    <div>
                        <div class="flex items-center gap-2 px-4 pb-4 pt-4">
                            <span class="material-symbols-outlined text-secondary">monitoring</span>
                            <h3 class="text-white text-xl font-bold leading-tight tracking-tight font-mono text-transparent bg-clip-text bg-gradient-to-r from-secondary to-primary">
                                &gt; GITHUB_METRICS.LOG
                            </h3>
                        </div>
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 p-4">
                            <!-- GitHub Readme Stats API - disesuaikan dengan tema gelap -->
                            <div class="rounded-xl border border-slate-700 bg-[#0b1120] p-4 overflow-hidden relative group hover:border-primary/50 transition-colors">
                                <img src="https://github-readme-stats.vercel.app/api?username=farhanop&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true" alt="GitHub Stats" class="w-full h-auto" />
                            </div>
                            <div class="rounded-xl border border-slate-700 bg-[#0b1120] p-4 overflow-hidden relative group hover:border-secondary/50 transition-colors">
                                <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=farhanop&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&layout=compact" alt="Top Languages" class="w-full h-auto" />
                            </div>
                            <!-- Streak Stats -->
                            <div class="rounded-xl border border-slate-700 bg-[#0b1120] p-4 overflow-hidden relative group hover:border-accent/50 transition-colors lg:col-span-2">
                                <img src="https://nirzak-streak-stats.vercel.app/?user=farhanop&theme=tokyonight&hide_border=true" alt="GitHub Streak" class="w-full h-auto max-w-2xl mx-auto" />
                            </div>
                        </div>
                    </div>

                    <!-- Tech Stack Section (Simplified from your README) -->
                    <div>
                        <div class="flex items-center gap-2 px-4 pb-4 pt-4">
                            <span class="material-symbols-outlined text-primary">terminal</span>
                            <h3 class="text-white text-xl font-bold leading-tight tracking-tight font-mono text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary">
                                &gt; INITIALIZE_TECH_STACK.EXE
                            </h3>
                        </div>
                        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 p-4">
                            <div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-yellow-400/50 hover:shadow-[0_0_15px_rgba(250,204,21,0.15)] transition-all">
                                <div class="text-yellow-400 group-hover:scale-110 transform duration-300"><span class="material-symbols-outlined text-[40px]">javascript</span></div>
                                <h2 class="text-slate-300 text-sm font-bold font-mono">JS / TS</h2>
                            </div>
                            <div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-blue-400/50 hover:shadow-[0_0_15px_rgba(96,165,250,0.15)] transition-all">
                                <div class="text-blue-400 group-hover:scale-110 transform duration-300"><span class="material-symbols-outlined text-[40px]">code_blocks</span></div>
                                <h2 class="text-slate-300 text-sm font-bold font-mono">React & Nuxt</h2>
                            </div>
                            <div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-red-500/50 hover:shadow-[0_0_15px_rgba(239,68,68,0.15)] transition-all">
                                <div class="text-red-500 group-hover:scale-110 transform duration-300"><span class="material-symbols-outlined text-[40px]">php</span></div>
                                <h2 class="text-slate-300 text-sm font-bold font-mono">PHP / Laravel</h2>
                            </div>
                            <div class="group flex flex-col gap-3 rounded-lg border border-slate-800 bg-surface-dark p-4 items-center hover:border-orange-500/50 hover:shadow-[0_0_15px_rgba(249,115,22,0.15)] transition-all">
                                <div class="text-orange-500 group-hover:scale-110 transform duration-300"><span class="material-symbols-outlined text-[40px]">database</span></div>
                                <h2 class="text-slate-300 text-sm font-bold font-mono">SQL & Firebase</h2>
                            </div>
                        </div>
                    </div>

                    <!-- Footer / Command Line -->
                    <div class="px-4 pb-8 pt-4 text-center">
                        <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-slate-800/50 border border-slate-700 text-xs text-slate-400 font-mono">
                            <span>root@farhanop:~# echo "Ready to collaborate!"</span>
                            <span class="w-2 h-4 bg-slate-500 animate-pulse inline-block"></span>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</body>
</html>
