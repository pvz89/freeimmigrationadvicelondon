import streamlit as st
import base64

def main():
    # Custom CSS for styling
    st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .header {
            background: linear-gradient(135deg, #1a3a6c 0%, #2c5282 100%);
            color: white;
            padding: 3rem 1rem;
            text-align: center;
            border-bottom: 5px solid #e9b949;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .contact-bar {
            background-color: #e9b949;
            padding: 1rem;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 2rem;
            font-weight: 600;
            margin-bottom: 2rem;
        }
        .content-card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            padding: 2.5rem;
            margin: 2rem auto;
            max-width: 900px;
            position: relative;
            border-left: 8px solid #1a3a6c;
        }
        .highlight-box {
            background-color: #f0f7ff;
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #2c5282;
            margin: 1.5rem 0;
        }
        .testimonial {
            background-color: #f0f7ff;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 2rem 0;
            position: relative;
        }
        .option-card {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.05);
            text-align: center;
            transition: all 0.3s ease;
            margin-bottom: 1rem;
            height: 95%;
        }
        .option-card:hover {
            transform: translateY(-5px);
        }
        .keyword-link {
            color: #1a3a6c;
            font-weight: 600;
            text-decoration: none;
            border-bottom: 2px dotted #e9b949;
        }
        .keyword-link:hover {
            color: #e9b949;
            border-bottom-style: solid;
        }
        .footer {
            background-color: #1a3a6c;
            color: white;
            text-align: center;
            padding: 1.5rem;
            margin-top: 2rem;
            border-top: 5px solid #e9b949;
        }
        h1 {
            color: #1a3a6c;
            margin-bottom: 1.5rem;
        }
        h2 {
            color: #2c5282;
            margin: 1.5rem 0 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #e9b949;
        }
        @media (max-width: 768px) {
            .contact-bar {
                flex-direction: column;
                align-items: center;
                gap: 1rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header section
    st.markdown(
        """
        <div class="header">
            <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">Deluxe Law Chambers</h1>
            <p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto;">
                Expert Immigration Legal Services with Offices Throughout London
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Contact bar
    st.markdown(
        """
        <div class="contact-bar">
            <div class="contact-item">📞 Free Advice Helpline: 020 3930 0554</div>
            <div class="contact-item">📧 Email: info@deluxelawchambers.co.uk</div>
            <div class="contact-item">💻 Online Booking Available</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Main content container
    with st.container():
        st.markdown(
            """
            <div class="content-card">
                <h1>Professional Immigration Legal Support in London</h1>
                
                <p>For individuals and families navigating the complexities of UK immigration law, professional guidance is essential. London-based legal practices offer specialised support through every stage of the immigration process.</p>
                
                <div class="highlight-box">
                    <p>Deluxe Law Chambers provides comprehensive immigration services from multiple locations across London. Their team of experienced solicitors handles a diverse range of UK visa and immigration matters, offering tailored solutions to meet individual circumstances.</p>
                </div>
                
                <h2>Expert Guidance Through the Immigration Process</h2>
                
                <p>Navigating the UK immigration system requires careful attention to detail and thorough understanding of current regulations. Specialist legal professionals can provide critical assistance with:</p>
                
                <ul>
                    <li>Visa applications and extensions</li>
                    <li>Work permits and sponsorship</li>
                    <li>Family immigration and settlement</li>
                    <li>Asylum claims and human rights applications</li>
                    <li>Appeals and administrative reviews</li>
                </ul>
                
                <p>The quality of service provided by London-based immigration specialists is evident through client testimonials and professional recognition in the field.</p>
                
                <div class="testimonial">
                    <div style="color: #e9b949; font-size: 1.3rem; margin-bottom: 0.5rem;">★★★★★</div>
                    <p><i>"The team at Deluxe Law Chambers provided exceptional guidance throughout my spouse visa application. Their attention to detail and clear communication made a complex process manageable. I couldn't have navigated the system without their expertise."</i></p>
                    <div style="font-weight: 600; color: #1a3a6c; text-align: right;">- Sarah K., Client since 2023</div>
                </div>
                
                <h2>Flexible Consultation Options</h2>
                
                <p>Understanding that each client's situation is unique, multiple consultation methods are available to discuss immigration matters:</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Consultation options in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                """
                <div class="option-card">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem;">🏢</div>
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
                    <div style="font-size: 2.5rem; margin-bottom: 1rem;">📱</div>
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
                    <div style="font-size: 2.5rem; margin-bottom: 1rem;">💻</div>
                    <h3>Virtual Meetings</h3>
                    <p>Connect via Zoom, Microsoft Teams, or WhatsApp for secure online consultations.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Bottom content section
        st.markdown(
            """
            <div class="content-card">
                <p>Initial enquiries can be directed to our London team at London@deluxelawchambers.co.uk. For more complex matters, we recommend scheduling a comprehensive consultation.</p>
                
                <h2>Introductory Legal Advice</h2>
                
                <p>For those beginning their immigration journey, preliminary guidance is available to help understand options and requirements. This initial discussion can provide clarity on:</p>
                
                <ul>
                    <li>Eligibility for different visa categories</li>
                    <li>Documentation requirements and timelines</li>
                    <li>Potential challenges and solutions</li>
                    <li>Pathways to settlement and citizenship</li>
                </ul>
                
                <p>When facing the complexities of UK immigration law, consulting with experienced 
                    <a href="https://deluxelawchambers.co.uk/immigration-solicitors-in-london/" class="keyword-link">immigration solicitors in London</a> 
                    ensures proper handling of your case with professional expertise.</p>
                
                <p>London-based immigration law specialists continue to support clients through changing regulations, providing clarity and confidence throughout the application process.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
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

if __name__ == "__main__":
    main()
