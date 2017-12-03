import os

def etime():
	user, sys, chuser, chsys, real = os.times()
	return user + sys

def bisection(list, target):
	start = 0
	end = len(list) - 1
	if end < 0:
		return "empty list"
	while True:
		if end - start + 1 % 2 == 0: # even number 
		#	print "len = ", end, start
			if target <= list[(start+end-1)/2]:
				end = (start+end-1)/2
			elif target >= list[(start+end+1)/2]:
				start = (start+end+1)/2
			else:
				return "no"
		else:
		#	print "len = ", end, start
			if list[(start+end)/2] == target:
				return "yes"
			elif end - start == 0:
				return "no"
			elif list[(start+end)/2] > target:
				end = (start+end)/2 - 1
			else:
				start = (start+end)/2 + 1
				
				
#  much more effective version
# seems faster
def bisection2(list, target):
	start = 0
	end = len(list)
	while start < end:
		mid = (start + end) // 2
		if list[mid] == target:
			return "yes"
		elif list[mid] < target:
			start = mid + 1
		else:
			end = mid
	return "no"
				
list = range(0, 10**8, 2)
# print list[:10]
start = etime()
print bisection(list, 6)
end = etime()
print "time used = ", end-start
start = etime()
print bisection2(list, 6)
end = etime()
print "time used = ", end-start
