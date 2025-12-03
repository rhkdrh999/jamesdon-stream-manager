# 제임스돈 아이디 관리 통합 프로그램

프리즘 6개 인스턴스 관리 및 구글 계정 1000개 관리 시스템

## 기능

- 프리즘 6개 인스턴스 동시 관리
- 구글 계정 1000개 저장 및 관리
- 스트리머 10명 관리
- 킥/유튜브 스트리밍 설정
- 유튜브 영상 삭제 기능

## 사전 요구사항

### 필수 설치
1. **Python 3.8 이상** 설치 필요
   - 다운로드: https://www.python.org/downloads/
   - 설치 시 "Add Python to PATH" 체크 필수!

2. **Git** 설치 (이미 있을 수 있음)
   - 다운로드: https://git-scm.com/downloads

## 설치 방법

### 1. 저장소 클론
```bash
git clone https://github.com/rhkdrh999/jamesdon-stream-manager.git
cd jamesdon-stream-manager
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

**만약 pip가 없다면:**
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**권한 오류가 발생하면:**
- Windows: 관리자 권한으로 PowerShell 실행
- Mac/Linux: `sudo pip install -r requirements.txt`

### 3. 프로그램 실행
```bash
python main.py
```

## 문제 해결

### Python이 인식되지 않는 경우
- Python 설치 시 "Add Python to PATH" 체크했는지 확인
- 재부팅 후 다시 시도
- 수동으로 PATH에 Python 추가

### pip가 없는 경우
```bash
python -m ensurepip --upgrade
```

### PyQt5 설치 오류
```bash
pip install --upgrade pip
pip install PyQt5
```

### Windows에서 실행 안 될 때
- Python이 제대로 설치되었는지 확인: `python --version`
- pip가 작동하는지 확인: `pip --version`
- 관리자 권한으로 실행

## 다른 컴퓨터에서 작업하기

1. 저장소 클론
2. 의존성 설치
3. 실행

모든 변경사항은 자동으로 Git으로 관리되므로:
```bash
git pull  # 최신 버전 가져오기
git push  # 변경사항 업로드
```

## 저장소 정보

- GitHub: https://github.com/rhkdrh999/jamesdon-stream-manager
- 브랜치: main
