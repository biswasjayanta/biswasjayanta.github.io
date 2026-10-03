import json

with open('portfolio_data.json') as f:
    data = json.load(f)

profile = data['Profile'][0]
publications = data['Publications']
presentations = data['Presentations']
repositories = data['Repositories']

# Pre-render publications HTML
pub_cards = []
for p in publications:
    # Highlight Jayanta Biswas in authors
    authors_formatted = []
    for a in p['authors']:
        if 'Jayanta Biswas' in a or 'Biswas, J' in a or 'J. Biswas' in a:
            authors_formatted.append(f"<span class='font-semibold text-emerald-600 dark:text-emerald-400'>{a}</span>")
        else:
            authors_formatted.append(f"<span>{a}</span>")
    authors_str = ", ".join(authors_formatted)
    
    tags_html = "".join([f"<span class='text-xs px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-medium'>{t}</span>" for t in p.get('tags', [])[:5]])
    
    action_buttons = []
    
    is_tech_report = p.get('publication_type') == 'Technical Report'
    
    if is_tech_report:
        type_badge = f"<span class='inline-flex items-center gap-1 text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-blue-100 dark:bg-blue-950/70 text-blue-800 dark:text-blue-300'><i class='fa-solid fa-file-lines text-xs'></i> Technical Report &middot; {p.get('report_number', 'RES2024-02')}</span>"
        link_url = p.get('url', 'https://rosap.ntl.bts.gov/view/dot/92824')
        action_buttons.append(f"""<a href='{link_url}' target='_blank' rel='noopener' class='inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-lg bg-blue-50 hover:bg-blue-100 dark:bg-blue-950/50 dark:hover:bg-blue-900/60 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800 transition'>
            <i class='fa-solid fa-landmark text-xs'></i> USDOT / NTL Report
        </a>""")
        if p.get('pdf_url'):
            action_buttons.append(f"""<a href='{p['pdf_url']}' target='_blank' rel='noopener' class='inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 dark:bg-emerald-950/40 dark:hover:bg-emerald-900/60 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 transition'>
                <i class='fa-solid fa-file-pdf text-xs text-rose-500'></i> Download PDF (5.3 MB)
            </a>""")
    else:
        type_badge = f"<span class='text-xs font-medium text-slate-500 dark:text-slate-400 italic'>{p['journal']}</span>"
        link_url = p.get('doi_url', '#')
        action_buttons.append(f"""<a href='{p['doi_url']}' target='_blank' rel='noopener' class='inline-flex items-center gap-1.5 text-xs font-medium px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 dark:bg-emerald-950/40 dark:hover:bg-emerald-900/60 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 transition'>
            <i class='fa-solid fa-arrow-up-right-from-square text-xs'></i> DOI: {p.get('doi', '')}
        </a>""")
        if p.get('related_repository'):
            repo_name = p['related_repository'].split('/')[-1]
            action_buttons.append(f"""<a href='{p['related_repository']}' target='_blank' rel='noopener' class='inline-flex items-center gap-1.5 text-xs font-medium px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-emerald-50 dark:bg-slate-800 dark:hover:bg-emerald-950/40 text-slate-700 dark:text-slate-200 hover:text-emerald-600 dark:hover:text-emerald-400 border border-slate-200 dark:border-slate-700 transition'>
                <i class='fa-brands fa-github text-sm'></i> Code: {repo_name}
            </a>""")

    if p.get('scholar_url'):
        action_buttons.append(f"""<a href='{p['scholar_url']}' target='_blank' rel='noopener' class='inline-flex items-center gap-1.5 text-xs font-medium px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-blue-50 dark:bg-slate-800 dark:hover:bg-blue-950/40 text-slate-700 dark:text-slate-200 hover:text-blue-600 dark:hover:text-blue-400 border border-slate-200 dark:border-slate-700 transition'>
            <i class='fa-brands fa-google-scholar text-sm text-blue-500'></i> Scholar
        </a>""")

    category_tag = "first-author" if "Jayanta Biswas" == p.get('lead_author') else "collaborative"
    pub_type_cat = "tech-report" if is_tech_report else "journal"
    
    pub_card = f"""
    <div class='pub-card group p-6 rounded-2xl bg-white dark:bg-slate-900/90 border border-slate-200/80 dark:border-slate-800 shadow-sm hover:shadow-md transition-all duration-200' data-year='{p['year']}' data-category='{category_tag}' data-type='{pub_type_cat}' data-title='{p['title'].lower()}' data-tags='{" ".join(p.get("tags", [])).lower()}'>
        <div class='flex flex-wrap items-center justify-between gap-2 mb-3'>
            <span class='inline-flex items-center gap-1.5 text-xs font-semibold px-2.5 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300'>
                <i class='fa-regular fa-calendar'></i> {p['year']}
            </span>
            {type_badge}
        </div>
        <h3 class='text-lg font-bold text-slate-900 dark:text-white leading-snug mb-2 group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors'>
            <a href='{link_url}' target='_blank' rel='noopener'>{p['title']}</a>
        </h3>
        <p class='text-sm text-slate-600 dark:text-slate-300 mb-4 leading-relaxed'>
            {authors_str}
        </p>
        <p class='text-sm text-slate-500 dark:text-slate-400 mb-4 line-clamp-3 group-hover:line-clamp-none transition-all'>
            {p['abstract']}
        </p>
        <div class='flex flex-wrap gap-2 mb-4'>
            {tags_html}
        </div>
        <div class='flex flex-wrap items-center gap-2 pt-3 border-t border-slate-100 dark:border-slate-800/80'>
            {" ".join(action_buttons)}
        </div>
    </div>
    """
    pub_cards.append(pub_card)

# Pre-render presentations HTML
pres_cards = []
for pr in presentations:
    award_badge = ""
    if pr.get('awards'):
        award_badge = f"""<div class='mb-2 inline-flex items-center gap-1.5 text-xs font-bold px-3 py-1 rounded-full bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-700/60'>
            <i class='fa-solid fa-trophy text-amber-500'></i> {pr['awards'][0]}
        </div>"""
    
    repo_links = ""
    if pr.get('related_repositories'):
        links = []
        for rurl in pr['related_repositories']:
            rname = rurl.split('/')[-1]
            links.append(f"<a href='{rurl}' target='_blank' rel='noopener' class='text-xs font-medium text-emerald-600 dark:text-emerald-400 hover:underline'><i class='fa-brands fa-github'></i> {rname}</a>")
        repo_links = "<div class='flex flex-wrap gap-3 mt-3 pt-3 border-t border-slate-100 dark:border-slate-800'>" + " ".join(links) + "</div>"
    elif pr.get('related_publication'):
        repo_links = f"""<div class='mt-3 pt-3 border-t border-slate-100 dark:border-slate-800 flex flex-wrap gap-3'>
            <a href='{pr['related_publication']}' target='_blank' rel='noopener' class='text-xs font-medium text-emerald-600 dark:text-emerald-400 hover:underline'><i class='fa-solid fa-book-open'></i> Related Publication (Land 2025)</a>
            <a href='https://rosap.ntl.bts.gov/view/dot/92824' target='_blank' rel='noopener' class='text-xs font-medium text-blue-600 dark:text-blue-400 hover:underline'><i class='fa-solid fa-landmark'></i> USDOT / NTL Report</a>
        </div>"""

    pres_card = f"""
    <div class='p-6 rounded-2xl bg-white dark:bg-slate-900/90 border border-slate-200/80 dark:border-slate-800 shadow-sm hover:shadow-md transition'>
        {award_badge}
        <div class='flex items-center justify-between gap-2 mb-2'>
            <span class='text-xs font-semibold px-2.5 py-0.5 rounded-full bg-blue-50 dark:bg-blue-950/50 text-blue-700 dark:text-blue-300'>
                {pr.get('date', pr.get('year', ''))}
            </span>
            <span class='text-xs font-medium text-slate-500 dark:text-slate-400'>
                <i class='fa-solid fa-location-dot text-slate-400 mr-1'></i> {pr['location']}
            </span>
        </div>
        <h3 class='text-base font-bold text-slate-900 dark:text-white mb-2 leading-snug'>
            {pr['title']}
        </h3>
        <p class='text-sm text-slate-600 dark:text-slate-300 font-medium mb-1'>
            {pr['conference']}
        </p>
        <p class='text-xs text-slate-500 dark:text-slate-400 mb-3'>
            {", ".join(pr['authors'])}
        </p>
        <p class='text-xs text-slate-600 dark:text-slate-300 leading-relaxed'>
            {pr['abstract']}
        </p>
        {repo_links}
    </div>
    """
    pres_cards.append(pres_card)

