import sys

sungjuks = {}

def showSungJukMenu():
    print(f'''
    ------------------------------
        성적 처리 프로그램 v7
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
    sungjuk = input('이름과 성적을 입력하세요 (예: 홍길동 99 88 77) : ')
    sj = sungjuk.split()
    
    sungjuks[sj[0]] = [int(sj[1]), int(sj[2]), int(sj[3]), 0, 0.0, '가']
    computeSungJuk(sj[0])
    saveSungJuk(sj[0])

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

def saveSungJuk(name):
    sj = f'{name}, {sungjuks[name][0]}, {sungjuks[name][1]}, {sungjuks[name][2]},'\
    f'{sungjuks[name][3]}, {sungjuks[name][4]}, {sungjuks[name][5]}\n'

    with open('./sungjukv7.dat', 'a') as f:
        f.write(sj)

def loadSungJuk():
    with open('./sungjukv7.dat', 'r') as f:
        for line in f:
            sj = line.split(',')
            sungjuks[sj[0]] = [int(sj[1]), int(sj[2]), int(sj[3]), int(sj[4]), float(sj[5]), sj[6].strip()]

def mainSungJuk():
    loadSungJuk()
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