
import streamlit as st
from src.agent_utils import configure_genai, initialize_agent
from src.video_utils import save_temp_video, process_video, cleanup_temp_file



st.set_page_config(
    page_title="Video Summarizer Agent",
    page_icon="📽️",
    layout="wide"
)

st.title("Video Summarizer Agent📽️")
st.header("This app is powered by Gemini")



# Configure Gemini API
configure_genai()

# Initialize agent
multimodal_Agent = initialize_agent()


video_file = st.file_uploader(
    "Upload a Video file here", type=["mp4", "mov", "avi"], help="Upload a video for AI Analysis"
)

if video_file:
    video_path = save_temp_video(video_file)
    st.video(video_path, format="video/mp4", start_time=0)

    user_query = st.text_area(
        "What insights are you seeking from the video?",
        placeholder="Ask anything about the video content. The AI agent will analyze and gather additional context if needed.",
        help="Provide specific questions or insights you want from the video."
    )

    if st.button("🔍 Analyze Video", key="analyze_video_button"):
        if not user_query:
            st.warning("Please enter a question or insight to analyze the video.")
        else:
            try:
                with st.spinner("Processing video and gathering insights..."):
                    processed_video = process_video(video_path)
                    analysis_prompt = (
                        f"""
                        Analyze the uploaded video for content and context.
                        Respond to the following query using video insights and supplementary web research:
                        {user_query}

                        Provide a detailed, user-friendly, and actionable response.
                        """
                    )
                    response = multimodal_Agent.run(analysis_prompt, videos=[processed_video])

                st.subheader("Analysis Result")
                st.markdown(response.content)

            except Exception as error:
                st.error(f"An error occurred during analysis: {error}")
            finally:
                cleanup_temp_file(video_path)
    else:
        st.info("Upload a video file to begin analysis.")


# Customize text area height
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
