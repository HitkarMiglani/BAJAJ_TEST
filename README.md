# Bajaj FinServe API Documentation

## API Overview

**Title:** Bajaj FinServe API  
**Description:** REST API for mathematical operations and AI responses  
**Version:** 1.0.0  
**Base URL:** `https://localhost:5000`

---

## Endpoints

### 1. Health Check Endpoint

**GET** `/health`

**Summary:** Check API Health Status

**Description:** Returns the health status of the API server

**Request:**

```bash
curl -k https://localhost:5000/health
```

**Response (200 OK):**

```json
{
  "status": "OK",
  "is_success": true,
  "official_email": "user@chitkara.edu.in"
}
```

**Status Codes:**

- `200` - API is healthy

---

### 2. Operations Endpoint

**POST** `/bfhl`

**Summary:** Execute mathematical or AI operations

**Description:** Handles five types of operations:

- **fibonacci** - Generate Fibonacci series
- **prime** - Filter prime numbers
- **lcm** - Calculate Least Common Multiple
- **hcf** - Calculate Highest Common Factor
- **AI** - Get AI response using Gemini API

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{operation}'
```

---

## Operation Details

### Operation 1: Fibonacci

Generate Fibonacci series up to n terms

**Request Body:**

```json
{
  "fibonacci": 5
}
```

**Parameter:**

- `fibonacci` (integer, minimum 0): Number of Fibonacci terms

**Example:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 5}'
```

**Response (200 OK):**

```json
{
  "is_success": true,
  "data": [0, 1, 1, 2, 3],
  "official_email": "user@chitkara.edu.in"
}
```

---

### Operation 2: Prime Numbers

Filter and return prime numbers from an array

**Request Body:**

```json
{
  "prime": [1, 2, 3, 4, 5, 6]
}
```

**Parameter:**

- `prime` (array of integers): Numbers to filter for primes

**Example:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": [1, 2, 3, 4, 5, 6]}'
```

**Response (200 OK):**

```json
{
  "is_success": true,
  "data": [2, 3, 5],
  "official_email": "user@chitkara.edu.in"
}
```

---

### Operation 3: LCM (Least Common Multiple)

Calculate the Least Common Multiple of an array

**Request Body:**

```json
{
  "lcm": [12, 18, 24]
}
```

**Parameter:**

- `lcm` (array of integers, minItems 1): Numbers to calculate LCM

**Example:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [12, 18, 24]}'
```

**Response (200 OK):**

```json
{
  "is_success": true,
  "data": 72,
  "official_email": "user@chitkara.edu.in"
}
```

---

### Operation 4: HCF (Highest Common Factor)

Calculate the Highest Common Factor of an array

**Request Body:**

```json
{
  "hcf": [48, 18, 24]
}
```

**Parameter:**

- `hcf` (array of integers, minItems 1): Numbers to calculate HCF

**Example:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [48, 18, 24]}'
```

**Response (200 OK):**

```json
{
  "is_success": true,
  "data": 6,
  "official_email": "user@chitkara.edu.in"
}
```

---

### Operation 5: AI

Get AI response using Gemini API (single-word response)

**Request Body:**

```json
{
  "AI": "What is the weather?"
}
```

**Parameter:**

- `AI` (string): Question or prompt for the AI

**Example:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "What is the weather?"}'
```

**Response (200 OK):**

```json
{
  "is_success": true,
  "data": "Sunny",
  "official_email": "user@chitkara.edu.in"
}
```

---

## Response Codes

### Success Response

**Code:** 200  
**Description:** Operation successful  
**Format:**

```json
{
  "is_success": true,
  "data": <result>,
  "official_email": "<email>"
}
```

---

### Error Responses

**Code:** 400  
**Description:** Bad Request (missing data, invalid operation)  
**Format:**

```json
{
  "is_success": false,
  "error": "Error message"
}
```

**Code:** 415  
**Description:** Unsupported Media Type (non-JSON content)

**Code:** 422  
**Description:** Unprocessable Entity (validation error)

