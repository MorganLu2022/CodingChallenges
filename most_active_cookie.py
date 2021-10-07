import argparse 

parser = argparse.ArgumentParser(description='Counting cookies.')
parser.add_argument('filename', type=str)
parser.add_argument('-d', type = str)
args = parser.parse_args()

try: 
  file = open(args.filename, "r")
except: 
  print("Invalid file")

lineList = [] #List of strings of every line in the file. 
for line in file: 
  lineList.append(line)

cookieList = [] #Filtered list of cookies that have correct timestamp
for line in lineList: #Processing lines 
  tempArr = line.split(',')
  cookie = tempArr[0]
  timeStamp = tempArr[1]
  timeStamp_filt = timeStamp[:10] 
  if timeStamp_filt == args.d: #Timestamp matches argument given
    cookieList.append(cookie)

highcount = 0 #Highest number of cookies
cookieCounts = {} #Dictionary with key = cookie, value = count of number of times that cookie appears.
for cookie in cookieList:
  if cookie in cookieCounts:
    cookieCounts[cookie] += 1 
  else: 
    cookieCounts[cookie] = 1
  highcount = max(highcount, cookieCounts[cookie])
for cookie in cookieCounts: 
  if cookieCounts[cookie] == highcount: #Printing all cookies with highest count
    print(cookie)
