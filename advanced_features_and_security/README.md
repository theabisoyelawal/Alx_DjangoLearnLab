# Advanced Features and Security

This project demonstrates the use of Django groups and custom permissions
to restrict access to parts of the application.

## Book Model Custom Permissions
- can_view
- can_create
- can_edit
- can_delete

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Permission Enforcement
The `book_list` view is protected using @permission_required('bookshelf.can_view', raise_exception=True)
Other views like create, edit, delete books are also protected using their respective permissions.