**Code:** 429  
**Description:** Too Many Requests (rate limit exceeded)

**Code:** 500  
**Description:** Internal Server Error

**Code:** 502  
**Description:** Bad Gateway (Gemini API error)

**Code:** 503  
**Description:** Service Unavailable (API key not configured)

---

## Rate Limiting

- **GET /health:** 30 requests per minute
- **POST /bfhl:** 20 requests per minute
- **Global:** 200 requests per day, 50 requests per hour

**Rate Limit Exceeded Response (429):**

```json
{
  "is_success": false,
  "error": "429 Too Many Requests: The user has sent too many requests in a given amount of time."
}
```

---

## Installation & Running

**Install Dependencies:**

```bash
pip install -r requirements.txt
```

**Configure Environment (.env):**

```env
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
USE_HTTPS=True
CHITKARA_EMAIL_ID=your_email@chitkara.edu.in
GEMINI_API_KEY=your_api_key
CORS_ORIGINS=*
```

**Run Application - Development (Flask):**

```bash
python app.py
```

**Run Application - Production (Gunicorn):**

```bash
# Basic startup (4 worker processes)
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# With custom configuration
gunicorn -w 4 -b 0.0.0.0:5000 --timeout 120 --access-logfile - app:app
```

**Windows Command:**
```powershell
# On Windows PowerShell
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Access API Documentation (Swagger):**

```
https://localhost:5000/apidocs
```

---

**Last Updated:** February 10, 2026

✅ **Supported Operations**

- **fibonacci** - Generate Fibonacci series up to n terms
- **prime** - Filter prime numbers from an array
- **lcm** - Calculate Least Common Multiple
- **hcf** - Calculate Highest Common Factor (GCD)
- **AI** - Get intelligent single-word responses using Google Gemini API

✅ **Security & Production Ready**

- HTTPS/SSL support
- CORS (Cross-Origin Resource Sharing)
- Security headers (HSTS, CSP)
- Rate limiting
- Input validation
- Comprehensive error handling

---

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip

### Steps

1. **Navigate to project directory**

```bash
cd c:\Users\Admin\Desktop\Bajaj_API_Test
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure environment variables**

Edit `.env` file:

```env
# Flask Configuration
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
USE_HTTPS=True

# Email
CHITKARA_EMAIL_ID=your_email@chitkara.edu.in

# Gemini API Key
GEMINI_API_KEY=your_gemini_api_key_here

# CORS
CORS_ORIGINS=*
```

**Get Gemini API Key:**

- Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
- Create a new API key
- Add to `.env` file

4. **Run the application**

```bash
python app.py
```

Server runs on: `https://localhost:5000`

---

## API Documentation

### 1. GET /health

**Health Check Endpoint**

Check if the API server is running and healthy.

**Request:**

```bash
curl -k https://localhost:5000/health
```

**Response (200 OK):**

```json
{
  "status": "OK",
  "is_success": true,
  "official_email": "user@chitkara.edu.in"
}
```

**Rate Limit:** 30 requests per minute

**Status Codes:**

- `200` - Server is healthy

---

### 2. POST /bfhl

**Multi-Operation Endpoint**

Execute mathematical or AI operations. Exactly one operation must be provided.

**Rate Limit:** 20 requests per minute

---

#### Operation A: Fibonacci Series

**Description:** Generate Fibonacci series up to n terms

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 5}'
```

**Request Parameters:**

```json
{
  "fibonacci": 5
}
```

- `fibonacci` (integer, required): Number of Fibonacci terms to generate (non-negative)

**Response (200 OK):**

```json
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": [0, 1, 1, 2, 3]
}
```

**Examples:**

```bash
# 7 Fibonacci numbers
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 7}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": [0, 1, 1, 2, 3, 5, 8]
}
```

**Error Cases:**

- Missing `fibonacci` field → 400
- Non-integer value → 422
- Negative value → 422

---

#### Operation B: Prime Numbers

**Description:** Filter and return only prime numbers from an array

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": [2, 3, 4, 5, 6, 7, 8, 9, 10]}'
```

