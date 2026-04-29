```markdown
# website Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the `website` Python codebase. You'll learn how to structure files, write imports and exports, follow commit message styles, and implement and run tests. The repository is Python-based, with no specific framework, and uses a set of lightweight, consistent conventions to keep code clean and maintainable.

## Coding Conventions

### File Naming
- Use **camelCase** for file names.
  - Example: `userProfile.py`, `dataLoader.py`

### Import Style
- Use **relative imports** within the codebase.
  - Example:
    ```python
    from .utils import formatDate
    ```

### Export Style
- Use **named exports** (explicitly define what is exported).
  - Example:
    ```python
    def processData(data):
        # processing logic
        return result

    __all__ = ['processData']
    ```

### Commit Messages
- Freeform style, no strict prefix required.
- Average length: ~25 characters.
  - Example:
    ```
    fix login redirect bug
    add user profile endpoint
    ```

## Workflows

### Adding a New Module
**Trigger:** When you need to add new functionality.
**Command:** `/add-module`

1. Create a new Python file using camelCase (e.g., `newFeature.py`).
2. Write your functions/classes.
3. Use relative imports for dependencies.
4. Define `__all__` for named exports.
5. Add or update tests in a corresponding `*.test.*` file.

### Running Tests
**Trigger:** When you want to verify code correctness.
**Command:** `/run-tests`

1. Locate test files matching the pattern `*.test.*`.
2. Use the project's preferred test runner (framework unknown; check project docs or use `python <testfile>`).
3. Review test outputs and fix any failures.

### Making a Commit
**Trigger:** When you have made changes and want to commit.
**Command:** `/commit-changes`

1. Write a concise, descriptive commit message (~25 chars).
2. No strict prefix required.
3. Commit your changes.

## Testing Patterns

- Test files follow the pattern `*.test.*` (e.g., `userProfile.test.py`).
- The specific testing framework is unknown; check for test runner in project documentation or use standard Python testing tools.
- Example test file:
    ```python
    from .userProfile import getUser

    def test_getUser():
        assert getUser(1).name == "Alice"
    ```

## Commands
| Command         | Purpose                              |
|-----------------|--------------------------------------|
| /add-module     | Scaffold a new module with conventions|
| /run-tests      | Run all test files                   |
| /commit-changes | Commit changes with proper message   |
```
