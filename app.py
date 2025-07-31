import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Immigration Solicitors in London | Deluxe Law Chambers",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS styling with optimized spacing
st.markdown("""
<style>
    /* Base styles with reduced padding */
    [data-testid="stAppViewContainer"] {
        background-color: #f8f9fa;
        font-family: 'Arial', sans-serif;
        padding: 0 !important;
    }
    
    /* Header styles with tighter spacing */
    .header {
        background: linear-gradient(135deg, #1a3a6c 0%, #2c5282 100%);
        color: white;
        padding: 2rem 1rem;
        text-align: center;
        border-bottom: 5px solid #e9b949;
        margin-bottom: 0;
    }
    
    .logo {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    /* Compact contact bar */
    .contact-info {
        background-color: #e9b949;
        padding: 0.8rem;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 1.5rem;
        font-weight: 600;
        font-size: 0.95rem;
        margin: 0;
    }
    
    /* Content card with optimized spacing */
    .content-card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        padding: 1.5rem;
        margin: 1.2rem 0;
        border-left: 5px solid #1a3a6c;
    }
    
    /* Tighter heading spacing */
    h1 {
        color: #1a3a6c;
        margin: 0.5rem 0 1rem;
        font-size: 2rem;
        border-bottom: 3px solid #e9b949;
        padding-bottom: 0.5rem;
    }
    
    h2 {
        color: #2c5282;
        margin: 1.2rem 0 0.8rem;
        font-size: 1.6rem;
    }
    
    /* Compact highlight box */
    .highlight-box {
        background-color: #f0f7ff;
        padding: 1.2rem;
        border-radius: 8px;
        border-left: 4px solid #2c5282;
        margin: 1.2rem 0;
        font-size: 0.95rem;
    }
    
    /* Option cards with reduced padding */
    .option-card {
        background: #f8f9fa;
        padding: 1.2rem;
        border-radius: 8px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #eaeaea;
        margin-bottom: 0;
        height: 100%;
    }
    
    /* Compact testimonial */
    .testimonial {
        background-color: #f0f7ff;
        padding: 1.2rem;
        border-radius: 8px;
        margin: 1.5rem 0;
        border: 1px solid #d4e3f7;
        font-size: 0.95rem;
    }
    
    /* Footer with reduced padding */
    .footer {
        background-color: #1a3a6c;
        color: white;
        text-align: center;
        padding: 1.5rem;
        margin-top: 1.5rem;
        border-top: 5px solid #e9b949;
        font-size: 0.9rem;
    }
    
    /* Button styling */
    .cta-button {
        background: linear-gradient(135deg, #1a3a6c 0%, #2c5282 100%);
        color: white;
        border: none;
        padding: 0.7rem 1.3rem;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        display: block;
        margin: 1.2rem auto 0;
        width: 100%;
        max-width: 280px;
        text-align: center;
        cursor: pointer;
    }
    
    /* List styling */
    ul {
        padding-left: 1.2rem;
        margin: 0.8rem 0;
    }
    
    li {
        margin-bottom: 0.5rem;
    }
    
    /* Remove extra Streamlit spacing */
    .stMarkdown, .stWrite {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .contact-info {
            gap: 0.8rem;
            padding: 0.7rem;
        }
        .content-card {
            padding: 1.2rem;
        }
        .logo {
            font-size: 2rem;
        }
        .option-card {
            margin-bottom: 0.8rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown(
    """
    <div class="header">
        <div class="logo">Deluxe Law Chambers</div>
        <p style="font-size: 1.1rem; margin: 0.5rem auto; max-width: 800px;">
            Expert Immigration Legal Services with Offices Throughout London
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Contact information
st.markdown(
    """
    <div class="contact-info">
        <div>📞 Free Advice: 020 3930 0554</div>
        <div>📧 info@deluxelawchambers.co.uk</div>
        <div>💻 Online Booking</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Main content
with st.container():
    # Title
    st.markdown("<h1>Professional Immigration Legal Support in London</h1>", unsafe_allow_html=True)
    
    # Introduction
    st.write("For individuals and families navigating UK immigration law complexities, professional guidance is essential. London-based legal practices offer specialised support throughout the immigration process.")
    
   
    
    # Expertise section
    st.markdown("<h2>Expert Guidance Through Immigration</h2>", unsafe_allow_html=True)
    st.write("Navigating the UK immigration system requires attention to detail and current regulatory knowledge. Our specialists assist with:")
    
    # Services list
    services = """
    - Visa applications and extensions
    - Work permits and sponsorship
    - Family immigration and settlement
    - Asylum and human rights cases
    - Appeals and administrative reviews
    """
    st.markdown(services)
    
    st.write("Our London-based specialists' quality is evident through client feedback and professional recognition.")
    

    
    # Consultation options
    st.markdown("<h2>Flexible Consultation Options</h2>", unsafe_allow_html=True)
    st.write("We offer multiple consultation methods to suit different needs:")
    
    # Create columns for consultation options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="option-card">', unsafe_allow_html=True)
        st.markdown("**🏢 In-Person**")
        st.write("Visit our London offices for face-to-face consultations.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="option-card">', unsafe_allow_html=True)
        st.markdown("**📱 Phone**")
        st.write("Discuss your case with a specialist solicitor by phone.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="option-card">', unsafe_allow_html=True)
        st.markdown("**💻 Virtual**")
        st.write("Secure online consultations via Zoom, Teams, or WhatsApp.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # CTA Button
    st.markdown(
        """
        <a href="https://deluxelawchambers.co.uk/immigration-solicitors-in-london/" target="_blank">
            <button class="cta-button">Schedule Consultation</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    
    # Legal advice section
    st.markdown("<h2>Introductory Legal Advice</h2>", unsafe_allow_html=True)
    st.write("For those beginning their immigration journey, we offer preliminary guidance on:")
    
    # Advice list
    advice = """
    - Visa category eligibility
    - Documentation requirements
    - Potential challenges
    - Settlement pathways
    """
    st.markdown(advice)
    
    # Backlink section
    st.write("When facing UK immigration complexities, consulting experienced " +
             "[immigration solicitors in London](https://deluxelawchambers.co.uk/immigration-solicitors-in-london/) " +
             "ensures professional case handling.")
    
    st.write("Our specialists support clients through regulatory changes, providing clarity throughout the application process.")

# Footer
st.markdown(
    """
    <div class="footer">
        <p>© 2023 Deluxe Law Chambers | Immigration Legal Specialists | London, UK</p>
    </div>
    """,
    unsafe_allow_html=True
)
