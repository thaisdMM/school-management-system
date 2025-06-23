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
