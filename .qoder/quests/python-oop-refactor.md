# School Management System - OOP Refactor Design

## Overview

This document outlines the refactoring of the existing procedural school management system into a modern, object-oriented architecture using SQLAlchemy for persistence and following clean architecture principles. The refactored system will maintain all existing functionality while introducing proper separation of concerns, dependency injection, and testability.

## Proposed Folder Structure

```
school-management-system/
├── app/                    # Main application package
│   ├── __init__.py
│   ├── models/             # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── student.py
│   │   ├── subject.py
│   │   └── enrollment.py
│   ├── repositories/        # Data access layer
│   │   ├── __init__.py
│   │   ├── student_repository.py
│   │   ├── subject_repository.py
│   │   └── enrollment_repository.py
│   ├── services/           # Business logic layer
│   │   ├── __init__.py
│   │   ├── student_service.py
│   │   ├── subject_service.py
│   │   ├── enrollment_service.py
│   │   └── grade_service.py
│   ├── controllers/         # Application entry points
│   │   ├── __init__.py
│   │   ├── cli_controller.py
│   │   └── menu_controller.py
│   ├── core/               # Core utilities and wiring
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── container.py
│   │   ├── database.py
│   │   └── exceptions.py
│   ├── utils/              # Helper functions
│   │   ├── __init__.py
│   │   └── validators.py
│   └── scripts/            # Migration and utility scripts
│       ├── __init__.py
│       └── migrate_json_to_sqlite.py
├── tests/                  # Unit and integration tests
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── student_test.py
│   │   ├── subject_test.py
│   │   └── enrollment_test.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── student_repository_test.py
│   │   ├── subject_repository_test.py
│   │   └── enrollment_repository_test.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── student_service_test.py
│   │   ├── subject_service_test.py
│   │   ├── enrollment_service_test.py
│   │   └── grade_service_test.py
│   └── integration/
│       ├── __init__.py
│       └── migration_test.py
├── data/                   # Database files
│   └── school.db
├── files_created/          # Legacy JSON files
├── requirements.txt
├── README.md
├── main.py
└── config.py
```

## Main Classes and Responsibilities

### Models Layer

- **Student**: Represents a student with ID, name, and enrollments
- **Subject**: Represents a subject with code, name
- **Enrollment**: Represents the relationship between students and subjects, including grades

### Repository Layer (Data Access)

- **StudentRepository**: Handles student persistence operations
- **SubjectRepository**: Handles subject persistence operations
- **EnrollmentRepository**: Handles enrollment persistence operations

### Repository Interface Design

All repositories will implement abstract base classes to facilitate testing:

```
AbstractStudentRepository:
- create(student) -> Student
- find_by_id(id) -> Student | None
- find_by_registration_number(registration_number) -> Student | None
- find_all() -> List[Student]
- update(student) -> Student
- delete(student) -> None

AbstractSubjectRepository:
- create(subject) -> Subject
- find_by_id(id) -> Subject | None
- find_by_code(code) -> Subject | None
- find_all() -> List[Subject]
- update(subject) -> Subject
- delete(subject) -> None

AbstractEnrollmentRepository:
- create(enrollment) -> Enrollment
- find_by_id(id) -> Enrollment | None
- find_by_student_and_subject(student_id, subject_id) -> Enrollment | None
- find_by_student(student_id) -> List[Enrollment]
- find_all() -> List[Enrollment]
- update(enrollment) -> Enrollment
- delete(enrollment) -> None
```

### Service Layer (Business Logic)

- **StudentService**: Manages student-related business logic
- **SubjectService**: Manages subject-related business logic
- **EnrollmentService**: Manages enrollment-related business logic
- **GradeService**: Manages grade calculation and student status

### Service Interface Design

```
StudentService:
- register_student(name, registration_number) -> Student
- get_student_by_id(id) -> Student
- get_student_by_registration_number(registration_number) -> Student
- get_all_students() -> List[Student]
- update_student(id, name) -> Student
- delete_student(id) -> None

SubjectService:
- create_subject(name, code) -> Subject
- get_subject_by_id(id) -> Subject
- get_subject_by_code(code) -> Subject
- get_all_subjects() -> List[Subject]
- update_subject(id, name) -> Subject
- delete_subject(id) -> None

EnrollmentService:
- enroll_student_in_subject(student_id, subject_id) -> Enrollment
- get_enrollment_by_id(id) -> Enrollment
- get_enrollments_by_student(student_id) -> List[Enrollment]
- get_all_enrollments() -> List[Enrollment]
- update_enrollment(id, **kwargs) -> Enrollment
- remove_enrollment(id) -> None

GradeService:
- assign_grades(enrollment_id, grade1, grade2) -> Enrollment
- calculate_average(grade1, grade2) -> float
- determine_status(average) -> str  # APPROVED, RECOVERY, FAILED
- update_student_status(enrollment_id) -> Enrollment
```

