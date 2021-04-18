###1 loop + list

# i = 1
# numlist = list()
# print("Start loop")
# while i in range(10):
#     print(i)
#     i += 1
#     numlist.append(i)
# print("Finish loop")
#
# numlist.reverse()
# print("List= " + str(numlist))


###2 Guess Game: while loop + if

# flag = "secret"
# guess = ""
# guess_count = 0
# guess_limit = 5
# out_of_guesses = False
#
# while guess != flag and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = (input("Guess the flag: ")).lower()
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("\n"+ "Out of Guesses, YOU LOSE!")
#     print("Number of trials= " + str(guess_count))
# else:
#     print("\n"+ "Flag= " + guess + "!")
#     print("Number of trials= " + str(guess_count))


### 3 for loop
#print values in arrays
# friends = ["Jim", "Karen", "Kevin"]
# for friend in friends:
#     print(friend)
#
# print("\n" + str(len(friends)))


# for i in range (2,10):
#     print(i)



###
# for i in range(5):
#     if i == 0:
#         print("first Iteration")
#     else:
#         print("Not first")