import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Assistant Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# # Custom CSS for beautiful design
# st.markdown("""
# <style>
#     /* Main theme colors */
#     :root {
#         --primary-color: #6366f1;
#         --secondary-color: #8b5cf6;
#         --background-color: #f8fafc;
#         --text-color: #1e293b;
#     }
    
#     /* Header styling */
#     .main-header {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         padding: 2rem;
#         border-radius: 15px;
#         margin-bottom: 2rem;
#         text-align: center;
#         color: white;
#         box-shadow: 0 10px 25px rgba(0,0,0,0.1);
#     }
    
#     .main-header h1 {
#         margin: 0;
#         font-size: 2.5rem;
#         font-weight: 700;
#     }
    
#     .main-header p {
#         margin: 0.5rem 0 0 0;
#         font-size: 1.1rem;
#         opacity: 0.9;
#     }
    
#     /* Feature cards */
#     .feature-card {
#         background: white;
#         padding: 1.5rem;
#         border-radius: 12px;
#         border-left: 4px solid #667eea;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.05);
#         margin-bottom: 1rem;
#         transition: transform 0.2s;
#     }
    
#     .feature-card:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 6px 12px rgba(0,0,0,0.1);
#     }
    
#     /* Chat messages */
#     .stChatMessage {
#         background-color: #f1f5f9 !important;
#         border-radius: 15px !important;
#         padding: 1rem !important;
#         margin-bottom: 1rem !important;
#     }
    
#     /* Sidebar styling */
#     section[data-testid="stSidebar"] {
#         background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
#     }
    
#     section[data-testid="stSidebar"] * {
#         color: white !important;
#     }
    
#     /* Buttons */
#     .stButton>button {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         border: none;
#         border-radius: 10px;
#         padding: 0.6rem 2rem;
#         font-weight: 600;
#         transition: all 0.3s;
#     }
    
#     .stButton>button:hover {
#         transform: scale(1.05);
#         box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
#     }
    
#     /* Stats cards */
#     .stats-card {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         padding: 1.5rem;
#         border-radius: 12px;
#         text-align: center;
#         color: white;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#     }
    
#     .stats-card h3 {
#         margin: 0;
#         font-size: 2rem;
#         font-weight: 700;
#     }
    
#     .stats-card p {
#         margin: 0.5rem 0 0 0;
#         opacity: 0.9;
#     }
# </style>
# """, unsafe_allow_html=True)

# Initialize OpenAI model
try:
    model = ChatOpenAI(
        model='gpt-4o',
        openai_api_key=os.getenv('OPENAI_API_KEY')
    )
except Exception as e:
    st.error(f"⚠️ Error initializing OpenAI: {str(e)}")
    st.stop()

