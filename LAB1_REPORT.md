# LAB 1 – IMRS Architecture Baseline

## 1. Thông tin Lab

- Project: IMRS Architecture
- Lab: Lab 1 – Architecture Baseline
- Mục tiêu: Khảo sát bài toán, xác định yêu cầu và xây dựng kiến trúc hệ thống ban đầu.
- Repository: `imrs-architecture`

---

# 2. Mục tiêu

Lab 1 nhằm xác định các thành phần cơ bản của hệ thống IMRS trước khi triển khai
các lab tiếp theo.

Các mục tiêu chính:

1. Xác định bài toán cần giải quyết.
2. Xác định người dùng và các thành phần tham gia hệ thống.
3. Xác định các chức năng chính.
4. Xác định yêu cầu phi chức năng.
5. Xác định các thành phần kiến trúc ban đầu.
6. Xác định luồng dữ liệu tổng quát.
7. Xác định các vấn đề cần giải quyết ở các Lab tiếp theo.

---

# 3. Mô tả bài toán

IMRS là một hệ thống sử dụng các thành phần AI để hỗ trợ xử lý,
tìm kiếm và cung cấp thông tin cho người dùng.

Hệ thống có thể tiếp nhận yêu cầu từ người dùng, phân tích yêu cầu,
truy xuất dữ liệu cần thiết và tạo ra câu trả lời.

Kiến trúc được thiết kế theo hướng module để có thể mở rộng các
thành phần AI, dữ liệu và dịch vụ trong các giai đoạn tiếp theo.

---

# 4. Đối tượng sử dụng

Hệ thống có các nhóm người dùng chính:

| Đối tượng | Vai trò |
|---|---|
| User | Gửi yêu cầu và nhận kết quả |
| Admin | Quản lý hệ thống |
| AI Agent | Phân tích và xử lý yêu cầu |
| Data Source | Cung cấp dữ liệu |
| System | Điều phối các thành phần |

---

# 5. Chức năng chính

## 5.1. Tiếp nhận yêu cầu

Người dùng gửi câu hỏi hoặc yêu cầu đến hệ thống.

Ví dụ:

```text
User
  |
  | Query
  v
IMRS