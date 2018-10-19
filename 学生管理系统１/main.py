from menu import *
from studen_info import *                                 


def main():
    l = []
    while True:
        login_interface()
        selst_user_action = input('请选择您需要的操作：')
       
        if selst_user_action == '1':
            l += add_student_message()
        elif selst_user_action == '2':
            show_student_message(l)
        elif selst_user_action == '3':
            l += del_student_message(l)
        elif selst_user_action == '4':
            l += revise_student_message(l)
        elif selst_user_action == '5':
            score_high_low(l)
        elif selst_user_action == '6':
            score_low_high(l)
        elif selst_user_action == '7':
            age_high_low(l)
        elif selst_user_action == '8':
            age_low_high(l)
        elif selst_user_action == '9':
            save_data(l)
        elif selst_user_action == '10':
            l += read_message()
        elif selst_user_action == 'q':
            break

            
if __name__ == '__main__':
    main()

