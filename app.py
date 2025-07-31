import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Immigration Solicitors in London | Deluxe Law Chambers",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
<style>
    /* Base styles */
    [data-testid="stAppViewContainer"] {
        background-color: #f8f9fa;
        font-family: 'Arial', sans-serif;
    }
    
    /* Header styles */
    .header {
        background: linear-gradient(135deg, #1a3a6c 0%, #2c5282 100%);
        color: white;
        padding: 3rem 1rem;
        text-align: center;
        border-bottom: 5px solid #e9b949;
        margin-bottom: 1.5rem;
    }
    
    .logo {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    /* Content card */
    .content-card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        padding: 2rem;
        margin: 1.5rem 0;
        position: relative;
        border-left: 5px solid #1a3a6c;
    }
    
    /* Consultation cards */
    .option-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        text-align: center;
        height: 100%;
        border: 1px solid #eaeaea;
        transition: transform 0.3s ease;
    }
    
    .option-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    }
    
    /* Testimonial */
    .testimonial {
        background-color: #f0f7ff;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 2rem 0;
        border: 1px solid #d4e3f7;
    }
    
    /* Footer */
    .footer {
        background-color: #1a3a6c;
        color: white;
        text-align: center;
        padding: 2rem;
        margin-top: 2.5rem;
        border-top: 5px solid #e9b949;
    }
    
    /* Button */
    .cta-button {
        background: linear-gradient(135deg, #1a3a6c 0%, #2c5282 100%);
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        display: block;
        margin: 1.5rem auto 0;
        width: 100%;
        max-width: 300px;
        text-align: center;
        cursor: pointer;
    }
    
    .cta-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(26, 58, 108, 0.4);
    }
    
    /* Headings */
    h1 {
        color: #1a3a6c;
        margin-bottom: 1.5rem;
        font-size: 2.2rem;
        border-bottom: 3px solid #e9b949;
        padding-bottom: 0.5rem;
    }
    
    h2 {
        color: #2c5282;
        margin: 1.5rem 0 1rem;
        font-size: 1.7rem;
    }
    
    /* Highlight box */
    .highlight-box {
        background-color: #f0f7ff;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #2c5282;
        margin: 1.5rem 0;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .content-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown(
    """
    <div class="header">
        <div class="logo">Deluxe Law Chambers</div>
        <p style="font-size: 1.25rem; max-width: 800px; margin: 0 auto; opacity: 0.9;">
            Expert Immigration Legal Services with Offices Throughout London
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Contact information using Streamlit native components
st.info("📞 **Free Advice Helpline**: 020 3930 0554  |  📧 **Email**: info@deluxelawchambers.co.uk  |  💻 **Online Booking Available**", icon="ℹ️")

# Main content - using Streamlit native components instead of HTML
with st.container():
    # Title
    st.markdown("<h1>Professional Immigration Legal Support in London</h1>", unsafe_allow_html=True)
    
    # Introduction
    st.write("For individuals and families navigating the complexities of UK immigration law, professional guidance is essential. London-based legal practices offer specialised support through every stage of the immigration process.")
    
    # Highlight box
    with st.container():
        st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
        st.write("**Deluxe Law Chambers** provides comprehensive immigration services from multiple locations across London. Our team of experienced solicitors handles a diverse range of UK visa and immigration matters, offering tailored solutions to meet individual circumstances.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Expertise section
    st.markdown("<h2>Expert Guidance Through the Immigration Process</h2>", unsafe_allow_html=True)
    st.write("Navigating the UK immigration system requires careful attention to detail and thorough understanding of current regulations. Our specialist legal professionals provide critical assistance with:")
    
    # Services list
    services = """
    - Visa applications and extensions
    - Work permits and sponsorship
    - Family immigration and settlement
    - Asylum claims and human rights applications
    - Appeals and administrative reviews
    """
    st.markdown(services)
    
    st.write("The quality of service provided by our London-based immigration specialists is evident through our exceptional client feedback and professional recognition in the field.")
    
    # Testimonial
    with st.container():
        st.markdown('<div class="testimonial">', unsafe_allow_html=True)
        st.markdown("**★★★★★**")
        st.write('_"The team at Deluxe Law Chambers provided exceptional guidance throughout my spouse visa application. Their attention to detail and clear communication made a complex process manageable. I couldn\'t have navigated the system without their expertise."_')
        st.markdown("<p style='text-align: right; font-weight: 600;'>- Sarah K., Client since 2023</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Consultation options
    st.markdown("<h2>Flexible Consultation Options</h2>", unsafe_allow_html=True)
    st.write("Understanding that each client's situation is unique, we offer multiple consultation methods to discuss immigration matters:")
    
    # Create columns for consultation options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="option-card">', unsafe_allow_html=True)
        st.markdown("**🏢 In-Person Meetings**")
        st.write("Visit one of our conveniently located offices throughout London for a face-to-face consultation.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="option-card">', unsafe_allow_html=True)
        st.markdown("**📱 Phone Consultations**")
        st.write("Discuss your case with a specialist solicitor over the phone at a time that suits you.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="option-card">', unsafe_allow_html=True)
        st.markdown("**💻 Virtual Meetings**")
        st.write("Connect via Zoom, Microsoft Teams, or WhatsApp for secure online consultations.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # CTA Button
    st.markdown(
        """
        <a href="https://deluxelawchambers.co.uk/immigration-solicitors-in-london/" target="_blank">
            <button class="cta-button">Schedule Your Consultation Today</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    
    # Legal advice section
    st.markdown("<h2>Introductory Legal Advice</h2>", unsafe_allow_html=True)
    st.write("For those beginning their immigration journey, we offer preliminary guidance to help understand options and requirements. This initial discussion provides clarity on:")
    
    # Advice list
    advice = """
    - Eligibility for different visa categories
    - Documentation requirements and timelines
    - Potential challenges and solutions
    - Pathways to settlement and citizenship
    """
    st.markdown(advice)
    
    # Backlink section
    st.write("When facing the complexities of UK immigration law, consulting with experienced " +
             "[immigration solicitors in London](https://deluxelawchambers.co.uk/immigration-solicitors-in-london/) " +
             "ensures proper handling of your case with professional expertise.")
    
    st.write("Our London-based immigration law specialists continue to support clients through changing regulations, providing clarity and confidence throughout the application process.")

# Footer
st.markdown(
    """
    <div class="footer">
        <p>© 2023 Deluxe Law Chambers | Immigration Legal Specialists | London, UK</p>
        <p>Professional legal services for all UK visa and immigration matters</p>
    </div>
    """,
    unsafe_allow_html=True
)
