# TaskFlow

TaskFlow is an internal task-and-project management platform designed for
small engineering pods operating in Blinkit-style dark stores.

It is implemented as a single GitHub repository containing:

- FastAPI backend
- SQLAlchemy ORM
- SQLite development database
- Pydantic validation
- REST CRUD endpoints
- SQL aggregation
- insertion sort
- binary search
- linear search
- algorithm operation counters
- deterministic Quick-Add parser
- optional LLM feature flag with deterministic fallback
- vanilla HTML/CSS/JavaScript frontend
- localStorage caching
- seed data
- algorithm PASS/FAIL checks

---

## 1. Repository structure

```text
taskflow/
├── backend/
│   ├── __init__.py
│   ├── algorithms.py
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   ├── parser.py
│   └── schemas.py
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── styles.css
├── check_algorithms.py
├── requirements.txt
├── seed.py
└── README.md