**Request Parameters:**

```json
{
  "prime": [2, 3, 4, 5, 6, 7, 8, 9, 10]
}
```

- `prime` (array of integers, required): Array of numbers to filter

**Response (200 OK):**

```json
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": [2, 3, 5, 7]
}
```

**Examples:**

```bash
# Find primes in range 1-20
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": [2, 3, 5, 7, 11, 13, 17, 19]
}

# Empty array
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": []}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": []
}
```

**Error Cases:**

- Missing `prime` field → 400
- Non-array value → 422
- Array with non-integers → 422

---

#### Operation C: LCM (Least Common Multiple)

**Description:** Calculate the Least Common Multiple of an array of numbers

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [12, 18, 24]}'
```

**Request Parameters:**

```json
{
  "lcm": [12, 18, 24]
}
```

- `lcm` (array of integers, required): Non-empty array of numbers (minimum 1 element)

**Response (200 OK):**

```json
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 72
}
```

**Examples:**

```bash
# LCM of 4, 6, 8
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [4, 6, 8]}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 24
}

# LCM of single number
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [15]}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 15
}
```

**Error Cases:**

- Missing `lcm` field → 400
- Empty array → 422
- Non-array value → 422
- Array with non-integers → 422

---

#### Operation D: HCF (Highest Common Factor / GCD)

**Description:** Calculate the Highest Common Factor (Greatest Common Divisor) of an array of numbers

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [48, 18, 24]}'
```

**Request Parameters:**

```json
{
  "hcf": [48, 18, 24]
}
```

- `hcf` (array of integers, required): Non-empty array of numbers (minimum 1 element)

**Response (200 OK):**

```json
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 6
}
```

**Examples:**

```bash
# HCF of 100, 50, 25
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [100, 50, 25]}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 25
}

# HCF of consecutive numbers
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [12, 15, 18]}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 3
}
```

**Error Cases:**

- Missing `hcf` field → 400
- Empty array → 422
- Non-array value → 422
- Array with non-integers → 422

---

#### Operation E: AI Response

**Description:** Get an intelligent single-word response to a question using Google Gemini API

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "What is machine learning?"}'
```

**Request Parameters:**

```json
{
  "AI": "What is machine learning?"
}
```

- `AI` (string, required): A question or prompt for the AI

**Response (200 OK):**

```json
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": "Intelligence"
}
```

**Examples:**

```bash
# Question about weather
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "What is the weather?"}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": "Sunny"
}

# Question about technology
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "Explain artificial intelligence"}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": "Learning"
}
```

**Note:** AI responses may take 1-3 seconds due to Gemini API latency.

**Error Cases:**

- Missing `AI` field → 400
- Non-string value → 422
- Gemini API not configured → 503
- Gemini API error → 502

---

## Error Handling

All error responses include `is_success: false` with an appropriate HTTP status code.

### Error Response Format

```json
{
  "is_success": false,
  "error": "Descriptive error message"
}
```

### HTTP Status Codes

| Code | Status                 | Description                                 |
| ---- | ---------------------- | ------------------------------------------- |
| 200  | OK                     | Request successful                          |
| 400  | Bad Request            | Missing required field or invalid operation |
| 415  | Unsupported Media Type | Content-Type is not application/json        |
| 422  | Unprocessable Entity   | Invalid data type or validation error       |
| 429  | Too Many Requests      | Rate limit exceeded                         |
| 500  | Internal Server Error  | Unexpected server error                     |
| 502  | Bad Gateway            | Gemini API error                            |
| 503  | Service Unavailable    | Gemini API key not configured               |

### Example Error Responses

**Missing Field:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{}'
```

```json
{
  "is_success": false,
  "error": "Request must contain exactly one of: fibonacci, prime, lcm, hcf, AI"
}
```

