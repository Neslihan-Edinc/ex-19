def split_into_list(text):
    return text.split()
def list_to_string(word_list):
    result=""
    for word in word_list:
        result+=word+" "
    return result.strip()
user_input=input("enter a sentence: ")
word_list=split_into_list(user_input)
result=list_to_string(word_list)
print("result:",result)
