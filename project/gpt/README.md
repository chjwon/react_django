# GPT Response API

This API provides an interface to interact with OpenAI's GPT models, enabling users to submit text prompts and receive generated responses.

## Endpoint

- **URL:** `/api/gpt/`
- **Methods:**
  - `GET`: Returns a message indicating that the `POST` method should be used.
  - `POST`: Accepts a text input and returns a generated response from the GPT model.

## Usage

### GET Request

**Description:**
Returns a message prompting the user to use the `POST` method for submitting text.

**Response:**
```json
{
  "message": "Please use POST to submit text for a response."
}
