import requests
#Session stores and reuses cookies across multiple requests,
#while cookies parameter sends cookies for a single request only.
#http://rahulshettyacademy.com/
cookie = {'visit-month' : 'February'}
response=requests.get('http://rahulshettyacademy.com/' , cookies=cookie)
print(response.status_code)

#https://httpbin.org/cookies
se = requests.session()
se.cookies.update({'visit-month' : 'February'})        #Here, Request 2 remembers the cookie from Request 1 because the Session maintains state.
response2 = se.get('https://httpbin.org/cookies' , allow_redirects=False , cookies= {'visit-year' : "2022"} , timeout=1)
print(response2.text)
print(response2.history)
print(response2.status_code)
# Cookie = key-value pair sent between client(browser) and server

# cookies={} -> temporary (single request)

# Session() -> persistent (multiple requests)

# session.cookies.update() -> store cookie in session

# Session automatically sends stored cookies

# Session behaves like a browser
#Difference between requests.get() and Session().get()?
# requests.get() is stateless. Session().get() maintains cookies and state across requests.
#stateless means the request does not remember anything from previous requests.
# Redirect = Server sends client to another URL

# 301 = Permanent Redirect

# 302 = Temporary Redirect

# allow_redirects=True
# Requests automatically follows redirect

# allow_redirects=False
# Returns original redirect response (301/302)

# Location header contains redirect URL

# Used in API testing to validate redirect behavior