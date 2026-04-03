# 2. English Version

## `.claude/rules/error-handling.md`
```markdown
# Rule: Enterprise Error Handling

## 1. Backend Principles (Python/FastAPI)
- **No Raw Exceptions**: Never leak raw Python exceptions or stack traces to the client.
- **Global Handler**: Use a global exception handler to wrap all errors into the standard JSON envelope.
- **Custom Error Classes**: Use domain-specific exceptions (e.g., `AppException`, `UnauthorizedException`).
- **Validation**: Pydantic validation errors must return a 422 or 400 status code with a structured `details` array.

## 2. Frontend Principles (React)
- **Axios Interceptors**: Intercept all 4xx and 5xx responses globally.
- **User Feedback**: Display errors via a central Toast system or UI Error Boundaries.
- **Logging**: Log errors to external services (e.g., Sentry), but display sanitized messages to the end-user.

## 3. Format (JSON Envelope)
Every error response must strictly follow this schema:
```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "STRING_CONSTANT_CODE",
    "message": "Human-readable error message",
    "details": [] 
  }
}