"""Mô phỏng tìm kiếm vector có lọc vai trò bằng dữ liệu hoàn toàn giả lập."""

from math import sqrt
from typing import TypedDict

Vector = tuple[float, float, float, float, float]


class Document(TypedDict):
    id: str
    title: str
    allowed_role: str
    vector: Vector


def normalize(vector: Vector) -> Vector:
    """Chuẩn hóa vector theo độ dài L2."""
    magnitude = sqrt(sum(value * value for value in vector))
    if magnitude == 0:
        raise ValueError("Không thể chuẩn hóa vector có độ dài bằng 0.")
    return (
        vector[0] / magnitude,
        vector[1] / magnitude,
        vector[2] / magnitude,
        vector[3] / magnitude,
        vector[4] / magnitude,
    )


def cosine_similarity(left: Vector, right: Vector) -> float:
    """Tính cosine similarity cho hai vector đã chuẩn hóa L2."""
    return sum(a * b for a, b in zip(left, right))


# Mỗi tài liệu dùng vector đặc trưng 5 chiều tự tạo, không phải dữ liệu bệnh án.
documents = [
    {
        "id": "D1",
        "title": "Hướng dẫn giả lập về tim mạch",
        "allowed_role": "doctor",
        "vector": normalize((3, 1, 0, 0, 0)),
    },
    {
        "id": "D2",
        "title": "Phác đồ giả lập về thuốc",
        "allowed_role": "doctor",
        "vector": normalize((0, 3, 1, 0, 0)),
    },
    {
        "id": "D3",
        "title": "Tờ thông tin giả lập cho bệnh nhân",
        "allowed_role": "patient",
        "vector": normalize((0, 0, 0, 3, 1)),
    },
    {
        "id": "D4",
        "title": "Hướng dẫn giả lập về dinh dưỡng",
        "allowed_role": "patient",
        "vector": normalize((0, 0, 2, 1, 0)),
    },
    {
        "id": "D5",
        "title": "Tài liệu giả lập về phòng ngừa",
        "allowed_role": "doctor",
        "vector": normalize((1, 0, 0, 0, 3)),
    },
]


def search(
    query_vector: Vector, allowed_role: str, top_k: int = 3
) -> list[tuple[float, Document]]:
    """Lọc quyền trước, rồi xếp hạng các tài liệu còn lại theo cosine."""
    if top_k < 1:
        raise ValueError("top_k phải lớn hơn hoặc bằng 1.")

    # Pre-filter: loại tài liệu sai vai trò trước khi tính điểm tương đồng.
    permitted_documents = [
        document
        for document in documents
        if document["allowed_role"] == allowed_role
    ]

    # Tính điểm cho tài liệu được phép và sắp xếp từ cao xuống thấp.
    ranked = [
        (cosine_similarity(query_vector, document["vector"]), document)
        for document in permitted_documents
    ]
    return sorted(ranked, key=lambda item: item[0], reverse=True)[:top_k]


# Ba câu hỏi giả lập được biểu diễn bằng năm đặc trưng tương ứng.
queries = [
    ("tra cứu giả lập về tim", "doctor", normalize((1, 1, 0, 0, 0))),
    ("tra cứu giả lập về thuốc", "doctor", normalize((0, 1, 1, 0, 0))),
    ("hướng dẫn giả lập cho bệnh nhân", "patient", normalize((0, 0, 0, 1, 1))),
]


if __name__ == "__main__":
    # Chạy từng câu hỏi và chỉ in tài liệu phù hợp với vai trò được phép.
    for query_text, role, query_vector in queries:
        print(f"\nCâu hỏi: {query_text} (role={role})")
        for score, document in search(query_vector, role):
            print(
                f"  {document['id']} | {document['title']} "
                f"| cosine={score:.3f} | allowed_role={document['allowed_role']}"
            )