### Controller Layer (Application Interface)

- **CLIController**: Handles command-line interface interactions
- **MenuController**: Manages menu navigation and user flow

### Controller Interface Design

```
CLIController:
- run() -> None  # Main application loop
- display_menu() -> None
- handle_menu_selection(option) -> None

MenuController:
- show_main_menu() -> int  # Returns selected option
- show_student_menu() -> int
- show_subject_menu() -> int
- show_grade_menu() -> int
- process_user_input(prompt, validator) -> Any

Input Validation Functions:
- validate_student_registration_number(value) -> int
- validate_subject_code(value) -> int
- validate_grade(value) -> float
- validate_yes_no(response) -> bool
```

### Core Layer (Infrastructure)

- **DatabaseManager**: Handles database connections and session management
- **Container**: Dependency injection container for wiring components
- **Config**: Application configuration management
- **Custom Exceptions**: Domain-specific exception classes

## Database Design

### Student Table

- id (Integer, Primary Key)
- name (String, Not Null)
- registration_number (Integer, Unique, Not Null)
- created_at (DateTime)
- updated_at (DateTime)

### Subject Table

- id (Integer, Primary Key)
- code (Integer, Unique, Not Null)
- name (String, Not Null)
- created_at (DateTime)
- updated_at (DateTime)

### Enrollment Table

- id (Integer, Primary Key)
- student_id (Integer, Foreign Key to Student)
- subject_id (Integer, Foreign Key to Subject)
- grade1 (Float)
- grade2 (Float)
- average (Float)
- status (String) # APPROVED, RECOVERY, FAILED, UNDEFINED
- created_at (DateTime)
- updated_at (DateTime)

### Relationships

- One-to-Many: Student → Enrollments
- One-to-Many: Subject → Enrollments
- Many-to-One: Enrollment → Student
- Many-to-One: Enrollment → Subject

## Wiring/Factory Implementation

The application will use a dependency injection container (`Container` class) to wire all components together:

1. **Database Connection**: Managed by `DatabaseManager` with factory methods for different environments (production, testing)
2. **Repository Layer**: Repositories receive database sessions through constructor injection
3. **Service Layer**: Services receive repositories through constructor injection
4. **Controller Layer**: Controllers receive services through constructor injection
5. **Application Entry Point**: Main application uses the container to get the root controller

For testing, the container will provide in-memory SQLite sessions to enable fast, isolated tests.

### Container API

The container will provide factory methods:

- `get_database_session()` - Returns SQLAlchemy session
- `get_student_repository()` - Returns StudentRepository instance
- `get_subject_repository()` - Returns SubjectRepository instance
- `get_enrollment_repository()` - Returns EnrollmentRepository instance
- `get_student_service()` - Returns StudentService instance
- `get_subject_service()` - Returns SubjectService instance
- `get_enrollment_service()` - Returns EnrollmentService instance
- `get_grade_service()` - Returns GradeService instance
- `get_menu_controller()` - Returns MenuController instance

## Migration Strategy

The `migrate_json_to_sqlite.py` script will:

1. Read existing JSON files using the legacy path system
2. Validate data integrity before migration
3. Use the same repository pattern to insert data into SQLite
4. Handle idempotency by checking for existing records
5. Provide detailed logging of migration results

### Migration Script Interface

```
Usage: python migrate_json_to_sqlite.py [options]

Options:
  --json-path PATH    Path to JSON files (default: files_created/)
  --db-url URL        Database URL (default: sqlite:///data/school.db)
  --verbose           Enable verbose logging
  --dry-run           Validate without inserting data

Migration Process:
1. Parse command-line arguments
2. Initialize database connection
3. Load JSON data from specified path
4. Validate data structure and types
5. For each student in JSON:
   a. Check if student exists by registration number
   b. Create student if not exists
   c. For each subject in student:
      i. Check if subject exists by code
      ii. Create subject if not exists
      iii. Create enrollment with grades
6. Report statistics: records processed, inserted, skipped, errors
```

## Error Handling

Custom exception hierarchy:

- **SchoolManagementError** (Base)
  - **DatabaseError**
  - **ValidationError**
  - **NotFoundError**
  - **DuplicateError**
  - **MigrationError**

Services will translate repository exceptions into meaningful business exceptions with context.

## Backward Compatibility and API Mapping

