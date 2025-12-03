# 빠른 동기화 가이드

하루에도 수십번 컴퓨터를 전환하면서 작업하시는 분을 위한 가이드입니다.

## 🚀 빠른 동기화 (추천)

### 작업 시작 전
```bash
quick_sync.bat
```
또는
```bash
start_work.bat    # 동기화 + 프로그램 실행
```

### 작업 종료 후
```bash
quick_sync.bat
```

## 📋 상세 동기화

문제가 발생했을 때 사용:
```bash
sync.bat
```

## ⚡ 한 줄 명령어

### Pull (다른 컴퓨터에서 작업한 내용 가져오기)
```bash
git pull
```

### Push (현재 작업 내용 업로드)
```bash
git add . && git commit -m "작업 내용" && git push
```

## 🔄 작업 흐름

### 컴퓨터 A에서 작업
1. `quick_sync.bat` 실행 (최신 버전 가져오기)
2. 작업
3. `quick_sync.bat` 실행 (업로드)

### 컴퓨터 B로 이동
1. `git pull` 또는 `quick_sync.bat` 실행
2. 작업
3. `quick_sync.bat` 실행

## ⚠️ 충돌 발생 시

1. `git status` - 상태 확인
2. `git pull` - 다시 시도
3. 충돌 파일 수동 수정
4. `git add .`
5. `git commit -m "충돌 해결"`
6. `git push`

## 💡 팁

- 작업 전후로 항상 `quick_sync.bat` 실행
- 큰 변경사항은 커밋 메시지를 명확히 작성
- 충돌이 자주 발생하면 작업 전에 반드시 pull

