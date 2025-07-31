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
    
    .tagline {
        font-size: 1.25rem;
        max-width: 800px;
        margin: 0 auto;
        opacity: 0.9;
    }
    
    /* Contact bar */
    .contact-bar {
        background-color: #e9b949;
        padding: 1rem;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 2rem;
        font-weight: 600;
        border-radius: 8px;
        margin: 1.5rem 0;
        box-shadow: 0 3px 8px rgba(0,0,0,0.1);
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
    
    .icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: #2c5282;
    }
    
    /* Testimonial */
    .testimonial {
        background-color: #f0f7ff;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 2rem 0;
        border: 1px solid #d4e3f7;
    }
    
    .stars {
        color: #e9b949;
        font-size: 1.5rem;
        margin-bottom: 0.8rem;
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
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .contact-bar {
            flex-direction: column;
            align-items: center;
            gap: 0.8rem;
        }
        
        .content-card {
            padding: 1.5rem;
        }
        
        .logo {
            font-size: 2.2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown(
    """
    <div class="header">
        <div class="logo">Deluxe Law Chambers</div>
        <p class="tagline">Expert Immigration Legal Services with Offices Throughout London</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Contact bar
st.markdown(
    """
    <div class="contact-bar">
        <div>📞 Free Advice Helpline: 020 3930 0554</div>
        <div>📧 Email: info@deluxelawchambers.co.uk</div>
        <div>💻 Online Booking Available</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Main content container
st.markdown(
    """
    <div class="content-card">
        <h1>Professional Immigration Legal Support in London</h1>
        <p>For individuals and families navigating the complexities of UK immigration law, professional guidance is essential. London-based legal practices offer specialised support through every stage of the immigration process.</p>
        
        <div class="highlight-box">
            <p><strong>Deluxe Law Chambers</strong> provides comprehensive immigration services from multiple locations across London. Our team of experienced solicitors handles a diverse range of UK visa and immigration matters, offering tailored solutions to meet individual circumstances.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Expertise section
st.markdown(
    """
    <div class="content-card">
        <h2>Expert Guidance Through the Immigration Process</h2>
        <p>Navigating the UK immigration system requires careful attention to detail and thorough understanding of current regulations. Our specialist legal professionals provide critical assistance with:</p>
        
        <ul>
            <li>Visa applications and extensions</li>
            <li>Work permits and sponsorship</li>
            <li>Family immigration and settlement</li>
            <li>Asylum claims and human rights applications</li>
            <li>Appeals and administrative reviews</li>
        </ul>
        
        <p>The quality of service provided by our London-based immigration specialists is evident through our exceptional client feedback and professional recognition in the field.</p>
        
        <div class="testimonial">
            <div class="stars">★★★★★</div>
            <p><em>"The team at Deluxe Law Chambers provided exceptional guidance throughout my spouse visa application. Their attention to detail and clear communication made a complex process manageable. I couldn't have navigated the system without their expertise."</em></p>
            <p style="text-align: right; font-weight: 600;">- Sarah K., Client since 2023</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Consultation options
st.markdown(
    """
    <div class="content-card">
        <h2>Flexible Consultation Options</h2>
        <p>Understanding that each client's situation is unique, we offer multiple consultation methods to discuss immigration matters:</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Create columns for consultation options
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="option-card">
            <div class="icon">🏢</div>
            <h3>In-Person Meetings</h3>
            <p>Visit one of our conveniently located offices throughout London for a face-to-face consultation.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="option-card">
            <div class="icon">📱</div>
            <h3>Phone Consultations</h3>
            <p>Discuss your case with a specialist solicitor over the phone at a time that suits you.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="option-card">
            <div class="icon">💻</div>
            <h3>Virtual Meetings</h3>
            <p>Connect via Zoom, Microsoft Teams, or WhatsApp for secure online consultations.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

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
st.markdown(
    """
    <div class="content-card">
        <h2>Introductory Legal Advice</h2>
        <p>For those beginning their immigration journey, we offer preliminary guidance to help understand options and requirements. This initial discussion provides clarity on:</p>
        
        <ul>
            <li>Eligibility for different visa categories</li>
            <li>Documentation requirements and timelines</li>
            <li>Potential challenges and solutions</li>
            <li>Pathways to settlement and citizenship</li>
        </ul>
        
        <p>When facing the complexities of UK immigration law, consulting with experienced 
            <a href="https://deluxelawchambers.co.uk/immigration-solicitors-in-london/" 
            style="color: #1a3a6c; font-weight: 600; text-decoration: none; border-bottom: 2px solid #e9b949;">
            immigration solicitors in London</a> 
            ensures proper handling of your case with professional expertise.</p>
        
        <p>Our London-based immigration law specialists continue to support clients through changing regulations, providing clarity and confidence throughout the application process.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Contact form
with st.expander("📩 Send Us a Message", expanded=True):
    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.success("Thank you for your message! We'll contact you shortly.")

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
