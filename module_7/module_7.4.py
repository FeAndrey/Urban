if __name__ == "__main__":

    team1_num = 5   # количество участников
    team2_num = 6   # количество участников
    score_1 = 40    # количество задач решённых командой
    score_2 = 42    # количество задач решённых командой
    team1_time = 1552.512
    team2_time = 2153.31451
    tasks_total = score_1 + score_2
    time_avg = (team1_time + team2_time) / tasks_total
    challenge_result = ''

    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        challenge_result = 'Победила команда Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        challenge_result = 'Победила команда Волшебники Данных!'
    else:
        challenge_result = 'Ничья!'

    print('В команде Мастера кода участников: %s ! ' % (team1_num))
    print('В команде Волшебники данных участников: %s ! ' % (team2_num))
    print('Итого сегодня в командах участников: %s !\n' % (team1_num+team2_num))

    print('Команда Мастера кода решила задач: {} !'.format(score_1))
    print('Команда Волшебники данных решила задач: {} !'.format(score_2))
    print('Команда Мастера кода решили задачи за {} с !'.format(team1_time))
    print('Команда Волшебники данных решили задачи за {} с !\n'.format(team2_time))

    print('Обе команды сегодня решили задач: {}'.format(score_1 + score_2))
    print(f'Потратив на это: {team1_time + team2_time} с !\n')

    print(f'Результат битвы: {challenge_result}')
    print(f'Сегодня было решено задач: {tasks_total}, в среднем по {(team1_time + team2_time) / tasks_total} '
          f'секунды на задачу!.')