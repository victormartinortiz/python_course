def protected(func):
	def wrapper(password):
		if password == "dude":
			return func()
		else:
			print("Password is wrong")
	return wrapper

@protected
def func_protected():
	print("Your password is correct")


if __name__ == "__main__":
	password = str(input("Put your password: "))

	func_protected(password)