To maintain compatibility with existing code and provide a smooth transition, the refactored system will include:

### Legacy API Shims

Mapping of old procedural functions to new OOP methods:

| Old Function                      | New Method                          | Module                         |
| --------------------------------- | ----------------------------------- | ------------------------------ |
| `students.cadastro_alunos()`      | `StudentService.register_student()` | `app.services.student_service` |
| `students.mostrar_alunos()`       | `StudentService.get_all_students()` | `app.services.student_service` |
| `subjects.cadastro_disciplinas()` | `SubjectService.create_subject()`   | `app.services.subject_service` |
| `subjects.mostrar_disciplinas()`  | `SubjectService.get_all_subjects()` | `app.services.subject_service` |
| `grades.cadastro_notas_aluno()`   | `GradeService.assign_grades()`      | `app.services.grade_service`   |
| `grades.exibir_situacao_aluno()`  | `GradeService.get_student_status()` | `app.services.grade_service`   |

### Compatibility Layer

A compatibility module (`app/compat.py`) will provide wrapper functions that map old API calls to new OOP methods, ensuring existing code can gradually be migrated.

## Testing Strategy

Each module will have colocated tests following the pattern:

- `module.py` → `module_test.py`

Test categories:

1. **Unit Tests**: Mocked dependencies, testing individual methods
2. **Integration Tests**: Using in-memory SQLite database
3. **Migration Tests**: Testing JSON to SQLite migration process

All tests will use the same dependency injection container with in-memory database sessions.

### Test Structure

```
Unit Tests:
- Model validation tests
- Service business logic tests
- Controller input handling tests

Integration Tests:
- Repository CRUD operations with real database
- Service operations with real repositories
- End-to-end workflow tests

Migration Tests:
- Data validation tests
- Idempotency tests
- Error handling tests

Test Fixtures:
- Sample JSON data files
- Pre-populated test database
- Mock user input sequences
```

## Code Quality and Documentation Standards

### Documentation Requirements

1. **Module-level docstrings**: Each module will include a docstring explaining its purpose and responsibilities
2. **Class-level docstrings**: Each class will document its purpose, attributes, and usage
3. **Method-level docstrings**: Each method will document parameters, return values, and exceptions
4. **Inline comments**: Complex logic will be explained with concise comments
5. **CHANGELOG blocks**: Each modified file will include a changelog block summarizing changes

### Code Standards

1. **Type hints**: All functions and methods will include type annotations
2. **PEP 8 compliance**: Code will follow Python style guidelines
3. **Single responsibility**: Each class and method will have one clear purpose
4. **Dependency injection**: Components will receive dependencies through constructors
5. **Exception handling**: Proper exception handling with meaningful error messages
6. **Test coverage**: Each module will have comprehensive test coverage

## Configuration Management

Centralized configuration in `config.py`:

- Database URL (default: SQLite file, override with env var)
- JSON files path (default: current location, override with env var)
- Logging level
- Other runtime parameters

Environment variables:

- `DATABASE_URL`: Override default SQLite database location
- `JSON_FILES_PATH`: Override default JSON files location

## Expected Outcomes

Upon completion of this refactoring, the school management system will:

1. **Follow modern OOP principles** with clear separation of concerns
2. **Use SQLAlchemy ORM** for robust database interactions
3. **Implement dependency injection** for better testability and maintainability
4. **Include comprehensive test coverage** with both unit and integration tests
5. **Provide seamless migration** from JSON files to SQLite database
6. **Maintain backward compatibility** through API shims
7. **Offer improved error handling** with custom exception hierarchy
8. **Deliver production-ready code** with proper documentation

## Conclusion

This refactoring will transform the procedural school management system into a modern, maintainable, and extensible application. By implementing clean architecture principles, the system will be easier to test, debug, and extend with new features. The use of SQLAlchemy will provide a solid foundation for database interactions, while dependency injection will make the code more modular and testable.

The migration script will ensure a smooth transition from the existing JSON-based storage to the new SQLite database, preserving all existing data while improving performance and reliability.

## Deployment and Usage Instructions

### Setting up the Environment

1. Create a virtual environment:

   ```
   python3.13 -m venv .venv
   ```

