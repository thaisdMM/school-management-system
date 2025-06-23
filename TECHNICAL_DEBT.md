# TECHNICAL_DEBT.md

## 1. Duplicated error messages between file access and business logic

**Date recorded:** 2025-06-23  
**Location:** `project_file` module — functions for file read/write  
**Issue:**  
Error messages (`print()`) are being triggered both in low-level file handling (`try-except`) and in higher-level logic functions such as `mostrar_disciplinas()` and `cadastro_notas_aluno()`.  
This results in redundant output when a file is missing, empty, or invalid.

**Decision:**  
This behavior will be preserved temporarily to assist in testing and provide clear runtime feedback.  
A future refactoring will centralize the user-facing messages in the interface layer, and remove direct `print()` statements from the file-handling module.

**Responsible:** Thaís Moreira  
**Status:** Pending — to be addressed after core functionality is completed.

---

## 2. Use of `try-except` instead of `raise` or custom exceptions

**Date recorded:** 2025-06-23  
**Context:** All input/output operations are wrapped in `try-except` blocks with direct `print()` outputs.  
**Reason:** At the current stage of learning, exception raising (`raise`) and custom exception classes have not been studied.  
**Decision:** Maintain this structure to ensure safe user experience and handle errors gracefully.  
A future refactoring will replace `print()`s with structured exception handling.

**Planned improvement:** After studying custom exceptions and structured error propagation.

---

## 3. Use of plain files (`.json`) instead of a database system

**Date recorded:** 2025-06-23  
**Context:** All application data is stored in `.json` files using manual file read/write operations.  
**Reason:** Databases (SQL or NoSQL) and ORMs are outside the current scope of study.  
**Decision:** Keep data persisted in JSON files for simplicity and transparency.  
In future stages, this will be migrated to a structured database system (e.g. SQLite or PostgreSQL).

**Planned improvement:** After studying databases, persistence layers, and SQL basics.

---

## 4. No use of object-oriented design (OOP)

**Date recorded:** 2025-06-23  
**Context:** All logic is written using functional programming and data manipulation with dictionaries and lists.  
**Reason:** OOP concepts (classes, encapsulation, inheritance) are scheduled for future learning.  
**Decision:** Keep code procedural for now to maximize clarity and focus on control flow and data structure handling.

**Planned improvement:** After learning Python OOP concepts, classes and design patterns.