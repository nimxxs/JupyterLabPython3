import sys
import json
from collections import OrderedDict

sungjuks = []

def showSungJukMenu():
    print(f'''
    ------------------------------
        성적 처리 프로그램 v7c
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

    data = OrderedDict()
    data[sj[0]] = [int(sj[1]), int(sj[2]), int(sj[3]), 0, 0.0, '가']

    computeSungJuk(data, sj[0])
    saveSungJuk(data)


def computeSungJuk(data, name):
    val = data[name]

    val[3] = val[0] + val[1] + val[2]
    val[4] = val[3] / 3
    val[5] = '수' if (90 <= val[4] <= 100) else \
         ('우' if (80 <= val[4] <= 89) else \
         ('미' if (70 <= val[4] <= 79) else \
         ('양' if (60 <= val[4] <= 69) else '가')))
    
    data[name] = val

def readSungJuk():
     for sj in sungjuks:
         for k in sj:
            print(f'{k} {sj[k][0]} {sj[k][1]} {sj[k][2]}')

def readOneSungJuk():
    name = input('상세조회 할 학생 이름은? ')
    
    for sj in sungjuks:
        for k in sj:
            if k == name:
                print(f'{name} {sj[name]}')

def modifySungJuk():
    name = input('수정할 학생 이름은? ')
    
    try:
        # 수정할 학생 데이터 찾음
        data = None
        for sj in sungjuks:
            for k in sj:
                if k == name:
                    data = sj[name]

        # 수정할 학생 데이터를 찾으면
        # 새로운 값을 입력받고, 성적처리함
        if data:
            kor = int(input(f'새로운 국어는 ({data[0]}): '))
            eng = int(input(f'새로운 영어는 ({data[1]}): '))
            mat = int(input(f'새로운 수학은 ({data[2]}): '))

            data = OrderedDict()
            data[name] = [kor, eng, mat, 0, 0.0, '가']
            
            computeSungJuk(data, name)

            # 기존 데이터가 아닌 새로운 데이터로 재설정
            for sj in sungjuks:
                for k in sj:
                    if k == name:
                        sj[k] = data[name]

        flushSungJuk()
    
    except:
        print('존재하지 않음')

def removeSungJuk():
    name = input('삭제할 학생이름은? ')

    try:
        for sj in sungjuks:
            for k in sj:
                if k == name:
                    sungjuks.remove(sj)
                    print(f'{name}의 데이터가 삭제되었습니다!')

        flushSungJuk()
    
    except:
        print('존재하지 않음')

def saveSungJuk(data):
    sungjuks.append(data)
    
    with open('./sungjukv7c.json', 'w', encoding='utf-8') as f:
         json.dump(sungjuks, f, ensure_ascii=False)

def flushSungJuk():
    with open('./sungjukv7c.json', 'w', encoding='utf-8') as f:
         json.dump(sungjuks, f, ensure_ascii=False)


def loadSungJuk():
    global sungjuks
    with open('./sungjukv7c.json', encoding='utf-8') as f:
        sungjuks = json.load(f)
    
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