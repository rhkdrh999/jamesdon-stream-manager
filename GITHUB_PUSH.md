# GitHub에 푸시하는 방법

## 현재 상태
- 로컬 Git 저장소 초기화 완료
- 커밋 완료
- GitHub MCP 서버 설정 완료 (GH2)

## GitHub 저장소 생성 및 푸시

### 방법 1: GitHub 웹사이트에서 저장소 생성 후 푸시

1. https://github.com/new 접속
2. Repository name: `jamesdon-stream-manager`
3. Public 또는 Private 선택
4. "Create repository" 클릭
5. 아래 명령어 실행:

```bash
cd C:\Users\PC\jamesdon_stream_manager
git remote add origin https://github.com/YOUR_USERNAME/jamesdon-stream-manager.git
git branch -M main
git push -u origin main
```

### 방법 2: GitHub CLI 사용 (이미 설치되어 있다면)

```bash
gh repo create jamesdon-stream-manager --public --source=. --remote=origin --push
```

## 참고
- GitHub MCP 서버가 이미 설정되어 있으므로, Cursor를 재시작하면 MCP 도구를 사용할 수 있습니다.
- 현재 GitHub Personal Access Token이 설정되어 있습니다.