# Pre-render repositories HTML
repo_cards = []
categories = sorted(list(set([r['category'] for r in repositories])))
for r in repositories:
    lang_color = {
        'Python': 'bg-blue-500',
        'Jupyter Notebook': 'bg-orange-500',
        'HTML': 'bg-red-500',
        'JavaScript': 'bg-yellow-400',
        'R': 'bg-blue-600',
        'C++': 'bg-pink-600'
    }.get(r['primary_language'], 'bg-slate-400')
    
    feat_badge = "<span class='text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300'>Featured</span>" if r.get('is_featured') else ""

    repo_card = f"""
    <div class='repo-card group p-5 rounded-2xl bg-white dark:bg-slate-900/90 border border-slate-200/80 dark:border-slate-800 shadow-sm hover:shadow-md transition flex flex-col justify-between' data-category='{r['category']}' data-name='{r['name'].lower()}'>
        <div>
            <div class='flex items-center justify-between gap-2 mb-2.5'>
                <div class='flex items-center gap-1.5'>
                    <i class='fa-regular fa-folder text-emerald-500'></i>
                    <span class='text-xs text-slate-400 dark:text-slate-500'>{r['category']}</span>
                </div>
                {feat_badge}
            </div>
            <h4 class='text-base font-bold text-slate-900 dark:text-white mb-2 group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors'>
                <a href='{r['url']}' target='_blank' rel='noopener' class='inline-flex items-center gap-1.5'>
                    {r['name']} <i class='fa-solid fa-arrow-up-right-from-square text-xs opacity-0 group-hover:opacity-100 transition'></i>
                </a>
            </h4>
            <p class='text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4'>
                {r['description'] if r['description'] else 'Geospatial workflows, scripts, and analytical code.'}
            </p>
        </div>
        <div class='flex items-center justify-between pt-3 border-t border-slate-100 dark:border-slate-800/80 text-xs text-slate-500 dark:text-slate-400'>
            <div class='flex items-center gap-2'>
                <span class='w-2.5 h-2.5 rounded-full {lang_color}'></span>
                <span>{r['primary_language'] if r['primary_language'] else 'Data / GIS'}</span>
            </div>
            <a href='{r['url']}' target='_blank' rel='noopener' class='hover:text-emerald-600 dark:hover:text-emerald-400 font-medium'>
                GitHub &rarr;
            </a>
        </div>
    </div>
    """
    repo_cards.append(repo_card)

# Pre-render categories buttons for repos
cat_buttons = ["<button class='repo-filter-btn active px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 text-white shadow-sm transition' data-cat='all'>All (20)</button>"]
for cat in categories:
    count = sum(1 for r in repositories if r['category'] == cat)
    cat_buttons.append(f"<button class='repo-filter-btn px-3.5 py-1.5 rounded-lg text-xs font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition' data-cat='{cat}'>{cat} ({count})</button>")