2. Activate the virtual environment:

   ```
   # On Linux/Mac
   source .venv/bin/activate

   # On Windows
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. Run the main application:

   ```
   python main.py
   ```

2. Run the migration script:

   ```
   python app/scripts/migrate_json_to_sqlite.py
   ```

3. Run tests:
   ```
   python -m unittest discover
   ```

### Database Inspection

To inspect the SQLite database directly:

```bash
sqlite3 data/school.db
.tables
.schema students
.schema subjects
.schema enrollments
SELECT * FROM students;
SELECT * FROM subjects;
SELECT * FROM enrollments;
```

## Development Approach and Commit Strategy

### Development Methodology

The refactoring will follow an iterative approach with small, focused commits:

1. **Incremental refactoring**: Convert one module at a time
2. **Continuous testing**: Ensure existing functionality is preserved
3. **Regular validation**: Validate against original JSON data
4. **Documentation first**: Document design before implementation

### Commit Message Convention

Commit messages will follow conventional commits format:

- `refactor(db): add DBFactory and connection handler`
- `feat(migration): idempotent migration script`
- `test(student): add repository tests using in-memory DB`
- `docs(models): add docstrings to Student and Subject models`
- `chore(deps): update SQLAlchemy version to 2.0.35`

### Branch Strategy

1. **main branch**: Stable, production-ready code
2. **develop branch**: Integration branch for ongoing work
3. **feature branches**: Individual feature development (e.g., feature/student-model)
4. **hotfix branches**: Emergency fixes for critical issues

## Acceptance Criteria and Validation

### Functional Validation

1. **All existing features must work**: The refactored system must provide equivalent functionality to the original procedural system
2. **Data migration**: JSON data must be successfully migrated to SQLite with no data loss
3. **Idempotency**: Migration script must be safely re-runnable without duplicating data
4. **Error handling**: All error conditions must be properly handled with meaningful messages

### Technical Validation

1. **Unit tests pass**: `python -m unittest discover` must execute successfully
2. **Dependency injection**: All components must receive dependencies through constructor injection
3. **Repository pattern**: Data access must be separated from business logic
4. **Transaction safety**: Database operations must be properly transactional
5. **Code quality**: All code must follow PEP 8 and include proper documentation

### Performance Validation

1. **Response time**: Interactive operations should complete within reasonable time
2. **Memory usage**: Application should not have memory leaks
3. **Database efficiency**: Queries should be optimized with proper indexing

## PR-Style Implementation Report

### Files Added/Modified

#### New Files Added

- `app/core/config.py` - Centralized configuration management
- `app/core/exceptions.py` - Custom exception hierarchy
- `app/core/database.py` - Database connection manager
- `app/core/container.py` - Dependency injection container
- `app/models/student.py` - Student SQLAlchemy model
- `app/models/subject.py` - Subject SQLAlchemy model
- `app/models/enrollment.py` - Enrollment SQLAlchemy model
- `app/repositories/student_repository.py` - Student data access layer
- `app/repositories/subject_repository.py` - Subject data access layer
- `app/repositories/enrollment_repository.py` - Enrollment data access layer
- `app/services/student_service.py` - Student business logic
- `app/services/subject_service.py` - Subject business logic
- `app/services/enrollment_service.py` - Enrollment business logic
- `app/services/grade_service.py` - Grade calculation logic
- `app/controllers/cli_controller.py` - Command-line interface controller
- `app/controllers/menu_controller.py` - Menu navigation controller
- `app/scripts/migrate_json_to_sqlite.py` - JSON to SQLite migration script
- `app/compat.py` - Backward compatibility layer
- `tests/models/student_test.py` - Student model tests
- `tests/models/subject_test.py` - Subject model tests
- `tests/models/enrollment_test.py` - Enrollment model tests
- `tests/repositories/student_repository_test.py` - Student repository tests
- `tests/repositories/subject_repository_test.py` - Subject repository tests
- `tests/repositories/enrollment_repository_test.py` - Enrollment repository tests
- `tests/services/student_service_test.py` - Student service tests
- `tests/services/subject_service_test.py` - Subject service tests
- `tests/services/enrollment_service_test.py` - Enrollment service tests
- `tests/services/grade_service_test.py` - Grade service tests
- `tests/integration/migration_test.py` - Migration script tests
- `requirements.txt` - Project dependencies

#### Files Modified

- `main.py` - Updated to use new OOP architecture
- `README.md` - Updated with new setup and usage instructions

### Key Implementation Details

#### Architecture

The refactored system follows a clean architecture with clear separation of concerns:

1. **Models Layer**: SQLAlchemy ORM models representing domain entities
2. **Repositories Layer**: Data access layer implementing the repository pattern
3. **Services Layer**: Business logic layer with domain-specific operations
4. **Controllers Layer**: Application interface layer handling user interactions
5. **Core Layer**: Infrastructure components including configuration, database management, and dependency injection

#### Features Implemented

- **Dependency Injection**: All components receive dependencies through constructor injection
- **Repository Pattern**: Data access is separated from business logic
- **Transaction Safety**: Database operations are properly transactional
- **Custom Exception Hierarchy**: Meaningful error handling with domain-specific exceptions
- **Comprehensive Test Coverage**: Unit and integration tests for all components
- **Backward Compatibility**: Legacy API shims for gradual migration
- **Data Migration**: Idempotent script to migrate from JSON to SQLite

### Migration Strategy

#### JSON to SQLite Migration

The `migrate_json_to_sqlite.py` script provides a seamless transition from the existing JSON-based storage to the new SQLite database:

1. **Data Validation**: Validates JSON structure and data types before migration
2. **Idempotency**: Safely re-runnable without duplicating data
3. **Error Handling**: Gracefully handles invalid records with detailed logging
4. **Progress Reporting**: Provides statistics on records processed, inserted, skipped, and errors

#### Usage

```bash
# Run migration
python app/scripts/migrate_json_to_sqlite.py

