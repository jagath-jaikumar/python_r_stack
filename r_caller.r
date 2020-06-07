# install.packages("httr")
library("httr")


print("Calling R Functions ~~~")

r <- GET("http://localhost:8000/echo",
  query = list(msg = "hello"))

print(content(r)$msg)


r <- POST("http://localhost:8000/sum",
  body = list(a='2',b='3'), encode = "json")

print(content(r))

print("Calling Python Functions ~~~")


r <- GET("http://localhost:5000/echo",
  query = list(msg = "hello"))

print(content(r)$msg)


r <- POST("http://localhost:5000/sum",
  body = list(a='2',b='3'), encode = "json")

print(content(r))
