import sys

sungjuks = {}

def showSungJukMenu():
    print(f'''
    ------------------------------
        성적 처리 프로그램 v6
    ------------------------------
       1. 성적 데이터 입력
       2. 성적 데이터 조회
       3. 성적 데이터 상세조회
       4. 성적 데이터 수정
       5. 성적 데이터 삭제
       0. 성적 프로그램 종료
    ------------------------------''')
    return input('   작업을 선택하세요 : ')
    
def addSungJuk():
    name = input('이름은 : ')
    kor = int(input('국어는 : '))
    eng = int(input('영어는 : '))
    mat = int(input('수학은 : '))
        
    sungjuks[name] = [kor, eng, mat, 0, 0.0, '가']
    computeSungJuk(name)

    # 예외처리 코드 - 수민
    # try:
    #     name = input('이름은 : ')
    #     kor = int(input('국어는 : '))
    #     eng = int(input('영어는 : '))
    #     mat = int(input('수학은 : '))
            
    #     sungjuks[name] = [kor, eng, mat, 0, 0.0, '가']
    #     computeSungJuk(name)
    # except:
    #     print('잘못 기입하셨습니다!')

def computeSungJuk(name):
    val = sungjuks[name]

    val[3] = val[0] + val[1] + val[2]
    val[4] = val[3] / 3
    val[5] = '수' if (90 <= val[4] <= 100) else \
         ('우' if (80 <= val[4] <= 89) else \
         ('미' if (70 <= val[4] <= 79) else \
         ('양' if (60 <= val[4] <= 69) else '가')))
    
    sungjuks[name] = val

def readSungJuk():
    for k, v in sungjuks.items():
        print(f'{k} {sungjuks[k][0]} {sungjuks[k][1]} {sungjuks[k][2]}')

def readOneSungJuk():
    name = input('상세조회 할 학생 이름은? ')
    print(f'{name} {sungjuks[name]}')

    # 예외처리 코드 - 수민
    # name = input('상세조회 할 학생 이름은? ')
    # try:
    #     print(f'{name} {sungjuks[name]}')
    # except:
    #     print('존재하지 않음')

def modifySungJuk():
    name = input('수정할 학생 이름은? ')
    try:
        if sungjuks[name]:
            kor = int(input(f'새로운 국어는 ({sungjuks[name][0]}): '))
            eng = int(input(f'새로운 영어는 ({sungjuks[name][1]}): '))
            mat = int(input(f'새로운 수학은 ({sungjuks[name][2]}): '))
            sungjuks[name] = [kor, eng, mat, 0, 0.0, '가']
            
            val = sungjuks[name]

            val[3] = val[0] + val[1] + val[2]
            val[4] = val[3] / 3
            val[5] = '수' if (90 <= val[4] <= 100) else \
                 ('우' if (80 <= val[4] <= 89) else \
                 ('미' if (70 <= val[4] <= 79) else \
                 ('양' if (60 <= val[4] <= 69) else '가')))
            
            sungjuks[name] = val
            
            print(sungjuks[name])
    except:
        print('존재하지 않음')

def removeSungJuk():
    name = input('삭제할 학생이름은? ')

    try:
        if sungjuks[name]:
            sungjuks.pop(name)
            print(f'{name}의 데이터가 삭제되었습니다!')
    except:
        print('존재하지 않음')

def mainSungJuk():
    while True:
        menu = showSungJukMenu()
        match(menu):
            case '1':
                addSungJuk()
                
            case '2':
                readSungJuk()
                
            case '3':
                readOneSungJuk()
                
            case '4':
                modifySungJuk()
                
            case '5':
                removeSungJuk()
                
            case '0':
                sys.exit(0)

# 프로그램 실행 진입점
if __name__ == "__main__":
    mainSungJuk()