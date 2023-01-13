"""
날짜 : 2023/01/13
이름 : 길은섭
내용 : 파이썬 사용자관리 실습
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                        user='root', 
                        password='1234',
                        db='java1db', 
                        charset='utf8')

while True:
    print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제, 5:수정')
    answer = 0

    try:
        answer = int(input('선택 : '))
    except Exception as e:
        print('다시 입력하세요. ', e)
        continue

    cur = conn.cursor()

    if answer == 0:
        break
    elif answer == 1:
        data = list(input('아이디, 비번, 이름, 휴대폰, 나이 순으로 입력 : ').split())
        cur = conn.cursor()
        sql = "insert into `user1` values ('%s', '%s', '%s', '%s', '%s')"
        cur.execute(sql % (data[0], data[1], data[2], data[3], data[4]))
        conn.commit()

        print('테이블 등록 완료...')
    elif answer == 2:
        cur = conn.cursor()
        cur.execute("select * from `user1`")
        conn.commit()

        print('|아이디|비번|이름|휴대폰|나이|')
        for row in cur.fetchall():
            print('-----------------------------------')
            print('|%s|%s|%s|%s|%s|' % (row[0], row[1], row[2], row[3], row[4]))
        print('-----------------------------------')
        print('테이블 조회 완료...')
    elif answer == 3:
        name = input('이름 검색 : ')

        cur = conn.cursor()
        cur.execute("select * from `user1` where `name`='{}'".format(name))
        conn.commit()

        print('|아이디|비번|이름|휴대폰|나이|')
        for row in cur.fetchall():
            print('-----------------------------------')
            print('|%s|%s|%s|%s|%s|' % (row[0], row[1], row[2], row[3], row[4]))
        print('-----------------------------------')
        print('테이블 검색 완료...')
    elif answer == 4:
        name = input('삭제할 이름 : ')

        cur = conn.cursor()
        cur.execute("delete from `user1` where `name`='{}'".format(name))
        conn.commit()
        print('테이블 삭제 완료...')
    elif answer == 5:
        name = input('수정할 이름 검색 : ')

        cur = conn.cursor()
        cur.execute("select * from `user1` where `name`='{}'".format(name))
        
        print('|아이디|비번|이름|휴대폰|나이|')
        for row in cur.fetchall():
            print('-----------------------------------')
            print('|%s|%s|%s|%s|%s|' % (row[0], row[1], row[2], row[3], row[4]))
        print('-----------------------------------')

        name = input('이름 수정하기 : ')

        cur = conn.cursor()
        cur.execute("update `user1` set `name`='{}'".format(name))
        conn.commit()
        print('테이블 수정 완료...')
    else:
        print('0 ~ 5 중에 입력하세요.')
        continue

# 데이터베니스 종료
conn.close()

# 프로그램 종료
print('프로그램 종료...')
