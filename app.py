import streamlit as st
from agent import create_research_brief

st.set_page_config(
    page_title="Task Automation Agent",
    page_icon="✨",
    layout="wide",
)

st.markdown("""
<style>
    .main {background: #f7f8fc;}
    .block-container {padding-top: 2.2rem; max-width: 950px;}
    .hero {
        padding: 2rem 2.2rem; border-radius: 22px;
        background: linear-gradient(120deg, #172554, #4338ca);
        color: white; margin-bottom: 1.5rem;
    }
    .hero h1 {color: white; margin-bottom: .4rem;}
    .hero p {color: #e0e7ff; font-size: 1.05rem;}
    .result-card {
        padding: 1rem 1.2rem; background: white;
        border: 1px solid #e5e7eb; border-radius: 14px;
        margin: .7rem 0; color: #111827;
    }
    .small-muted {color: #6b7280; font-size: .9rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>✨ Task Automation Agent</h1>
  <p>Research any topic and turn information into a clear, three-point brief — powered by Google Gemini.</p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([3, 1])
with left:
    topic = st.text_input(
        "What would you like to research?",
        placeholder="e.g. Latest trends in artificial intelligence",
        label_visibility="visible",
    )
with right:
    st.write("")
    st.write("")
    run = st.button("Generate brief ↗", type="primary", use_container_width=True)

st.markdown('<p class="small-muted">Fast • Simple • Gemini-powered</p>', unsafe_allow_html=True)

if run:
    if not topic.strip():
        st.warning("Enter a topic to get started.")
    else:
        with st.spinner("Gemini is preparing your research brief..."):
            try:
                result = create_research_brief(topic.strip())
                st.markdown("### Your research brief")
                for index, point in enumerate(result["points"], start=1):
                    st.markdown(
                        f'<div class="result-card"><b>{index}.</b>&nbsp; {point}</div>',
                        unsafe_allow_html=True,
                    )
                st.caption(f"Generated in {result['duration_seconds']:.2f} seconds.")
            except Exception as exc:
                st.error(f"Could not generate the brief: {exc}")
                st.info("For the hosted app, add GEMINI_API_KEY in the Space's Settings → Variables and secrets.")
else:
    st.markdown("### How it works")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**1. Enter a topic**")
        st.caption("Type the subject you want to explore.")
    with c2:
        st.markdown("**2. Ask Gemini**")
        st.caption("Gemini creates a concise research summary.")
    with c3:
        st.markdown("**3. View the brief**")
        st.caption("Get three clear points ready to use.")
