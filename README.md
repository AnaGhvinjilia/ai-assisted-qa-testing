# AI-Assisted QA Test Design

A small project exploring how AI can support a Senior QA Engineer in test design, while keeping human review and product context at the center of the process.

## Example Requirement

A user can reset their password using a verification link sent by email.

## How I Used AI

I asked AI to analyze the requirement and suggest:

- Positive scenarios
- Negative scenarios
- Edge cases
- API checks
- Usability checks

## Initial AI Suggestions

### Positive
- Verify a user can request a password reset.
- Verify the reset email is received.
- Verify a valid link allows the user to create a new password.

### Negative
- Verify an expired reset link cannot be used.
- Verify an invalid token is rejected.
- Verify an invalid email address is handled correctly.

### Edge Cases
- Use the same reset link twice.
- Request multiple reset links.
- Open an older reset link after requesting a new one.

### API Checks
- Verify the reset request returns the expected HTTP status.
- Verify invalid or expired tokens return the correct error response.
- Verify sensitive information is not exposed in the response.

### Usability
- Verify error messages clearly explain what went wrong.
- Verify the user knows how to request a new link after expiration.

## Senior QA Review

AI is useful for quickly expanding test coverage, but I would not use its output without review.

After reviewing the suggestions, I would additionally prioritize:

- Token expiration and reuse
- Multiple reset requests
- Cross-browser behavior
- Mobile responsiveness
- Clear error handling
- Regression impact on login and authentication
- Security and privacy risks around account recovery

## What I Learned

AI can speed up the brainstorming stage of test design and help identify additional scenarios. The QA engineer is still responsible for understanding product risk, validating the scenarios, removing irrelevant suggestions, and deciding what should actually be tested.

## Tools

- ChatGPT
- GitHub Copilot
- Manual QA techniques
- Risk-based testing
