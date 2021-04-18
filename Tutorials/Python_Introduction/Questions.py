from Questions_Class import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue \n\n",
    "What color are Orange?\n(a) Orange\n(b) Blue\n(c) Black \n\n"
]

correct_answers = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
]


def run_test(correct_answers):
    score = 0
    for i in correct_answers:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(correct_answers)) + " correct")


run_test(correct_answers)
