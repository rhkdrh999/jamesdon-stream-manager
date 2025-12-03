@echo off
REM 빠른 동기화 (에러 메시지 없이)
git pull origin main 2>nul
git add . 2>nul
git commit -m "Quick sync" 2>nul
git push origin main 2>nul
echo 동기화 완료!

