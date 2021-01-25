"""
P회사 회계를 처리하던 은정은 커피를 마시다가 키보드에 커피를 쏟고 말았습니다.
휴지로 닦고 말려보았지만 숫자 3, 4, 6이 도통 눌리지 않습니다.
10분 뒤, 모든 직원들에게 월급을 입금해주어야 합니다.
여유 키보드는 없으며, 프로그래밍을 매우 잘하고, 모든 작업을 수작업(?)으로 하고 있습니다.

이에 눌리지 않는 키보드를 누르지 않고 월급 입금을 두 번에 나눠주고 싶습니다.

1. 직원은 2000명이며, 3초 이내 수행을 해야합니다.
2. 입력값의 형식은 csv 파일이며 이과장 '3,000,000', 'S은행', '100-0000-0000-000' 형식으로 주어집니다.
3. 출력값의 형식은 csv 파일이며 이과장 '1,500,000', '1,500,000', 'S은행', '100-0000-0000-000' 입니다.
  또는 '1,000,000', '2,000,000', 'S은행', '100-0000-0000-000' 도 괜찮습니다.
4. 라이브러리 사용할 수 있습니다.
"""

import csv
import os.path


def broken_keyboard():
    # 파일이 없다면 파일을 쓴다.
    if not os.path.isfile('monthly_paycheck'):
        with open('monthly_paycheck', 'w', encoding='utf-8', newline='') as f:
            wr = csv.writer(f)
            # dump db
            wr.writerow(['이사원', '3,000,000', 'S은행', '100-0000-0000-000'])
            wr.writerow(['박사원', '3,200,000', 'B은행', '102-0000-0000-000'])
            wr.writerow(['강사원', '3,300,000', 'B은행', '102-0000-0000-000'])
            wr.writerow(['김팀장', '4,000,000', 'A은행', '101-0000-0000-000'])
            wr.writerow(['최이사', '6,000,000', 'B은행', '102-0000-0000-000'])
            wr.writerow(['최이사', '5,000,000', 'B은행', '102-0000-0000-000'])

    # 파일을 읽는다.
    with open('monthly_paycheck', 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        new_rows_list = []
        for row in rdr:
            s1, s2 = '', ''
            # ,를 없애고 3, 4, 6 중에 하나라도 발견하면 둘로 나눈다.
            for i in row[1].replace(',', ''):
                if i == '3':
                    s1 += '1'
                    s2 += '2'
                elif i == '4':
                    s1 += '2'
                    s2 += '2'
                elif i == '6':
                    s1 += '1'
                    s2 += '2'
                else:
                    s1 += i
                    s2 += '0'
            s1, s2 = format(int(s1), ','), format(int(s2), ',')
            if s2 != '0':
                new_row = [row[0], s1, s2, row[2], row[3]]
                new_rows_list.append(new_row)

    # 파일을 쓴다.
    with open('monthly_paycheck', 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(new_rows_list)


if __name__ == '__main__':
    broken_keyboard()
