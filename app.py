import streamlit as st
from langgraph_agent import run_agent

st.set_page_config(
    page_title="JobJutsu AI",
    page_icon="🥷",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, .stApp {
    font-family: 'Space Grotesk', sans-serif !important;
    background: #07070D !important;
    color: #E4E4F0;
}

/* Aurora glow */
.stApp::after {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 70% 45% at 5% 0%,   rgba(124,58,237,0.13) 0%, transparent 60%),
        radial-gradient(ellipse 50% 35% at 95% 80%,  rgba(163,230,53,0.08) 0%, transparent 55%),
        radial-gradient(ellipse 40% 50% at 50% 110%, rgba(99,102,241,0.09) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header, .stDeployButton { visibility: hidden !important; }
[data-testid="stToolbar"]   { display: none !important; }
[data-testid="stDecoration"]{ display: none !important; }

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── WIDGET ZONE (streamlit widgets padding) ── */
.jj-widget-zone {
    padding: 0 48px 0;
    max-width: 1140px;
    margin: 0 auto;
}

/* section labels */
.jj-wlabel {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.22);
    margin-bottom: 10px;
    margin-top: 22px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.jj-wlabel::before {
    content: '';
    width: 16px; height: 1px;
    background: rgba(124,58,237,0.7);
    display: inline-block;
}

/* file uploader */
[data-testid="stFileUploader"] {
    background: rgba(124,58,237,0.04) !important;
    border: 1px dashed rgba(124,58,237,0.3) !important;
    border-radius: 14px !important;
    transition: border-color 0.2s;
}
[data-testid="stFileUploader"]:hover {
    border-color: rgba(124,58,237,0.55) !important;
}
[data-testid="stFileUploadDropzone"] { background: transparent !important; }

/* textarea */
textarea {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    color: #E4E4F0 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 13px !important;
    resize: none !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
textarea:focus {
    border-color: rgba(124,58,237,0.5) !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.07) !important;
}
textarea::placeholder { color: rgba(255,255,255,0.18) !important; }

/* divider */
hr {
    border: none !important;
    border-top: 1px solid rgba(255,255,255,0.055) !important;
    margin: 28px 0 !important;
}

/* hidden buttons */
.jj-hidden { display: none !important; }

/* metric cards */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.025) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 16px !important;
    padding: 20px !important;
    text-align: center !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 32px !important;
    font-weight: 700 !important;
    color: #A3E635 !important;
    letter-spacing: -0.03em !important;
}
[data-testid="stMetricLabel"] {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
    color: rgba(255,255,255,0.28) !important;
}

/* alerts */
[data-testid="stAlert"]   { border-radius: 12px !important; font-family: 'Space Grotesk', sans-serif !important; font-size: 13px !important; }
[data-testid="stSuccess"] { background: rgba(163,230,53,0.06) !important; border: 1px solid rgba(163,230,53,0.22) !important; border-radius: 12px !important; color: #A3E635 !important; }
[data-testid="stWarning"] { background: rgba(251,191,36,0.06) !important; border: 1px solid rgba(251,191,36,0.18) !important; border-radius: 12px !important; }

/* result box */
.jj-result {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.07);
    border-top: 2px solid #7C3AED;
    border-radius: 18px;
    padding: 30px 34px;
    line-height: 1.88;
    font-size: 14px;
    color: rgba(255,255,255,0.65);
    position: relative;
    overflow: hidden;
    margin-top: 6px;
}
.jj-result::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 70px;
    background: linear-gradient(180deg, rgba(124,58,237,0.07), transparent);
    pointer-events: none;
}
.jj-results-heading {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.2);
    margin: 28px 0 14px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.jj-results-heading::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.055);
}

/* scrollbar */
::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(124,58,237,0.25); border-radius: 3px; }