# Sidebar Navigation
with st.sidebar:
    st.markdown("<h1 style='text-align: center; padding: 1rem 0;'>🤖 AI Hub</h1>", unsafe_allow_html=True)
    
    feature = st.radio(
        "Choose Your Tool:",
        ["💬 Conversational AI", "📚 Research Summarizer", "📄 Report Generator"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Stats
    if 'total_messages' not in st.session_state:
        st.session_state.total_messages = 0
    
    st.markdown(f"""
    <div class="stats-card">
        <h3>{st.session_state.total_messages}</h3>
        <p>Total Messages</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🛠️ Tech Stack
    - LangChain
    - OpenAI GPT-4o
    - Streamlit
    - Python 3.13
    
    ### 🔒 Secure & Private
    Your conversations are processed securely and not stored permanently.
    """)
    
    st.markdown("---")
    
    if st.button("🗑️ Clear All Data", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# Main Header
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Assistant Hub</h1>
    <p>Powered by LangChain & OpenAI GPT-4o | Built with ❤️ for Learning</p>
</div>
""", unsafe_allow_html=True)

# Feature 1: Conversational Chatbot
if feature == "💬 Conversational AI":
    st.markdown("### 💬 Conversational AI Assistant")
    st.markdown("Chat with an intelligent AI that remembers your entire conversation context.")
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [
            SystemMessage(content='You are a helpful, friendly, and knowledgeable AI assistant. Provide clear, concise, and accurate responses.')
        ]
    
    # Chat container with custom styling
    chat_container = st.container()
    
    with chat_container:
        # Display chat messages (skip system message)
        for idx, message in enumerate(st.session_state.chat_history[1:]):
            if isinstance(message, HumanMessage):
                with st.chat_message("user", avatar="👤"):
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("assistant", avatar="🤖"):
                    st.markdown(message.content)
    
    # Chat input at the bottom
    user_input = st.chat_input("Type your message here... 💭", key="chat_input")
    
    if user_input:
        # Add user message
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        st.session_state.total_messages += 1
        
        # Display user message
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)
        
        # Get and display AI response
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("🤔 Thinking..."):
                try:
                    result = model.invoke(st.session_state.chat_history)
                    st.markdown(result.content)
                    st.session_state.chat_history.append(AIMessage(content=result.content))
                    st.session_state.total_messages += 1
                except Exception as e:
                    st.error(f"⚠️ Error: {str(e)}")
        
        st.rerun()
    
    # Information cards
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🧠 Context Aware</h4>
            <p>Remembers entire conversation history for contextual responses</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>⚡ Real-time</h4>
            <p>Instant responses powered by GPT-4o technology</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 Accurate</h4>
            <p>Precise and well-reasoned answers to your questions</p>
        </div>
        """, unsafe_allow_html=True)

# Feature 2: Research Paper Summarizer
elif feature == "📚 Research Summarizer":
    st.markdown("### 📚 Research Paper Summarizer")
    st.markdown("Get customized, detailed summaries of groundbreaking research papers.")
    
    # Paper selection in columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        paper_input = st.selectbox(
            "📄 Select Research Paper:",
            [
                "Attention is all you need",
                "BERT: Pre-training for bidirectional transformers",
                "GPT-3: Language Models are few shot Learners",
                "Diffusion Models Beat GANs on Image Synthesis"
            ]
        )
        
        length_input = st.selectbox(
            "📏 Summary Length:",
            ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (Detailed Explanation)"]
        )
    
    with col2:
        style_input = st.selectbox(
            "🎨 Explanation Style:",
            ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        generate_btn = st.button('✨ Generate Summary', use_container_width=True, type="primary")
    
    template = PromptTemplate(
        template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

**Explanation Style:** {style_input}  
**Explanation Length:** {length_input}  

### Requirements:

1. **Mathematical Details:**  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  

2. **Analogies:**  
   - Use relatable analogies to simplify complex ideas.  

3. **Structure:**
   - Start with the main contribution
   - Explain the methodology
   - Discuss key results and impact

If certain information is not available, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
        """,
        input_variables=['paper_input', 'style_input', 'length_input']
    )
    
    if generate_btn:
        with st.spinner("🔍 Analyzing paper and generating summary..."):
            try:
                prompt = template.format(
                    paper_input=paper_input,
                    style_input=style_input,
                    length_input=length_input
                )
                result = model.invoke(prompt)
                
                st.markdown("---")
                st.markdown("### 📋 Summary Result")
                
                # Display in a nice container
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%); 
                            padding: 2rem; border-radius: 12px; border-left: 4px solid #667eea;">
                    {result.content}
                </div>
                """, unsafe_allow_html=True)
                
                st.session_state.total_messages += 1
                
                # Download option
                st.download_button(
                    label="📥 Download Summary",
                    data=result.content,
                    file_name=f"{paper_input.replace(':', '_')}_summary.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"⚠️ Error generating summary: {str(e)}")

# Feature 3: Report Generator
elif feature == "📄 Report Generator":
    st.markdown("### 📄 Advanced Report Generator")
    st.markdown("Generate detailed reports with automatic AI-powered summaries using LangChain chaining.")
    
    # Input section
    col1, col2 = st.columns([3, 1])
    
    with col1:
        topic = st.text_input(
            "🎯 Enter Topic:",
            placeholder="e.g., Quantum Computing, Climate Change, Blockchain Technology",
            help="Enter any topic you want a detailed report on"
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        generate_report_btn = st.button('🚀 Generate Report', use_container_width=True, type="primary")
    
    if generate_report_btn:
        if topic:
            # Create templates
            template1 = PromptTemplate(
                template="Write a comprehensive, well-structured report on {topic}. Include: introduction, main concepts, current developments, challenges, and future outlook. Make it detailed and informative with at least 5 paragraphs.",
                input_variables=['topic']
            )
            
            template2 = PromptTemplate(
                template="Write a concise 5-line executive summary of the following report:\n\n{text}",
                input_variables=['text']
            )
            
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Step 1: Generate detailed report
                status_text.text("🔍 Step 1/2: Generating detailed report...")
                progress_bar.progress(30)
                
                parser = StrOutputParser()
                full_report_result = model.invoke(template1.format(topic=topic))
                full_report = parser.parse(full_report_result.content)
                
                progress_bar.progress(60)
                
                # Step 2: Generate summary
                status_text.text("📝 Step 2/2: Creating executive summary...")
                summary_result = model.invoke(template2.format(text=full_report))
                summary = parser.parse(summary_result.content)
                
                progress_bar.progress(100)
                status_text.text("✅ Report generation complete!")
                
                st.session_state.total_messages += 2
                
                # Display results in tabs
                st.markdown("---")
                tab1, tab2 = st.tabs(["📋 Executive Summary", "📖 Full Report"])
                
                with tab1:
                    st.markdown("### 📋 Executive Summary")
                    st.info(summary)
                    
                    st.markdown("### 💡 Generation Process")
                    st.success("""
                    ✅ Generated comprehensive detailed report  
                    ✅ Extracted key points using LangChain  
                    ✅ Automatically summarized to 5 lines  
                    ✅ Used advanced prompt chaining
                    """)
                
                with tab2:
                    st.markdown("### 📖 Full Detailed Report")
                    st.markdown(f"""
                    <div style="background: white; padding: 2rem; border-radius: 12px; 
                                border: 1px solid #e2e8f0; line-height: 1.8;">
                        {full_report}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Download options
                st.markdown("---")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.download_button(
                        label="📥 Download Summary",
                        data=summary,
                        file_name=f"{topic.replace(' ', '_')}_summary.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col2:
                    st.download_button(
                        label="📥 Download Full Report",
                        data=full_report,
                        file_name=f"{topic.replace(' ', '_')}_report.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
            except Exception as e:
                st.error(f"⚠️ Error generating report: {str(e)}")
            finally:
                progress_bar.empty()
                status_text.empty()
        else:
            st.warning("⚠️ Please enter a topic first!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #64748b;">
    <p><strong>AI Assistant Hub</strong> | Built with LangChain, OpenAI & Streamlit</p>
    <p>Developed by Sanjoy Chattopadhay | © 2025</p>
</div>
""", unsafe_allow_html=True)