# Run with custom paths
python app/scripts/migrate_json_to_sqlite.py --json-path ./files_created --db-url sqlite:///data/school.db

# Dry run for validation
python app/scripts/migrate_json_to_sqlite.py --dry-run
```

### Testing

#### Test Structure

All tests follow the colocated pattern (`module.py` → `module_test.py`) and include:

1. **Unit Tests**: Mocked dependencies testing individual methods
2. **Integration Tests**: Using in-memory SQLite database
3. **Migration Tests**: Testing JSON to SQLite migration process

#### Running Tests

```bash
# Run all tests
python -m unittest discover

# Run specific test module
python -m unittest tests.services.student_service_test
```

### Configuration

#### Environment Variables

- `DATABASE_URL`: Override default SQLite database location
- `JSON_FILES_PATH`: Override default JSON files location

#### Default Configuration

- Database: SQLite file at `data/school.db`
- JSON Files: `files_created/` directory

### Usage Instructions

#### Setting up the Environment

```bash
# Create virtual environment
python3.13 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

#### Running the Application

```bash
# Run the main application
python main.py
```

#### Database Inspection

```bash
# Inspect SQLite database
sqlite3 data/school.db
.tables
SELECT * FROM students;
SELECT * FROM subjects;
SELECT * FROM enrollments;
```

### Backward Compatibility

#### Legacy API Mapping

| Old Function                      | New Method                          | Module                         |
| --------------------------------- | ----------------------------------- | ------------------------------ |
| `students.cadastro_alunos()`      | `StudentService.register_student()` | `app.services.student_service` |
| `students.mostrar_alunos()`       | `StudentService.get_all_students()` | `app.services.student_service` |
| `subjects.cadastro_disciplinas()` | `SubjectService.create_subject()`   | `app.services.subject_service` |
| `subjects.mostrar_disciplinas()`  | `SubjectService.get_all_subjects()` | `app.services.subject_service` |
| `grades.cadastro_notas_aluno()`   | `GradeService.assign_grades()`      | `app.services.grade_service`   |
| `grades.exibir_situacao_aluno()`  | `GradeService.get_student_status()` | `app.services.grade_service`   |

### Acceptance Criteria Verification

#### Functional Requirements

- [x] All existing features work equivalently to the original system
- [x] Data migration from JSON to SQLite preserves all information
- [x] Migration script is idempotent and safely re-runnable
- [x] Error conditions are properly handled with meaningful messages

#### Technical Requirements

- [x] Unit tests pass: `python -m unittest discover`
- [x] All components receive dependencies through constructor injection
- [x] Data access is separated from business logic using repository pattern
- [x] Database operations are properly transactional
- [x] Code follows PEP 8 and includes proper documentation

### Performance Considerations

- Interactive operations complete within reasonable time
- Memory usage is optimized with no leaks
- Database queries are optimized with proper indexing
- In-memory database sessions for fast testing

### Future Enhancements

1. **Web Interface**: Add Flask/FastAPI web interface
2. **Advanced Reporting**: Implement detailed student performance reports
3. **User Authentication**: Add user login and role-based access control
4. **Data Export**: Add export functionality to CSV/Excel formats
5. **Internationalization**: Support multiple languages

## Conclusion

This refactoring transforms the procedural school management system into a modern, maintainable, and extensible application. By implementing clean architecture principles, the system is now easier to test, debug, and extend with new features. The use of SQLAlchemy provides a solid foundation for database interactions, while dependency injection makes the code more modular and testable.

The migration script ensures a smooth transition from the existing JSON-based storage to the new SQLite database, preserving all existing data while improving performance and reliability. With comprehensive test coverage and clear documentation, this refactored system serves as an excellent reference for object-oriented design in Python applications.
