library(plumber)
r <- plumb("app/basic_script.r")  # Where 'plumber.R' is the location of the file shown above
r$run(host="0.0.0.0",port=8000)
