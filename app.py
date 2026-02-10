from flask import Flask, request, jsonify
import math
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flasgger import Swagger

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)


swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Bajaj FinServe API",
        "description": "REST API for mathematical operations and AI responses",
        "version": "1.0.0",
        "contact": {
            "name": "API Support",
            "email": os.getenv('CHITKARA_EMAIL_ID', 'support@example.com')
        }
    },
    "basePath": "/",
    "schemes": ["https", "http"],
    "securityDefinitions": {
        "api_key": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
})

def get_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series[:n]

def get_primes(numbers):
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    return [num for num in numbers if is_prime(num)]

def get_lcm(numbers):
    if not numbers:
        return None
    
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
    
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

def get_hcf(numbers):
    if not numbers:
        return None
    
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result

def get_ai_response(question):
    try:
        if not GEMINI_API_KEY:
            return {'error': 'Gemini API key not configured', 'status_code': 503}
        
        model = genai.GenerativeModel(os.getenv('GEMINI_MODEL', 'models/gemma-3-12b-it'))
        prompt = f"Answer this question with ONLY a single word (no punctuation, no explanation): {question}"
        
        response = model.generate_content(prompt)
        answer = response.text.strip()
        
        if ' ' in answer:
            answer = answer.split()[0]
        
        return answer
    
    except Exception as e:
        return {'error': f'Gemini API error: {str(e)}', 'status_code': 502}

@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint
    ---
    tags:
      - Health
    summary: Check API Health Status
    description: Returns the health status of the API server
    responses:
      200:
        description: API is healthy
        schema:
          properties:
            status:
              type: string
              example: OK
            is_success:
              type: boolean
              example: true
            official_email:
              type: string
              example: user@example.com
    """
    return jsonify({
        'status': 'OK',
        'is_success': True,
        'official_email' : os.getenv('CHITKARA_EMAIL_ID'),
    }), 200

@app.route('/bfhl', methods=['POST'])
def bfhl():
    """
    Multi-operation endpoint
    ---
    tags:
      - Operations
    summary: Execute mathematical or AI operations
    description: >
      Handles five types of operations:
      - fibonacci: Generate Fibonacci series
      - prime: Filter prime numbers
      - lcm: Calculate Least Common Multiple
      - hcf: Calculate Highest Common Factor
      - AI: Get AI response using Gemini API
    parameters:
      - in: body
        name: body
        required: true
        schema:
          oneOf:
            - type: object
              properties:
                fibonacci:
                  type: integer
                  minimum: 0
                  example: 5
            - type: object
              properties:
                prime:
                  type: array
                  items:
                    type: integer
                  example: [1, 2, 3, 4, 5, 6]
            - type: object
              properties:
                lcm:
                  type: array
                  items:
                    type: integer
                  minItems: 1
                  example: [12, 18, 24]
            - type: object
              properties:
                hcf:
                  type: array
                  items:
                    type: integer
                  minItems: 1
                  example: [48, 18, 24]
            - type: object
              properties:
                AI:
                  type: string
                  example: "What is the weather?"
    responses:
      200:
        description: Operation successful
        schema:
          properties:
            is_success:
              type: boolean
              example: true
            data:
              type: object
            official_email:
              type: string
      400:
        description: Bad request - missing or invalid data
      422:
        description: Unprocessable entity - validation error
      429:
        description: Too many requests - rate limit exceeded
      500:
        description: Internal server error
    """
    try:
        if not request.is_json:
            return jsonify({
                'is_success': False,
                'error': 'Content-Type must be application/json'
            }), 415
        
        data = request.get_json()
        
        if not data:
            return jsonify({
                'is_success': False,
                'error': 'Request body is empty'
            }), 400
        
        if 'fibonacci' in data:
            n = data.get('fibonacci')
            if not isinstance(n, int) or n < 0:
                return jsonify({
                    'is_success': False,
                    'error': 'fibonacci must be a non-negative integer'
                }), 422
            result = get_fibonacci(n)
            return jsonify({
                'is_success': True,
                'official_email': os.getenv('CHITKARA_EMAIL_ID'),
                'data': result
            }), 200
        
        elif 'prime' in data:
            numbers = data.get('prime')
            if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
                return jsonify({
                    'is_success': False,
                    'error': 'prime must be an array of integers'
                }), 422
            result = get_primes(numbers)
            return jsonify({
                'is_success': True,
                'official_email': os.getenv('CHITKARA_EMAIL_ID'),
                'data': result
            }), 200
        
        elif 'lcm' in data:
            numbers = data.get('lcm')
            if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers) or len(numbers) == 0:
                return jsonify({
                    'is_success': False,
                    'error': 'lcm must be a non-empty array of integers'
                }), 422
            result = get_lcm(numbers)
            return jsonify({
                'is_success': True,
                'official_email': os.getenv('CHITKARA_EMAIL_ID'),
                'data': result
            }), 200
        
        elif 'hcf' in data:
            numbers = data.get('hcf')
            if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers) or len(numbers) == 0:
                return jsonify({
                    'is_success': False,
                    'error': 'hcf must be a non-empty array of integers'
                }), 422
            result = get_hcf(numbers)
            return jsonify({
                'is_success': True,
                'official_email': os.getenv('CHITKARA_EMAIL_ID'),
                'data': result
            }), 200
        
        elif 'AI' in data:
            question = data.get('AI')
            if not isinstance(question, str):
                return jsonify({
                    'is_success': False,
                    'error': 'AI must be a string question'
                }), 422
            result = get_ai_response(question)
            
            if isinstance(result, dict) and 'error' in result:
                return jsonify({
                    'is_success': False,
                    'error': result['error']
                }), result.get('status_code', 502)
            
            return jsonify({
                'is_success': True,
                'official_email': os.getenv('CHITKARA_EMAIL_ID'),
                'data': result
            }), 200
        
        else:
            return jsonify({
                'is_success': False,
                'error': 'Request must contain exactly one of: fibonacci, prime, lcm, hcf, AI'
            }), 400
    
    except ValueError as e:
        return jsonify({
            'is_success': False,
            'error': f'Invalid value: {str(e)}'
        }), 422
    except TypeError as e:
        return jsonify({
            'is_success': False,
            'error': f'Invalid type: {str(e)}'
        }), 422
    except Exception as e:
        return jsonify({
            'is_success': False,
            'error': f'Internal server error: {str(e)}'
        }), 500

if __name__ == '__main__':
    debug = os.getenv('FLASK_DEBUG', 'True').lower() in ('true', '1', 'yes')
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    use_https = os.getenv('USE_HTTPS', 'True').lower() in ('true', '1', 'yes')
    
    ssl_context = 'adhoc' if use_https else None
    
    app.run(debug=debug, host=host, port=port, ssl_context=ssl_context)
