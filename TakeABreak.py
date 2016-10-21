import webbrowser
import time

total_break = 3
break_count = 0

print("Program started on:"+time.ctime())
while(break_count < total_break):
	webbrowser.open("https://www.youtube.com/watch?v=cnuAuuXvNPw")
	time.sleep(20*60)
	break_count = break_count + 1
