# GitHub 저장소 설정 방법

## 1. GitHub에서 저장소 생성
1. https://github.com/new 접속
2. Repository name: `jamesdon-stream-manager`
3. Public 또는 Private 선택
4. "Create repository" 클릭

## 2. 원격 저장소 추가 및 푸시

저장소를 만든 후 아래 명령어 실행:

```bash
git remote add origin https://github.com/YOUR_USERNAME/jamesdon-stream-manager.git
git branch -M main
git push -u origin main
```

또는 SSH를 사용하는 경우:

```bash
git remote add origin git@github.com:YOUR_USERNAME/jamesdon-stream-manager.git
git branch -M main
git push -u origin main
```

## 3. 다른 컴퓨터에서 클론

```bash
git clone https://github.com/YOUR_USERNAME/jamesdon-stream-manager.git
cd jamesdon-stream-manager
pip install -r requirements.txt
python main.py
```

