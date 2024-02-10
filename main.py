#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    #removing da whitespc n convrtin lowercase
    word = word.replace(" ", "").lower()
    #initializing empty str 4 rvrsd wrd
    reversed_word = ""
    #iterating through characters of str
    for char in word[::-1]:
        reversed_word += char
    #chckin if equal to reverse of itself
    if word == reversed_word:
        return True
    else:
        return False

#YOUR CODE GOES HERE
    #input stuff
input_text = input()
#check
result = palindrome(input_text)

print(result)

#pushing to make sure all the autograding stuff works