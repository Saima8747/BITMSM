#casefold()
string="PYTHON"
print("Lowercase string:",string.casefold())

#count()
string1="Python is awesome"
substring="is"
count=string1.count(substring)
print("The count is:",count)

#endswith()
text="Python is easy to learn."
result=text.endswith('easy to learn')
print(result)
result=text.endswith('easy to learn.')
print(result)

#find()
sentence="Hello,how are you?"
index=sentence.find("are")
print(index)

#format()
print("Hello {}, your balance is {}.".format("Adam",230.2346))
'''
#index()
sentence='Python programming is fun'
result=sentence.index('is fun')
print(result)
result=sentence.index('Java')
print(result)
'''

#replace()
message="I like cats"
new_message=message.replace("cats","dogs")
print(new_message)