# Full HTML template
html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jayanta Biswas | PhD Student in Geography | GeoAI & Health Geography</title>
    <meta name="description" content="Official academic portfolio of Jayanta Biswas, PhD student in Geography at UNC Charlotte. Research in GeoAI, deep learning downscaling, remote sensing, and spatial epidemiology.">
    <link rel="canonical" href="https://biswasjayanta.github.io/">

    <!-- Open Graph / Meta -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://biswasjayanta.github.io/">
    <meta property="og:title" content="Jayanta Biswas | PhD Student in Geography | GeoAI & Health Geography">
    <meta property="og:description" content="GeoAI downscaling of human mobility, mass-conserving deep learning, and multi-source remote sensing at UNC Charlotte GeoHDR Lab.">
    <meta property="og:image" content="https://biswasjayanta.github.io/assest/img/profile_1.png">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"Fira Code"', 'monospace'],
                    }},
                    colors: {{
                        emerald: {{
                            50: '#ecfdf5',
                            100: '#d1fae5',
                            200: '#a7f3d0',
                            300: '#6ee7b7',
                            400: '#34d399',
                            500: '#10b981',
                            600: '#059669',
                            700: '#047857',
                            800: '#065f46',
                            900: '#064e3b',
                            950: '#022c22',
                        }}
                    }}
                }}
            }}
        }}
    </script>

    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <style>
        ::selection {{
            background-color: #10b981;
            color: #ffffff;
        }}
        .glass-header {{
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }}
    </style>
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-100 transition-colors duration-300 font-sans antialiased min-h-screen flex flex-col">

    <!-- Sticky Navigation Header -->
    <header class="sticky top-0 z-50 w-full border-b border-slate-200/80 dark:border-slate-800/80 bg-white/80 dark:bg-slate-950/80 glass-header">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <a href="#hero" class="flex items-center gap-3 group">
                <div class="relative">
                    <img src="assest/img/profile_1.png" alt="Jayanta Biswas" class="w-9 h-9 rounded-full object-cover border border-emerald-500/40">
                    <span class="absolute -bottom-0.5 -right-0.5 w-2.5 h-2.5 bg-emerald-500 border-2 border-white dark:border-slate-950 rounded-full"></span>
                </div>
                <div>
                    <span class="font-bold text-slate-900 dark:text-white tracking-tight group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition">Jayanta Biswas</span>
                    <span class="hidden sm:inline-block ml-1.5 text-xs text-emerald-600 dark:text-emerald-400 font-medium">| UNC Charlotte</span>
                </div>
            </a>

            <!-- Desktop Nav Links -->
            <nav class="hidden md:flex items-center gap-6 text-sm font-medium text-slate-600 dark:text-slate-300">
                <a href="#about" class="hover:text-emerald-600 dark:hover:text-emerald-400 transition">About</a>
                <a href="#projects" class="hover:text-emerald-600 dark:hover:text-emerald-400 transition">Projects</a>
                <a href="#publications" class="hover:text-emerald-600 dark:hover:text-emerald-400 transition">Publications</a>
                <a href="#presentations" class="hover:text-emerald-600 dark:hover:text-emerald-400 transition">Presentations</a>
                <a href="#repositories" class="hover:text-emerald-600 dark:hover:text-emerald-400 transition">Repositories</a>
                <a href="#experience" class="hover:text-emerald-600 dark:hover:text-emerald-400 transition">Experience</a>
                <a href="#skills" class="hover:text-emerald-600 dark:hover:text-emerald-400 transition">Skills</a>
                <a href="#contact" class="hover:text-emerald-600 dark:hover:text-emerald-400 transition">Contact</a>
            </nav>

            <div class="flex items-center gap-3">
                <!-- GeoViz Archive Dropdown Link -->
                <div class="relative group hidden lg:block">
                    <button class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition">
                        <i class="fa-solid fa-map-location-dot text-emerald-500"></i> GeoViz Labs
                        <i class="fa-solid fa-chevron-down text-[10px]"></i>
                    </button>
                    <div class="absolute right-0 mt-1 w-56 rounded-xl bg-white dark:bg-slate-900 shadow-xl border border-slate-200 dark:border-slate-800 p-2 hidden group-hover:block transition-all z-50">
                        <a href="GeoVisualization_Portfolio.html" class="block px-3 py-2 text-xs rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-200">
                            <i class="fa-solid fa-layer-group text-emerald-500 mr-1.5"></i> GeoVisualization Portfolio
                        </a>
                        <a href="GeoViz_Showcase.html" class="block px-3 py-2 text-xs rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-200">
                            <i class="fa-solid fa-compass-drafting text-blue-500 mr-1.5"></i> GeoViz Showcase
                        </a>
                    </div>
                </div>

                <!-- Dark / Light Mode Toggle -->
                <button id="theme-toggle" type="button" aria-label="Toggle Dark Mode" class="w-9 h-9 flex items-center justify-center rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition">
                    <i id="theme-icon" class="fa-solid fa-moon"></i>
                </button>

                <!-- Mobile Menu Button -->
                <button id="mobile-menu-btn" type="button" aria-label="Open Mobile Menu" class="md:hidden w-9 h-9 flex items-center justify-center rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200">
                    <i class="fa-solid fa-bars"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Drawer -->
        <div id="mobile-menu" class="hidden md:hidden border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-950 px-4 pt-3 pb-5 space-y-2">
            <a href="#about" class="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-slate-100 dark:hover:bg-slate-800">About</a>
            <a href="#projects" class="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-slate-100 dark:hover:bg-slate-800">Projects</a>
            <a href="#publications" class="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-slate-100 dark:hover:bg-slate-800">Publications</a>
            <a href="#presentations" class="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-slate-100 dark:hover:bg-slate-800">Presentations</a>
            <a href="#repositories" class="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-slate-100 dark:hover:bg-slate-800">Repositories</a>
            <a href="#experience" class="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-slate-100 dark:hover:bg-slate-800">Experience</a>
            <a href="#skills" class="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-slate-100 dark:hover:bg-slate-800">Skills</a>
            <a href="#contact" class="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-slate-100 dark:hover:bg-slate-800">Contact</a>
            <div class="pt-2 border-t border-slate-200 dark:border-slate-800">
                <a href="GeoVisualization_Portfolio.html" class="block px-3 py-2 rounded-lg text-xs font-semibold text-emerald-600 dark:text-emerald-400">
                    <i class="fa-solid fa-map-location-dot mr-1.5"></i> GeoVisualization Portfolio Lab
                </a>
            </div>
        </div>
    </header>

    <main class="flex-grow">
        <!-- Hero Section -->
        <section id="hero" class="relative overflow-hidden py-16 sm:py-24 bg-gradient-to-b from-emerald-50/40 via-transparent to-transparent dark:from-emerald-950/20 dark:via-transparent dark:to-transparent">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                    
                    <!-- Left: Profile Info -->
                    <div class="lg:col-span-8 text-center lg:text-left">
                        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-100/80 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300 text-xs font-semibold mb-6 border border-emerald-300/40 dark:border-emerald-700/40">
                            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                            PhD Student in Geography &middot; UNC Charlotte
                        </div>

                        <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-slate-900 dark:text-white tracking-tight leading-tight mb-4">
                            Jayanta Biswas
                        </h1>

                        <p class="text-lg sm:text-xl font-medium text-slate-700 dark:text-slate-300 mb-4 leading-relaxed">
                            Spatial Geographer &amp; GeoAI Researcher bridging <span class="text-emerald-600 dark:text-emerald-400 font-semibold">knowledge-guided deep learning</span>, <span class="text-emerald-600 dark:text-emerald-400 font-semibold">human mobility downscaling</span>, and <span class="text-emerald-600 dark:text-emerald-400 font-semibold">spatial epidemiology</span>.
                        </p>

                        <div class="text-sm text-slate-600 dark:text-slate-400 mb-8 space-y-1">
                            <p><i class="fa-solid fa-graduation-cap text-emerald-500 mr-2"></i><strong>GeoHealth Dynamics Research (GeoHDR) Lab</strong> &amp; <strong>CAGIS</strong>, UNC Charlotte</p>
                            <p><i class="fa-solid fa-user-doctor text-emerald-500 mr-2"></i>Advisor: <strong>Dr. Yao Li</strong> &middot; NSF Award #2451156</p>
                            <p><i class="fa-solid fa-location-dot text-emerald-500 mr-2"></i>McEniry Building, Charlotte, NC, USA</p>
                        </div>

                        <!-- CTA Action Buttons -->
                        <div class="flex flex-wrap items-center justify-center lg:justify-start gap-3 mb-8">
                            <a href="#publications" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-semibold text-sm bg-emerald-600 hover:bg-emerald-700 text-white shadow-md shadow-emerald-500/20 transition-all">
                                <i class="fa-solid fa-book-bookmark"></i> View Publications &amp; Reports
                            </a>
                            <a href="#repositories" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-semibold text-sm bg-slate-900 hover:bg-slate-800 dark:bg-slate-800 dark:hover:bg-slate-700 text-white transition-all">
                                <i class="fa-brands fa-github"></i> Open Code &amp; Repos
                            </a>
                            <a href="portfolio_data.json" download target="_blank" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-semibold text-sm bg-white hover:bg-slate-100 dark:bg-slate-900 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-800 transition-all">
                                <i class="fa-solid fa-code text-emerald-500"></i> Portfolio JSON
                            </a>
                        </div>

                        <!-- Scholarly & Social Badges -->
                        <div class="flex flex-wrap items-center justify-center lg:justify-start gap-2.5 pt-2">
                            <a href="{profile['links']['google_scholar']}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-medium bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-800 hover:border-blue-500 hover:text-blue-600 transition">
                                <i class="fa-brands fa-google-scholar text-blue-500 text-sm"></i>
                                <span>Google Scholar</span>
                                <span class="px-1.5 py-0.5 rounded bg-blue-50 dark:bg-blue-950 text-blue-700 dark:text-blue-300 font-bold text-[10px]">{profile['scholar_metrics']['citations']}+ Cites</span>
                            </a>
                            <a href="{profile['links']['github']}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-medium bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-800 hover:border-slate-900 hover:text-slate-900 dark:hover:text-white transition">
                                <i class="fa-brands fa-github text-sm"></i> GitHub
                            </a>
                            <a href="{profile['links']['linkedin']}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-medium bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-800 hover:border-blue-600 hover:text-blue-600 transition">
                                <i class="fa-brands fa-linkedin text-blue-600 text-sm"></i> LinkedIn
                            </a>
                            <a href="{profile['links']['google_site']}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-medium bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-800 hover:border-amber-500 hover:text-amber-600 transition">
                                <i class="fa-brands fa-google text-amber-500 text-sm"></i> Google Portfolio
                            </a>
                            <a href="mailto:{profile['contact']['email']}" class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-medium bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-800 hover:border-emerald-500 hover:text-emerald-600 transition">
                                <i class="fa-solid fa-envelope text-emerald-500 text-sm"></i> Email
                            </a>
                        </div>
                    </div>

                    <!-- Right: Large Portrait & Card -->
                    <div class="lg:col-span-4 flex flex-col items-center">
                        <div class="relative group">
                            <div class="absolute -inset-1.5 bg-gradient-to-r from-emerald-500 to-teal-500 rounded-3xl blur opacity-30 group-hover:opacity-60 transition duration-300"></div>
                            <div class="relative rounded-3xl overflow-hidden bg-white dark:bg-slate-900 border-2 border-emerald-500/30 p-2 shadow-2xl">
                                <img src="assest/img/profile_1.png" alt="Jayanta Biswas" class="w-64 h-64 sm:w-72 sm:h-72 object-cover rounded-2xl">
                            </div>
                        </div>

                        <!-- Mini Status Card -->
                        <div class="mt-6 w-full max-w-xs bg-white dark:bg-slate-900/90 rounded-2xl border border-slate-200 dark:border-slate-800 p-4 shadow-sm text-center">
                            <div class="flex items-center justify-center gap-2 text-xs font-bold text-slate-900 dark:text-white mb-1">
                                <i class="fa-solid fa-flask-vial text-emerald-500"></i> NSF Award #2451156
                            </div>
                            <p class="text-[11px] text-slate-500 dark:text-slate-400">
                                Downscaling Human Mobility (5.5 km &rarr; 100 m) for Precision Malaria Modeling in Zambia
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Metrics Strip -->
                <div class="mt-14 grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div class="p-5 rounded-2xl bg-white dark:bg-slate-900/80 border border-slate-200/80 dark:border-slate-800 text-center shadow-sm">
                        <div class="text-3xl font-extrabold text-emerald-600 dark:text-emerald-400">172+</div>
                        <div class="text-xs font-medium text-slate-500 dark:text-slate-400 mt-1">Google Scholar Citations</div>
                    </div>
                    <div class="p-5 rounded-2xl bg-white dark:bg-slate-900/80 border border-slate-200/80 dark:border-slate-800 text-center shadow-sm">
                        <div class="text-3xl font-extrabold text-slate-900 dark:text-white">9</div>
                        <div class="text-xs font-medium text-slate-500 dark:text-slate-400 mt-1">Publications &amp; Reports</div>
                    </div>
                    <div class="p-5 rounded-2xl bg-white dark:bg-slate-900/80 border border-slate-200/80 dark:border-slate-800 text-center shadow-sm">
                        <div class="text-3xl font-extrabold text-slate-900 dark:text-white">5</div>
                        <div class="text-xs font-medium text-slate-500 dark:text-slate-400 mt-1">Conference Presentations</div>
                    </div>
                    <div class="p-5 rounded-2xl bg-white dark:bg-slate-900/80 border border-slate-200/80 dark:border-slate-800 text-center shadow-sm">
                        <div class="text-3xl font-extrabold text-emerald-600 dark:text-emerald-400">20</div>
                        <div class="text-xs font-medium text-slate-500 dark:text-slate-400 mt-1">Open-Source Repositories</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section id="about" class="py-16 sm:py-20 border-t border-slate-200/80 dark:border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="max-w-3xl mb-12">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Scholarly Background</span>
                    <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white mt-1">About &amp; Research Focus</h2>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
                    <div class="lg:col-span-7 space-y-4 text-slate-600 dark:text-slate-300 leading-relaxed text-sm sm:text-base">
                        <p>
                            I am a PhD student in Geography and Graduate Research Assistant at the <strong>University of North Carolina at Charlotte</strong>, affiliated with the <strong>GeoHealth Dynamics Research (GeoHDR) Lab</strong> and the <strong>Center for Applied Geographic Information Science (CAGIS)</strong> under the mentorship of <strong>Dr. Yao Li</strong>.
                        </p>
                        <p>
                            My doctoral research focuses on developing <strong>knowledge-guided GeoAI architectures</strong>—specifically U-Net deep ensembles with mass-conserving (pycnophylactic) loss constraints—to downscale Meta human mobility arrays from a coarse ~5.5 km grid to an ultra-fine 100 m resolution across Zambia. This work, funded by <strong>NSF Award #2451156</strong>, integrates 38 covariate layers in Google Earth Engine and mobile-phone Call Detail Records (CDR) to pinpoint <em>Human-Vector Contact Zones (HVCZ)</em> for precision malaria transmission containment.
                        </p>
                        <p>
                            Prior to UNC Charlotte, I completed my <strong>M.Sc. in Earth Sciences at The University of Memphis</strong>, working with Dr. Angela Antipova on a major TDOT/FHWA study evaluating induced travel demand and long-term land development in Tennessee using 2SLS instrumental variable regression. My foundational training includes both Bachelor's and Master's degrees in Urban and Rural Planning from <strong>Khulna University</strong>, Bangladesh.
                        </p>
                    </div>

                    <div class="lg:col-span-5 grid grid-cols-1 gap-4">
                        <div class="p-5 rounded-2xl bg-white dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 shadow-sm">
                            <div class="w-10 h-10 rounded-xl bg-emerald-100 dark:bg-emerald-950 flex items-center justify-center text-emerald-600 dark:text-emerald-400 mb-3">
                                <i class="fa-solid fa-brain"></i>
                            </div>
                            <h3 class="font-bold text-slate-900 dark:text-white text-sm mb-1">GeoAI &amp; Knowledge-Guided Deep Learning</h3>
                            <p class="text-xs text-slate-500 dark:text-slate-400 leading-relaxed">
                                PyTorch U-Net ensembles, pycnophylactic mass-conserving physics loss, spatial block cross-validation, and uncertainty quantification.
                            </p>
                        </div>

                        <div class="p-5 rounded-2xl bg-white dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 shadow-sm">
                            <div class="w-10 h-10 rounded-xl bg-blue-100 dark:bg-blue-950 flex items-center justify-center text-blue-600 dark:text-blue-400 mb-3">
                                <i class="fa-solid fa-satellite"></i>
                            </div>
                            <h3 class="font-bold text-slate-900 dark:text-white text-sm mb-1">Multi-Source Remote Sensing &amp; GEE</h3>
                            <p class="text-xs text-slate-500 dark:text-slate-400 leading-relaxed">
                                Planetary-scale raster processing on Google Earth Engine, Sentinel-2 time series, Landsat, WorldPop, and environmental ecological indexing (RSEI).
                            </p>
                        </div>

                        <div class="p-5 rounded-2xl bg-white dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 shadow-sm">
                            <div class="w-10 h-10 rounded-xl bg-purple-100 dark:bg-purple-950 flex items-center justify-center text-purple-600 dark:text-purple-400 mb-3">
                                <i class="fa-solid fa-shield-virus"></i>
                            </div>
                            <h3 class="font-bold text-slate-900 dark:text-white text-sm mb-1">Spatial Epidemiology &amp; Public Health</h3>
                            <p class="text-xs text-slate-500 dark:text-slate-400 leading-relaxed">
                                Modeling disease vectors, transmission contact zones, and disease vulnerability using population-weighted mobility and Voronoi catchments.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Featured Projects Section -->
        <section id="projects" class="py-16 sm:py-20 bg-slate-100/60 dark:bg-slate-900/40 border-t border-slate-200/80 dark:border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex flex-wrap items-end justify-between gap-4 mb-12">
                    <div>
                        <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Core Initiatives</span>
                        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white mt-1">Featured Research &amp; GeoAI Projects</h2>
                    </div>
                    <span class="text-xs text-slate-500 dark:text-slate-400 font-medium">Mapped directly to open repositories &amp; grants</span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    
                    <!-- Card 1: Zambia Malaria Downscaling -->
                    <div class="group rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
                        <div class="p-6">
                            <div class="flex items-center justify-between gap-2 mb-3">
                                <span class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300">
                                    NSF Award #2451156
                                </span>
                                <span class="text-xs font-semibold text-slate-400">2026</span>
                            </div>
                            <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-2 leading-snug group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition">
                                Fine-Scale Human Mobility Downscaling for Precision Malaria Modeling
                            </h3>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                                Deep ensemble U-Net downscaling Meta mobility from ~5.5 km to 100 m across Zambia using 38 covariate layers, enforcing pycnophylactic mass conservation and benchmarked against mobile Call Detail Records.
                            </p>
                            <div class="flex flex-wrap gap-1.5 mb-4">
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">PyTorch</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Earth Engine</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">U-Net</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Malaria</span>
                            </div>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-950/60 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between">
                            <a href="https://github.com/biswasjayanta/human-mobility-downscaling" target="_blank" rel="noopener" class="text-xs font-semibold text-emerald-600 dark:text-emerald-400 hover:underline">
                                <i class="fa-brands fa-github"></i> Code Repo
                            </a>
                            <a href="https://github.com/biswasjayanta/zambia_mobility" target="_blank" rel="noopener" class="text-xs font-semibold text-slate-600 dark:text-slate-300 hover:underline">
                                <i class="fa-solid fa-map"></i> Web Dashboard
                            </a>
                        </div>
                    </div>

                    <!-- Card 2: 100 Resilient Cities RSEI -->
                    <div class="group rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
                        <div class="p-6">
                            <div class="flex items-center justify-between gap-2 mb-3">
                                <span class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-300">
                                    Environ. Monit. Assess. (2026)
                                </span>
                                <span class="text-xs font-semibold text-slate-400">Lead Author</span>
                            </div>
                            <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-2 leading-snug group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition">
                                Improved Remote Sensing Ecological Index for Urban Sustainability
                            </h3>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                                Evaluated decadal environmental quality across South Asian cities, benchmarking Rockefeller Foundation 100 Resilient Cities (Pune, Surat) against non-resilient cities (Chattogram, Nagpur).
                            </p>
                            <div class="flex flex-wrap gap-1.5 mb-4">
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">R</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">RSEI</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">100RC</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Urban Ecology</span>
                            </div>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-950/60 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between">
                            <a href="https://doi.org/10.1007/s10661-026-15156-w" target="_blank" rel="noopener" class="text-xs font-semibold text-emerald-600 dark:text-emerald-400 hover:underline">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i> Read Article
                            </a>
                            <a href="https://github.com/biswasjayanta/100RCImproved-RSEI" target="_blank" rel="noopener" class="text-xs font-semibold text-slate-600 dark:text-slate-300 hover:underline">
                                <i class="fa-brands fa-github"></i> R Code
                            </a>
                        </div>
                    </div>

                    <!-- Card 3: California Wildfire GeoAI Ensembles -->
                    <div class="group rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
                        <div class="p-6">
                            <div class="flex items-center justify-between gap-2 mb-3">
                                <span class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300">
                                    Geomatica (2025)
                                </span>
                                <span class="text-xs font-semibold text-slate-400">Co-Author</span>
                            </div>
                            <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-2 leading-snug group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition">
                                GeoAI Ensembles for Wildfire Susceptibility Prediction
                            </h3>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                                Comparative assessment of deep learning vs. tree-based machine learning ensembles across California, evaluating computational efficiency and realistic spatial hazard surfaces.
                            </p>
                            <div class="flex flex-wrap gap-1.5 mb-4">
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">GeoAI</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Deep Learning</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Wildfires</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">California</span>
                            </div>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-950/60 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between">
                            <a href="https://doi.org/10.1016/j.geomat.2025.100081" target="_blank" rel="noopener" class="text-xs font-semibold text-emerald-600 dark:text-emerald-400 hover:underline">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i> Read Article
                            </a>
                            <a href="https://github.com/biswasjayanta/Geospatial_Workflows" target="_blank" rel="noopener" class="text-xs font-semibold text-slate-600 dark:text-slate-300 hover:underline">
                                <i class="fa-brands fa-github"></i> Workflows
                            </a>
                        </div>
                    </div>

                    <!-- Card 4: Tennessee Induced Travel & Land Development -->
                    <div class="group rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
                        <div class="p-6">
                            <div class="flex items-center justify-between gap-2 mb-3">
                                <span class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300">
                                    🏆 MAGIC 2025 First Place
                                </span>
                                <span class="text-xs font-semibold text-slate-400">TDOT / FHWA RES2024-02</span>
                            </div>
                            <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-2 leading-snug group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition">
                                Applying Induced Travel Study in Urban Areas in Tennessee
                            </h3>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                                Analyzed multi-decade land growth (1985–2023) and induced VMT elasticity across individual road facilities using 2SLS instrumental variable regression. Published in <em>Land</em> (2025) and official USDOT/NTL Technical Report RES2024-02.
                            </p>
                            <div class="flex flex-wrap gap-1.5 mb-4">
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Spatial Econometrics</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">2SLS</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">TDOT</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">VMT</span>
                            </div>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-950/60 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between gap-2">
                            <a href="https://rosap.ntl.bts.gov/view/dot/92824" target="_blank" rel="noopener" class="text-xs font-semibold text-blue-600 dark:text-blue-400 hover:underline">
                                <i class="fa-solid fa-landmark"></i> USDOT Report
                            </a>
                            <a href="https://doi.org/10.3390/land14051025" target="_blank" rel="noopener" class="text-xs font-semibold text-emerald-600 dark:text-emerald-400 hover:underline">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i> Land Paper
                            </a>
                        </div>
                    </div>

                    <!-- Card 5: Saint Martin Island Tourism Remote Sensing -->
                    <div class="group rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
                        <div class="p-6">
                            <div class="flex items-center justify-between gap-2 mb-3">
                                <span class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-purple-100 dark:bg-purple-950 text-purple-800 dark:text-purple-300">
                                    RSASE (2025)
                                </span>
                                <span class="text-xs font-semibold text-slate-400">Lead Author</span>
                            </div>
                            <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-2 leading-snug group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition">
                                Remote Sensing of Coastal Tourism on Coral Island Ecosystem
                            </h3>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                                Applied multi-temporal Sentinel-2 imagery (2018–2024) to quantify unregulated tourist infrastructure encroachment on Saint Martin Island with 94.6%–98.9% accuracy.
                            </p>
                            <div class="flex flex-wrap gap-1.5 mb-4">
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Sentinel-2</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Classification</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Coastal Ecology</span>
                            </div>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-950/60 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between">
                            <a href="https://doi.org/10.1016/j.rsase.2025.101484" target="_blank" rel="noopener" class="text-xs font-semibold text-emerald-600 dark:text-emerald-400 hover:underline">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i> Read Article
                            </a>
                            <a href="https://github.com/biswasjayanta/TourismRemoteSensing" target="_blank" rel="noopener" class="text-xs font-semibold text-slate-600 dark:text-slate-300 hover:underline">
                                <i class="fa-brands fa-github"></i> Notebook
                            </a>
                        </div>
                    </div>

                    <!-- Card 6: Interactive Web GIS & GeoViz Portfolio -->
                    <div class="group rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
                        <div class="p-6">
                            <div class="flex items-center justify-between gap-2 mb-3">
                                <span class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-teal-100 dark:bg-teal-950 text-teal-800 dark:text-teal-300">
                                    Web GIS Showcase
                                </span>
                                <span class="text-xs font-semibold text-slate-400">Interactive</span>
                            </div>
                            <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-2 leading-snug group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition">
                                Interactive Web GIS &amp; Cartographic Laboratory Showcase
                            </h3>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                                Explores Charlotte land use shifts, elevation terrain analysis in Bangladesh, waterbody dynamics, and complete laboratory visualization assignments.
                            </p>
                            <div class="flex flex-wrap gap-1.5 mb-4">
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Leaflet</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Mapbox</span>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">Cartography</span>
                            </div>
                        </div>
                        <div class="p-4 bg-slate-50 dark:bg-slate-950/60 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between">
                            <a href="GeoVisualization_Portfolio.html" class="text-xs font-semibold text-emerald-600 dark:text-emerald-400 hover:underline">
                                <i class="fa-solid fa-map-location-dot"></i> View GeoViz Lab
                            </a>
                            <a href="GeoViz_Showcase.html" class="text-xs font-semibold text-slate-600 dark:text-slate-300 hover:underline">
                                <i class="fa-solid fa-chart-simple"></i> Showcase
                            </a>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- Publications Section -->
        <section id="publications" class="py-16 sm:py-20 border-t border-slate-200/80 dark:border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex flex-wrap items-end justify-between gap-4 mb-8">
                    <div>
                        <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Scholarly Output</span>
                        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white mt-1">Publications &amp; Technical Reports</h2>
                    </div>
                    <div class="text-xs text-slate-500 dark:text-slate-400">
                        Total Citations: <strong class="text-emerald-600 dark:text-emerald-400">172+</strong> &middot; Google Scholar
                    </div>
                </div>

                <!-- Search and Filters -->
                <div class="mb-8 flex flex-col sm:flex-row gap-3 items-stretch sm:items-center justify-between">
                    <div class="relative flex-1 max-w-md">
                        <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                        <input id="pub-search" type="text" placeholder="Search publications and reports by title, tag, or topic..." class="w-full pl-9 pr-4 py-2 text-xs rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 focus:outline-none focus:border-emerald-500 dark:focus:border-emerald-500 transition">
                    </div>

                    <div class="flex flex-wrap gap-1.5" id="pub-filter-buttons">
                        <button class="pub-filter-btn active px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 text-white transition" data-filter="all">All (9)</button>
                        <button class="pub-filter-btn px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition" data-filter="journal">Journal Articles (8)</button>
                        <button class="pub-filter-btn px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition" data-filter="tech-report">Technical Reports (1)</button>
                        <button class="pub-filter-btn px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition" data-filter="first-author">First-Authored (5)</button>
                    </div>
                </div>

                <!-- Publication Cards Grid -->
                <div class="space-y-4" id="pub-list">
                    {"".join(pub_cards)}
                </div>
            </div>
        </section>

        <!-- Presentations & Posters Section -->
        <section id="presentations" class="py-16 sm:py-20 bg-slate-100/60 dark:bg-slate-900/40 border-t border-slate-200/80 dark:border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="max-w-3xl mb-12">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Academic Dissemination</span>
                    <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white mt-1">Conferences &amp; Presentations</h2>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {"".join(pres_cards)}
                </div>
            </div>
        </section>

        <!-- Repositories Showcase Section -->
        <section id="repositories" class="py-16 sm:py-20 border-t border-slate-200/80 dark:border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex flex-wrap items-end justify-between gap-4 mb-8">
                    <div>
                        <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Open-Source Codebases</span>
                        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white mt-1">GitHub Repositories</h2>
                    </div>
                    <a href="{profile['links']['github']}" target="_blank" rel="noopener" class="text-xs font-semibold text-emerald-600 dark:text-emerald-400 hover:underline">
                        Explore all on GitHub &rarr;
                    </a>
                </div>

                <!-- Repo Category Filter Buttons -->
                <div class="flex flex-wrap gap-2 mb-8" id="repo-filter-container">
                    {" ".join(cat_buttons)}
                </div>

                <!-- Repositories Grid -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5" id="repo-grid">
                    {"".join(repo_cards)}
                </div>
            </div>
        </section>

        <!-- Experience & Education Section -->
        <section id="experience" class="py-16 sm:py-20 bg-slate-100/60 dark:bg-slate-900/40 border-t border-slate-200/80 dark:border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
                    
                    <!-- Education Column -->
                    <div>
                        <div class="mb-8">
                            <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Academic Background</span>
                            <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Education</h2>
                        </div>

                        <div class="space-y-6 relative pl-6 border-l-2 border-emerald-500/30">
                            
                            <!-- PhD -->
                            <div class="relative">
                                <span class="absolute -left-[31px] top-1.5 w-3.5 h-3.5 rounded-full bg-emerald-600 border-2 border-white dark:border-slate-950"></span>
                                <span class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300">Jan 2026 – Present</span>
                                <h3 class="text-base font-bold text-slate-900 dark:text-white mt-1">Ph.D. in Geography</h3>
                                <p class="text-xs font-medium text-slate-600 dark:text-slate-300">University of North Carolina at Charlotte</p>
                                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">Advisor: Dr. Yao Li &middot; Research: Mass-conserving GeoAI downscaling for precision malaria modeling in Zambia (NSF Award #2451156).</p>
                            </div>

                            <!-- M.Sc. Memphis -->
                            <div class="relative">
                                <span class="absolute -left-[31px] top-1.5 w-3.5 h-3.5 rounded-full bg-emerald-500 border-2 border-white dark:border-slate-950"></span>
                                <span class="text-xs font-bold px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">Jan 2024 – Dec 2025</span>
                                <h3 class="text-base font-bold text-slate-900 dark:text-white mt-1">M.Sc. in Earth Sciences</h3>
                                <p class="text-xs font-medium text-slate-600 dark:text-slate-300">The University of Memphis, USA</p>
                                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">Thesis: Road Improvement Impact on Induced Travel &middot; Advisor: Dr. Angela Antipova &middot; Outstanding Earth Scientist Nominee.</p>
                            </div>

                            <!-- GIS Certificate -->
                            <div class="relative">
                                <span class="absolute -left-[31px] top-1.5 w-3.5 h-3.5 rounded-full bg-emerald-400 border-2 border-white dark:border-slate-950"></span>
                                <span class="text-xs font-bold px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">May 2025 – Dec 2025</span>
                                <h3 class="text-base font-bold text-slate-900 dark:text-white mt-1">Graduate Certificate in GIS</h3>
                                <p class="text-xs font-medium text-slate-600 dark:text-slate-300">The University of Memphis, USA</p>
                            </div>

                            <!-- MURP -->
                            <div class="relative">
                                <span class="absolute -left-[31px] top-1.5 w-3.5 h-3.5 rounded-full bg-emerald-300 border-2 border-white dark:border-slate-950"></span>
                                <span class="text-xs font-bold px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">Jul 2022 – Jan 2024</span>
                                <h3 class="text-base font-bold text-slate-900 dark:text-white mt-1">Master of Urban and Rural Planning (MURP)</h3>
                                <p class="text-xs font-medium text-slate-600 dark:text-slate-300">Khulna University, Bangladesh</p>
                                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">Thesis: First and Last Mile Mobility Operations for MRT-6 Transit Connection, Dhaka.</p>
                            </div>

                            <!-- BURP -->
                            <div class="relative">
                                <span class="absolute -left-[31px] top-1.5 w-3.5 h-3.5 rounded-full bg-emerald-200 border-2 border-white dark:border-slate-950"></span>
                                <span class="text-xs font-bold px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">Jan 2017 – Mar 2022</span>
                                <h3 class="text-base font-bold text-slate-900 dark:text-white mt-1">Bachelor of Urban and Rural Planning (BURP)</h3>
                                <p class="text-xs font-medium text-slate-600 dark:text-slate-300">Khulna University, Bangladesh</p>
                            </div>

                        </div>
                    </div>

                    <!-- Research Appointments Column -->
                    <div>
                        <div class="mb-8">
                            <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Professional Record</span>
                            <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Research Appointments</h2>
                        </div>

                        <div class="space-y-6 relative pl-6 border-l-2 border-blue-500/30">
                            
                            <!-- GeoHDR Lab -->
                            <div class="relative">
                                <span class="absolute -left-[31px] top-1.5 w-3.5 h-3.5 rounded-full bg-blue-600 border-2 border-white dark:border-slate-950"></span>
                                <span class="text-xs font-bold px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-300">Jan 2026 – Present</span>
                                <h3 class="text-base font-bold text-slate-900 dark:text-white mt-1">Graduate Research Assistant</h3>
                                <p class="text-xs font-medium text-slate-600 dark:text-slate-300">GeoHealth Dynamics Research (GeoHDR) Lab &middot; UNC Charlotte</p>
                                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">PI: Dr. Yao Li &middot; Built mass-conserving U-Net ensemble downscaling Meta mobility from 5.5 km to 100 m with 38 covariate layers on GEE (NSF Award #2451156).</p>
                            </div>

                            <!-- Univ of Memphis -->
                            <div class="relative">
                                <span class="absolute -left-[31px] top-1.5 w-3.5 h-3.5 rounded-full bg-blue-500 border-2 border-white dark:border-slate-950"></span>
                                <span class="text-xs font-bold px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">Jan 2024 – Dec 2025</span>
                                <h3 class="text-base font-bold text-slate-900 dark:text-white mt-1">Graduate Research Assistant</h3>
                                <p class="text-xs font-medium text-slate-600 dark:text-slate-300">Department of Earth Sciences &middot; The University of Memphis</p>
                                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">PI: Dr. Angela Antipova &middot; Estimated induced travel elasticity for TDOT/FHWA RES2024-02; published in <em>Land</em> (2025) and <a href='https://rosap.ntl.bts.gov/view/dot/92824' target='_blank' rel='noopener' class='text-emerald-600 dark:text-emerald-400 hover:underline'>USDOT/NTL Technical Report RES2024-02</a>.</p>
                            </div>

                            <!-- PDRC -->
                            <div class="relative">
                                <span class="absolute -left-[31px] top-1.5 w-3.5 h-3.5 rounded-full bg-blue-400 border-2 border-white dark:border-slate-950"></span>
                                <span class="text-xs font-bold px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">May 2022 – Dec 2023</span>
                                <h3 class="text-base font-bold text-slate-900 dark:text-white mt-1">Research Associate</h3>
                                <p class="text-xs font-medium text-slate-600 dark:text-slate-300">Planning and Development Research Center (PDRC)</p>
                                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">Led feasibility analyses combining spatial modeling and socioeconomic profiling; three master plans approved by city authorities.</p>
                            </div>

                            <!-- UNDP / SIDA -->
                            <div class="relative">
                                <span class="absolute -left-[31px] top-1.5 w-3.5 h-3.5 rounded-full bg-blue-300 border-2 border-white dark:border-slate-950"></span>
                                <span class="text-xs font-bold px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">Nov 2021 – Apr 2022</span>
                                <h3 class="text-base font-bold text-slate-900 dark:text-white mt-1">Research Assistant</h3>
                                <p class="text-xs font-medium text-slate-600 dark:text-slate-300">UNDP &amp; SIDA Program on Environment &amp; Climate Change</p>
                                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">Conducted extensive household surveys and focus groups on coastal food security and climate adaptation in Bangladesh.</p>
                            </div>

                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- Technical Skills Section -->
        <section id="skills" class="py-16 sm:py-20 border-t border-slate-200/80 dark:border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="max-w-3xl mb-12">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Toolkit &amp; Capabilities</span>
                    <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white mt-1">Technical Skills Matrix</h2>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    
                    <!-- Languages -->
                    <div class="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
                        <div class="flex items-center gap-2 mb-4 text-emerald-600 dark:text-emerald-400 font-bold text-sm">
                            <i class="fa-solid fa-code"></i> Programming Languages
                        </div>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Python</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">R</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">SQL</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">JavaScript (GEE)</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">C++</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">HTML / CSS</span>
                        </div>
                    </div>

                    <!-- Machine Learning & Deep Learning -->
                    <div class="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
                        <div class="flex items-center gap-2 mb-4 text-blue-600 dark:text-blue-400 font-bold text-sm">
                            <i class="fa-solid fa-network-wired"></i> Deep Learning &amp; GeoAI
                        </div>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">PyTorch</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">TensorFlow</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">U-Net Ensembles</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">scikit-learn</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">XGBoost / RF</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Spatial Cross-Validation</span>
                        </div>
                    </div>

                    <!-- Geospatial Technologies -->
                    <div class="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
                        <div class="flex items-center gap-2 mb-4 text-teal-600 dark:text-teal-400 font-bold text-sm">
                            <i class="fa-solid fa-earth-americas"></i> Geospatial Technologies
                        </div>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Google Earth Engine</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">ArcGIS Pro</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">QGIS</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">GeoPandas / Shapely</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Rasterio / GDAL</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">OSRM</span>
                        </div>
                    </div>

                    <!-- Spatial Econometrics & Statistics -->
                    <div class="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
                        <div class="flex items-center gap-2 mb-4 text-purple-600 dark:text-purple-400 font-bold text-sm">
                            <i class="fa-solid fa-chart-line"></i> Econometrics &amp; Spatial Stats
                        </div>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">2SLS Instrumental Variables</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Spatial Autoregression (SAR)</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Entropy Weight Method</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Pycnophylactic Interpolation</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">SPSS / SAS</span>
                        </div>
                    </div>

                    <!-- Cartography & Design -->
                    <div class="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
                        <div class="flex items-center gap-2 mb-4 text-amber-600 dark:text-amber-400 font-bold text-sm">
                            <i class="fa-solid fa-palette"></i> Cartography &amp; Design
                        </div>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Matplotlib / Seaborn</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Folium / Leaflet</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Adobe Illustrator</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">Adobe Photoshop</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">AutoCAD</span>
                            <span class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-medium">LaTeX</span>
                        </div>
                    </div>

                    <!-- Honors & Fellowships -->
                    <div class="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
                        <div class="flex items-center gap-2 mb-4 text-rose-600 dark:text-rose-400 font-bold text-sm">
                            <i class="fa-solid fa-award"></i> Honors &amp; Awards
                        </div>
                        <ul class="text-xs text-slate-600 dark:text-slate-300 space-y-2">
                            <li>🏆 <strong>First Place Winner</strong>, 2nd Annual MAGIC Collegiate Geospatial Showcase (2025)</li>
                            <li>🎓 <strong>GSA Award</strong>, The University of Memphis (2025)</li>
                            <li>🌟 <strong>Nominee</strong>, Outstanding Earth Scientist Award (2025)</li>
                            <li>🎖️ <strong>NST Fellowship</strong>, Govt. of Bangladesh (2022)</li>
                        </ul>
                    </div>

                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="py-16 sm:py-20 bg-slate-100/60 dark:bg-slate-900/40 border-t border-slate-200/80 dark:border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="max-w-3xl mx-auto text-center">
                    <span class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Get in Touch</span>
                    <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white mt-1 mb-4">Connect &amp; Collaborate</h2>
                    <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 mb-8 leading-relaxed">
                        I am always eager to discuss collaborative research in GeoAI, human mobility downscaling, satellite remote sensing, and spatial epidemiology.
                    </p>

                    <div class="inline-grid grid-cols-1 sm:grid-cols-2 gap-4 text-left p-6 sm:p-8 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
                        <div>
                            <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1">Email</div>
                            <a href="mailto:jbiswas@charlotte.edu" class="text-sm font-semibold text-emerald-600 dark:text-emerald-400 hover:underline">
                                jbiswas@charlotte.edu
                            </a>
                        </div>
                        <div>
                            <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1">Phone</div>
                            <span class="text-sm font-semibold text-slate-800 dark:text-slate-200">+1 (901) 297-9395</span>
                        </div>
                        <div class="sm:col-span-2 pt-2 border-t border-slate-100 dark:border-slate-800">
                            <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1">Office Location</div>
                            <p class="text-xs text-slate-600 dark:text-slate-300">
                                McEniry Building &middot; Department of Earth, Environmental, and Geographical Sciences (EEGS)<br>
                                University of North Carolina at Charlotte &middot; 9201 University City Blvd, Charlotte, NC 28223
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-200 dark:border-slate-800 py-8 bg-white dark:bg-slate-950 text-center text-xs text-slate-500 dark:text-slate-400">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                &copy; 2026 Jayanta Biswas. All rights reserved. Built with Tailwind CSS on GitHub Pages.
            </div>
            <div class="flex items-center gap-4">
                <a href="{profile['links']['github']}" target="_blank" rel="noopener" class="hover:text-emerald-500"><i class="fa-brands fa-github text-sm"></i></a>
                <a href="{profile['links']['google_scholar']}" target="_blank" rel="noopener" class="hover:text-blue-500"><i class="fa-brands fa-google-scholar text-sm"></i></a>
                <a href="{profile['links']['linkedin']}" target="_blank" rel="noopener" class="hover:text-blue-600"><i class="fa-brands fa-linkedin text-sm"></i></a>
                <a href="portfolio_data.json" download class="hover:text-emerald-500">JSON API</a>
            </div>
        </div>
    </footer>

    <!-- Interactive Client-side Script -->
    <script>
        // Dark / Light Mode Toggle with persistence
        const themeToggleBtn = document.getElementById('theme-toggle');
        const themeIcon = document.getElementById('theme-icon');

        function applyTheme(isDark) {{
            if (isDark) {{
                document.documentElement.classList.add('dark');
                themeIcon.classList.remove('fa-moon');
                themeIcon.classList.add('fa-sun');
            }} else {{
                document.documentElement.classList.remove('dark');
                themeIcon.classList.remove('fa-sun');
                themeIcon.classList.add('fa-moon');
            }}
        }}

        const savedTheme = localStorage.getItem('theme');
        const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        applyTheme(savedTheme === 'dark' || (!savedTheme && systemPrefersDark));

        themeToggleBtn.addEventListener('click', () => {{
            const isDark = document.documentElement.classList.toggle('dark');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            applyTheme(isDark);
        }});

        // Mobile Menu Drawer Toggle
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        mobileMenuBtn.addEventListener('click', () => {{
            mobileMenu.classList.toggle('hidden');
        }});

        // Publication Search & Filter
        const pubSearch = document.getElementById('pub-search');
        const pubCards = document.querySelectorAll('.pub-card');
        const pubFilterBtns = document.querySelectorAll('.pub-filter-btn');
        let currentPubFilter = 'all';

        function filterPublications() {{
            const query = pubSearch.value.toLowerCase().trim();
            pubCards.forEach(card => {{
                const title = card.getAttribute('data-title');
                const tags = card.getAttribute('data-tags');
                const cat = card.getAttribute('data-category');
                const ptype = card.getAttribute('data-type');

                const matchesQuery = !query || title.includes(query) || tags.includes(query);
                
                let matchesFilter = false;
                if (currentPubFilter === 'all') {{
                    matchesFilter = true;
                }} else if (currentPubFilter === 'journal') {{
                    matchesFilter = (ptype === 'journal');
                }} else if (currentPubFilter === 'tech-report') {{
                    matchesFilter = (ptype === 'tech-report');
                }} else if (currentPubFilter === 'first-author') {{
                    matchesFilter = (cat === 'first-author');
                }}

                if (matchesQuery && matchesFilter) {{
                    card.classList.remove('hidden');
                }} else {{
                    card.classList.add('hidden');
                }}
            }});
        }}

        pubSearch.addEventListener('input', filterPublications);

        pubFilterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                pubFilterBtns.forEach(b => {{
                    b.classList.remove('active', 'bg-emerald-600', 'text-white');
                    b.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-300');
                }});
                btn.classList.add('active', 'bg-emerald-600', 'text-white');
                btn.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-300');
                currentPubFilter = btn.getAttribute('data-filter');
                filterPublications();
            }});
        }});

        // Repositories Category Filter
        const repoFilterBtns = document.querySelectorAll('.repo-filter-btn');
        const repoCards = document.querySelectorAll('.repo-card');

        repoFilterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                repoFilterBtns.forEach(b => {{
                    b.classList.remove('active', 'bg-emerald-600', 'text-white');
                    b.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-300');
                }});
                btn.classList.add('active', 'bg-emerald-600', 'text-white');
                btn.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-300');

                const targetCat = btn.getAttribute('data-cat');
                repoCards.forEach(card => {{
                    if (targetCat === 'all' || card.getAttribute('data-category') === targetCat) {{
                        card.classList.remove('hidden');
                    }} else {{
                        card.classList.add('hidden');
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html)

print('Successfully regenerated index.html with 38 covariates, no GPA, and USDOT tech report! Size:', len(html))