**Invalid Type:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": "five"}'
```

```json
{
  "is_success": false,
  "error": "fibonacci must be a non-negative integer"
}
```

**Rate Limit Exceeded:**

```json
{
  "is_success": false,
  "error": "429 Too Many Requests: The user has sent too many requests in a given amount of time."
}
```

**Gemini API Not Configured:**

```json
{
  "is_success": false,
  "error": "Gemini API key not configured"
}
```

---

## Rate Limiting

Rate limits are enforced per IP address:

- **Global Limits:** 200 requests per day, 50 requests per hour
- **GET /health:** 30 requests per minute
- **POST /bfhl:** 20 requests per minute

When rate limit is exceeded, server returns **HTTP 429** with error message.

---

## Security Features

1. **HTTPS/SSL** - All traffic is encrypted with TLS
2. **CORS** - Configurable cross-origin requests
3. **Security Headers** - HSTS, CSP, X-Frame-Options
4. **Input Validation** - All inputs validated for type and range
5. **Rate Limiting** - Protection against abuse
6. **Error Handling** - No sensitive information in error messages

---

## Request/Response Examples

### Complete Workflow Example

```bash
# 1. Check health
curl -k https://localhost:5000/health

# 2. Get Fibonacci series
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 6}'

# 3. Find primes
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": [10, 11, 12, 13, 14, 15]}'

# 4. Calculate LCM
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [20, 30, 40]}'

# 5. Calculate HCF
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [120, 90, 60]}'

# 6. Ask AI
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "Who is the father of computers?"}'
```

---

## Requirements

- Flask 3.0.0
- Flask-Limiter 3.5.0
- Flasgger 0.9.7.1
- Flask-CORS 4.0.0
- Flask-Talisman 1.1.0
- google-generativeai 0.3.0
- python-dotenv 1.0.0

See `requirements.txt` for complete list.

---

## Environment Variables

```env
FLASK_DEBUG=True                          # Enable debug mode
FLASK_HOST=0.0.0.0                        # Server host
FLASK_PORT=5000                           # Server port
USE_HTTPS=True                            # Enable HTTPS
CHITKARA_EMAIL_ID=email@chitkara.edu.in   # Your email
GEMINI_API_KEY=key...                     # Google Gemini API key
CORS_ORIGINS=*                            # Allowed CORS origins
```

---

## Support & Troubleshooting

**SSL Certificate Error:**
Use `-k` flag with curl to skip SSL verification for self-signed certificates:

```bash
curl -k https://localhost:5000/health
```

**Gemini API Error:**

- Verify `GEMINI_API_KEY` is set in `.env`
- Check key is valid at [Google AI Studio](https://aistudio.google.com/app/apikey)
- Ensure internet connection is available

**Rate Limit Error:**

- Wait for the rate limit window to reset
- Check if making too many requests from same IP

---

**Assignment:** Bajaj FinServe Challenge  
**Author:** Student at Chitkara University  
**Date:** February 2026

✅ **Supported Operations**

- **fibonacci** - Generate Fibonacci series up to n terms
- **prime** - Filter prime numbers from an array
- **lcm** - Calculate Least Common Multiple
- **hcf** - Calculate Highest Common Factor (GCD)
- **AI** - Get intelligent single-word responses using Google Gemini API

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip

### Steps

1. **Navigate to project directory**

```bash
cd c:\Users\Admin\Desktop\Bajaj_API_Test
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure environment variables**

Edit `.env` file:

```env
# Flask Configuration
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
USE_HTTPS=True

# Email
CHITKARA_EMAIL_ID=your_email@chitkara.edu.in

# Gemini API Key
GEMINI_API_KEY=your_gemini_api_key_here

# CORS
CORS_ORIGINS=*
```

**Get Gemini API Key:**

- Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
- Create a new API key
- Add to `.env` file

4. **Run the application**

```bash
python app.py
```

Server runs on: `https://localhost:5000`

---

## API Documentation

### 1. GET /health

**Health Check Endpoint**

Check if the API server is running and healthy.

**Request:**

```bash
curl -k https://localhost:5000/health
```

**Response (200 OK):**

```json
{
  "status": "OK",
  "is_success": true,
  "official_email": "user@chitkara.edu.in"
}
```

