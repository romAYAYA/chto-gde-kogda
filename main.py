user_points = 0

while True:
    input_answer = input('Write a word which would be an answer (DON\'T SHOW TO THE PLAYER): ')
    input_question = input('Write a question on your answer (DON\'T SHOW TO THE PLAYER): ')
    user_answer = input('Write your answer (or type "exit" to quit): ')

    if user_answer.lower() == 'exit':
        break

    if user_answer == input_answer:
        user_points += 1
        print('YOU DID IT!!! CONGRATS, COMRADE!')
    else:
        user_points -= 1
        print('Nope')

    print('Current Points:', user_points)