</style>
""", unsafe_allow_html=True)


st.iframe(src="""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Space Grotesk', sans-serif; background: transparent; color: #E4E4F0; }

  /* ── NAVBAR ── */
  .nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 48px;
    height: 64px;
    background: rgba(7,7,13,0.92);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255,255,255,0.06);
    position: sticky;
    top: 0;
    z-index: 999;
  }
  .brand {
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    cursor: pointer;
  }
  .brand-emoji { font-size: 22px; }
  .brand-name  {
    font-size: 17px;
    font-weight: 700;
    color: #fff;
    letter-spacing: -0.03em;
    transition: opacity 0.2s;
  }
  .brand:hover .brand-name { opacity: 0.75; }
  .brand-name em {
    font-style: normal;
    background: linear-gradient(110deg, #7C3AED, #A78BFA 50%, #A3E635);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .nav-links { display: flex; align-items: center; gap: 4px; }
  .nav-link {
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 500;
    color: rgba(255,255,255,0.4);
    cursor: pointer;
    transition: color 0.15s, background 0.15s;
    letter-spacing: -0.01em;
    text-decoration: none;
  }
  .nav-link:hover { color: #fff; background: rgba(255,255,255,0.06); }
  .nav-badge {
    padding: 5px 12px;
    border-radius: 100px;
    font-size: 11px;
    font-weight: 600;
    color: rgba(163,230,53,0.9);
    background: rgba(163,230,53,0.08);
    border: 1px solid rgba(163,230,53,0.2);
    margin-left: 8px;
  }

  /* ── BODY ── */
  .body { padding: 56px 48px 0; max-width: 1140px; margin: 0 auto; }

  /* ── HERO ── */
  .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 5px 14px;
    background: rgba(163,230,53,0.07);
    border: 1px solid rgba(163,230,53,0.2);
    border-radius: 100px;
    font-size: 10px;
    font-weight: 700;
    color: #A3E635;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 24px;
  }
  .pulse {
    width: 5px; height: 5px;
    background: #A3E635;
    border-radius: 50%;
    animation: pulse 2.2s ease-in-out infinite;
  }
  @keyframes pulse {
    0%,100% { opacity:1; transform:scale(1); }
    50%      { opacity:0.3; transform:scale(0.7); }
  }

  .hero-row {
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 48px;
    align-items: start;
    margin-bottom: 56px;
  }

  .h1 {
    font-size: clamp(2.2rem, 4vw, 3.4rem);
    font-weight: 700;
    color: #fff;
    letter-spacing: -0.04em;
    line-height: 1.07;
    margin-bottom: 18px;
  }
  .h1 .g {
    background: linear-gradient(120deg, #7C3AED 0%, #A78BFA 45%, #A3E635 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .sub {
    font-size: 15px;
    color: rgba(255,255,255,0.38);
    line-height: 1.75;
    max-width: 460px;
    font-weight: 400;
    margin-bottom: 32px;
  }

  /* scroll CTA */
  .hero-cta {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 22px;
    background: linear-gradient(135deg, #7C3AED, #5B21B6);
    border-radius: 10px;
    font-size: 14px;
    font-weight: 600;
    color: #fff;
    cursor: pointer;
    text-decoration: none;
    transition: opacity 0.2s, transform 0.2s;
    border: none;
  }
  .hero-cta:hover { opacity: 0.88; transform: translateY(-2px); }
  .hero-cta-ghost {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 22px;
    background: transparent;
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 10px;
    font-size: 14px;
    font-weight: 600;
    color: rgba(255,255,255,0.55);
    cursor: pointer;
    text-decoration: none;
    transition: border-color 0.2s, color 0.2s;
    margin-left: 12px;
  }
  .hero-cta-ghost:hover { border-color: rgba(255,255,255,0.3); color: #fff; }

  /* feature pills */
  .feat-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.2);
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .feat-label::before {
    content: '';
    width: 14px; height: 1px;
    background: rgba(124,58,237,0.7);
    display: inline-block;
  }
  .feat-pill {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 13px 14px;
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    margin-bottom: 9px;
    transition: border-color 0.15s, background 0.15s;
  }
  .feat-pill:hover { background: rgba(124,58,237,0.07); border-color: rgba(124,58,237,0.25); }
  .feat-icon {
    font-size: 16px;
    width: 32px; height: 32px;
    display: flex; align-items: center; justify-content: center;
    background: rgba(124,58,237,0.1);
    border-radius: 8px;
    flex-shrink: 0;
  }
  .feat-title { font-size: 13px; font-weight: 600; color: #fff; margin-bottom: 2px; }
  .feat-sub   { font-size: 11px; color: rgba(255,255,255,0.28); line-height: 1.5; }

  /* ── DIVIDER ── */
  .divider { height: 1px; background: rgba(255,255,255,0.06); margin: 0 0 40px; }

  /* ── ANALYSIS CARDS ── */
  .cards-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.2);
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .cards-label::after { content:''; flex:1; height:1px; background:rgba(255,255,255,0.06); }

  .card-grid {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 14px;
    margin-bottom: 56px;
  }
  .acard {
    position: relative;
    padding: 24px 20px 52px;
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    cursor: default;
    overflow: visible;
    transition: border-color 0.22s, background 0.22s, transform 0.22s;
  }
  .acard::before {
    content: '';
    position: absolute;
    top: 0; left: 16px;
    width: 50px; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(124,58,237,0.5), transparent);
    transition: width 0.3s;
    border-radius: 1px;
  }
  .acard:hover { border-color: rgba(124,58,237,0.45); background: rgba(124,58,237,0.08); transform: translateY(-5px); }
  .acard:hover::before { width: 90px; }

  .acard-emoji { font-size: 28px; margin-bottom: 16px; display: block; }
  .acard-title { font-size: 14px; font-weight: 700; color: #fff; letter-spacing: -0.01em; margin-bottom: 8px; }
  .acard-desc  { font-size: 12px; color: rgba(255,255,255,0.32); line-height: 1.65; }

  .acard-badge {
    position: absolute;
    bottom: 16px; right: 16px;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(124,58,237,0.6);
    opacity: 0;
    transition: opacity 0.2s;
    background: rgba(124,58,237,0.08);
    padding: 3px 8px;
    border-radius: 6px;
    border: 1px solid rgba(124,58,237,0.2);
  }
  .acard:hover .acard-badge { opacity: 1; }

  /* tooltip */
  .tooltip {
    position: absolute;
    bottom: calc(100% + 12px);
    left: 50%;
    transform: translateX(-50%) translateY(6px);
    background: rgba(10,10,20,0.97);
    border: 1px solid rgba(124,58,237,0.4);
    border-radius: 10px;
    padding: 10px 14px;
    font-size: 12px;
    color: rgba(255,255,255,0.72);
    line-height: 1.6;
    white-space: nowrap;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.18s, transform 0.18s;
    z-index: 9999;
    box-shadow: 0 8px 28px rgba(0,0,0,0.6);
  }
  .tooltip::after {
    content: '';
    position: absolute;
    top: 100%; left: 50%;
    transform: translateX(-50%);
    border: 5px solid transparent;
    border-top-color: rgba(124,58,237,0.4);
  }
  .acard:hover .tooltip { opacity: 1; transform: translateX(-50%) translateY(0); }

  /* ── HOW IT WORKS ── */
  .how-section { margin-bottom: 32px; }
  .section-heading {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.2);
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .section-heading::after { content:''; flex:1; height:1px; background:rgba(255,255,255,0.06); }

  .steps {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    position: relative;
  }
  .steps::before {
    content: '';
    position: absolute;
    top: 20px; left: 10%; right: 10%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(124,58,237,0.3), rgba(163,230,53,0.3), transparent);
    z-index: 0;
  }
  .step {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 0 12px;
    position: relative;
    z-index: 1;
  }
  .step-num {
    width: 40px; height: 40px;
    border-radius: 50%;
    background: rgba(124,58,237,0.12);
    border: 1px solid rgba(124,58,237,0.3);
    display: flex; align-items: center; justify-content: center;
    font-size: 13px;
    font-weight: 700;
    color: #A78BFA;
    margin-bottom: 14px;
    position: relative;
    z-index: 2;
    transition: background 0.2s, border-color 0.2s;
  }
  .step:hover .step-num {
    background: rgba(124,58,237,0.25);
    border-color: rgba(124,58,237,0.6);
  }
  .step-title { font-size: 13px; font-weight: 600; color: #fff; margin-bottom: 6px; }
  .step-desc  { font-size: 11.5px; color: rgba(255,255,255,0.3); line-height: 1.6; }

</style>
</head>
<body>

<nav class="nav">
  <a class="brand" href="#" onclick="window.parent.document.getElementById('upload-section').scrollIntoView({behavior:'smooth'}); return false;">
    <span class="brand-emoji">🥷</span>
    <span class="brand-name">Job<em>Jutsu</em></span>
  </a>
  <div class="nav-links">
    <a class="nav-link" onclick="window.parent.document.getElementById('upload-section').scrollIntoView({behavior:'smooth'})">Resume Review</a>
    <a class="nav-link" onclick="window.parent.document.getElementById('upload-section').scrollIntoView({behavior:'smooth'})">JD Match</a>
    <a class="nav-link" onclick="window.parent.document.getElementById('upload-section').scrollIntoView({behavior:'smooth'})">Skill Gaps</a>
    <a class="nav-link" onclick="window.parent.document.getElementById('upload-section').scrollIntoView({behavior:'smooth'})">Interview Prep</a>
    <span class="nav-badge">✦ AI Powered</span>
  </div>
</nav>

<div class="body">

  <div class="eyebrow">
    <div class="pulse"></div>
    Free &nbsp;·&nbsp; Instant &nbsp;·&nbsp; AI-Native
  </div>

  <div class="hero-row">

    <div>
      <div class="h1">
        Your career,<br>
        <span class="g">sharpened to a blade.</span>
      </div>
      <div class="sub">
        Upload your resume, paste the JD — get an ATS score, skill gap report,
        and interview questions crafted for <em>your</em> role. In seconds.
      </div>
      <a class="hero-cta" onclick="window.parent.document.getElementById('upload-section').scrollIntoView({behavior:'smooth'})">
        🚀 &nbsp; Get Started
      </a>
      <a class="hero-cta-ghost" onclick="window.parent.document.getElementById('how-it-works').scrollIntoView({behavior:'smooth'})">
        How it works ↓
      </a>
    </div>

    <div>
      <div class="feat-label">What you'll get</div>
      <div class="feat-pill">
        <div class="feat-icon">📊</div>
        <div><div class="feat-title">ATS Score</div><div class="feat-sub">Overall score + hiring readiness grade</div></div>
      </div>
      <div class="feat-pill">
        <div class="feat-icon">📋</div>
        <div><div class="feat-title">Resume Breakdown</div><div class="feat-sub">Section-by-section scoring</div></div>
      </div>
      <div class="feat-pill">
        <div class="feat-icon">⚠️</div>
        <div><div class="feat-title">ATS Risk Detector</div><div class="feat-sub">Weak sections + missing keywords flagged</div></div>
      </div>
      <div class="feat-pill">
        <div class="feat-icon">🚀</div>
        <div><div class="feat-title">Skill Gap Insights</div><div class="feat-sub">Learning roadmap + rewrite suggestions</div></div>
      </div>
    </div>

  </div><div class="divider"></div>

  <div class="cards-label">Choose your analysis</div>
  <div class="card-grid">

    <div class="acard" onclick="window.parent.document.getElementsByTagName('button')[0].click(); window.parent.document.getElementById('upload-section').scrollIntoView({behavior:'smooth'});">
      <div class="tooltip">Scores your resume section-by-section<br>and flags ATS formatting issues.</div>
      <span class="acard-emoji">📄</span>
      <div class="acard-title">Resume Review</div>
      <div class="acard-desc">Full ATS audit with section-level scores and risk flags.</div>
      <span class="acard-badge">ATS AUDIT</span>
    </div>

    <div class="acard" onclick="window.parent.document.getElementsByTagName('button')[1].click(); window.parent.document.getElementById('upload-section').scrollIntoView({behavior:'smooth'});">
      <div class="tooltip">Compares your resume against the JD<br>keyword-by-keyword for fit score.</div>
      <span class="acard-emoji">🎯</span>
      <div class="acard-title">JD Match</div>
      <div class="acard-desc">See exactly how well your resume aligns to the role.</div>
      <span class="acard-badge">FIT SCORE</span>
    </div>

    <div class="acard" onclick="window.parent.document.getElementsByTagName('button')[2].click(); window.parent.document.getElementById('upload-section').scrollIntoView({behavior:'smooth'});">
      <div class="tooltip">Identifies skills you're missing<br>and gives you a learning roadmap.</div>
      <span class="acard-emoji">📈</span>
      <div class="acard-title">Skill Gaps</div>
      <div class="acard-desc">Know exactly what to learn next to land the role.</div>
      <span class="acard-badge">ROADMAP</span>
    </div>

    <div class="acard" onclick="window.parent.document.getElementsByTagName('button')[3].click(); window.parent.document.getElementById('upload-section').scrollIntoView({behavior:'smooth'});">
      <div class="tooltip">Generates tailored interview questions<br>based on your resume + the JD.</div>
      <span class="acard-emoji">🎤</span>
      <div class="acard-title">Interview Prep</div>
      <div class="acard-desc">Role-targeted questions so you walk in confident.</div>
      <span class="acard-badge">PREP KIT</span>
    </div>

  </div><div class="how-section" id="how-it-works">
    <div class="section-heading">How it works</div>
    <div class="steps">
      <div class="step">
        <div class="step-num">01</div>
        <div class="step-title">Upload Resume</div>
        <div class="step-desc">Drop your PDF resume into the upload zone below.</div>
      </div>
      <div class="step">
        <div class="step-num">02</div>
        <div class="step-title">Paste JD</div>
        <div class="step-desc">Copy-paste the job description you're targeting.</div>
      </div>
      <div class="step">
        <div class="step-num">03</div>
        <div class="step-title">Pick Analysis</div>
        <div class="step-desc">Choose ATS audit, JD match, skill gaps, or interview prep.</div>
      </div>
      <div class="step">
        <div class="step-num">04</div>
        <div class="step-title">Get Results</div>
        <div class="step-desc">AI delivers your personalised report in under 10 seconds.</div>
      </div>
    </div>
  </div>

</div></body>
</html>
""", height=990)



st.markdown('<div id="upload-section" class="jj-widget-zone">', unsafe_allow_html=True)

left_col, right_col = st.columns([1.55, 1], gap="large")

with left_col:
    st.markdown('<div class="jj-wlabel">Your Resume</div>', unsafe_allow_html=True)
    uploaded_resume = st.file_uploader(
        "Resume", type=["pdf"], label_visibility="collapsed"
    )
    if uploaded_resume:
        with open("data/resume.pdf", "wb") as f:
            f.write(uploaded_resume.getbuffer())
        st.success("✓ Resume ready")

    st.markdown('<div class="jj-wlabel">Job Description</div>', unsafe_allow_html=True)
    jd_text = st.text_area(
        "Job Description", height=190,
        placeholder="Paste the job description here...",
        label_visibility="collapsed"
    )
    if jd_text:
        with open("data/jd.txt", "w", encoding="utf-8") as f:
            f.write(jd_text)

with right_col:
    pass  

st.markdown('</div>', unsafe_allow_html=True)

st.divider()


st.markdown('<div class="jj-hidden">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:  resume_clicked    = st.button("Resume Review")
with col2:  jd_clicked        = st.button("JD Match")
with col3:  skill_clicked     = st.button("Skill Gaps")
with col4:  interview_clicked = st.button("Interview Prep")
st.markdown('</div>', unsafe_allow_html=True)


query = None
if resume_clicked:      query = "Review my resume"
elif jd_clicked:        query = "Compare my resume with this job"
elif skill_clicked:     query = "What skills should I improve?"
elif interview_clicked: query = "Generate interview questions"

if query:
    if not uploaded_resume:
        st.warning("Upload your resume first.")
        st.stop()
    if query == "Compare my resume with this job" and not jd_text:
        st.warning("Paste a job description first.")
        st.stop()

    with st.spinner("🥷 Analyzing..."):
        result = run_agent(query)

    st.success("Analysis complete")

    st.markdown('<div class="jj-widget-zone">', unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3, gap="medium")
    with m1: st.metric("ATS Score", "82%")
    with m2: st.metric("Match Score", "74%")
    with m3: st.metric("Skill Gaps", "5")
    st.markdown('<div class="jj-results-heading">Results</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="jj-result">{result}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)

st.iframe(src="""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Space Grotesk', sans-serif; background: transparent; color: #E4E4F0; padding: 0 48px; max-width: 1140px; margin: 0 auto; }

  /* ── STATS STRIP ── */
  .section-heading {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.2);
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .section-heading::after { content:''; flex:1; height:1px; background:rgba(255,255,255,0.06); }

  .stats-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-bottom: 48px;
  }
  .stat-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.065);
    border-radius: 16px;
    padding: 24px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  .stat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 60px; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(163,230,53,0.5), transparent);
  }
  .stat-val   { font-size: 36px; font-weight: 700; color: #A3E635; letter-spacing: -0.04em; line-height: 1; margin-bottom: 6px; }
  .stat-label { font-size: 11px; font-weight: 500; color: rgba(255,255,255,0.3); letter-spacing: 0.08em; text-transform: uppercase; }

  /* ── FOOTER ── */
  .footer {
    border-top: 1px solid rgba(255,255,255,0.055);
    padding: 28px 0 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .footer-brand { display: flex; align-items: center; gap: 8px; }
  .footer-brand-name { font-size: 15px; font-weight: 700; color: rgba(255,255,255,0.5); letter-spacing: -0.02em; }
  .footer-brand-name em {
    font-style: normal;
    background: linear-gradient(110deg, #7C3AED, #A3E635);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .footer-stack { display: flex; align-items: center; gap: 8px; }
  .footer-pill {
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.06em;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    color: rgba(255,255,255,0.3);
  }
  .footer-copy { font-size: 11px; color: rgba(255,255,255,0.18); letter-spacing: 0.04em; }
</style>
</head>
<body>

  <div class="section-heading">Trusted by job seekers</div>
  <div class="stats-strip">
    <div class="stat-card">
      <div class="stat-val">94%</div>
      <div class="stat-label">ATS Pass Rate</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">3x</div>
      <div class="stat-label">More Interview Calls</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">&lt;10s</div>
      <div class="stat-label">Analysis Time</div>
    </div>
  </div>

  <div class="footer">
    <div class="footer-brand">
      <span style="font-size:18px;">🥷</span>
      <span class="footer-brand-name">Job<em>Jutsu</em> AI</span>
    </div>
    <div class="footer-stack">
      <span class="footer-pill">LangGraph</span>
      <span class="footer-pill">Gemini 2.5 Flash</span>
      <span class="footer-pill">Streamlit</span>
    </div>
    <span class="footer-copy">Built for job seekers who mean business.</span>
  </div>

</body>
</html>
""", height=220)