**Rate Limit:** 30 requests per minute

**Status Codes:**

- `200` - Server is healthy

---

### 2. POST /bfhl

**Multi-Operation Endpoint**

Execute mathematical or AI operations. Exactly one operation must be provided.

**Rate Limit:** 20 requests per minute

---

#### Operation A: Fibonacci Series

**Description:** Generate Fibonacci series up to n terms

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 5}'
```

**Request Parameters:**

```json
{
  "fibonacci": 5
}
```

- `fibonacci` (integer, required): Number of Fibonacci terms to generate (non-negative)

**Response (200 OK):**

```json
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": [0, 1, 1, 2, 3]
}
```

**Examples:**

```bash
# 7 Fibonacci numbers
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 7}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": [0, 1, 1, 2, 3, 5, 8]
}
```

**Error Cases:**

- Missing `fibonacci` field → 400
- Non-integer value → 422
- Negative value → 422

---

#### Operation B: Prime Numbers

**Description:** Filter and return only prime numbers from an array

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": [2, 3, 4, 5, 6, 7, 8, 9, 10]}'
```

**Request Parameters:**

```json
{
  "prime": [2, 3, 4, 5, 6, 7, 8, 9, 10]
}
```

- `prime` (array of integers, required): Array of numbers to filter

**Response (200 OK):**

```json
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": [2, 3, 5, 7]
}
```

**Examples:**

```bash
# Find primes in range 1-20
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": [2, 3, 5, 7, 11, 13, 17, 19]
}

# Empty array
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": []}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": []
}
```

**Error Cases:**

- Missing `prime` field → 400
- Non-array value → 422
- Array with non-integers → 422

---

#### Operation C: LCM (Least Common Multiple)

**Description:** Calculate the Least Common Multiple of an array of numbers

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [12, 18, 24]}'
```

**Request Parameters:**

```json
{
  "lcm": [12, 18, 24]
}
```

- `lcm` (array of integers, required): Non-empty array of numbers (minimum 1 element)

**Response (200 OK):**

```json
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 72
}
```

**Examples:**

```bash
# LCM of 4, 6, 8
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [4, 6, 8]}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 24
}

# LCM of single number
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [15]}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 15
}
```

**Error Cases:**

- Missing `lcm` field → 400
- Empty array → 422
- Non-array value → 422
- Array with non-integers → 422

---

#### Operation D: HCF (Highest Common Factor / GCD)

**Description:** Calculate the Highest Common Factor (Greatest Common Divisor) of an array of numbers

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [48, 18, 24]}'
```

**Request Parameters:**

```json
{
  "hcf": [48, 18, 24]
}
```

- `hcf` (array of integers, required): Non-empty array of numbers (minimum 1 element)

**Response (200 OK):**

```json
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 6
}
```

**Examples:**

```bash
# HCF of 100, 50, 25
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [100, 50, 25]}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 25
}

# HCF of consecutive numbers
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [12, 15, 18]}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": 3
}
```

**Error Cases:**

- Missing `hcf` field → 400
- Empty array → 422
- Non-array value → 422
- Array with non-integers → 422

---

#### Operation E: AI Response

**Description:** Get an intelligent single-word response to a question using Google Gemini API

**Request:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "What is machine learning?"}'
```

**Request Parameters:**

```json
{
  "AI": "What is machine learning?"
}
```

- `AI` (string, required): A question or prompt for the AI

**Response (200 OK):**

```json
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": "Intelligence"
}
```

**Examples:**

```bash
# Question about weather
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "What is the weather?"}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": "Sunny"
}

# Question about technology
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "Explain artificial intelligence"}'

