def cal(a, b, c, d):
    submit_proportion, submit_gpa, open_proportion, open_gpa = a, b, c, d
    print('\n작업을 선택하세요.')
    print('1. 입력')
    print('2. 계산')
    user_value=input()

    match user_value:
        case '1':
            print('\n학점을 입력하세요:')
            user_value_1=input()
            value_1=float(user_value_1)
            print('평점을 입력하세요:')
            user_value_2=input()

            match user_value_2:
                case 'A+':
                    user_value_3=4.5
                    submit_proportion += value_1
                    submit_gpa += value_1 * user_value_3
                    open_proportion += value_1
                    open_gpa += value_1 * user_value_3
                case 'A':
                    user_value_3 = 4.0
                    submit_proportion += value_1
                    submit_gpa += value_1 * user_value_3
                    open_proportion += value_1
                    open_gpa += value_1 * user_value_3
                case 'B+':
                    user_value_3 = 3.5
                    submit_proportion += value_1
                    submit_gpa += value_1 * user_value_3
                    open_proportion += value_1
                    open_gpa += value_1 * user_value_3
                case 'B':
                    user_value_3 = 3.0
                    submit_proportion += value_1
                    submit_gpa += value_1 * user_value_3
                    open_proportion += value_1
                    open_gpa += value_1 * user_value_3
                case 'C+':
                    user_value_3 = 2.5
                    submit_proportion += value_1
                    submit_gpa += value_1 * user_value_3
                    open_proportion += value_1
                    open_gpa += value_1 * user_value_3
                case 'C':
                    user_value_3 = 2.0
                    submit_proportion += value_1
                    submit_gpa += value_1 * user_value_3
                    open_proportion += value_1
                    open_gpa += value_1 * user_value_3
                case 'D+':
                    user_value_3 = 1.5
                    submit_proportion += value_1
                    submit_gpa += value_1 * user_value_3
                    open_proportion += value_1
                    open_gpa += value_1 * user_value_3
                case 'D':
                    user_value_3 = 1.0
                    submit_proportion += value_1
                    submit_gpa += value_1 * user_value_3
                    open_proportion += value_1
                    open_gpa += value_1 * user_value_3
                case 'F':
                    user_value_3 = 0.0
                    open_proportion += value_1
                    open_gpa += value_1 * user_value_3
            return cal(submit_proportion, submit_gpa, open_proportion, open_gpa)

        case '2':
            submit_gpa=submit_gpa/submit_proportion
            open_gpa=open_gpa/open_proportion
            print('제출용:'+str(submit_proportion)+'학점 (GPA:'+str(submit_gpa)+')')
            print('열람용:' + str(open_proportion) + '학점 (GPA:' + str(open_gpa) + ')')

            print('프로그램을 종료합니다.')
            return

cal(0, 0, 0, 0)
