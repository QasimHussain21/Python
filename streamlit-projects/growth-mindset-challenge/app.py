from io import BytesIO
import streamlit as st
import pandas as pd
import os  

# 🎨 Page Config
st.set_page_config(page_title="Data Sweeper", page_icon="🧹", layout="wide")

# 🎨 Custom CSS for Modern Design
st.markdown(
    """
    <style>
    body { font-family: 'Segoe UI', Tahoma, sans-serif; }
    .main-title {
        text-align: center; color: #007BFF; font-size: 40px; font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-title {
        text-align: center; font-size: 18px; color: #555; margin-bottom: 30px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #007BFF, #00C6FF);
        color: white; font-size: 16px; font-weight: bold;
        padding: 10px 24px; border-radius: 8px; border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); background: linear-gradient(90deg, #0056b3, #0096c7); }
    .stDownloadButton>button { 
        background: linear-gradient(90deg, #28A745, #85E085);
        color: white; font-size: 16px; font-weight: bold;
        padding: 10px 24px; border-radius: 8px; border: none;
    }
    .data-box {
        background: #f9f9f9; padding: 20px; border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🏆 Title
st.markdown("<div class='main-title'>🚀 Data Sweeper</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Transform your files between CSV and Excel formats with built-in cleaning & visualization tools</div>", unsafe_allow_html=True)

# 📂 File Upload
uploaded_files = st.file_uploader("📤 Upload your files (CSV or Excel)", type=['csv', 'xlsx'], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        try:
            file_ext = os.path.splitext(file.name)[1].lower()
            file_name = file.name

            # 📌 Read File
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)  # openpyxl engine auto handled
            else:
                st.error(f"❌ Unsupported file type: {file_ext}")
                continue  

            # 📝 File Info
            st.markdown(f"<div class='data-box'>", unsafe_allow_html=True)
            st.write(f"**📂 File:** `{file_name}`")
            st.write(f"**📏 Size:** `{file.getbuffer().nbytes / 1024:.2f} KB`")

            # 🔍 Data Preview
            st.subheader("👀 Data Preview")
            st.dataframe(df.head())

            # 🛠 Data Cleaning
            st.subheader("🛠 Data Cleaning")

            if st.checkbox(f"🧹 Enable Cleaning for `{file_name}`"):
                col1, col2 = st.columns(2)

                with col1:
                    if st.button(f"🗑 Remove Duplicates `{file_name}`"):
                        df.drop_duplicates(inplace=True)
                        st.success("✅ Duplicates removed!")

                with col2:
                    if st.button(f"🩹 Fill Missing Values `{file_name}`"):
                        numeric_cols = df.select_dtypes(include=['number']).columns
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.success("✅ Missing values filled!")

            # 🎯 Column Selection
            st.subheader("🎯 Select Columns to Keep")
            selected_columns = st.multiselect(f"📌 Choose Columns `{file_name}`", df.columns, default=df.columns)
            df = df[selected_columns]  

            # 📊 Visualization
            st.subheader("📊 Data Visualization")

            if st.checkbox(f"📍 Visualize `{file_name}`"):
                numeric_df = df.select_dtypes(include=['number'])

                if not numeric_df.empty:
                    col1, col2 = st.columns(2)
                    with col1:
                        chart_type = st.radio("📊 Chart Type", ["Bar", "Line", "Area"], key=f"chart_{file_name}")
                    with col2:
                        x_axis = st.selectbox("📌 X-axis", df.columns, key=f"x_{file_name}")
                        y_axis = st.selectbox("📌 Y-axis", numeric_df.columns, key=f"y_{file_name}")

                    if x_axis and y_axis and df[x_axis].nunique() > 1:
                        chart_data = df[[x_axis, y_axis]].dropna()
                        if not chart_data.empty:
                            if chart_type == "Bar":
                                st.bar_chart(chart_data.set_index(x_axis))
                            elif chart_type == "Line":
                                st.line_chart(chart_data.set_index(x_axis))
                            elif chart_type == "Area":
                                st.area_chart(chart_data.set_index(x_axis))
                        else:
                            st.warning("⚠️ No valid data points for chart.")
                    else:
                        st.warning("⚠️ Invalid X or Y-axis selected.")
                else:
                    st.warning("⚠️ No numeric columns for visualization.")

            # 🔄 Conversion
            st.subheader("🔄 File Conversion")
            conversion_type = st.radio(f"Convert `{file_name}` to:", ["CSV", "Excel"], key=file_name)

            if st.button(f"🔄 Convert `{file_name}`"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    new_name = file_name.replace(file_ext, ".csv")
                    mime = "text/csv"
                else:
                    df.to_excel(buffer, index=False)
                    new_name = file_name.replace(file_ext, ".xlsx")
                    mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                buffer.seek(0)

                st.download_button(
                    label=f"📥 Download `{new_name}`",
                    data=buffer,
                    file_name=new_name,
                    mime=mime
                )

            st.markdown("</div>", unsafe_allow_html=True)
            st.success("✅ File processed successfully!")

        except Exception as e:
            st.error(f"❌ Error processing `{file.name}`: {str(e)}")

