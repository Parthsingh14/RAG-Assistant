def build_context(results):
    context_parts = []
    sources = []

    for index, result in enumerate(results, start=1):
        text = result.get("text")

        if text:
            context_parts.append(
                f"--- Document Chunk {index} ---\n{text}"
            )

        sources.append(
            {
                "filename": result.get("filename"),
                "page_number": result.get("page_number")
            }
        )

    context = "\n\n".join(context_parts)

    return context, sources


# Fake retrieval results
results = [
    {
        "id": "hr_0",
        "score": 0.91,
        "document_id": "hr",
        "filename": "HR_Policy.pdf",
        "page_number": 4,
        "chunk_index": 0,
        "text": "Employees receive 20 days of annual leave."
    },
    {
        "id": "hr_1",
        "score": 0.86,
        "document_id": "hr",
        "filename": "HR_Policy.pdf",
        "page_number": 5,
        "chunk_index": 1,
        "text": "Leave requests must be submitted through the HR portal."
    },
    {
        "id": "hr_2",
        "score": 0.79,
        "document_id": "hr",
        "filename": "HR_Policy.pdf",
        "page_number": 6,
        "chunk_index": 2,
        "text": "Employees should submit leave requests at least three days in advance."
    }
]


# Build context and sources
context, sources = build_context(results)


# Display the results
print("===== CONTEXT =====")
print(context)

print("\n===== SOURCES =====")
print(sources)