# Response
{
  "is_success": true,
  "official_email": "user@chitkara.edu.in",
  "data": "Learning"
}
```

**Note:** AI responses may take 1-3 seconds due to Gemini API latency.

**Error Cases:**

- Missing `AI` field → 400
- Non-string value → 422
- Gemini API not configured → 503
- Gemini API error → 502

---

## Error Handling

All error responses include `is_success: false` with an appropriate HTTP status code.

### Error Response Format

```json
{
  "is_success": false,
  "error": "Descriptive error message"
}
```

### HTTP Status Codes

| Code | Status                 | Description                                 |
| ---- | ---------------------- | ------------------------------------------- |
| 200  | OK                     | Request successful                          |
| 400  | Bad Request            | Missing required field or invalid operation |
| 415  | Unsupported Media Type | Content-Type is not application/json        |
| 422  | Unprocessable Entity   | Invalid data type or validation error       |
| 429  | Too Many Requests      | Rate limit exceeded                         |
| 500  | Internal Server Error  | Unexpected server error                     |
| 502  | Bad Gateway            | Gemini API error                            |
| 503  | Service Unavailable    | Gemini API key not configured               |

### Example Error Responses

**Missing Field:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{}'
```

```json
{
  "is_success": false,
  "error": "Request must contain exactly one of: fibonacci, prime, lcm, hcf, AI"
}
```

**Invalid Type:**

```bash
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": "five"}'
```

```json
{
  "is_success": false,
  "error": "fibonacci must be a non-negative integer"
}
```

**Rate Limit Exceeded:**

```json
{
  "is_success": false,
  "error": "429 Too Many Requests: The user has sent too many requests in a given amount of time."
}
```

**Gemini API Not Configured:**

```json
{
  "is_success": false,
  "error": "Gemini API key not configured"
}
```

---

## Rate Limiting

Rate limits are enforced per IP address:

- **Global Limits:** 200 requests per day, 50 requests per hour
- **GET /health:** 30 requests per minute
- **POST /bfhl:** 20 requests per minute

When rate limit is exceeded, server returns **HTTP 429** with error message.

---

## Security Features

1. **HTTPS/SSL** - All traffic is encrypted with TLS
2. **CORS** - Configurable cross-origin requests
3. **Security Headers** - HSTS, CSP, X-Frame-Options
4. **Input Validation** - All inputs validated for type and range
5. **Rate Limiting** - Protection against abuse
6. **Error Handling** - No sensitive information in error messages

---

## Request/Response Examples

### Complete Workflow Example

```bash
# 1. Check health
curl -k https://localhost:5000/health

# 2. Get Fibonacci series
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 6}'

# 3. Find primes
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": [10, 11, 12, 13, 14, 15]}'

# 4. Calculate LCM
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [20, 30, 40]}'

# 5. Calculate HCF
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [120, 90, 60]}'

# 6. Ask AI
curl -k -X POST https://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "Who is the father of computers?"}'
```

---

## Requirements

- Flask 3.0.0
- Flask-Limiter 3.5.0
- Flasgger 0.9.7.1
- Flask-CORS 4.0.0
- Flask-Talisman 1.1.0
- google-generativeai 0.3.0
- python-dotenv 1.0.0

See `requirements.txt` for complete list.

---

## Environment Variables

```env
FLASK_DEBUG=True                          # Enable debug mode
FLASK_HOST=0.0.0.0                        # Server host
FLASK_PORT=5000                           # Server port
USE_HTTPS=True                            # Enable HTTPS
CHITKARA_EMAIL_ID=email@chitkara.edu.in   # Your email
GEMINI_API_KEY=key...                     # Google Gemini API key
CORS_ORIGINS=*                            # Allowed CORS origins
```

---

## Support & Troubleshooting

**SSL Certificate Error:**
Use `-k` flag with curl to skip SSL verification for self-signed certificates:

```bash
curl -k https://localhost:5000/health
```

**Gemini API Error:**

- Verify `GEMINI_API_KEY` is set in `.env`
- Check key is valid at [Google AI Studio](https://aistudio.google.com/app/apikey)
- Ensure internet connection is available

**Rate Limit Error:**

- Wait for the rate limit window to reset
- Check if making too many requests from same IP

---

**Assignment:** Bajaj FinServe Challenge  
**Author:** Student at Chitkara University  
**Date:** February 2026
