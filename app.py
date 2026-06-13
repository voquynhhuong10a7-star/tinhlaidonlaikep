import streamlit as st

# --- TIÊU ĐỀ ỨNG DỤNG ---
st.title("🏦 Công Cụ Tính Lãi Tiết Kiệm")
st.markdown("So sánh Tổng tiền nhận được theo phương pháp **Lãi đơn** và **Lãi kép**.")
st.divider()

# --- KHU VỰC NHẬP DỮ LIỆU (THAY THẾ CHỨC NĂNG INPUT) ---
st.subheader("Nhập thông tin gửi tiền:")

# Sử dụng number_input để nhập số liệu an toàn hơn, thiết lập sẵn giá trị mặc định (value)
C = st.number_input("Nhập số tiền gửi (trđ):", min_value=0.0, value=500.0, step=10.0)
i = st.number_input("Nhập lãi suất tiết kiệm theo năm (VD: 0.06 cho 6%):", min_value=0.0, value=0.06, step=0.01)
n = st.number_input("Nhập số tháng gửi:", min_value=1.0, value=4.0, step=1.0)

# --- XỬ LÝ TOÁN HỌC & IN KẾT QUẢ ---
# Tạo một nút bấm để người dùng click vào mới bắt đầu tính toán
if st.button("Tính toán ngay"):
    
    # Giữ nguyên logic tính toán của bạn
    A = C * (1 + i * n / 12)
    B = C * (1 + i / 12) ** n
    
    st.divider()
    st.subheader("Kết quả tính toán:")
    
    # Hiển thị kết quả bằng giao diện metric cho đẹp mắt (hoặc dùng st.write)
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("Phương pháp Lãi Đơn")
        st.write(f"**{A:,.4f} trđ**")
        
    with col2:
        st.success("Phương pháp Lãi Kép")
        st.write(f"**{B:,.4f} trđ**")
